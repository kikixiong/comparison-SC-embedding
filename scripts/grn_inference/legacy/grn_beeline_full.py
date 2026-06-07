#!/usr/bin/env python3
"""
GRN Benchmark on BEELINE datasets - Embedding Only
====================================================
Downloads BEELINE benchmark data from Zenodo, processes all datasets,
and evaluates gene embeddings on GRN prediction.

Cell types: hESC, hHep, mDC, mESC, mHSC-E, mHSC-GM, mHSC-L
Network types: Specific ChIP-seq, Non-Specific ChIP-seq, STRING
Gene counts: 500, 1000
"""

import os, sys, json, gzip, zipfile, warnings, random, re
from pathlib import Path
import numpy as np
import pandas as pd
import torch
import urllib.request
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, average_precision_score, f1_score, confusion_matrix

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common.embedding_config import build_primary_embeddings, merge_incremental_results
from common.combined_results_markdown import update_combined_summary_markdown
warnings.filterwarnings("ignore")

# =============================================================
# Config
# =============================================================
BASE_DIR = '/root/autodl-tmp/projects/comparison-SC-embedding/scbenchmark'
BEELINE_DIR = '/root/autodl-tmp/projects/comparison-SC-embedding/BEELINE'
SCGREAT_DIR = '/root/autodl-tmp/projects/scGREAT'
OUTPUT_DIR = '/root/autodl-tmp/projects/comparison-SC-embedding/grn_benchmark'
os.makedirs(OUTPUT_DIR, exist_ok=True)
REPO_ROOT = Path(__file__).resolve().parents[3]
RESULTS_DIR = os.path.join(REPO_ROOT, 'results', 'grn_beeline_full')
os.makedirs(RESULTS_DIR, exist_ok=True)
# Keep the user-requested spelling for the diagnostics directory name.
DIAGNOSTICS_DIR = os.path.join(RESULTS_DIR, 'diagnotics')
os.makedirs(DIAGNOSTICS_DIR, exist_ok=True)

LOG_FILE = os.path.join(RESULTS_DIR, 'grn_beeline_full.log')
VOCAB_PATH = f'{BASE_DIR}/vocab.json'

EMBEDDINGS = build_primary_embeddings(BASE_DIR)

# Cell type -> expression dir, species, specific network file
CELL_CONFIGS = {
    'hESC': {
        'expr_dir': 'BEELINE-data/inputs/scRNA-Seq/hESC',
        'species': 'human',
        'specific_net': 'hESC-ChIP-seq-network.csv',
    },
    'hHep': {
        'expr_dir': 'BEELINE-data/inputs/scRNA-Seq/hHep',
        'species': 'human',
        'specific_net': 'HepG2-ChIP-seq-network.csv',
    },
    'mDC': {
        'expr_dir': 'BEELINE-data/inputs/scRNA-Seq/mDC',
        'species': 'mouse',
        'specific_net': 'mDC-ChIP-seq-network.csv',
    },
    'mESC': {
        'expr_dir': 'BEELINE-data/inputs/scRNA-Seq/mESC',
        'species': 'mouse',
        'specific_net': 'mESC-ChIP-seq-network.csv',
    },
    'mHSC-E': {
        'expr_dir': 'BEELINE-data/inputs/scRNA-Seq/mHSC-E',
        'species': 'mouse',
        'specific_net': 'mHSC-ChIP-seq-network.csv',
    },
    'mHSC-GM': {
        'expr_dir': 'BEELINE-data/inputs/scRNA-Seq/mHSC-GM',
        'species': 'mouse',
        'specific_net': 'mHSC-ChIP-seq-network.csv',
    },
    'mHSC-L': {
        'expr_dir': 'BEELINE-data/inputs/scRNA-Seq/mHSC-L',
        'species': 'mouse',
        'specific_net': 'mHSC-ChIP-seq-network.csv',
    },
}

# Network types per species
NETWORK_TYPES = {
    'human': {
        'Specific': None,   # filled per cell type
        'Non-Specific': 'Non-specific-ChIP-seq-network.csv',
        'STRING': 'STRING-network.csv',
    },
    'mouse': {
        'Specific': None,
        'Non-Specific': 'Non-Specific-ChIP-seq-network.csv',
        'STRING': 'STRING-network.csv',
    },
}

N_HVGS = [500, 1000]
# Negative protocols:
# - tf_stratified_1to10: controlled primary protocol that samples up to 10 negatives per positive per TF/split.
# - full_candidate: legacy stress-test protocol that keeps all non-target genes as candidate negatives.
# Override with GRN_NEGATIVE_PROTOCOLS="tf_stratified_1to10,full_candidate".
NEGATIVE_PROTOCOL_SPECS = {
    'tf_stratified_1to1': {'mode': 'tf_stratified_fixed_ratio', 'neg_pos_ratio': 1},
    'tf_stratified_1to5': {'mode': 'tf_stratified_fixed_ratio', 'neg_pos_ratio': 5},
    'tf_stratified_1to10': {'mode': 'tf_stratified_fixed_ratio', 'neg_pos_ratio': 10},
    'full_candidate': {'mode': 'full_candidate', 'neg_pos_ratio': None},
}
DEFAULT_NEGATIVE_PROTOCOLS = ['tf_stratified_1to10', 'full_candidate']


# Validation is not used for model selection in this script; train+validation are
# combined before fitting. Keep the historical combined-train fraction (~77%)
# while avoiding a hard-coded 10% validation split that can starve sparse TFs.
DEFAULT_SPLIT_RATIOS = {'train': 0.77, 'validation': 0.0}


def resolve_split_ratios():
    """Resolve train/validation split ratios.

    Override with GRN_SPLIT_RATIOS="train,validation" (for example "0.77,0.00").
    The remaining fraction is used for test. Ratios are intentionally configurable
    because hard-coding a validation fraction can create pathological sparse
    split behavior for TFs with few targets.
    """
    raw = os.environ.get('GRN_SPLIT_RATIOS', '').strip()
    if not raw:
        return DEFAULT_SPLIT_RATIOS['train'], DEFAULT_SPLIT_RATIOS['validation']
    parts = [p.strip() for p in raw.split(',') if p.strip()]
    if len(parts) != 2:
        raise ValueError('GRN_SPLIT_RATIOS must be formatted as "train_ratio,validation_ratio"')
    train_ratio, validation_ratio = [float(p) for p in parts]
    if train_ratio <= 0 or validation_ratio < 0 or train_ratio + validation_ratio >= 1:
        raise ValueError('GRN split ratios must satisfy train > 0, validation >= 0, train + validation < 1')
    return train_ratio, validation_ratio


def resolve_negative_protocols():
    raw = os.environ.get('GRN_NEGATIVE_PROTOCOLS', '').strip()
    names = [p.strip() for p in raw.split(',') if p.strip()] if raw else DEFAULT_NEGATIVE_PROTOCOLS
    invalid = [p for p in names if p not in NEGATIVE_PROTOCOL_SPECS]
    if invalid:
        valid = ', '.join(sorted(NEGATIVE_PROTOCOL_SPECS))
        raise ValueError(f"Unknown negative protocol(s): {invalid}. Valid options: {valid}")
    return [(name, NEGATIVE_PROTOCOL_SPECS[name]) for name in names]

# Historical extras (difference_v3/GF/random/BioBERT) are intentionally disabled for config consistency.
EMBED_ORDER = ['minus', 'baseline', 'scGPT_human', 'v4_bias_rec_best', 'v4_plain_best', 'v4_type_pe_best', 'scconcept', 'scconcept_encoded', 'cl_scratch_v5', 'cl_v6_fair']
def log(msg):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f'[{ts}] {msg}'
    print(line, flush=True)
    with open(LOG_FILE, 'a') as f:
        f.write(line + '\n')


