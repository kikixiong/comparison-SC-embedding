#!/usr/bin/env python3
"""Failure-subset analysis for single-cell embedding benchmark results.

This script is intentionally an analysis layer over existing CSV artifacts. It does
not import or modify benchmark/evaluation code. All outputs are diagnostics meant
to identify settings where average benchmark scores can be misleading.
"""
from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

LOW_POSITIVE_RATIO = 0.05
LOW_TEST_POSITIVES = 50
HIGH_NEG_POS_RATIO = 10.0
AUPRC_RANDOM_MULTIPLIER = 1.25
DELTA_EPS = 1e-9

METRIC_ALIASES = {
    "auroc": ("auroc", "mean_auroc"),
    "auprc": ("auprc", "mean_auprc"),
    "f1": ("f1", "mean_f1"),
    "precision_at_k": ("precision_at_k", "mean_precision_at_k"),
    "recall_at_k": ("recall_at_k", "mean_recall_at_k"),
    "balanced_accuracy": ("balanced_accuracy", "mean_balanced_accuracy"),
    "accuracy": ("accuracy", "accuracy_mean"),
    "f1_macro": ("f1_macro", "f1_macro_mean"),
    "pearson_r": ("pearson_r",),
    "sign_acc": ("sign_acc",),
    "mse": ("mse",),
    "rmse": ("rmse",),
    "mae": ("mae",),
    "loss": ("loss",),
    "calibration_brier": ("calibration_brier", "mean_calibration_brier"),
}

LOWER_IS_BETTER = {"mse", "rmse", "mae", "loss"}
STD_SUFFIXES = ("_std", "std_")


def metric_direction(metric: str) -> str:
    canonical = canonical_metric(metric) or metric
    return "lower_is_better" if canonical in LOWER_IS_BETTER else "higher_is_better"


@dataclass
class CsvTable:
    path: Path
    rows: List[Dict[str, str]]
    columns: List[str]


class WarningLog:
    def __init__(self) -> None:
        self.messages: List[str] = []

    def add(self, message: str) -> None:
        if message not in self.messages:
            self.messages.append(message)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results-root", default="results", help="Root directory containing benchmark result CSVs.")
    parser.add_argument("--out-dir", default="results/failure_subset_analysis", help="Directory for failure-analysis outputs.")
    parser.add_argument("--baseline", default="baseline", help="Embedding name used as the primary baseline.")
    parser.add_argument("--external-baseline", default="scGPT_human", help="External baseline embedding for model-specific comparisons.")
    parser.add_argument("--grn-results", nargs="*", default=None, help="Optional explicit GRN result CSV paths.")
    parser.add_argument("--transfer-results", nargs="*", default=None, help="Optional explicit transfer_v2 result CSV paths.")
    parser.add_argument("--perturbation-results", nargs="*", default=None, help="Optional explicit perturbation regression CSV paths.")
    parser.add_argument("--annotation-results", nargs="*", default=None, help="Optional explicit annotation result CSV paths.")
    parser.add_argument("--metadata", nargs="*", default=None, help="Optional topology/frequency metadata CSV paths.")
    parser.add_argument("--make-plots", action="store_true", help="Create optional plots when matplotlib is importable.")
    return parser.parse_args()


def read_csv(path: Path, warnings: WarningLog) -> Optional[CsvTable]:
    if not path.exists():
        warnings.add(f"Missing CSV: {path}")
        return None
    try:
        with path.open(newline="") as handle:
            reader = csv.DictReader(handle)
            rows = [dict(row) for row in reader]
            return CsvTable(path=path, rows=rows, columns=list(reader.fieldnames or []))
    except Exception as exc:  # pragma: no cover - defensive IO diagnostics
        warnings.add(f"Could not read {path}: {exc}")
        return None


def discover_csvs(results_root: Path, explicit: Optional[Sequence[str]], patterns: Sequence[str], warnings: WarningLog) -> List[CsvTable]:
    paths: List[Path] = []
    if explicit:
        paths = [Path(p) for p in explicit]
    else:
        seen = set()
        for pattern in patterns:
            for path in results_root.glob(pattern):
                if path.is_file() and path not in seen:
                    paths.append(path)
                    seen.add(path)
    tables = []
    for path in paths:
        table = read_csv(path, warnings)
        if table is not None:
            tables.append(table)
    return tables


def to_float(value: object) -> Optional[float]:
    if value is None:
        return None
    text = str(value).strip()
    if text == "" or text.lower() in {"nan", "none", "null"}:
        return None
    try:
        val = float(text)
    except ValueError:
        return None
    if math.isnan(val) or math.isinf(val):
        return None
    return val


def get_metric(row: Dict[str, str], metric: str) -> Tuple[Optional[float], Optional[str]]:
    for col in METRIC_ALIASES.get(metric, (metric,)):
        if col in row:
            return to_float(row.get(col)), col
    return None, None


def first_existing(columns: Iterable[str], candidates: Sequence[str]) -> Optional[str]:
    column_set = set(columns)
    for candidate in candidates:
        if candidate in column_set:
            return candidate
    return None


def is_metric_column(col: str) -> bool:
    canonical = canonical_metric(col)
    if canonical is not None:
        return True
    if col.endswith(STD_SUFFIXES) or col.startswith("std_"):
        return True
    if col.startswith("delta_") or col.startswith("mean_") and canonical_metric(col) is not None:
        return True
    return False


def canonical_metric(col: str) -> Optional[str]:
    for metric, aliases in METRIC_ALIASES.items():
        if col in aliases:
            return metric
    return None


