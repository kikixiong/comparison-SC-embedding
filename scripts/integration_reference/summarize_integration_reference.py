#!/usr/bin/env python3
"""Collect integration/reference-mapping CSVs into one compact Markdown summary."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd


def parse_args():
    p = argparse.ArgumentParser(description="Summarize integration/reference mapping benchmark outputs")
    p.add_argument("--results-dir", default="results/integration_reference")
    p.add_argument("--out", default=None)
    return p.parse_args()


def fmt(v, best=None, baseline=None, higher=True):
    if pd.isna(v): return "N/A"
    text = f"{float(v):.4f}"
    if best is not None and pd.notna(best) and np.isclose(float(v), float(best)):
        return f'<span style="color:red"><strong>{text}</strong></span>'
    if baseline is not None and pd.notna(baseline) and ((float(v) > float(baseline)) if higher else (float(v) < float(baseline))):
        return f"**{text}**"
    return text


def metric_table(df: pd.DataFrame, metrics: List[tuple[str, str, bool]], embeddings: List[str]) -> List[str]:
    lines = ["| Metric | Direction | " + " | ".join(embeddings) + " |", "|---|---:|" + "---:|" * len(embeddings)]
    for col, label, higher in metrics:
        if col not in df:
            continue
        agg = df.groupby("embedding")[col].mean(numeric_only=True)
        best = agg.max(skipna=True) if higher else agg.min(skipna=True)
        base = agg.get("baseline", np.nan)
        cells = [fmt(agg.get(e, np.nan), best, base, higher) for e in embeddings]
        lines.append(f"| {label} | {'higher' if higher else 'lower'} | " + " | ".join(cells) + " |")
    return lines


def main() -> None:
    args = parse_args(); root = Path(args.results_dir)
    out = Path(args.out) if args.out else root / "combined_integration_reference_summary.md"
    lines = ["# Combined Integration + Reference Mapping Summary", "", "This file summarizes frozen-embedding downstream evaluations. Integration and reference mapping are intentionally not collapsed into one score.", "", "**Bold** means better than `baseline`; <span style=\"color:red\"><strong>red bold</strong></span> marks the best value.", ""]
    integ_path = root / "integration_metrics.csv"
    if integ_path.exists():
        integ = pd.read_csv(integ_path)
        embeddings = integ["embedding"].drop_duplicates().tolist()
        lines += ["## Integration: label preservation", ""]
        lines += metric_table(integ, [("label_knn_accuracy", "KNN label accuracy", True), ("label_macro_f1", "KNN label macro F1", True), ("label_weighted_f1", "KNN label weighted F1", True), ("silhouette_label", "Silhouette by label", True), ("adjusted_rand_index", "ARI vs labels", True), ("normalized_mutual_info", "NMI vs labels", True)], embeddings)
        lines += ["", "## Integration: batch mixing", ""]
        lines += metric_table(integ, [("batch_mixing_entropy", "Batch mixing entropy", True), ("same_label_cross_batch_neighbor_ratio", "Same-label cross-batch neighbor ratio", True), ("silhouette_batch", "Silhouette by batch", False)], embeddings)
        lines.append("")
    else:
        lines += ["## Integration", "", f"Missing `{integ_path}`.", ""]

    ref_path = root / "reference_mapping_metrics.csv"
    if ref_path.exists():
        ref = pd.read_csv(ref_path)
        embeddings = ref["embedding"].drop_duplicates().tolist()
        for scope in ["including_unseen", "excluding_unseen"]:
            sub = ref[ref["scope"].eq(scope)]
            lines += [f"## Reference mapping: {scope.replace('_', ' ')}", ""]
            for method in ["knn", "logistic_regression"]:
                msub = sub[sub["method"].eq(method)]
                if msub.empty: continue
                lines += [f"### {method}", ""]
                lines += metric_table(msub, [("accuracy", "Accuracy", True), ("balanced_accuracy", "Balanced accuracy", True), ("macro_f1", "Macro F1", True), ("weighted_f1", "Weighted F1", True), ("top_k_accuracy", "Top-k accuracy", True)], embeddings)
                lines.append("")
    else:
        lines += ["## Reference mapping", "", f"Missing `{ref_path}`.", ""]

    lines += ["## Interpretation guardrails", "", "* Report label preservation and batch mixing separately.", "* For reference mapping, compare including vs excluding unseen query labels to identify label-space mismatch effects.", "* Do not claim global embedding superiority from these tasks alone; place them alongside annotation, perturbation regression, and GRN benchmarks.", ""]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