def _style_metric_matrix(pivot, higher_is_better=True):
    """Style matrix where rows=embedding, cols=dataset/aggregate.
    Per column: red bold = best; bold = better than baseline.
    """
    styled = {}
    for emb in pivot.index:
        styled[emb] = {}
        for ds in pivot.columns:
            v = pivot.at[emb, ds]
            if pd.isna(v):
                styled[emb][ds] = '-'
                continue
            txt = f'{v:.4f}'
            col = pivot[ds].dropna()
            best = col.max() if higher_is_better else col.min() if not col.empty else np.nan
            baseline = pivot.at['baseline', ds] if 'baseline' in pivot.index else np.nan
            better_than_baseline = (v > baseline) if higher_is_better else (v < baseline)
            if pd.notna(best) and np.isclose(v, best):
                styled[emb][ds] = f'<span style="color:red"><strong>{txt}</strong></span>'
            elif pd.notna(baseline) and better_than_baseline:
                styled[emb][ds] = f'**{txt}**'
            else:
                styled[emb][ds] = txt
    return styled


def _collapse_dataset_label(name):
    """Collapse transfer datasets like A->B, A->C into A for table display."""
    if not isinstance(name, str):
        return name
    return name.split('->', 1)[0].strip()


def _dataset_size_label(name):
    """Return the terminal gene-count/HVG suffix so _500 and _1000 aggregate separately."""
    if not isinstance(name, str):
        return "unknown"
    collapsed = _collapse_dataset_label(name)
    match = re.search(r"_?(\d+)$", collapsed)
    return match.group(1) if match else "unknown"


def _infer_network_group(dataset_name):
    """Infer network group from dataset label for conference table split."""
    if not isinstance(dataset_name, str):
        return None
    name_u = dataset_name.upper()
    if '_STRING_' in name_u:
        return 'STRING'
    if '_NON-SPECIFIC_' in name_u:
        return 'Non-Specific'
    if '_SPECIFIC_' in name_u:
        return 'Specific'
    return None


PRIMARY_METRICS = ['auroc', 'auprc', 'auprc_lift']
SUPPLEMENTARY_METRICS = ['precision_at_k', 'recall_at_k', 'f1', 'specificity']
DIAGNOSTIC_METRICS = [
    'random_auprc_baseline',
    'test_positive_ratio',
    'test_negative_to_positive_ratio',
    'delta_auprc_vs_baseline',
    'lift_ratio_vs_baseline',
    'delta_precision_at_k_vs_baseline',
    'delta_recall_at_k_vs_baseline',
    'test_cosine_delta',
    'test_l2_delta',
    'test_pos_cosine_mean',
    'test_neg_cosine_mean',
    'test_pos_l2_mean',
    'test_neg_l2_mean',
]


def _split_label_diagnostics(prefix, labels):
    """Return class-balance diagnostics for one labeled split."""
    labels = np.asarray(labels).astype(int) if labels is not None else np.array([], dtype=int)
    n_total = int(len(labels))
    n_positive = int(np.sum(labels == 1)) if n_total else 0
    n_negative = int(np.sum(labels == 0)) if n_total else 0
    positive_ratio = n_positive / n_total if n_total else np.nan
    negative_to_positive_ratio = n_negative / n_positive if n_positive else np.nan
    return {
        f'{prefix}_n_total': n_total,
        f'{prefix}_n_positive': n_positive,
        f'{prefix}_n_negative': n_negative,
        f'{prefix}_positive_ratio': positive_ratio,
        f'{prefix}_negative_to_positive_ratio': negative_to_positive_ratio,
    }


def build_dataset_diagnostic(ds_name, source, gene_list, train_labels, val_labels, test_labels,
                             n_positive_edges=None, n_tfs=None, network_path=None,
                             expression_path=None, n_hvg=None, negative_protocol='',
                             negative_sampling_mode='', target_neg_pos_ratio=None,
                             network_diagnostics=None):
    """Build one dataset-level diagnostics row.

    AUPRC is highly sensitive to the positive class prevalence; the test split
    positive ratio is therefore also the random-ranking AUPRC baseline.
    """
    all_train_labels = np.concatenate([
        np.asarray(train_labels).astype(int),
        np.asarray(val_labels).astype(int),
    ]) if len(val_labels) else np.asarray(train_labels).astype(int)

    row = {
        'dataset': ds_name,
        'source': source,
        'network_group': _infer_network_group(ds_name) or source,
        'n_genes': int(len(gene_list)),
        'n_positive_edges_after_filter': int(n_positive_edges) if n_positive_edges is not None else np.nan,
        'n_tfs_after_filter': int(n_tfs) if n_tfs is not None else np.nan,
        'n_hvg': int(n_hvg) if n_hvg is not None else np.nan,
        'negative_protocol': negative_protocol or '',
        'negative_sampling_mode': negative_sampling_mode or '',
        'target_negative_to_positive_ratio': target_neg_pos_ratio if target_neg_pos_ratio is not None else np.nan,
        'network_path': network_path or '',
        'expression_path': expression_path or '',
    }
    if network_diagnostics:
        row.update(network_diagnostics)
    row.update(_split_label_diagnostics('train', train_labels))
    row.update(_split_label_diagnostics('validation', val_labels))
    row.update(_split_label_diagnostics('combined_train', all_train_labels))
    row.update(_split_label_diagnostics('test', test_labels))
    row['random_auprc_baseline'] = row['test_positive_ratio']
    return row



def _infer_n_hvg(dataset_name):
    """Infer HVG count from labels ending with _500/_1000 before optional decorations."""
    if not isinstance(dataset_name, str):
        return np.nan
    clean = dataset_name.split('[', 1)[0].strip()
    tail = clean.rsplit('_', 1)[-1]
    try:
        return int(tail)
    except ValueError:
        return np.nan



def ensure_auprc_lift(df):
    """Ensure AUPRC lift and its random-ranking baseline are present per result row."""
    if df is None or len(df) == 0:
        return df
    out = df.copy()
    if 'random_auprc_baseline' not in out.columns:
        out['random_auprc_baseline'] = np.nan
    if 'test_positive_ratio' not in out.columns:
        out['test_positive_ratio'] = out['random_auprc_baseline']

    baseline = out['random_auprc_baseline']
    missing_baseline = baseline.isna()
    out.loc[missing_baseline, 'random_auprc_baseline'] = out.loc[missing_baseline, 'test_positive_ratio']
    out['test_positive_ratio'] = out['random_auprc_baseline']

    if 'auprc' in out.columns:
        baseline = out['random_auprc_baseline']
        out['auprc_lift'] = np.where(
            pd.notna(baseline) & (baseline > 0),
            out['auprc'] / baseline,
            np.nan,
        )
    elif 'auprc_lift' not in out.columns:
        out['auprc_lift'] = np.nan
    return out

def add_baseline_comparisons(df):
    """Add per-dataset/protocol/classifier deltas relative to the baseline embedding."""
    if df is None or len(df) == 0 or 'embedding' not in df.columns:
        return df
    out = df.copy()
    for col in [
        'delta_auprc_vs_baseline',
        'lift_ratio_vs_baseline',
        'delta_precision_at_k_vs_baseline',
        'delta_recall_at_k_vs_baseline',
    ]:
        if col not in out.columns:
            out[col] = np.nan

    group_cols = ['dataset', 'clf']
    if 'negative_protocol' in out.columns:
        group_cols.insert(1, 'negative_protocol')
    baseline_cols = [c for c in ['auprc', 'auprc_lift', 'precision_at_k', 'recall_at_k'] if c in out.columns]
    if not baseline_cols:
        return out

    base = out[out['embedding'] == 'baseline'][group_cols + baseline_cols].copy()
    if base.empty:
        return out
    rename = {c: f'baseline_{c}' for c in baseline_cols}
    base = base.rename(columns=rename)
    out = out.merge(base, on=group_cols, how='left')

    if 'auprc' in out.columns and 'baseline_auprc' in out.columns:
        out['delta_auprc_vs_baseline'] = out['auprc'] - out['baseline_auprc']
    if 'auprc_lift' in out.columns and 'baseline_auprc_lift' in out.columns:
        denom = out['baseline_auprc_lift']
        out['lift_ratio_vs_baseline'] = np.where(
            pd.notna(denom) & (denom > 0), out['auprc_lift'] / denom, np.nan)
    if 'precision_at_k' in out.columns and 'baseline_precision_at_k' in out.columns:
        out['delta_precision_at_k_vs_baseline'] = out['precision_at_k'] - out['baseline_precision_at_k']
    if 'recall_at_k' in out.columns and 'baseline_recall_at_k' in out.columns:
        out['delta_recall_at_k_vs_baseline'] = out['recall_at_k'] - out['baseline_recall_at_k']

    return out.drop(columns=[c for c in out.columns if c.startswith('baseline_')])