def setting_key(row: Dict[str, str], columns: Sequence[str], *, drop: Sequence[str] = ("embedding",)) -> Tuple[Tuple[str, str], ...]:
    drop_set = set(drop)
    parts = []
    for col in columns:
        if col in drop_set or is_metric_column(col):
            continue
        if col.startswith("delta_") or col.endswith("_vs_baseline") or col.startswith("lift_ratio"):
            continue
        parts.append((col, row.get(col, "")))
    return tuple(parts)


def key_to_string(key: Tuple[Tuple[str, str], ...]) -> str:
    return ";".join(f"{k}={v}" for k, v in key)


def write_csv(path: Path, rows: List[Dict[str, object]], fieldnames: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fieldnames), extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def mean(values: Iterable[Optional[float]]) -> Optional[float]:
    clean = [v for v in values if v is not None]
    if not clean:
        return None
    return sum(clean) / len(clean)


def delta(a: Optional[float], b: Optional[float], metric: str) -> Optional[float]:
    if a is None or b is None:
        return None
    return a - b


def delta_is_failure(value: float, metric: str) -> bool:
    if metric_direction(metric) == "lower_is_better":
        return value > DELTA_EPS
    return value < -DELTA_EPS


def delta_is_improvement(value: float, metric: str) -> bool:
    if metric_direction(metric) == "lower_is_better":
        return value < -DELTA_EPS
    return value > DELTA_EPS


def delta_magnitude(value: float) -> float:
    return abs(value)


def perturbation_diagnostic_flags(task: str, row: Dict[str, str]) -> Tuple[bool, bool, bool]:
    if task != "perturbation_regression":
        return False, False, False
    n_test = to_float(row.get("n_test"))
    n_train = to_float(row.get("n_train"))
    small_test_warning = n_test is not None and n_test < 5
    small_train_warning = n_train is not None and n_train < 20
    return small_test_warning, small_train_warning, small_test_warning or small_train_warning


def fmt(value: object, digits: int = 4) -> str:
    if value is None or value == "":
        return "NA"
    if isinstance(value, str):
        numeric = to_float(value)
        if numeric is None:
            return value
        value = numeric
    if isinstance(value, (int, float)):
        if digits == 0:
            return str(int(round(value)))
        return f"{value:.{digits}g}"
    return str(value)


def detect_task(table: CsvTable) -> str:
    p = str(table.path).lower()
    cols = set(table.columns)
    if "transfer_v2" in p or {"train_dataset", "test_dataset", "protocol"}.issubset(cols):
        return "transfer_v2"
    if "grn" in p or {"negative_protocol", "random_auprc_baseline"}.issubset(cols):
        return "grn"
    if "perturbation_regression" in p or {"pearson_r", "mse", "sign_acc"}.issubset(cols):
        return "perturbation_regression"
    if "annotation" in p or {"accuracy_mean", "f1_macro_mean"}.issubset(cols):
        return "annotation"
    return "unknown"


def metric_disagreement(tables: List[CsvTable], baseline: str, warnings: WarningLog) -> List[Dict[str, object]]:
    rows_out: List[Dict[str, object]] = []
    checks = [
        ("auroc", "auprc", "AUROC improves but AUPRC drops"),
        ("auroc", "f1", "AUROC improves but F1 drops"),
        ("auroc", "precision_at_k", "AUROC improves but Precision@K drops"),
        ("accuracy", "f1_macro", "accuracy improves but F1-macro drops"),
    ]
    for table in tables:
        if "embedding" not in table.columns:
            warnings.add(f"Skipping metric disagreement for {table.path}: no embedding column.")
            continue
        task = detect_task(table)
        by_key: Dict[Tuple[Tuple[str, str], ...], List[Dict[str, str]]] = defaultdict(list)
        for row in table.rows:
            by_key[setting_key(row, table.columns)].append(row)
        for key, group in by_key.items():
            baselines = [r for r in group if r.get("embedding") == baseline]
            if not baselines:
                continue
            base = baselines[0]
            for row in group:
                emb = row.get("embedding", "")
                if emb == baseline:
                    continue
                for primary, secondary, label in checks:
                    primary_value, primary_col = get_metric(row, primary)
                    primary_base, _ = get_metric(base, primary)
                    secondary_value, secondary_col = get_metric(row, secondary)
                    secondary_base, _ = get_metric(base, secondary)
                    if primary_col is None or secondary_col is None:
                        continue
                    d_primary = delta(primary_value, primary_base, primary)
                    d_secondary = delta(secondary_value, secondary_base, secondary)
                    if d_primary is None or d_secondary is None:
                        continue
                    if delta_is_improvement(d_primary, primary) and delta_is_failure(d_secondary, secondary):
                        rows_out.append({
                            "task": task,
                            "source_file": str(table.path),
                            "setting": key_to_string(key),
                            "embedding": emb,
                            "baseline": baseline,
                            "primary_metric": primary_col,
                            "secondary_metric": secondary_col,
                            "primary_value": primary_value,
                            "primary_baseline": primary_base,
                            "primary_delta": d_primary,
                            "secondary_value": secondary_value,
                            "secondary_baseline": secondary_base,
                            "secondary_delta": d_secondary,
                            "failure_type": label,
                        })
        for primary, secondary, _ in checks:
            if not any(alias in table.columns for alias in METRIC_ALIASES[primary]) and any(alias in table.columns for alias in METRIC_ALIASES[secondary]):
                warnings.add(f"{table.path}: cannot test {primary} disagreement; required column is unavailable.")
    rows_out.sort(key=lambda r: (r["task"], r["failure_type"], float(r["secondary_delta"])))
    return rows_out


