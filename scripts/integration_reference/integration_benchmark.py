#!/usr/bin/env python3
"""Frozen-embedding integration benchmark for batch mixing and label preservation."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, adjusted_rand_score, f1_score, normalized_mutual_info_score, silhouette_score
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import LabelEncoder, StandardScaler

sys.path.append(str(Path(__file__).resolve().parent))
from cell_embedding_utils import DEFAULT_BASE_DIR, get_cell_embeddings, load_embedding_registry, log, read_h5ad, save_config, validate_obs_keys


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Embedding-agnostic integration benchmark")
    p.add_argument("--h5ad", required=True)
    p.add_argument("--embedding-registry", default=None, help="JSON registry keyed by embedding name; defaults to common primary registry.")
    p.add_argument("--embedding-names", required=True, help="Comma-separated embedding names to evaluate.")
    p.add_argument("--base-dir", default=DEFAULT_BASE_DIR, help="Base directory for the existing primary embedding specs and vocab.json.")
    p.add_argument("--vocab-path", default=None, help="Vocabulary JSON for gene embeddings.")
    p.add_argument("--batch-key", required=True)
    p.add_argument("--label-key", required=True)
    p.add_argument("--out-dir", default="results/integration_reference")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--obsm-key", default=None, help="Use precomputed cell embeddings from adata.obsm[KEY] instead of gene embeddings.")
    p.add_argument("--max-cells", type=int, default=None)
    p.add_argument("--min-cells-per-label", type=int, default=1)
    p.add_argument("--min-cells-per-batch", type=int, default=1)
    p.add_argument("--n-neighbors", type=int, default=15)
    p.add_argument("--enable-scib", action="store_true", help="Optionally try scIB metrics if scib is installed; never required.")
    return p.parse_args()


def _filter_and_subsample(adata, args: argparse.Namespace) -> np.ndarray:
    obs = adata.obs
    keep = np.ones(adata.n_obs, dtype=bool)
    if args.min_cells_per_label > 1:
        label_counts = obs[args.label_key].astype(str).value_counts()
        keep &= obs[args.label_key].astype(str).isin(label_counts[label_counts >= args.min_cells_per_label].index).to_numpy()
    if args.min_cells_per_batch > 1:
        batch_counts = obs[args.batch_key].astype(str).value_counts()
        keep &= obs[args.batch_key].astype(str).isin(batch_counts[batch_counts >= args.min_cells_per_batch].index).to_numpy()
    idx = np.flatnonzero(keep)
    if idx.size == 0:
        raise ValueError("No cells remain after min-cells filters.")
    if args.max_cells and idx.size > args.max_cells:
        rng = np.random.default_rng(args.seed)
        idx = np.sort(rng.choice(idx, size=args.max_cells, replace=False))
    return idx


def _entropy(labels: np.ndarray) -> float:
    _, counts = np.unique(labels, return_counts=True)
    p = counts.astype(float) / counts.sum()
    ent = float(-(p * np.log(p + 1e-12)).sum())
    denom = np.log(len(counts)) if len(counts) > 1 else 1.0
    return ent / denom if denom > 0 else 0.0


def _safe_silhouette(x: np.ndarray, labels: np.ndarray) -> float:
    if len(np.unique(labels)) < 2 or len(labels) <= len(np.unique(labels)):
        return np.nan
    try:
        return float(silhouette_score(x, labels, metric="euclidean"))
    except Exception as exc:
        log(f"Silhouette skipped: {exc}")
        return np.nan


def compute_metrics(x: np.ndarray, labels: np.ndarray, batches: np.ndarray, seed: int, k: int) -> Dict[str, float]:
    if x.shape[0] < 3:
        raise ValueError("Need at least 3 cells for integration metrics.")
    scaler = StandardScaler()
    xs = scaler.fit_transform(x)
    n_neighbors = min(k + 1, x.shape[0])
    nn = NearestNeighbors(n_neighbors=n_neighbors, metric="euclidean")
    nn.fit(xs)
    _, idx = nn.kneighbors(xs)
    neigh = idx[:, 1:] if idx.shape[1] > 1 else idx
    k_eff = neigh.shape[1]
    if k_eff < 1:
        raise ValueError("No neighbors available after self-neighbor removal.")

    pred = []
    entropies = []
    cross_ratios = []
    for i, row in enumerate(neigh):
        neigh_labels = labels[row]
        vals, counts = np.unique(neigh_labels, return_counts=True)
        pred.append(vals[np.argmax(counts)])
        entropies.append(_entropy(batches[row]))
        same_label = neigh_labels == labels[i]
        denom = int(same_label.sum())
        cross_ratios.append(float(((batches[row] != batches[i]) & same_label).sum() / denom) if denom else np.nan)

    n_clusters = len(np.unique(labels))
    cluster_labels = KMeans(n_clusters=n_clusters, random_state=seed, n_init=10).fit_predict(xs) if 1 < n_clusters < x.shape[0] else None
    out = {
        "n_cells": int(x.shape[0]),
        "n_labels": int(len(np.unique(labels))),
        "n_batches": int(len(np.unique(batches))),
        "knn_k": int(k_eff),
        "label_knn_accuracy": float(accuracy_score(labels, pred)),
        "label_macro_f1": float(f1_score(labels, pred, average="macro", zero_division=0)),
        "label_weighted_f1": float(f1_score(labels, pred, average="weighted", zero_division=0)),
        "batch_mixing_entropy": float(np.nanmean(entropies)),
        "same_label_cross_batch_neighbor_ratio": float(np.nanmean(cross_ratios)),
        "silhouette_label": _safe_silhouette(xs, labels),
        "silhouette_batch": _safe_silhouette(xs, batches),
        "adjusted_rand_index": np.nan,
        "normalized_mutual_info": np.nan,
    }
    if cluster_labels is not None:
        out["adjusted_rand_index"] = float(adjusted_rand_score(labels, cluster_labels))
        out["normalized_mutual_info"] = float(normalized_mutual_info_score(labels, cluster_labels))
    return out


def _fmt(value: float, higher: bool = True) -> str:
    if pd.isna(value):
        return "N/A"
    return f"{float(value):.4f}"


def _highlight_table(df: pd.DataFrame, metrics: List[Tuple[str, str, bool]]) -> List[str]:
    lines = ["| Metric | Direction | " + " | ".join(df["embedding"].tolist()) + " |", "|---|---:|" + "---:|" * len(df)]
    for metric, label, higher in metrics:
        vals = pd.to_numeric(df[metric], errors="coerce") if metric in df else pd.Series(dtype=float)
        best = vals.max(skipna=True) if higher else vals.min(skipna=True)
        base = vals[df["embedding"].eq("baseline")].iloc[0] if df["embedding"].eq("baseline").any() and not vals[df["embedding"].eq("baseline")].empty else np.nan
        cells = []
        for v in vals:
            if pd.isna(v):
                cells.append("N/A")
                continue
            text = f"{float(v):.4f}"
            if pd.notna(best) and np.isclose(v, best):
                text = f'<span style="color:red"><strong>{text}</strong></span>'
            elif pd.notna(base) and ((v > base) if higher else (v < base)):
                text = f"**{text}**"
            cells.append(text)
        lines.append(f"| {label} | {'higher' if higher else 'lower'} | " + " | ".join(cells) + " |")
    return lines


def write_reports(metrics_df: pd.DataFrame, out_dir: Path, args: argparse.Namespace) -> None:
    label_metrics = [("label_knn_accuracy", "KNN label accuracy", True), ("label_macro_f1", "KNN label macro F1", True), ("label_weighted_f1", "KNN label weighted F1", True), ("silhouette_label", "Silhouette by label", True), ("adjusted_rand_index", "ARI vs labels", True), ("normalized_mutual_info", "NMI vs labels", True)]
    batch_metrics = [("batch_mixing_entropy", "Batch mixing entropy", True), ("same_label_cross_batch_neighbor_ratio", "Same-label cross-batch neighbor ratio", True), ("silhouette_batch", "Silhouette by batch", False)]
    best_label = metrics_df.sort_values("label_macro_f1", ascending=False).head(3)["embedding"].tolist() if "label_macro_f1" in metrics_df else []
    best_batch = metrics_df.sort_values("batch_mixing_entropy", ascending=False).head(3)["embedding"].tolist() if "batch_mixing_entropy" in metrics_df else []
    lines = [
        "# Integration Benchmark Report", "",
        f"Input H5AD: `{args.h5ad}`", f"Batch key: `{args.batch_key}`; label key: `{args.label_key}`; seed: `{args.seed}`", "",
        "## Label preservation metrics", "",
        *_highlight_table(metrics_df, label_metrics), "",
        "## Batch mixing metrics", "",
        *_highlight_table(metrics_df, batch_metrics), "",
        "## Interpretation", "",
        f"* Best label preservation by macro F1: {', '.join(best_label) if best_label else 'not available'}.",
        f"* Strongest batch mixing by neighbor entropy: {', '.join(best_batch) if best_batch else 'not available'}.",
        "* Interpret label preservation and batch mixing jointly: high mixing is not sufficient if label KNN accuracy or label F1 collapses.",
        "* Do not claim global embedding superiority from this task alone; report alongside annotation, perturbation regression, and GRN benchmarks.", "",
    ]
    (out_dir / "integration_report.md").write_text("\n".join(lines), encoding="utf-8")

    conf = ["# Integration Benchmark (Conference-style Tables)", "", "**Bold** means better than `baseline`; <span style=\"color:red\"><strong>red bold</strong></span> marks the best value. Label preservation and batch mixing are intentionally separate.", "", "## Table A. Label preservation (higher is better)", ""]
    conf.extend(_highlight_table(metrics_df, label_metrics)); conf.extend(["", "## Table B. Batch mixing", ""]); conf.extend(_highlight_table(metrics_df, batch_metrics))
    (out_dir / "integration_conference_table.md").write_text("\n".join(conf), encoding="utf-8")
    try:
        sys.path.append(str(Path(__file__).resolve().parents[1]))
        from common.combined_results_markdown import update_combined_summary_markdown
        update_combined_summary_markdown(out_dir.resolve().parents[0])
    except Exception as exc:
        log(f"Combined summary refresh skipped: {exc}")


def main() -> None:
    args = parse_args()
    np.random.seed(args.seed)
    out_dir = Path(args.out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    adata = read_h5ad(args.h5ad)
    validate_obs_keys(adata, [args.batch_key, args.label_key])
    registry = load_embedding_registry(args.embedding_registry, args.base_dir, args.embedding_names)
    idx = _filter_and_subsample(adata, args)
    batches = adata.obs[args.batch_key].astype(str).to_numpy()[idx]
    labels = adata.obs[args.label_key].astype(str).to_numpy()[idx]
    save_config(out_dir, "integration_config.json", args, {"embedding_names_resolved": list(registry), "n_cells_selected": int(len(idx)), "batch_distribution": pd.Series(batches).value_counts().to_dict(), "label_distribution": pd.Series(labels).value_counts().to_dict()})

    rows = []; covs = []
    for name, cfg in registry.items():
        log(f"Evaluating integration embedding: {name}")
        x_all, cov = get_cell_embeddings(adata, name, cfg, obsm_key=args.obsm_key, vocab_path=args.vocab_path, base_dir=args.base_dir)
        x = x_all[idx]
        if not np.isfinite(x).all():
            raise ValueError(f"{name}: cell embedding contains NaN/inf values")
        row = {"embedding": name, **compute_metrics(x, labels, batches, args.seed, args.n_neighbors)}
        rows.append(row); covs.append(cov.assign(benchmark="integration"))
    metrics_df = pd.DataFrame(rows)
    metrics_df.to_csv(out_dir / "integration_metrics.csv", index=False)
    pd.concat(covs, ignore_index=True).to_csv(out_dir / "integration_coverage.csv", index=False)
    write_reports(metrics_df, out_dir, args)

    if args.enable_scib:
        try:
            import scib  # noqa: F401
            log("scIB is installed, but lightweight integration metrics were run by default; add project-specific scIB calls as needed.")
        except ImportError:
            log("--enable-scib requested but scib is not installed; continuing with lightweight metrics only.")


if __name__ == "__main__":
    main()