def validate_protocol_prevalence(dataset_diagnostics):
    """Warn if full_candidate prevalence exceeds the controlled protocol for a dataset."""
    diag_df = pd.DataFrame(dataset_diagnostics)
    if diag_df.empty or 'negative_protocol' not in diag_df.columns:
        return
    if 'test_positive_ratio' not in diag_df.columns:
        return
    pivot = diag_df.pivot_table(
        index='dataset', columns='negative_protocol', values='test_positive_ratio', aggfunc='first')
    if {'full_candidate', 'tf_stratified_1to10'}.issubset(set(pivot.columns)):
        suspicious = pivot[pivot['full_candidate'] > pivot['tf_stratified_1to10']]
        for ds, row in suspicious.iterrows():
            log(
                f"WARNING: full_candidate positive ratio exceeds tf_stratified_1to10 for {ds}: "
                f"full_candidate={row['full_candidate']:.6f}, "
                f"tf_stratified_1to10={row['tf_stratified_1to10']:.6f}")


def write_full_candidate_interpretation_md(results_df):
    """Write a full-candidate-specific AUPRC interpretation summary."""
    out_path = os.path.join(DIAGNOSTICS_DIR, 'full_candidate_auprc_interpretation.md')
    lines = [
        '# Full-candidate AUPRC interpretation',
        '',
        'Under `full_candidate` negative sampling, raw AUPRC is expected to be much lower than under `tf_stratified_1to10` because the positive edge ratio is much smaller. The random-ranking AUPRC baseline equals the test positive ratio. Therefore, full_candidate results should be interpreted using AUPRC lift and relative improvement over baseline, not raw AUPRC alone.',
        '',
    ]
    if results_df is None or len(results_df) == 0 or 'negative_protocol' not in results_df.columns:
        lines += ['No protocol-aware results are available.', '']
        with open(out_path, 'w') as f:
            f.write('\n'.join(lines) + '\n')
        return

    sub = results_df[results_df['negative_protocol'] == 'full_candidate'].copy()
    if sub.empty:
        lines += ['No `full_candidate` rows are available.', '']
        with open(out_path, 'w') as f:
            f.write('\n'.join(lines) + '\n')
        return

    sub['network_group'] = sub['dataset'].map(lambda x: _infer_network_group(x) or 'other')
    sub['n_hvg'] = sub['dataset'].map(_infer_n_hvg)
    metrics = [
        'auprc', 'random_auprc_baseline', 'auprc_lift', 'auprc_gain',
        'delta_auprc_vs_baseline', 'test_positive_ratio', 'test_negative_to_positive_ratio',
    ]
    metrics = [m for m in metrics if m in sub.columns]
    if not metrics:
        lines += ['No AUPRC interpretation metrics are available.', '']
        with open(out_path, 'w') as f:
            f.write('\n'.join(lines) + '\n')
        return

    summary = (
        sub.groupby(['network_group', 'n_hvg', 'embedding', 'clf'], dropna=False)[metrics]
        .agg(['mean', 'std'])
    )
    summary.columns = ['_'.join(col).strip('_') for col in summary.columns]
    summary = summary.reset_index()

    lines += [
        '## Summary by network group, HVG count, embedding, and classifier',
        '',
        '| ' + ' | '.join(summary.columns) + ' |',
        '| ' + ' | '.join(['---'] * len(summary.columns)) + ' |',
    ]
    for _, row in summary.iterrows():
        vals = []
        for col in summary.columns:
            val = row[col]
            if isinstance(val, float):
                vals.append('nan' if pd.isna(val) else f'{val:.6f}')
            else:
                vals.append(str(val))
        lines.append('| ' + ' | '.join(vals) + ' |')
    lines.append('')

    with open(out_path, 'w') as f:
        f.write('\n'.join(lines) + '\n')


def write_diagnostics(dataset_diagnostics, results_df):
    """Write BEELINE-full-only diagnostics under results/grn_beeline_full/diagnotics."""
    os.makedirs(DIAGNOSTICS_DIR, exist_ok=True)
    diag_df = pd.DataFrame(dataset_diagnostics)
    dataset_csv = os.path.join(DIAGNOSTICS_DIR, 'dataset_class_balance.csv')
    diag_df.to_csv(dataset_csv, index=False)

    validate_protocol_prevalence(dataset_diagnostics)

    metric_csv = os.path.join(DIAGNOSTICS_DIR, 'metric_summary_by_network_embedding.csv')
    if results_df is not None and len(results_df) > 0:
        metric_df = add_baseline_comparisons(results_df)
        metric_df['network_group'] = metric_df['dataset'].map(lambda x: _infer_network_group(x) or ('scGREAT' if 'scGREAT' in str(x) else 'other'))
        summary_metric_candidates = PRIMARY_METRICS + SUPPLEMENTARY_METRICS + DIAGNOSTIC_METRICS
        summary_metrics = [m for m in summary_metric_candidates if m in metric_df.columns]
        group_cols = ['network_group', 'embedding', 'clf']
        if 'negative_protocol' in metric_df.columns:
            group_cols.insert(1, 'negative_protocol')
        metric_summary = (
            metric_df
            .groupby(group_cols, dropna=False)[summary_metrics]
            .agg(['mean', 'std', 'min', 'max', 'count'])
        )
        metric_summary.columns = ['_'.join(col).strip('_') for col in metric_summary.columns]
        metric_summary = metric_summary.reset_index()
        metric_summary.to_csv(metric_csv, index=False)
    else:
        pd.DataFrame().to_csv(metric_csv, index=False)

    md_path = os.path.join(DIAGNOSTICS_DIR, 'diagnostics_summary.md')
    lines = [
        '# GRN BEELINE Full Diagnostics',
        '',
        'Diagnostics are scoped to the GRN BEELINE full benchmark only.',
        '',
        '## Files',
        '',
        '- `dataset_class_balance.csv`: per-dataset split sizes, positive ratios, random-ranking AUPRC baseline, and network-context retention diagnostics.',
        '- `metric_summary_by_network_embedding.csv`: metric summaries by network group, negative protocol, embedding, classifier, AUPRC lift, and pair-space separability diagnostics.',
        '',
    ]
    if not diag_df.empty:
        display_cols = [
            'dataset', 'network_group', 'negative_protocol', 'n_genes',
            'n_edges_raw', 'n_edges_after_expression_filter', 'n_positive_edges_after_filter',
            'hvg_edge_retention', 'test_n_positive', 'test_n_negative',
            'test_positive_ratio', 'test_negative_to_positive_ratio', 'random_auprc_baseline',
        ]
        available_cols = [c for c in display_cols if c in diag_df.columns]
        lines += [
            '## Class-balance summary',
            '',
            '| ' + ' | '.join(available_cols) + ' |',
            '| ' + ' | '.join(['---'] * len(available_cols)) + ' |',
        ]
        for _, row in diag_df[available_cols].iterrows():
            values = []
            for col in available_cols:
                val = row[col]
                if isinstance(val, float):
                    values.append('nan' if pd.isna(val) else f'{val:.6f}')
                else:
                    values.append(str(val))
            lines.append('| ' + ' | '.join(values) + ' |')
        lines.append('')
    with open(md_path, 'w') as f:
        f.write('\n'.join(lines) + '\n')

    write_full_candidate_interpretation_md(add_baseline_comparisons(results_df) if results_df is not None else results_df)
    log(f'Diagnostics saved to {DIAGNOSTICS_DIR}')