def protocol_sensitivity(transfer_tables: List[CsvTable], baseline: str, warnings: WarningLog) -> List[Dict[str, object]]:
    table = next((t for t in transfer_tables if "protocol" in t.columns and "embedding" in t.columns and ("mean_auprc" in t.columns or "auprc" in t.columns)), None)
    if table is None:
        warnings.add("Protocol sensitivity unavailable: no transfer_v2 table with protocol, embedding, and AUPRC columns.")
        return []
    metrics = [m for m in ("auroc", "auprc", "f1", "precision_at_k", "balanced_accuracy") if any(a in table.columns for a in METRIC_ALIASES[m])]
    if not metrics:
        warnings.add(f"Protocol sensitivity unavailable for {table.path}: no supported metric columns.")
        return []

    base_cols = [c for c in ("train_dataset", "test_dataset", "clf") if c in table.columns]
    grouped: Dict[Tuple[str, ...], List[Dict[str, str]]] = defaultdict(list)
    for row in table.rows:
        grouped[tuple(row.get(c, "") for c in base_cols)].append(row)

    out: List[Dict[str, object]] = []
    for group_key, group in grouped.items():
        for metric in metrics:
            values: Dict[Tuple[str, str], float] = {}
            for row in group:
                value, _ = get_metric(row, metric)
                if value is None:
                    continue
                values[(row.get("embedding", ""), row.get("protocol", ""))] = value
            protocol_embeddings: Dict[str, List[Tuple[str, float]]] = defaultdict(list)
            for (embedding, protocol), value in values.items():
                protocol_embeddings[protocol].append((embedding, value))
            ranks: Dict[Tuple[str, str], int] = {}
            for protocol, items in protocol_embeddings.items():
                reverse = metric_direction(metric) == "higher_is_better"
                for rank, (embedding, _) in enumerate(sorted(items, key=lambda x: x[1], reverse=reverse), start=1):
                    ranks[(embedding, protocol)] = rank
            embeddings = sorted({embedding for embedding, _protocol in values})
            native_winners = {emb for emb in embeddings if ranks.get((emb, "native")) == 1}
            topology_winners = {emb for emb in embeddings if ranks.get((emb, "topology_matched")) == 1}
            for embedding in embeddings:
                native = values.get((embedding, "native"))
                coverage = values.get((embedding, "coverage_matched"))
                strict = values.get((embedding, "strict"))
                topology = values.get((embedding, "topology_matched"))
                d_native_topology = delta(topology, native, metric) if native is not None and topology is not None else None
                d_coverage_strict = delta(strict, coverage, metric) if coverage is not None and strict is not None else None
                rank_native = ranks.get((embedding, "native"))
                rank_topology = ranks.get((embedding, "topology_matched"))
                rank_coverage = ranks.get((embedding, "coverage_matched"))
                rank_strict = ranks.get((embedding, "strict"))
                native_wins_topology_loses = embedding in native_winners and embedding not in topology_winners and topology is not None
                coverage_improves_vs_baseline = False
                strict_collapse = False
                if embedding != baseline:
                    base_cov = values.get((baseline, "coverage_matched"))
                    base_strict = values.get((baseline, "strict"))
                    d_cov_base = delta(coverage, base_cov, metric)
                    d_strict_base = delta(strict, base_strict, metric)
                    coverage_improves_vs_baseline = d_cov_base is not None and delta_is_improvement(d_cov_base, metric)
                    strict_collapse = d_strict_base is not None and delta_is_failure(d_strict_base, metric)
                rank_change = None
                if rank_native is not None and rank_topology is not None:
                    rank_change = rank_topology - rank_native
                sensitivity_score = max(abs(x) for x in [rank_change or 0, (rank_strict or 0) - (rank_coverage or 0)] + [0])
                out.append({
                    **{col: val for col, val in zip(base_cols, group_key)},
                    "metric": metric,
                    "embedding": embedding,
                    "native": native,
                    "coverage_matched": coverage,
                    "strict": strict,
                    "topology_matched": topology,
                    "delta_topology_minus_native": d_native_topology,
                    "delta_strict_minus_coverage": d_coverage_strict,
                    "rank_native": rank_native,
                    "rank_coverage_matched": rank_coverage,
                    "rank_strict": rank_strict,
                    "rank_topology_matched": rank_topology,
                    "rank_change_native_to_topology": rank_change,
                    "native_wins_topology_loses": native_wins_topology_loses,
                    "coverage_improves_strict_collapses": coverage_improves_vs_baseline and strict_collapse,
                    "protocol_sensitivity_score": sensitivity_score,
                    "source_file": str(table.path),
                })
    out.sort(key=lambda r: (-(abs(float(r.get("rank_change_native_to_topology") or 0))), r.get("metric", "")))
    return out


def load_class_balance(results_root: Path, warnings: WarningLog) -> Dict[Tuple[str, str], Dict[str, str]]:
    balance: Dict[Tuple[str, str], Dict[str, str]] = {}
    for path in results_root.glob("**/*class_balance*.csv"):
        table = read_csv(path, warnings)
        if table is None:
            continue
        if "dataset" not in table.columns or "negative_protocol" not in table.columns:
            continue
        for row in table.rows:
            balance[(row.get("dataset", ""), row.get("negative_protocol", ""))] = row
    return balance


