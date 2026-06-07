#!/usr/bin/env python3
"""Frozen-embedding reference-to-query label-transfer benchmark."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, balanced_accuracy_score, confusion_matrix, f1_score, precision_recall_fscore_support
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

sys.path.append(str(Path(__file__).resolve().parent))
from cell_embedding_utils import DEFAULT_BASE_DIR, get_cell_embeddings, load_embedding_registry, log, read_h5ad, save_config, validate_obs_keys


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Embedding-agnostic reference mapping benchmark")
    p.add_argument("--h5ad", required=True)
    p.add_argument("--embedding-registry", default=None)
    p.add_argument("--embedding-names", required=True)
    p.add_argument("--base-dir", default=DEFAULT_BASE_DIR)
    p.add_argument("--vocab-path", default=None)
    p.add_argument("--reference-query-mode", required=True, choices=["batch_heldout", "dataset_heldout", "random_split", "custom_column"])
    p.add_argument("--batch-key", required=True)
    p.add_argument("--label-key", required=True)
    p.add_argument("--dataset-key", default=None)
    p.add_argument("--custom-column", default=None)
    p.add_argument("--reference-value", default=None)
    p.add_argument("--query-value", default=None)
    p.add_argument("--out-dir", default="results/integration_reference")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--obsm-key", default=None)
    p.add_argument("--k-values", default="1,5,10,20")
    p.add_argument("--query-fraction", type=float, default=0.2)
    return p.parse_args()


def parse_k_values(raw: str) -> List[int]:
    vals = [int(x.strip()) for x in raw.split(",") if x.strip()]
    if not vals or any(k < 1 for k in vals):
        raise ValueError("--k-values must contain positive integers")
    return vals


def make_splits(adata, args: argparse.Namespace) -> List[Tuple[str, np.ndarray, np.ndarray]]:
    obs = adata.obs
    n = adata.n_obs
    if args.reference_query_mode == "random_split":
        labels = obs[args.label_key].astype(str).to_numpy()
        splitter = StratifiedShuffleSplit(n_splits=1, test_size=args.query_fraction, random_state=args.seed)
        ref, qry = next(splitter.split(np.zeros(n), labels))
        return [("random_split", ref, qry)]

    if args.reference_query_mode == "batch_heldout":
        col = args.batch_key
    elif args.reference_query_mode == "dataset_heldout":
        if not args.dataset_key:
            raise ValueError("--dataset-key is required for --reference-query-mode dataset_heldout")
        col = args.dataset_key
    else:
        if not args.custom_column:
            raise ValueError("--custom-column is required for --reference-query-mode custom_column")
        col = args.custom_column
    validate_obs_keys(adata, [col])
    values = obs[col].astype(str).to_numpy()
    splits = []
    if args.reference_value is not None or args.query_value is not None:
        if args.reference_value is None or args.query_value is None:
            raise ValueError("Provide both --reference-value and --query-value, or neither.")
        ref = np.flatnonzero(values == str(args.reference_value))
        qry = np.flatnonzero(values == str(args.query_value))
        splits.append((f"{col}:{args.reference_value}-> {args.query_value}", ref, qry))
    else:
        for v in sorted(pd.unique(values)):
            qry = np.flatnonzero(values == v)
            ref = np.flatnonzero(values != v)
            splits.append((f"heldout_{col}_{v}", ref, qry))
    good = [(name, ref, qry) for name, ref, qry in splits if len(ref) > 0 and len(qry) > 0]
    if not good:
        raise ValueError("No non-empty reference/query splits could be created.")
    return good


def topk_from_scores(y_true: np.ndarray, classes: np.ndarray, scores: np.ndarray, k: int) -> float:
    kk = min(k, scores.shape[1])
    top = np.argsort(-scores, axis=1)[:, :kk]
    hits = [y_true[i] in set(classes[top[i]]) for i in range(len(y_true))]
    return float(np.mean(hits)) if hits else np.nan


def metric_rows(y_true: np.ndarray, y_pred: np.ndarray, *, embedding: str, split: str, method: str, k: int | None, scope: str, topk_acc: float | None, unseen_labels: set[str]) -> Dict[str, object]:
    return {
        "embedding": embedding, "split": split, "method": method, "k": k, "scope": scope,
        "accuracy": float(accuracy_score(y_true, y_pred)) if len(y_true) else np.nan,
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)) if len(np.unique(y_true)) > 1 and len(y_true) else np.nan,
        "macro_f1": float(f1_score(y_true, y_pred, average="macro", zero_division=0)) if len(y_true) else np.nan,
        "weighted_f1": float(f1_score(y_true, y_pred, average="weighted", zero_division=0)) if len(y_true) else np.nan,
        "top_k_accuracy": topk_acc,
        "n_query": int(len(y_true)),
        "n_unseen_query_labels": int(len(unseen_labels)),
    }


def per_label_rows(y_true: np.ndarray, y_pred: np.ndarray, *, embedding: str, split: str, method: str, k: int | None, labels_all: List[str], ref_labels: set[str]) -> List[Dict[str, object]]:
    p, r, f, s = precision_recall_fscore_support(y_true, y_pred, labels=labels_all, zero_division=0)
    return [{"embedding": embedding, "split": split, "method": method, "k": k, "label": lab, "precision": float(p[i]), "recall": float(r[i]), "f1": float(f[i]), "support": int(s[i]), "label_seen_in_reference": lab in ref_labels} for i, lab in enumerate(labels_all)]


def confusion_rows(y_true: np.ndarray, y_pred: np.ndarray, *, embedding: str, split: str, method: str, k: int | None, labels_all: List[str]) -> List[Dict[str, object]]:
    cm = confusion_matrix(y_true, y_pred, labels=labels_all)
    rows = []
    for i, true_lab in enumerate(labels_all):
        for j, pred_lab in enumerate(labels_all):
            if cm[i, j]:
                rows.append({"embedding": embedding, "split": split, "method": method, "k": k, "true_label": true_lab, "pred_label": pred_lab, "count": int(cm[i, j])})
    return rows


def evaluate_one(x: np.ndarray, labels: np.ndarray, splits: List[Tuple[str, np.ndarray, np.ndarray]], embedding: str, k_values: List[int], seed: int):
    metric_out = []; per_label_out = []; cm_out = []; diag_out = []
    for split_name, ref_idx, qry_idx in splits:
        x_ref, x_qry = x[ref_idx], x[qry_idx]
        y_ref, y_qry = labels[ref_idx], labels[qry_idx]
        ref_label_set = set(y_ref.tolist())
        unseen = set(y_qry.tolist()) - ref_label_set
        seen_mask = np.array([y in ref_label_set for y in y_qry], dtype=bool)
        diag_out.append({"embedding": embedding, "split": split_name, "n_reference": int(len(ref_idx)), "n_query": int(len(qry_idx)), "n_reference_labels": int(len(ref_label_set)), "n_query_labels": int(len(set(y_qry.tolist()))), "n_query_labels_absent_from_reference": int(len(unseen)), "fraction_query_cells_true_label_unseen": float((~seen_mask).mean()) if len(seen_mask) else np.nan, "unseen_query_labels": ";".join(sorted(unseen))})
        scaler = StandardScaler(); x_ref_s = scaler.fit_transform(x_ref); x_qry_s = scaler.transform(x_qry)
        labels_all = sorted(set(y_qry.tolist()) | ref_label_set)

        for k in k_values:
            kk = min(k, len(ref_idx))
            clf = KNeighborsClassifier(n_neighbors=kk, weights="uniform")
            clf.fit(x_ref_s, y_ref)
            pred = clf.predict(x_qry_s)
            proba = clf.predict_proba(x_qry_s)
            topk = topk_from_scores(y_qry, clf.classes_, proba, k)
            for scope, mask in [("including_unseen", np.ones(len(y_qry), dtype=bool)), ("excluding_unseen", seen_mask)]:
                metric_out.append(metric_rows(y_qry[mask], pred[mask], embedding=embedding, split=split_name, method="knn", k=k, scope=scope, topk_acc=topk_from_scores(y_qry[mask], clf.classes_, proba[mask], k) if mask.any() else np.nan, unseen_labels=unseen))
            per_label_out.extend(per_label_rows(y_qry, pred, embedding=embedding, split=split_name, method="knn", k=k, labels_all=labels_all, ref_labels=ref_label_set))
            cm_out.extend(confusion_rows(y_qry, pred, embedding=embedding, split=split_name, method="knn", k=k, labels_all=labels_all))

        if len(ref_label_set) == 1:
            only = next(iter(ref_label_set))
            pred = np.full(len(y_qry), only, dtype=object)
            classes = np.array([only], dtype=object)
            proba = np.ones((len(y_qry), 1), dtype=float)
        else:
            lr = LogisticRegression(max_iter=1000, random_state=seed, n_jobs=-1, class_weight="balanced")
            lr.fit(x_ref_s, y_ref)
            pred = lr.predict(x_qry_s)
            proba = lr.predict_proba(x_qry_s)
            classes = lr.classes_
        for scope, mask in [("including_unseen", np.ones(len(y_qry), dtype=bool)), ("excluding_unseen", seen_mask)]:
            metric_out.append(metric_rows(y_qry[mask], pred[mask], embedding=embedding, split=split_name, method="logistic_regression", k=None, scope=scope, topk_acc=topk_from_scores(y_qry[mask], classes, proba[mask], min(max(k_values), len(classes))) if mask.any() else np.nan, unseen_labels=unseen))
        per_label_out.extend(per_label_rows(y_qry, pred, embedding=embedding, split=split_name, method="logistic_regression", k=None, labels_all=labels_all, ref_labels=ref_label_set))
        cm_out.extend(confusion_rows(y_qry, pred, embedding=embedding, split=split_name, method="logistic_regression", k=None, labels_all=labels_all))
    return metric_out, per_label_out, cm_out, diag_out


def _format_cells(agg: pd.Series, embeddings: List[str], higher=True) -> List[str]:
    base = agg.get("baseline", np.nan); best = agg.max(skipna=True) if higher else agg.min(skipna=True)
    out = []
    for emb in embeddings:
        v = agg.get(emb, np.nan)
        if pd.isna(v): out.append("N/A"); continue
        text = f"{float(v):.4f}"
        if pd.notna(best) and np.isclose(v, best): text = f'<span style="color:red"><strong>{text}</strong></span>'
        elif pd.notna(base) and ((v > base) if higher else (v < base)): text = f"**{text}**"
        out.append(text)
    return out


def write_reports(metrics: pd.DataFrame, diag: pd.DataFrame, out_dir: Path, args: argparse.Namespace) -> None:
    main = metrics[metrics["scope"].eq("excluding_unseen")].copy()
    embeddings = metrics["embedding"].drop_duplicates().tolist()
    lines = ["# Reference Mapping Benchmark Report", "", f"Input H5AD: `{args.h5ad}`", f"Mode: `{args.reference_query_mode}`; label key: `{args.label_key}`; seed: `{args.seed}`", "", "## Aggregate transfer metrics (excluding unseen query labels)", ""]
    for metric in ["accuracy", "balanced_accuracy", "macro_f1", "weighted_f1", "top_k_accuracy"]:
        agg = main.groupby("embedding")[metric].mean(numeric_only=True)
        lines += [f"### {metric} (higher is better)", "", "| Embedding | Mean |", "|---|---:|"]
        for emb in embeddings:
            lines.append(f"| {emb} | {agg.get(emb, np.nan):.4f} |" if pd.notna(agg.get(emb, np.nan)) else f"| {emb} | N/A |")
        lines.append("")
    best = main.groupby("embedding")["macro_f1"].mean().sort_values(ascending=False).head(3).index.tolist() if not main.empty else []
    high_unseen = diag.groupby("embedding")["fraction_query_cells_true_label_unseen"].mean().sort_values(ascending=False).head(3).to_dict() if not diag.empty else {}
    lines += ["## Interpretation", "", f"* Best label transfer by macro F1 after excluding unseen query labels: {', '.join(best) if best else 'not available'}.", "* Inspect split-level rows to determine whether gains are consistent across held-out batches or datasets.", f"* Unseen query labels can affect results; average unseen fractions include: {high_unseen}.", "* Do not claim global embedding superiority from this task alone; report alongside annotation, perturbation regression, GRN, and integration results."]
    (out_dir / "reference_mapping_report.md").write_text("\n".join(lines), encoding="utf-8")

    conf = ["# Reference Mapping Benchmark (Conference-style Tables)", "", "Aggregate means are computed across generated splits. **Bold** means better than `baseline`; <span style=\"color:red\"><strong>red bold</strong></span> marks the best value.", ""]
    for scope in ["including_unseen", "excluding_unseen"]:
        sub = metrics[metrics["scope"].eq(scope)]
        conf += [f"## Table A. {scope.replace('_', ' ').title()} (higher is better)", "", "| Method | Metric | " + " | ".join(embeddings) + " |", "|---|---:|" + "---:|" * len(embeddings)]
        for method in ["knn", "logistic_regression"]:
            msub = sub[sub["method"].eq(method)]
            for metric in ["accuracy", "balanced_accuracy", "macro_f1", "weighted_f1", "top_k_accuracy"]:
                agg = msub.groupby("embedding")[metric].mean(numeric_only=True)
                conf.append(f"| {method} | {metric} | " + " | ".join(_format_cells(agg, embeddings)) + " |")
        conf.append("")
    (out_dir / "reference_mapping_conference_table.md").write_text("\n".join(conf), encoding="utf-8")
    try:
        sys.path.append(str(Path(__file__).resolve().parents[1]))
        from common.combined_results_markdown import update_combined_summary_markdown
        update_combined_summary_markdown(out_dir.resolve().parents[0])
    except Exception as exc:
        log(f"Combined summary refresh skipped: {exc}")


def main() -> None:
    args = parse_args(); np.random.seed(args.seed)
    out_dir = Path(args.out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    adata = read_h5ad(args.h5ad)
    validate_obs_keys(adata, [args.batch_key, args.label_key] + ([args.dataset_key] if args.dataset_key else []))
    splits = make_splits(adata, args)
    registry = load_embedding_registry(args.embedding_registry, args.base_dir, args.embedding_names)
    k_values = parse_k_values(args.k_values)
    labels = adata.obs[args.label_key].astype(str).to_numpy()
    save_config(out_dir, "reference_mapping_config.json", args, {"embedding_names_resolved": list(registry), "splits": [{"name": n, "n_reference": len(r), "n_query": len(q)} for n, r, q in splits], "label_distribution": pd.Series(labels).value_counts().to_dict()})
    metric_rows_all=[]; per_label_rows_all=[]; cm_rows_all=[]; diag_rows_all=[]; covs=[]
    for name, cfg in registry.items():
        log(f"Evaluating reference mapping embedding: {name}")
        x, cov = get_cell_embeddings(adata, name, cfg, obsm_key=args.obsm_key, vocab_path=args.vocab_path, base_dir=args.base_dir)
        if not np.isfinite(x).all(): raise ValueError(f"{name}: cell embedding contains NaN/inf values")
        a,b,c,d = evaluate_one(x, labels, splits, name, k_values, args.seed)
        metric_rows_all += a; per_label_rows_all += b; cm_rows_all += c; diag_rows_all += d; covs.append(cov.assign(benchmark="reference_mapping"))
    metrics = pd.DataFrame(metric_rows_all); per_label = pd.DataFrame(per_label_rows_all); diag = pd.DataFrame(diag_rows_all)
    metrics.to_csv(out_dir / "reference_mapping_metrics.csv", index=False)
    per_label.to_csv(out_dir / "reference_mapping_per_label.csv", index=False)
    pd.DataFrame(cm_rows_all).to_csv(out_dir / "reference_mapping_confusion_matrix.csv", index=False)
    diag.to_csv(out_dir / "reference_mapping_split_diagnostics.csv", index=False)
    pd.concat(covs, ignore_index=True).to_csv(out_dir / "reference_mapping_coverage.csv", index=False)
    write_reports(metrics, diag, out_dir, args)


if __name__ == "__main__":
    main()