def write_conference_md(csv_path=None):
    out_md = os.path.join(RESULTS_DIR, 'conference_table.md')
    csv_path = csv_path or os.path.join(RESULTS_DIR, 'grn_beeline_full_results.csv')

    if not os.path.exists(csv_path):
        log(f'Skip conference table export: missing {csv_path}')
        return
    df = ensure_auprc_lift(pd.read_csv(csv_path))
    if df.empty:
        log(f'Skip conference table export: empty {csv_path}')
        return

    embeddings = [e for e in EMBED_ORDER if e in df['embedding'].unique()] + [e for e in sorted(df['embedding'].unique()) if e not in EMBED_ORDER]
    lines = [
        '# GRN BEELINE Full (Conference-style Tables)',
        '',
        '说明：`-`表示该组合无结果；按列（同一dataset）比较：**加粗**表示优于baseline；<span style="color:red"><strong>红色加粗</strong></span>表示该列最优。',
        '仅将`dataset`与`embedding`作为显式变量；其余设置作为表上方 latent variables 展示；`dataset_split`与`classifier`已聚合，不再展示拆分明细。',
        ''
    ]
    network_groups = ['Specific', 'Non-Specific', 'STRING']
    all_metrics = (
        [m for m in PRIMARY_METRICS if m in df.columns]
        + [m for m in SUPPLEMENTARY_METRICS if m in df.columns]
    )
    protocol_values = ['']
    if 'negative_protocol' in df.columns:
        requested_protocols = ['tf_stratified_1to10', 'full_candidate']
        observed_protocols = [p for p in df['negative_protocol'].dropna().unique()]
        protocol_values = requested_protocols.copy()
        protocol_values += [p for p in observed_protocols if p not in protocol_values]

    for metric in all_metrics:
        section = "Supplementary" if metric in SUPPLEMENTARY_METRICS else "Main"
        lines += [f'## {metric.upper()} ({section})', '']
        if metric == 'auprc_lift':
            lines.append(
                'AUPRC_LIFT normalizes AUPRC by the random-ranking baseline, which equals the test positive ratio. '
                'It indicates how many times better the model ranks true edges compared with random expectation.')
            lines.append('')

        for protocol in protocol_values:
            sub = df.copy()
            if 'negative_protocol' in sub.columns:
                sub = sub[sub['negative_protocol'] == protocol]
            sub['dataset_display'] = sub['dataset'].map(_collapse_dataset_label)

            protocol_label = protocol or 'default'
            lines.append(f'### Negative protocol: {protocol_label}')
            lines.append('')
            lines.append(
                f'Latent variables: metric={metric.upper()}, negative_protocol={protocol_label}, '
                'classifier=aggregated(lr,mlp), aggregation=mean')
            lines.append('')

            for group in network_groups:
                sub_group = sub[sub['dataset_display'].map(_infer_network_group) == group]
                lines.append(f'#### {group}')
                lines.append('')
                if sub_group.empty:
                    lines.append('无可用结果。')
                    lines.append('')
                    continue

                pivot = sub_group.pivot_table(index='embedding', columns='dataset_display', values=metric, aggfunc='mean')
                pivot = pivot.reindex(index=embeddings)
                styled = _style_metric_matrix(pivot)
                datasets = list(pivot.columns)

                lines.append('| Embedding | ' + ' | '.join(datasets) + ' |')
                lines.append('|---|' + '|'.join(['---:'] * len(datasets)) + '|')
                for emb in pivot.index:
                    lines.append('| ' + emb + ' | ' + ' | '.join(styled[emb][ds] for ds in datasets) + ' |')
                lines.append('')

                size_groups = {}
                for ds in datasets:
                    size_groups.setdefault(_dataset_size_label(ds), []).append(ds)
                for size_label in sorted(size_groups, key=lambda x: (x == 'unknown', int(x) if str(x).isdigit() else str(x))):
                    ds_for_size = size_groups[size_label]
                    mean_pivot = pivot[ds_for_size].mean(axis=1, skipna=True).to_frame('Mean')
                    mean_pivot = mean_pivot.reindex(index=embeddings)
                    styled_mean = _style_metric_matrix(mean_pivot)
                    size_title = f'{size_label}-gene' if size_label != 'unknown' else 'unknown-size'
                    lines.append(f'##### Aggregate mean across {group} {size_title} datasets')
                    lines.append('')
                    lines.append(
                        f'Latent variables: metric={metric.upper()}, negative_protocol={protocol_label}, network_group={group}, '
                        f'dataset_size={size_label}, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets')
                    lines.append('')
                    lines.append('| Embedding | Mean |')
                    lines.append('|---|---:|')
                    for emb in mean_pivot.index:
                        lines.append('| ' + emb + ' | ' + styled_mean[emb]['Mean'] + ' |')
                    lines.append('')
    with open(out_md, 'w') as f:
        f.write('\n'.join(lines) + '\n')
    log(f'Conference table saved to {out_md}')
    combined_path = update_combined_summary_markdown(Path(RESULTS_DIR).parent)
    log(f'Combined summary markdown refreshed at {combined_path}')


def first_existing(paths):
    for p in paths:
        if p and os.path.exists(p):
            return p
    return None


def resolve_expression_path(cell_type, cfg):
    """
    Resolve ExpressionData.csv path with local override support.
    Priority:
      1) BEELINE_EXPR_ROOT/<cell_type>/ExpressionData.csv (env)
      2) ./scRNA-Seq/<cell_type>/ExpressionData.csv (current working tree)
      3) legacy BEELINE zip layout path
    """
    env_root = os.environ.get('BEELINE_EXPR_ROOT', '').strip()
    return first_existing([
        os.path.join(env_root, cell_type, 'ExpressionData.csv') if env_root else None,
        os.path.join(os.getcwd(), 'scRNA-Seq', cell_type, 'ExpressionData.csv'),
        os.path.join(BEELINE_DIR, cfg['expr_dir'], 'ExpressionData.csv'),
    ])


def resolve_tf_list_path(species):
    return first_existing([
        os.path.join(BEELINE_DIR, f'{species}-tfs.csv'),
        os.path.join(BEELINE_DIR, 'BEELINE-data', 'inputs', 'TFs', f'{species}-tfs.csv'),
    ])


def resolve_network_root():
    return first_existing([
        os.path.join(BEELINE_DIR, 'Networks'),
        os.path.join(BEELINE_DIR, 'BEELINE-Networks'),
    ])


# =============================================================
# Download BEELINE data
# =============================================================
def download_beeline():
    data_check = os.path.join(BEELINE_DIR, 'BEELINE-data')
    net_check = os.path.join(BEELINE_DIR, 'Networks')
    if os.path.exists(data_check) and os.path.exists(net_check):
        log("BEELINE data already present.")
        return

    os.makedirs(BEELINE_DIR, exist_ok=True)
    base_url = 'https://zenodo.org/records/3701939/files'
    for fname in ['BEELINE-data.zip', 'BEELINE-Networks.zip']:
        fpath = os.path.join(BEELINE_DIR, fname)
        if not os.path.exists(fpath):
            log(f"Downloading {fname}...")
            urllib.request.urlretrieve(f'{base_url}/{fname}?download=1', fpath)
            log(f"  Downloaded: {os.path.getsize(fpath) / 1e6:.1f} MB")

    for fname in ['BEELINE-data.zip', 'BEELINE-Networks.zip']:
        fpath = os.path.join(BEELINE_DIR, fname)
        log(f"Extracting {fname}...")
        with zipfile.ZipFile(fpath, 'r') as z:
            z.extractall(BEELINE_DIR)
    log("BEELINE data ready.")


# =============================================================
# Loading embeddings
# =============================================================
def load_vocab():
    with open(VOCAB_PATH) as f:
        return json.load(f)


def load_checkpoint_embedding(path, key):
    ckpt = torch.load(path, map_location='cpu', weights_only=False)
    return ckpt[key].detach().numpy()


def load_gf_embedding(emb_dir, name='GF-12L95M'):
    emb_path = os.path.join(emb_dir, f'{name}_emb.csv')
    gl_path = os.path.join(emb_dir, f'{name}_genelist.txt')
    emb = pd.read_csv(emb_path, header=None).values.astype(np.float32)
    with open(gl_path) as f:
        genelist = [line.strip() for line in f]
    return emb, genelist


def build_symbol_to_entrez():
    mapping_file = os.path.join(OUTPUT_DIR, 'gene_symbol_to_entrez.json')
    if os.path.exists(mapping_file):
        with open(mapping_file) as f:
            return json.load(f)
    alt_path = '/root/autodl-tmp/projects/embedding_benchmark/gene_symbol_to_entrez.json'
    if os.path.exists(alt_path):
        import shutil
        shutil.copy2(alt_path, mapping_file)
        with open(mapping_file) as f:
            return json.load(f)
    return {}