def low_positive_grn(grn_tables: List[CsvTable], results_root: Path, warnings: WarningLog) -> List[Dict[str, object]]:
    balance = load_class_balance(results_root, warnings)
    out: List[Dict[str, object]] = []
    for table in grn_tables:
        if not {"dataset", "negative_protocol"}.issubset(table.columns):
            continue
        required_any = ["test_positive_ratio", "random_auprc_baseline", "auprc"]
        for col in required_any:
            if col not in table.columns:
                warnings.add(f"{table.path}: low-positive GRN analysis missing optional/expected column {col}.")
        seen = set()
        for row in table.rows:
            key = (row.get("dataset", ""), row.get("negative_protocol", ""), row.get("embedding", ""), row.get("clf", row.get("classifier", "")))
            if key in seen:
                continue
            seen.add(key)
            bal = balance.get((key[0], key[1]), {})
            pos_ratio = to_float(row.get("test_positive_ratio")) or to_float(bal.get("test_positive_ratio"))
            neg_pos = to_float(row.get("test_negative_to_positive_ratio")) or to_float(bal.get("test_negative_to_positive_ratio"))
            test_pos = to_float(bal.get("test_n_positive"))
            auprc, _ = get_metric(row, "auprc")
            random_base = to_float(row.get("random_auprc_baseline")) or to_float(bal.get("random_auprc_baseline"))
            lift = (auprc / random_base) if auprc is not None and random_base not in (None, 0.0) else None
            flags = []
            if pos_ratio is not None and pos_ratio < LOW_POSITIVE_RATIO:
                flags.append("low_positive_ratio")
            if test_pos is not None and test_pos < LOW_TEST_POSITIVES:
                flags.append("few_test_positives")
            if neg_pos is not None and neg_pos > HIGH_NEG_POS_RATIO:
                flags.append("high_negative_to_positive_ratio")
            if lift is not None and lift <= AUPRC_RANDOM_MULTIPLIER:
                flags.append("auprc_near_random")
            if flags:
                out.append({
                    "dataset": key[0],
                    "negative_protocol": key[1],
                    "embedding": key[2],
                    "clf": key[3],
                    "test_positive_ratio": pos_ratio,
                    "test_n_positive": test_pos,
                    "test_negative_to_positive_ratio": neg_pos,
                    "auprc": auprc,
                    "random_auprc_baseline": random_base,
                    "auprc_lift_over_random": lift,
                    "flags": ";".join(flags),
                    "source_file": str(table.path),
                })
    out.sort(key=lambda r: (float(r.get("test_positive_ratio") or 1), float(r.get("test_n_positive") or 1e9)))
    return out


def bin_fixed(value: Optional[float], low: float, high: float) -> str:
    if value is None:
        return "unknown"
    if value < low:
        return "low"
    if value < high:
        return "medium"
    return "high"


def topology_frequency_summary(transfer_tables: List[CsvTable], metadata_tables: List[CsvTable], baseline: str, warnings: WarningLog) -> List[Dict[str, object]]:
    perf = next((t for t in transfer_tables if "protocol" in t.columns and "embedding" in t.columns and ("mean_auprc" in t.columns or "auprc" in t.columns)), None)
    meta = next((t for t in metadata_tables if {"train_dataset", "test_dataset", "protocol"}.issubset(t.columns)), None)
    if perf is None or meta is None:
        warnings.add("Topology/frequency summary unavailable: missing transfer performance or metadata diagnostics.")
        return []
    meta_by_key: Dict[Tuple[str, str, str, str], List[Dict[str, str]]] = defaultdict(list)
    for row in meta.rows:
        meta_by_key[(row.get("train_dataset", ""), row.get("test_dataset", ""), row.get("protocol", ""), row.get("side", ""))].append(row)
    base_cols = [c for c in ("train_dataset", "test_dataset", "protocol", "clf") if c in perf.columns]
    perf_by_key: Dict[Tuple[str, ...], List[Dict[str, str]]] = defaultdict(list)
    for row in perf.rows:
        perf_by_key[tuple(row.get(c, "") for c in base_cols)].append(row)
    raw: List[Dict[str, object]] = []
    for key, group in perf_by_key.items():
        base_row = next((r for r in group if r.get("embedding") == baseline), None)
        base_auprc, _ = get_metric(base_row or {}, "auprc")
        values = dict(zip(base_cols, key))
        metas = meta_by_key.get((values.get("train_dataset", ""), values.get("test_dataset", ""), values.get("protocol", ""), "test"), [])
        if not metas:
            metas = meta_by_key.get((values.get("train_dataset", ""), values.get("test_dataset", ""), values.get("protocol", ""), ""), [])
        if not metas:
            continue
        m = metas[0]
        degree = to_float(m.get("mean_degree"))
        train_freq = to_float(m.get("mean_train_node_freq"))
        test_freq = to_float(m.get("mean_test_node_freq"))
        ratio = (test_freq / train_freq) if test_freq is not None and train_freq not in (None, 0.0) else None
        pos_ratio = to_float(m.get("pos_edge_ratio"))
        for row in group:
            auprc, _ = get_metric(row, "auprc")
            d = delta(auprc, base_auprc, "auprc")
            raw.append({
                "degree_bin": bin_fixed(degree, 0.5, 2.0),
                "train_freq_bin": bin_fixed(train_freq, 0.25, 1.0),
                "test_freq_bin": bin_fixed(test_freq, 0.05, 0.5),
                "test_train_freq_ratio_bin": bin_fixed(ratio, 0.5, 1.5),
                "protocol": values.get("protocol", ""),
                "embedding": row.get("embedding", ""),
                "auprc": auprc,
                "delta_auprc_vs_baseline": d,
                "mean_degree": degree,
                "mean_train_node_freq": train_freq,
                "mean_test_node_freq": test_freq,
                "test_train_freq_ratio": ratio,
                "tf_proxy_fraction": to_float(m.get("tf_proxy_fraction")),
                "pos_edge_ratio": pos_ratio,
                "hub_fraction": to_float(m.get("hub_fraction")),
            })
    grouped: Dict[Tuple[str, str, str, str, str, str], List[Dict[str, object]]] = defaultdict(list)
    for row in raw:
        grouped[(str(row["protocol"]), str(row["embedding"]), str(row["degree_bin"]), str(row["train_freq_bin"]), str(row["test_freq_bin"]), str(row["test_train_freq_ratio_bin"]))].append(row)
    out = []
    for key, rows in grouped.items():
        out.append({
            "protocol": key[0],
            "embedding": key[1],
            "degree_bin": key[2],
            "train_freq_bin": key[3],
            "test_freq_bin": key[4],
            "test_train_freq_ratio_bin": key[5],
            "n_settings": len(rows),
            "mean_auprc": mean(to_float(r.get("auprc")) for r in rows),
            "mean_delta_auprc_vs_baseline": mean(to_float(r.get("delta_auprc_vs_baseline")) for r in rows),
            "mean_degree": mean(to_float(r.get("mean_degree")) for r in rows),
            "mean_train_node_freq": mean(to_float(r.get("mean_train_node_freq")) for r in rows),
            "mean_test_node_freq": mean(to_float(r.get("mean_test_node_freq")) for r in rows),
            "mean_test_train_freq_ratio": mean(to_float(r.get("test_train_freq_ratio")) for r in rows),
            "mean_tf_proxy_fraction": mean(to_float(r.get("tf_proxy_fraction")) for r in rows),
            "mean_pos_edge_ratio": mean(to_float(r.get("pos_edge_ratio")) for r in rows),
            "mean_hub_fraction": mean(to_float(r.get("hub_fraction")) for r in rows),
        })
    out.sort(key=lambda r: (r["protocol"], r["embedding"], r["degree_bin"]))
    return out