# =============================================================
# Build dataset from BEELINE expression + network
# =============================================================
def build_beeline_dataset(expr_path, net_path, tf_list_path, n_hvg=500):
    """
    Build gene list, positive pairs, and network-context diagnostics from BEELINE raw data.
    Returns (gene_list, gene_to_idx, pos_pairs_set, tf_indices, diagnostics) or None.
    """
    # Read expression: rows=genes, cols=cells
    expr = pd.read_csv(expr_path, index_col=0, header=0)
    all_genes = list(expr.index)
    all_genes_set = set(all_genes)

    # Read network: Gene1,Gene2
    net_raw = pd.read_csv(net_path)
    tf_col, tgt_col = net_raw.columns[0], net_raw.columns[1]
    n_edges_raw = int(len(net_raw))
    n_tfs_raw = int(net_raw[tf_col].nunique()) if len(net_raw) else 0

    # Filter to genes in expression data
    net = net_raw[net_raw[tf_col].isin(all_genes_set) & net_raw[tgt_col].isin(all_genes_set)]
    n_edges_expr = int(len(net))
    n_tfs_expr = int(net[tf_col].nunique()) if len(net) else 0
    if len(net) < 10:
        return None

    # Read TF list; keep diagnostics for TF-list coverage but do not filter historical labels.
    tf_df = pd.read_csv(tf_list_path)
    known_tfs = set(tf_df.iloc[:, 0].tolist())
    n_tfs_in_tf_list_expr = int(net[net[tf_col].isin(known_tfs)][tf_col].nunique()) if len(net) else 0

    # Select top n_hvg genes by variance (same as scGREAT)
    gene_var = expr.var(axis=1).sort_values(ascending=False)
    hvg = set(gene_var.head(n_hvg).index.tolist())

    gene_list = sorted(hvg)
    gene_to_idx = {g: i for i, g in enumerate(gene_list)}
    gene_set = set(gene_list)

    # Filter network to selected genes
    net_filt = net[net[tf_col].isin(gene_set) & net[tgt_col].isin(gene_set)]
    if len(net_filt) < 10:
        return None

    # Positive pairs as (TF_idx, Target_idx)
    pos_pairs = set()
    for _, row in net_filt.iterrows():
        tf_idx = gene_to_idx[row[tf_col]]
        tgt_idx = gene_to_idx[row[tgt_col]]
        pos_pairs.add((tf_idx, tgt_idx))

    # TF indices (those that appear as Gene1 in positive network)
    tf_indices = sorted(set(gene_to_idx[g] for g in net_filt[tf_col].unique()))

    diagnostics = {
        'n_edges_raw': n_edges_raw,
        'n_tfs_raw': n_tfs_raw,
        'n_edges_after_expression_filter': n_edges_expr,
        'n_tfs_after_expression_filter': n_tfs_expr,
        'n_tfs_in_tf_list_after_expression_filter': n_tfs_in_tf_list_expr,
        'n_edges_after_hvg_filter': int(len(net_filt)),
        'n_tfs_after_hvg_filter': int(net_filt[tf_col].nunique()),
        'expression_edge_retention': n_edges_expr / n_edges_raw if n_edges_raw else np.nan,
        'hvg_edge_retention': len(net_filt) / n_edges_expr if n_edges_expr else np.nan,
        'hvg_tf_retention': net_filt[tf_col].nunique() / n_tfs_expr if n_tfs_expr else np.nan,
    }

    return gene_list, gene_to_idx, pos_pairs, tf_indices, diagnostics


# =============================================================
# Negative Split Protocols
# =============================================================
def _build_pos_neg_dicts(pos_pairs, gene_indices, tf_indices):
    """Build TF-indexed positive targets and full non-target candidate negatives."""
    gene_set = np.array(gene_indices)

    pos_dict = {}
    for tf, tgt in pos_pairs:
        if tf not in pos_dict:
            pos_dict[tf] = []
        pos_dict[tf].append(tgt)

    neg_dict = {}
    for tf in tf_indices:
        if tf in pos_dict:
            pos_items = set(pos_dict[tf])
            pos_items.add(tf)
            neg_dict[tf] = [g for g in gene_set if g not in pos_items]
        else:
            neg_dict[tf] = [g for g in gene_set if g != tf]

    return pos_dict, neg_dict


def _split_positive_targets(pos_dict, train_ratio=0.67, validation_ratio=0.1):
    """Split positives per TF while preserving the historical scGREAT split rules."""
    train_pos, val_pos, test_pos = {}, {}, {}
    for k, targets in pos_dict.items():
        targets = list(targets)
        np.random.shuffle(targets)
        if len(targets) == 1:
            if np.random.uniform() <= 0.5:
                train_pos[k] = targets
            else:
                test_pos[k] = targets
        elif len(targets) == 2:
            train_pos[k] = [targets[0]]
            test_pos[k] = [targets[1]]
        else:
            n_train = int(len(targets) * train_ratio)
            n_val = int(len(targets) * validation_ratio)
            train_pos[k] = targets[:n_train]
            val_pos[k] = targets[n_train:n_train + n_val]
            test_pos[k] = targets[n_train + n_val:]
    return train_pos, val_pos, test_pos


def _sample_without_replacement(items, n):
    """Return up to n shuffled items without replacement."""
    items = list(items)
    np.random.shuffle(items)
    if n is None:
        return items
    return items[:min(int(n), len(items))]


def _split_full_candidate_negatives(pos_dict, neg_dict, train_ratio=0.67, validation_ratio=0.1):
    """Legacy split: keep every non-target gene as a candidate negative."""
    train_neg, val_neg, test_neg = {}, {}, {}
    for k in pos_dict.keys():
        negs = _sample_without_replacement(neg_dict.get(k, []), None)
        n = len(negs)
        n_train = int(n * train_ratio)
        n_val = int(n * validation_ratio)
        train_neg[k] = negs[:n_train]
        val_neg[k] = negs[n_train:n_train + n_val]
        test_neg[k] = negs[n_train + n_val:]
    return train_neg, val_neg, test_neg


def _allocate_counts_by_quota(quotas, available, protected_order=(2, 0, 1)):
    """Allocate scarce candidates across splits while preserving evaluability.

    `quotas` are ordered as train/validation/test. When negatives are scarce,
    reserve one negative for each non-empty split whenever possible, prioritizing
    test and train over validation because validation is folded back into train in
    this benchmark. The remaining negatives are distributed proportionally.
    """
    quotas = np.asarray(quotas, dtype=float)
    available = int(max(0, available))
    counts = np.zeros(len(quotas), dtype=int)
    active = [i for i, q in enumerate(quotas) if q > 0]
    if available == 0 or not active:
        return counts.tolist()

    if np.sum(quotas) <= available:
        return [int(q) for q in quotas]

    priority = [i for i in protected_order if i in active] + [i for i in active if i not in protected_order]
    remaining = available
    for idx in priority:
        if remaining <= 0:
            break
        counts[idx] = 1
        remaining -= 1

    if remaining <= 0:
        return counts.tolist()

    residual = np.maximum(quotas - counts, 0)
    if np.sum(residual) <= 0:
        return counts.tolist()
    raw = residual / np.sum(residual) * remaining
    extra = np.floor(raw).astype(int)
    counts += extra
    remainder = remaining - int(np.sum(extra))
    if remainder > 0:
        order = np.argsort(-(raw - extra))
        for idx in order[:remainder]:
            counts[idx] += 1
    return counts.tolist()


def _sample_tf_stratified_negatives(pos_splits, neg_dict, neg_pos_ratio):
    """Sample fixed-ratio negatives per TF without starving later splits.

    Earlier code consumed candidates in train/validation/test order. For dense
    networks (for example mHSC Specific), train could exhaust all available
    negatives and leave test with positives only, producing undefined AUROC and
    AUPRC=1.0. This allocator first computes each split's desired quota, then
    distributes scarce negatives proportionally across train/validation/test.
    """
    train_pos, val_pos, test_pos = pos_splits
    split_pos = [train_pos, val_pos, test_pos]
    split_neg = [{}, {}, {}]

    for tf in sorted(set().union(*[set(d.keys()) for d in split_pos])):
        candidates = _sample_without_replacement(neg_dict.get(tf, []), None)
        quotas = [len(pos_d.get(tf, [])) * int(neg_pos_ratio) for pos_d in split_pos]
        counts = _allocate_counts_by_quota(quotas, len(candidates))
        cursor = 0
        for i, n_neg in enumerate(counts):
            if n_neg <= 0:
                continue
            split_neg[i][tf] = candidates[cursor:cursor + n_neg]
            cursor += n_neg

    return tuple(split_neg)


def _build_labeled_split(pos_d, neg_d):
    pairs, labels = [], []
    for k, targets in pos_d.items():
        for t in targets:
            pairs.append([k, t])
            labels.append(1)
    for k, targets in neg_d.items():
        for t in targets:
            pairs.append([k, t])
            labels.append(0)
    if len(pairs) == 0:
        return np.array([]).reshape(0, 2).astype(int), np.array([]).astype(int)
    pairs = np.array(pairs, dtype=int)
    labels = np.array(labels, dtype=int)
    return pairs, labels


def hard_negative_split(pos_pairs, gene_indices, tf_indices, seed=42,
                        mode='full_candidate', neg_pos_ratio=None,
                        train_ratio=0.67, validation_ratio=0.1):
    """Generate train/validation/test splits with configurable negative sampling.

    mode='full_candidate' reproduces the historical behavior that treats all
    non-target HVG genes as negatives for each TF. mode='tf_stratified_fixed_ratio'
    samples up to neg_pos_ratio negatives per positive per TF and split, which
    keeps class balance comparable across datasets and makes AUPRC easier to
    interpret alongside the random-ranking baseline.
    """
    random.seed(seed)
    np.random.seed(seed)

    pos_dict, neg_dict = _build_pos_neg_dicts(pos_pairs, gene_indices, tf_indices)
    train_pos, val_pos, test_pos = _split_positive_targets(
        pos_dict, train_ratio=train_ratio, validation_ratio=validation_ratio)

    if mode == 'full_candidate':
        train_neg, val_neg, test_neg = _split_full_candidate_negatives(
            pos_dict, neg_dict, train_ratio=train_ratio, validation_ratio=validation_ratio)
    elif mode == 'tf_stratified_fixed_ratio':
        if neg_pos_ratio is None or int(neg_pos_ratio) <= 0:
            raise ValueError('tf_stratified_fixed_ratio requires a positive neg_pos_ratio')
        train_neg, val_neg, test_neg = _sample_tf_stratified_negatives(
            (train_pos, val_pos, test_pos), neg_dict, int(neg_pos_ratio))
    else:
        raise ValueError(f'Unknown negative sampling mode: {mode}')

    train_pairs, train_labels = _build_labeled_split(train_pos, train_neg)
    val_pairs, val_labels = _build_labeled_split(val_pos, val_neg)
    test_pairs, test_labels = _build_labeled_split(test_pos, test_neg)

    return (train_pairs, train_labels), (val_pairs, val_labels), (test_pairs, test_labels)


# =============================================================
# Features & evaluation
# =============================================================
def build_gene_lookup(emb_matrix, vocab, gene_list):
    n = len(gene_list)
    d = emb_matrix.shape[1]
    lookup = np.zeros((n, d), dtype=np.float32)
    mapped = 0
    for i, g in enumerate(gene_list):
        if g in vocab:
            lookup[i] = emb_matrix[vocab[g]]
            mapped += 1
    return lookup, mapped


def build_gene_lookup_gf(gf_emb, gf_genelist, s2e, gene_list):
    n = len(gene_list)
    d = gf_emb.shape[1]
    lookup = np.zeros((n, d), dtype=np.float32)
    e2gf = {eid: i for i, eid in enumerate(gf_genelist)}
    mapped = 0
    for i, g in enumerate(gene_list):
        if g in s2e:
            eid = s2e[g]
            if eid in e2gf:
                lookup[i] = gf_emb[e2gf[eid]]
                mapped += 1
    return lookup, mapped


def build_pair_features(lookup, pairs):
    if len(pairs) == 0:
        return np.array([]).reshape(0, lookup.shape[1] * 3 + 2)
    tf_emb = lookup[pairs[:, 0]]
    tgt_emb = lookup[pairs[:, 1]]
    hadamard = tf_emb * tgt_emb
    norm_tf = np.linalg.norm(tf_emb, axis=1, keepdims=True) + 1e-8
    norm_tgt = np.linalg.norm(tgt_emb, axis=1, keepdims=True) + 1e-8
    cosine = np.sum(tf_emb * tgt_emb, axis=1, keepdims=True) / (norm_tf * norm_tgt)
    l2 = np.linalg.norm(tf_emb - tgt_emb, axis=1, keepdims=True)
    return np.concatenate([tf_emb, tgt_emb, hadamard, cosine, l2], axis=1)


def build_pair_embedding_diagnostics(lookup, pairs, labels, prefix='test'):
    """Summarize raw pair-space separability before fitting a classifier."""
    labels = np.asarray(labels).astype(int) if labels is not None else np.array([], dtype=int)
    if len(pairs) == 0 or len(labels) == 0:
        return {}

    tf_emb = lookup[pairs[:, 0]]
    tgt_emb = lookup[pairs[:, 1]]
    norm_tf = np.linalg.norm(tf_emb, axis=1) + 1e-8
    norm_tgt = np.linalg.norm(tgt_emb, axis=1) + 1e-8
    cosine = np.sum(tf_emb * tgt_emb, axis=1) / (norm_tf * norm_tgt)
    l2 = np.linalg.norm(tf_emb - tgt_emb, axis=1)
    pos_mask = labels == 1
    neg_mask = labels == 0

    def safe_mean(values):
        return float(np.mean(values)) if len(values) else np.nan

    pos_cos = safe_mean(cosine[pos_mask])
    neg_cos = safe_mean(cosine[neg_mask])
    pos_l2 = safe_mean(l2[pos_mask])
    neg_l2 = safe_mean(l2[neg_mask])

    return {
        f'{prefix}_pos_cosine_mean': pos_cos,
        f'{prefix}_neg_cosine_mean': neg_cos,
        f'{prefix}_cosine_delta': pos_cos - neg_cos if pd.notna(pos_cos) and pd.notna(neg_cos) else np.nan,
        f'{prefix}_pos_l2_mean': pos_l2,
        f'{prefix}_neg_l2_mean': neg_l2,
        f'{prefix}_l2_delta': neg_l2 - pos_l2 if pd.notna(pos_l2) and pd.notna(neg_l2) else np.nan,
    }


def _precision_recall_at_k(y_true, y_score, k):
    """Precision@k and Recall@k on ranked prediction scores."""
    if len(y_true) == 0:
        return np.nan, np.nan
    k = int(max(1, min(k, len(y_true))))
    order = np.argsort(-y_score)
    topk_true = y_true[order[:k]]
    tp_at_k = int(np.sum(topk_true))
    precision_at_k = tp_at_k / k
    total_pos = int(np.sum(y_true))
    recall_at_k = tp_at_k / total_pos if total_pos > 0 else np.nan
    return precision_at_k, recall_at_k