def margin_collapse(all_tables: List[CsvTable], warnings: WarningLog) -> List[Dict[str, object]]:
    out: List[Dict[str, object]] = []
    source_pos_names = ("mean_pos_score_source", "source_pos_score_mean", "source_pos_mean", "train_pos_score_mean")
    source_neg_names = ("mean_neg_score_source", "source_neg_score_mean", "source_neg_mean", "train_neg_score_mean")
    target_pos_names = ("mean_pos_score_target", "target_pos_score_mean", "target_pos_mean", "test_pos_score_mean", "test_pos_cosine_mean")
    target_neg_names = ("mean_neg_score_target", "target_neg_score_mean", "target_neg_mean", "test_neg_score_mean", "test_neg_cosine_mean")
    found_partial = False
    for table in all_tables:
        sp = first_existing(table.columns, source_pos_names)
        sn = first_existing(table.columns, source_neg_names)
        tp = first_existing(table.columns, target_pos_names)
        tn = first_existing(table.columns, target_neg_names)
        if not (sp and sn and tp and tn):
            if tp and tn:
                found_partial = True
            continue
        for row in table.rows:
            source_pos = to_float(row.get(sp))
            source_neg = to_float(row.get(sn))
            target_pos = to_float(row.get(tp))
            target_neg = to_float(row.get(tn))
            if None in (source_pos, source_neg, target_pos, target_neg):
                continue
            margin_source = source_pos - source_neg
            margin_target = target_pos - target_neg
            delta_pos = target_pos - source_pos
            delta_neg = target_neg - source_neg
            delta_margin = margin_target - margin_source
            positive_collapse = delta_pos < 0 and abs(delta_pos) > abs(delta_neg)
            negative_drift = delta_neg > 0 and abs(delta_neg) >= abs(delta_pos)
            out.append({
                "task": detect_task(table),
                "source_file": str(table.path),
                "setting": key_to_string(setting_key(row, table.columns, drop=())),
                "embedding": row.get("embedding", ""),
                "mean_pos_score_source": source_pos,
                "mean_neg_score_source": source_neg,
                "margin_source": margin_source,
                "mean_pos_score_target": target_pos,
                "mean_neg_score_target": target_neg,
                "margin_target": margin_target,
                "delta_pos": delta_pos,
                "delta_neg": delta_neg,
                "delta_margin": delta_margin,
                "abs_shift_margin": abs(delta_margin),
                "dominant_shift": "positive_score_collapse" if positive_collapse else ("negative_score_drift" if negative_drift else "mixed_or_small_shift"),
            })
    if not out:
        if found_partial:
            warnings.add("Margin-collapse analysis found target score statistics but no source/train score statistics; source-target deltas were not fabricated.")
        else:
            warnings.add("Margin-collapse analysis unavailable: no compatible source/target score-statistic columns were found.")
    out.sort(key=lambda r: -float(r.get("abs_shift_margin") or 0))
    return out