def evaluate(train_X, train_y, test_X, test_y, clf_name='lr'):
    if len(test_X) == 0 or len(train_X) == 0:
        return None
    if len(np.unique(train_y)) < 2 or len(np.unique(test_y)) < 2:
        return None
    scaler = StandardScaler()
    train_X = scaler.fit_transform(train_X)
    test_X = scaler.transform(test_X)

    if clf_name == 'lr':
        clf = LogisticRegression(max_iter=1000, n_jobs=1, C=1.0)
    else:
        clf = MLPClassifier(hidden_layer_sizes=(256, 128), max_iter=500,
                            early_stopping=True, random_state=42)
    clf.fit(train_X, train_y)
    probs = clf.predict_proba(test_X)[:, 1]
    preds = (probs >= 0.5).astype(int)

    metrics = {}
    metrics['auroc'] = roc_auc_score(test_y, probs)
    metrics['auprc'] = average_precision_score(test_y, probs)
    random_auprc_baseline = float(np.mean(test_y)) if len(test_y) else np.nan
    metrics['random_auprc_baseline'] = random_auprc_baseline
    metrics['test_positive_ratio'] = random_auprc_baseline
    metrics['test_negative_to_positive_ratio'] = (
        float(np.sum(test_y == 0) / np.sum(test_y == 1)) if np.sum(test_y == 1) else np.nan
    )
    metrics['auprc_lift'] = (
        metrics['auprc'] / random_auprc_baseline
        if pd.notna(random_auprc_baseline) and random_auprc_baseline > 0 else np.nan
    )
    metrics['auprc_gain'] = (
        metrics['auprc'] - random_auprc_baseline
        if pd.notna(random_auprc_baseline) and random_auprc_baseline > 0 else np.nan
    )
    if abs(metrics['random_auprc_baseline'] - metrics['test_positive_ratio']) >= 1e-12:
        warnings.warn('random_auprc_baseline must equal test_positive_ratio for AUPRC')
    if pd.notna(metrics['auprc_lift']) and metrics['auprc_lift'] < 0:
        warnings.warn(f"AUPRC lift should be non-negative, got {metrics['auprc_lift']}")

    pos_cnt = int(np.sum(test_y))
    k = pos_cnt if pos_cnt > 0 else len(test_y)
    precision_at_k, recall_at_k = _precision_recall_at_k(test_y, probs, k)
    metrics['precision_at_k'] = precision_at_k
    metrics['recall_at_k'] = recall_at_k

    metrics['f1'] = f1_score(test_y, preds, zero_division=0)

    cm = confusion_matrix(test_y, preds, labels=[0, 1])
    tn, fp, fn, tp = cm.ravel()
    metrics['specificity'] = tn / (tn + fp) if (tn + fp) > 0 else np.nan
    return metrics


# =============================================================
# Load scGREAT pre-processed datasets
# =============================================================
def load_scgreat_dataset(ds_name):
    ds_dir = os.path.join(SCGREAT_DIR, ds_name)
    if not os.path.exists(ds_dir):
        return None

    target_path = os.path.join(ds_dir, 'Target.csv')
    if not os.path.exists(target_path):
        return None

    df = pd.read_csv(target_path)
    gene_list = df['Gene'].tolist()

    splits = {}
    for split_name in ['Train_set', 'Validation_set', 'Test_set']:
        path = os.path.join(ds_dir, f'{split_name}.csv')
        if not os.path.exists(path):
            return None
        sdf = pd.read_csv(path, index_col=0, header=0)
        pairs = sdf.iloc[:, :2].values.astype(int)
        labels = sdf.iloc[:, 2].values.astype(int)
        splits[split_name] = (pairs, labels)

    return gene_list, splits


# =============================================================
# Run evaluation on one dataset
# =============================================================
def run_one_dataset(ds_name, gene_list, train_pairs, train_labels,
                    test_pairs, test_labels, loaded_embs, vocab, s2e,
                    negative_protocol='', split_diagnostics=None):
    """Evaluate all embeddings on one dataset. Returns list of result dicts."""
    results = []

    log(f"\n{'='*70}")
    log(f"Dataset: {ds_name} ({len(gene_list)} genes)")
    log(f"{'='*70}")
    log(f"Train: {len(train_labels)} (pos={train_labels.sum()})")
    log(f"Test:  {len(test_labels)} (pos={test_labels.sum()})")
    if split_diagnostics:
        log(
            f"Protocol diagnostics: negative_protocol={negative_protocol}, "
            f"test_pos={split_diagnostics.get('test_n_positive')}, "
            f"test_neg={split_diagnostics.get('test_n_negative')}, "
            f"test_positive_ratio={split_diagnostics.get('test_positive_ratio'):.6f}, "
            f"random_auprc_baseline={split_diagnostics.get('random_auprc_baseline'):.6f}, "
            f"test_neg_to_pos={split_diagnostics.get('test_negative_to_positive_ratio'):.6f}")

    log(f"\n{'Embedding':<20} {'Clf':<5} {'Coverage':>12} {'AUROC':>8} {'AUPRC':>8}")
    log("-" * 60)

    for emb_name, emb_data in loaded_embs.items():
        if emb_data['type'] == 'checkpoint':
            lookup, mapped = build_gene_lookup(emb_data['matrix'], vocab, gene_list)
        else:
            lookup, mapped = build_gene_lookup_gf(
                emb_data['matrix'], emb_data['genelist'], s2e, gene_list)

        cov = f"{mapped}/{len(gene_list)}"
        train_X = build_pair_features(lookup, train_pairs)
        test_X = build_pair_features(lookup, test_pairs)
        pair_diagnostics = build_pair_embedding_diagnostics(lookup, test_pairs, test_labels, prefix='test')

        for clf_name in ['lr', 'mlp']:
            try:
                metrics = evaluate(train_X, train_labels, test_X, test_labels, clf_name)
                if metrics is not None:
                    auroc = metrics['auroc']
                    auprc = metrics['auprc']
                    log(f"{emb_name:<20} {clf_name:<5} {cov:>12} {auroc:>7.4f} {auprc:>7.4f}")
                    results.append({
                        'dataset': ds_name, 'embedding': emb_name,
                        'clf': clf_name, 'coverage': cov,
                        'negative_protocol': negative_protocol,
                        **pair_diagnostics,
                        **metrics,
                    })
            except Exception as e:
                log(f"{emb_name:<20} {clf_name:<5} ERROR: {e}")

    return results