def model_specific_vulnerabilities(tables: List[CsvTable], baseline: str, external: str, warnings: WarningLog) -> List[Dict[str, object]]:
    out: List[Dict[str, object]] = []
    metric_candidates = ("auprc", "auroc", "f1", "precision_at_k", "balanced_accuracy", "accuracy", "f1_macro", "pearson_r", "sign_acc", "mse", "rmse", "mae", "loss")
    for table in tables:
        if "embedding" not in table.columns:
            continue
        metrics = [m for m in metric_candidates if any(alias in table.columns for alias in METRIC_ALIASES[m])]
        if not metrics:
            warnings.add(f"Model-specific vulnerability analysis skipped {table.path}: no supported metric columns.")
            continue
        task = detect_task(table)
        by_key: Dict[Tuple[Tuple[str, str], ...], List[Dict[str, str]]] = defaultdict(list)
        for row in table.rows:
            by_key[setting_key(row, table.columns)].append(row)
        for key, group in by_key.items():
            comparators = {name: next((r for r in group if r.get("embedding") == name), None) for name in (baseline, external)}
            for row in group:
                emb = row.get("embedding", "")
                for comparator_name, comp in comparators.items():
                    if comp is None or emb == comparator_name:
                        continue
                    for metric in metrics:
                        value, col = get_metric(row, metric)
                        comp_value, _ = get_metric(comp, metric)
                        d = delta(value, comp_value, metric)
                        if d is None:
                            continue
                        is_failure = delta_is_failure(d, metric)
                        is_improvement = delta_is_improvement(d, metric)
                        small_test_warning, small_train_warning, diagnostic_only = perturbation_diagnostic_flags(task, row)
                        out.append({
                            "task": task,
                            "source_file": str(table.path),
                            "setting": key_to_string(key),
                            "embedding": emb,
                            "comparator": comparator_name,
                            "metric": col or metric,
                            "value": value,
                            "comparator_value": comp_value,
                            "delta_vs_comparator_positive_is_better": d,
                            "metric_direction": metric_direction(metric),
                            "is_failure": is_failure,
                            "is_improvement": is_improvement,
                            "failure_magnitude": delta_magnitude(d) if is_failure else 0,
                            "improvement_magnitude": delta_magnitude(d) if is_improvement else 0,
                            "small_test_warning": small_test_warning,
                            "small_train_warning": small_train_warning,
                            "diagnostic_only": diagnostic_only,
                            "severity_if_negative": delta_magnitude(d) if is_failure else 0,
                            "direction": "failure" if is_failure else ("improvement" if is_improvement else "tie"),
                        })
    # Keep the report manageable: worst and best per embedding/comparator/metric/task.
    grouped: Dict[Tuple[str, str, str, str], List[Dict[str, object]]] = defaultdict(list)
    for row in out:
        grouped[(str(row["task"]), str(row["embedding"]), str(row["comparator"]), str(row["metric"]))].append(row)
    trimmed: List[Dict[str, object]] = []
    for rows in grouped.values():
        failures = sorted([r for r in rows if r.get("is_failure") is True and r.get("diagnostic_only") is not True], key=lambda r: -float(r.get("failure_magnitude") or 0))[:10]
        improvements = sorted([r for r in rows if r.get("is_improvement") is True and r.get("diagnostic_only") is not True], key=lambda r: -float(r.get("improvement_magnitude") or 0))[:10]
        diagnostics = sorted([r for r in rows if r.get("diagnostic_only") is True], key=lambda r: -(float(r.get("failure_magnitude") or 0) + float(r.get("improvement_magnitude") or 0)))[:10]
        trimmed.extend(failures + improvements + diagnostics)
    trimmed.sort(key=lambda r: (r["embedding"], r["comparator"], r["task"], r["metric"], -float(r.get("failure_magnitude") or 0), -float(r.get("improvement_magnitude") or 0)))
    return trimmed


def maybe_make_plots(out_dir: Path, metric_rows: List[Dict[str, object]], protocol_rows: List[Dict[str, object]], low_pos_rows: List[Dict[str, object]], margin_rows: List[Dict[str, object]], warnings: WarningLog) -> None:
    try:
        import matplotlib.pyplot as plt  # type: ignore
    except Exception as exc:  # pragma: no cover - optional dependency
        warnings.add(f"Optional plots skipped: matplotlib is unavailable ({exc}).")
        return
    if metric_rows:
        xs = [float(r["primary_delta"]) for r in metric_rows if r.get("primary_metric") in {"auroc", "mean_auroc"}]
        ys = [float(r["secondary_delta"]) for r in metric_rows if r.get("primary_metric") in {"auroc", "mean_auroc"}]
        if xs and len(xs) == len(ys):
            plt.figure(figsize=(6, 4))
            plt.axhline(0, color="grey", linewidth=0.8)
            plt.axvline(0, color="grey", linewidth=0.8)
            plt.scatter(xs, ys, alpha=0.7)
            plt.xlabel("AUROC delta vs baseline")
            plt.ylabel("Secondary metric delta vs baseline")
            plt.title("Metric-disagreement failures")
            plt.tight_layout()
            plt.savefig(out_dir / "auroc_delta_vs_secondary_delta.png", dpi=160)
            plt.close()
    if low_pos_rows:
        xs = [to_float(r.get("test_positive_ratio")) for r in low_pos_rows]
        ys = [to_float(r.get("auprc")) for r in low_pos_rows]
        pairs = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
        if pairs:
            plt.figure(figsize=(6, 4))
            plt.scatter([p[0] for p in pairs], [p[1] for p in pairs], alpha=0.7)
            plt.xlabel("Test positive ratio")
            plt.ylabel("AUPRC")
            plt.title("Sparse GRN stress-test settings")
            plt.tight_layout()
            plt.savefig(out_dir / "positive_ratio_vs_auprc.png", dpi=160)
            plt.close()
    if margin_rows:
        pairs = [(to_float(r.get("margin_source")), to_float(r.get("margin_target"))) for r in margin_rows]
        pairs = [(x, y) for x, y in pairs if x is not None and y is not None]
        if pairs:
            plt.figure(figsize=(6, 4))
            plt.scatter([p[0] for p in pairs], [p[1] for p in pairs], alpha=0.7)
            plt.xlabel("Source margin")
            plt.ylabel("Target margin")
            plt.title("Margin transfer collapse")
            plt.tight_layout()
            plt.savefig(out_dir / "margin_source_vs_target.png", dpi=160)
            plt.close()


def top_n(rows: List[Dict[str, object]], n: int, key) -> List[Dict[str, object]]:
    return sorted(rows, key=key)[:n]


def write_markdown(path: Path, *, metric_rows: List[Dict[str, object]], protocol_rows: List[Dict[str, object]], low_pos_rows: List[Dict[str, object]], topology_rows: List[Dict[str, object]], margin_rows: List[Dict[str, object]], vuln_rows: List[Dict[str, object]], warnings: WarningLog, baseline: str, external: str) -> None:
    lines: List[str] = []
    lines.append("# Failure-subset analysis")
    lines.append("")
    lines.append("This diagnostic report analyzes failure modes on top of existing benchmark CSVs. It should not be read as a new benchmark protocol or as evidence that any model is globally better across tasks.")
    lines.append("")
    lines.append("## Main findings")
    lines.append(f"- Metric-disagreement failures found: **{len(metric_rows)}**.")
    lines.append(f"- Protocol-sensitivity rows summarized: **{len(protocol_rows)}**.")
    lines.append(f"- Low-positive / sparse GRN warnings: **{len(low_pos_rows)}**.")
    lines.append(f"- Topology/frequency summary rows: **{len(topology_rows)}**.")
    lines.append(f"- Margin-collapse rows: **{len(margin_rows)}**.")
    lines.append(f"- Model-specific vulnerability rows: **{len(vuln_rows)}** comparing against `{baseline}` and `{external}` where available.")
    lines.append("")

    lines.append("Perturbation folds with n_test < 5 or n_train < 20 are treated as diagnostic only and excluded from headline failure tables.")
    lines.append("")

    lines.append("## Top failure subsets")
    if vuln_rows:
        worst = top_n([r for r in vuln_rows if r.get("is_failure") is True and r.get("diagnostic_only") is not True], 10, key=lambda r: -float(r.get("failure_magnitude") or 0))
        lines.append("| embedding | comparator | task | metric | delta | setting |")
        lines.append("|---|---|---|---:|---:|---|")
        for r in worst:
            lines.append(f"| {r.get('embedding','')} | {r.get('comparator','')} | {r.get('task','')} | {r.get('metric','')} | {fmt(r.get('delta_vs_comparator_positive_is_better'))} | {str(r.get('setting',''))[:180]} |")
    else:
        lines.append("No model-specific vulnerability rows were available.")
    lines.append("")

    lines.append("## Protocol sensitivity summary")
    flagged_protocol = [r for r in protocol_rows if str(r.get("native_wins_topology_loses")) == "True" or str(r.get("coverage_improves_strict_collapses")) == "True" or abs(float(r.get("rank_change_native_to_topology") or 0)) >= 2]
    lines.append(f"- Flagged protocol-sensitive cases: **{len(flagged_protocol)}**.")
    if flagged_protocol:
        lines.append("| embedding | metric | native | topology_matched | rank_native | rank_topology | flags |")
        lines.append("|---|---|---:|---:|---:|---:|---|")
        for r in flagged_protocol[:10]:
            flags = []
            if str(r.get("native_wins_topology_loses")) == "True":
                flags.append("native_win_topology_loss")
            if str(r.get("coverage_improves_strict_collapses")) == "True":
                flags.append("coverage_gain_strict_collapse")
            if abs(float(r.get("rank_change_native_to_topology") or 0)) >= 2:
                flags.append("rank_change>=2")
            lines.append(f"| {r.get('embedding','')} | {r.get('metric','')} | {fmt(r.get('native'))} | {fmt(r.get('topology_matched'))} | {fmt(r.get('rank_native'),0)} | {fmt(r.get('rank_topology_matched'),0)} | {';'.join(flags)} |")
    lines.append("")

    lines.append("## Metric disagreement summary")
    if metric_rows:
        counts = defaultdict(int)
        for r in metric_rows:
            counts[str(r.get("failure_type"))] += 1
        for label, count in sorted(counts.items()):
            lines.append(f"- {label}: **{count}** rows.")
        lines.append("")
        lines.append("| embedding | task | failure_type | primary_delta | secondary_delta | setting |")
        lines.append("|---|---|---|---:|---:|---|")
        for r in metric_rows[:10]:
            lines.append(f"| {r.get('embedding','')} | {r.get('task','')} | {r.get('failure_type','')} | {fmt(r.get('primary_delta'))} | {fmt(r.get('secondary_delta'))} | {str(r.get('setting',''))[:180]} |")
    else:
        lines.append("No AUROC/AUPRC, AUROC/F1, AUROC/Precision@K, or accuracy/F1-macro disagreements were found in available comparable rows.")
    lines.append("")

    lines.append("## Low-positive GRN warnings")
    if low_pos_rows:
        flag_counts = defaultdict(int)
        for r in low_pos_rows:
            for flag in str(r.get("flags", "")).split(";"):
                if flag:
                    flag_counts[flag] += 1
        for flag, count in sorted(flag_counts.items()):
            lines.append(f"- {flag}: **{count}** rows.")
        lines.append("")
        lines.append("These settings should be treated as diagnostic/stress-test subsets, not headline evidence, especially when AUPRC is close to the random positive-rate baseline.")
    else:
        lines.append("No GRN sparse-setting warnings were triggered with the current thresholds.")
    lines.append("")

    lines.append("## Topology/frequency-shift summary")
    if topology_rows:
        worst = top_n(topology_rows, 10, key=lambda r: float(r.get("mean_delta_auprc_vs_baseline") or 0))
        lines.append("| protocol | embedding | degree_bin | train_freq_bin | test_freq_bin | ratio_bin | mean_delta_auprc | n |")
        lines.append("|---|---|---|---|---|---|---:|---:|")
        for r in worst:
            lines.append(f"| {r.get('protocol','')} | {r.get('embedding','')} | {r.get('degree_bin','')} | {r.get('train_freq_bin','')} | {r.get('test_freq_bin','')} | {r.get('test_train_freq_ratio_bin','')} | {fmt(r.get('mean_delta_auprc_vs_baseline'))} | {r.get('n_settings','')} |")
    else:
        lines.append("No compatible topology/frequency metadata was available or joinable.")
    lines.append("")

    lines.append("## Margin-collapse summary")
    if margin_rows:
        counts = defaultdict(int)
        for r in margin_rows:
            counts[str(r.get("dominant_shift"))] += 1
        for label, count in sorted(counts.items()):
            lines.append(f"- {label}: **{count}** rows.")
        lines.append("")
        lines.append("Settings labeled `positive_score_collapse` are cases where target-domain failure is more consistent with positives losing score than negatives drifting upward.")
    else:
        lines.append("No source/target score-statistic pairs were available; margin deltas were not fabricated from target-only score summaries.")
    lines.append("")

    lines.append("## Recommended interpretation")
    lines.append("- Do not declare a model globally better because it wins one metric or one protocol.")
    lines.append("- Treat AUROC gains paired with AUPRC/F1/Precision@K losses as suspicious: global separability may improve while positive retrieval worsens.")
    lines.append("- Treat native gains that disappear under topology-matched evaluation as protocol-sensitive rather than robust.")
    lines.append("- Treat very sparse GRN settings and near-random AUPRC as stress tests; they are useful for diagnosing instability but weak as headline evidence.")
    lines.append("- Use recurring topology/frequency and score-collapse failures to motivate task-aware contrastive objectives, especially perturbation-effect contrastive losses and GRN topology-aware edge contrastive losses.")
    lines.append("")

    if warnings.messages:
        lines.append("## Warnings")
        for warning in warnings.messages:
            lines.append(f"- {warning}")
        lines.append("")

    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    args = parse_args()
    results_root = Path(args.results_root)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    warnings = WarningLog()

    grn_tables = discover_csvs(results_root, args.grn_results, ["**/*grn*_results.csv", "**/grn_*results*.csv"], warnings)
    transfer_tables = discover_csvs(results_root, args.transfer_results, ["**/embedding_transfer_summary_v2.csv", "**/embedding_transfer_seed_results_v2.csv"], warnings)
    perturb_tables = discover_csvs(results_root, args.perturbation_results, ["**/perturbation_regression_results.csv", "**/perturbation_regression_fold_results.csv"], warnings)
    annotation_tables = discover_csvs(results_root, args.annotation_results, ["**/annotation*/benchmark_results.csv"], warnings)
    metadata_tables = discover_csvs(results_root, args.metadata, ["**/transfer_control_v2_diagnostics.csv", "**/pair_diagnostics.csv"], warnings)

    all_result_tables = grn_tables + transfer_tables + perturb_tables + annotation_tables
    if not all_result_tables:
        warnings.add(f"No result CSVs discovered under {results_root}.")

    metric_rows = metric_disagreement(all_result_tables, args.baseline, warnings)
    protocol_rows = protocol_sensitivity(transfer_tables, args.baseline, warnings)
    low_pos_rows = low_positive_grn(grn_tables, results_root, warnings)
    topology_rows = topology_frequency_summary(transfer_tables, metadata_tables, args.baseline, warnings)
    margin_rows = margin_collapse(all_result_tables, warnings)
    vuln_rows = model_specific_vulnerabilities(all_result_tables, args.baseline, args.external_baseline, warnings)

    write_csv(out_dir / "metric_disagreement_failures.csv", metric_rows, [
        "task", "source_file", "setting", "embedding", "baseline", "primary_metric", "secondary_metric", "primary_value", "primary_baseline", "primary_delta", "secondary_value", "secondary_baseline", "secondary_delta", "failure_type",
    ])
    write_csv(out_dir / "protocol_sensitivity.csv", protocol_rows, [
        "train_dataset", "test_dataset", "clf", "metric", "embedding", "native", "coverage_matched", "strict", "topology_matched", "delta_topology_minus_native", "delta_strict_minus_coverage", "rank_native", "rank_coverage_matched", "rank_strict", "rank_topology_matched", "rank_change_native_to_topology", "native_wins_topology_loses", "coverage_improves_strict_collapses", "protocol_sensitivity_score", "source_file",
    ])
    write_csv(out_dir / "low_positive_grn_settings.csv", low_pos_rows, [
        "dataset", "negative_protocol", "embedding", "clf", "test_positive_ratio", "test_n_positive", "test_negative_to_positive_ratio", "auprc", "random_auprc_baseline", "auprc_lift_over_random", "flags", "source_file",
    ])
    write_csv(out_dir / "topology_frequency_failure_summary.csv", topology_rows, [
        "protocol", "embedding", "degree_bin", "train_freq_bin", "test_freq_bin", "test_train_freq_ratio_bin", "n_settings", "mean_auprc", "mean_delta_auprc_vs_baseline", "mean_degree", "mean_train_node_freq", "mean_test_node_freq", "mean_test_train_freq_ratio", "mean_tf_proxy_fraction", "mean_pos_edge_ratio", "mean_hub_fraction",
    ])
    write_csv(out_dir / "margin_collapse_summary.csv", margin_rows, [
        "task", "source_file", "setting", "embedding", "mean_pos_score_source", "mean_neg_score_source", "margin_source", "mean_pos_score_target", "mean_neg_score_target", "margin_target", "delta_pos", "delta_neg", "delta_margin", "abs_shift_margin", "dominant_shift",
    ])
    model_specific_fields = [
        "task", "source_file", "setting", "embedding", "comparator", "metric", "value", "comparator_value", "delta_vs_comparator_positive_is_better", "metric_direction", "is_failure", "is_improvement", "failure_magnitude", "improvement_magnitude", "small_test_warning", "small_train_warning", "diagnostic_only", "severity_if_negative", "direction",
    ]
    write_csv(out_dir / "model_specific_vulnerable_settings.csv", vuln_rows, model_specific_fields)
    write_csv(out_dir / "fold_level_extreme_diagnostics.csv", [r for r in vuln_rows if r.get("diagnostic_only") is True], model_specific_fields)

    if args.make_plots:
        maybe_make_plots(out_dir, metric_rows, protocol_rows, low_pos_rows, margin_rows, warnings)

    write_markdown(
        out_dir / "failure_summary.md",
        metric_rows=metric_rows,
        protocol_rows=protocol_rows,
        low_pos_rows=low_pos_rows,
        topology_rows=topology_rows,
        margin_rows=margin_rows,
        vuln_rows=vuln_rows,
        warnings=warnings,
        baseline=args.baseline,
        external=args.external_baseline,
    )


if __name__ == "__main__":
    main()