# =============================================================
# Main
# =============================================================
def main():
    log("=" * 70)
    log("GRN BEELINE Full Benchmark - Embedding Only")
    log("=" * 70)

    # Load vocab & embeddings
    vocab = load_vocab()
    log(f"Vocab: {len(vocab)} genes")

    loaded_embs = {}
    for name, cfg in EMBEDDINGS.items():
        try:
            if cfg['type'] == 'checkpoint':
                mat = load_checkpoint_embedding(cfg['path'], cfg['key'])
                loaded_embs[name] = {'matrix': mat, 'type': 'checkpoint'}
                log(f"Loaded {name}: {mat.shape}")
            else:
                emb, gl = load_gf_embedding(cfg['dir'])
                loaded_embs[name] = {'matrix': emb, 'genelist': gl, 'type': 'geneformer'}
                log(f"Loaded {name}: {emb.shape}")
        except Exception as e:
            log(f"SKIP embedding {name}: {e}")

    if not loaded_embs:
        log("No embedding loaded successfully. Exiting.")
        return

    s2e = build_symbol_to_entrez()

    negative_protocols = resolve_negative_protocols()
    split_train_ratio, split_validation_ratio = resolve_split_ratios()
    log(f"Negative protocols: {[name for name, _ in negative_protocols]}")
    log(f"Split ratios: train={split_train_ratio:.3f}, validation={split_validation_ratio:.3f}, test={1 - split_train_ratio - split_validation_ratio:.3f}")

    # Download BEELINE
    download_beeline()

    all_results = []
    dataset_diagnostics = []

    # =========================================================
    # Part 1: scGREAT pre-processed datasets (hESC500, mESC500)
    # =========================================================
    log("\n--- Part 1: scGREAT pre-processed datasets ---")
    if os.path.exists(SCGREAT_DIR):
        for d in sorted(os.listdir(SCGREAT_DIR)):
            ds_dir = os.path.join(SCGREAT_DIR, d)
            if os.path.isdir(ds_dir) and os.path.exists(os.path.join(ds_dir, 'Target.csv')):
                result = load_scgreat_dataset(d)
                if result is None:
                    continue
                gene_list, splits = result
                train_p, train_l = splits['Train_set']
                val_p, val_l = splits['Validation_set']
                test_p, test_l = splits['Test_set']
                dataset_diagnostics.append(build_dataset_diagnostic(
                    f"{d} [scGREAT]", 'scGREAT', gene_list, train_l, val_l, test_l,
                    negative_protocol='preprocessed_scGREAT',
                    negative_sampling_mode='preprocessed'))

                # Combine train+val
                if len(val_p) > 0:
                    all_train_p = np.vstack([train_p, val_p])
                    all_train_l = np.concatenate([train_l, val_l])
                else:
                    all_train_p, all_train_l = train_p, train_l

                res = run_one_dataset(
                    f"{d} [scGREAT]", gene_list,
                    all_train_p, all_train_l, test_p, test_l,
                    loaded_embs, vocab, s2e,
                    negative_protocol='preprocessed_scGREAT')
                all_results.extend(res)

    # =========================================================
    # Part 2: BEELINE raw datasets (all cell types × network types × gene counts)
    # =========================================================
    log("\n--- Part 2: BEELINE datasets (from raw data) ---")

    for cell_type, cfg in CELL_CONFIGS.items():
        expr_path = resolve_expression_path(cell_type, cfg)
        if expr_path is None or not os.path.exists(expr_path):
            log(f"  {cell_type}: ExpressionData.csv not found, skipping")
            continue

        species = cfg['species']
        tf_list_path = resolve_tf_list_path(species)
        if tf_list_path is None:
            log(f"  {cell_type}: TF list for {species} not found, skipping")
            continue
        network_root = resolve_network_root()
        if network_root is None:
            log(f"  {cell_type}: network root not found, skipping")
            continue

        # Build network type -> file path mapping
        net_types = {}
        # Specific network
        specific_file = os.path.join(network_root, species, cfg['specific_net'])
        if os.path.exists(specific_file):
            net_types['Specific'] = specific_file

        # Non-Specific and STRING
        for net_name, net_file in NETWORK_TYPES[species].items():
            if net_name == 'Specific':
                continue
            fpath = os.path.join(network_root, species, net_file)
            if os.path.exists(fpath):
                net_types[net_name] = fpath

        log(f"\n  Cell type: {cell_type} ({species}), networks: {list(net_types.keys())}")

        for net_name, net_path in net_types.items():
            for n_hvg in N_HVGS:
                ds_name = f"{cell_type}_{net_name}_{n_hvg}"

                try:
                    result = build_beeline_dataset(expr_path, net_path, tf_list_path, n_hvg=n_hvg)
                    if result is None:
                        log(f"  {ds_name}: too few edges after filtering, skipping")
                        continue

                    gene_list, gene_to_idx, pos_pairs, tf_indices, network_diag = result
                    gene_indices = list(range(len(gene_list)))

                    for protocol_name, protocol_spec in negative_protocols:
                        split_seed = 42
                        (train_p, train_l), (val_p, val_l), (test_p, test_l) = \
                            hard_negative_split(
                                pos_pairs, gene_indices, tf_indices, seed=split_seed,
                                mode=protocol_spec['mode'],
                                neg_pos_ratio=protocol_spec.get('neg_pos_ratio'),
                                train_ratio=split_train_ratio,
                                validation_ratio=split_validation_ratio)
                        split_diag = build_dataset_diagnostic(
                            ds_name, 'BEELINE', gene_list, train_l, val_l, test_l,
                            n_positive_edges=len(pos_pairs), n_tfs=len(tf_indices),
                            network_path=net_path, expression_path=expr_path, n_hvg=n_hvg,
                            negative_protocol=protocol_name,
                            negative_sampling_mode=protocol_spec['mode'],
                            target_neg_pos_ratio=protocol_spec.get('neg_pos_ratio'),
                            network_diagnostics=network_diag)
                        dataset_diagnostics.append(split_diag)
                        log(
                            f"Split diagnostics: dataset={ds_name}, negative_protocol={protocol_name}, "
                            f"test_pos={split_diag['test_n_positive']}, test_neg={split_diag['test_n_negative']}, "
                            f"test_positive_ratio={split_diag['test_positive_ratio']:.6f}, "
                            f"random_auprc_baseline={split_diag['random_auprc_baseline']:.6f}, "
                            f"test_neg_to_pos={split_diag['test_negative_to_positive_ratio']:.6f}")

                        if len(test_p) < 10 or len(train_p) < 10:
                            log(f"  {ds_name} [{protocol_name}]: too few samples after split, skipping")
                            continue
                        if len(np.unique(train_l)) < 2 or len(np.unique(test_l)) < 2:
                            log(
                                f"  {ds_name} [{protocol_name}]: split has one class "
                                f"(train_pos={int(train_l.sum())}/{len(train_l)}, "
                                f"test_pos={int(test_l.sum())}/{len(test_l)}), skipping")
                            continue

                        # Combine train+val
                        if len(val_p) > 0:
                            all_train_p = np.vstack([train_p, val_p])
                            all_train_l = np.concatenate([train_l, val_l])
                        else:
                            all_train_p, all_train_l = train_p, train_l

                        res = run_one_dataset(
                            ds_name, gene_list,
                            all_train_p, all_train_l, test_p, test_l,
                            loaded_embs, vocab, s2e,
                            negative_protocol=protocol_name,
                            split_diagnostics=split_diag)
                        all_results.extend(res)

                except Exception as e:
                    log(f"  {ds_name}: ERROR - {e}")

    # =========================================================
    # Final Summary
    # =========================================================
    log(f"\n{'='*70}")
    log("FINAL SUMMARY (LR results)")
    log(f"{'='*70}")

    if all_results:
        df = add_baseline_comparisons(ensure_auprc_lift(pd.DataFrame(all_results)))
        lr_df = df[df['clf'] == 'lr']
        mlp_df = df[df['clf'] == 'mlp']

        emb_names = list(EMBEDDINGS.keys())
        header = f"{'Dataset':<35} {'Protocol':<24} " + " ".join(f"{n:<16}" for n in emb_names)

        def log_classifier_summary(title, clf_df):
            log(f"\n{'='*70}")
            log(title)
            log(f"{'='*70}")
            log(f"\n{header}")
            log("-" * (60 + 17 * len(emb_names)))
            if clf_df.empty:
                return
            protocols = ['']
            if 'negative_protocol' in clf_df.columns:
                protocols = [p for p in clf_df['negative_protocol'].dropna().unique()]
            for protocol in protocols:
                protocol_df = clf_df[clf_df['negative_protocol'] == protocol] if 'negative_protocol' in clf_df.columns else clf_df
                for ds in protocol_df['dataset'].unique():
                    ds_data = protocol_df[protocol_df['dataset'] == ds]
                    row = f"{ds:<35} {protocol:<24} "
                    for emb_name in emb_names:
                        emb_row = ds_data[ds_data['embedding'] == emb_name]
                        if len(emb_row) > 0:
                            auroc = emb_row.iloc[0]['auroc']
                            auprc = emb_row.iloc[0]['auprc']
                            row += f"{auroc:.4f}/{auprc:.4f}  "
                        else:
                            row += f"{'N/A':<16} "
                    log(row)

        log_classifier_summary('FINAL SUMMARY (LR results)', lr_df)
        log_classifier_summary('FINAL SUMMARY (MLP results)', mlp_df)

        # Average across datasets
        log(f"\n{'='*70}")
        log("AVERAGE ACROSS BEELINE DATASETS (LR)")
        log(f"{'='*70}")
        beeline_lr = lr_df[~lr_df['dataset'].str.contains('scGREAT')]
        if len(beeline_lr) > 0:
            protocols = ['']
            if 'negative_protocol' in beeline_lr.columns:
                protocols = [p for p in beeline_lr['negative_protocol'].dropna().unique()]
            for protocol in protocols:
                protocol_df = beeline_lr[beeline_lr['negative_protocol'] == protocol] if 'negative_protocol' in beeline_lr.columns else beeline_lr
                log(f"\nProtocol: {protocol or 'default'}")
                for emb_name in emb_names:
                    emb_data = protocol_df[protocol_df['embedding'] == emb_name]
                    if len(emb_data) > 0:
                        mean_auroc = emb_data['auroc'].mean()
                        mean_auprc = emb_data['auprc'].mean()
                        std_auroc = emb_data['auroc'].std()
                        std_auprc = emb_data['auprc'].std()
                        log(f"  {emb_name:<20} AUROC: {mean_auroc:.4f}±{std_auroc:.4f}  AUPRC: {mean_auprc:.4f}±{std_auprc:.4f}  (n={len(emb_data)})")

        csv_path = os.path.join(RESULTS_DIR, 'grn_beeline_full_results.csv')
        result_keys = ['dataset', 'negative_protocol', 'embedding', 'clf']
        df = merge_incremental_results(df, csv_path, result_keys)
        df = add_baseline_comparisons(ensure_auprc_lift(df))
        df.to_csv(csv_path, index=False)
        write_conference_md(csv_path)
        write_diagnostics(dataset_diagnostics, df)
        log(f"\nResults merged into {csv_path}")

    log("\nDone!")


if __name__ == '__main__':
    main()
