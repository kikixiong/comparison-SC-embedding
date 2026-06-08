"""Shared embedding registry and incremental-run helpers for benchmark pipelines."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Iterable, Sequence


PRIMARY_EMBEDDING_SPECS: Dict[str, Dict[str, str]] = {
    "minus": {"subpath": "save_pretrain/minus/best_model.pt", "key": "module.embedding.weight", "type": "checkpoint"},
    "baseline": {"subpath": "save_pretrain/baseline/best_model.pt", "key": "module.embedding.weight", "type": "checkpoint"},
    "scGPT_human": {"subpath": "save_pretrain/scGPT_human/best_model.pt", "key": "encoder.embedding.weight", "type": "checkpoint"},
    "v4_bias_rec_best": {"subpath": "save_pretrain/v4_bias_rec_best/best_model.pt", "key": "embedding.weight", "type": "checkpoint"},
    "v4_plain_best": {"subpath": "save_pretrain/v4_plain_best/best_model.pt", "key": "embedding.weight", "type": "checkpoint"},
    "v4_type_pe_best": {"subpath": "save_pretrain/v4_type_pe_best/best_model.pt", "key": "embedding.weight", "type": "checkpoint"},
    "scconcept": {
        "subpath": "save_pretrain/scconcept/best_model.pt",
        "key": "gene_token_encoder.learnable_embs.hsapiens.weight",
        "type": "checkpoint"
    },
    "scconcept_encoded": {"subpath": "save_pretrain/scconcept_encoded/best_model.pt", "key": "embedding.weight", "type": "checkpoint"},
    "cl_scratch_v5": {"subpath": "save_pretrain/cl_scratch_v5/best_model.pt", "key": "embedding.weight", "type": "checkpoint"},
    "cl_v6_fair": {"subpath": "save_pretrain/cl_v6_fair/best_model.pt", "key": "embedding.weight", "type": "checkpoint"},
}

# Incremental benchmark switch. Leave empty to run all registered embeddings.
# Set to one or more embedding names when a new save_pretrain/<name>/best_model.pt
# is added and only that subset should be evaluated. CSV/markdown writers in the
# primary runners merge those new rows with existing outputs instead of replacing
# prior embeddings.
INCRE_EMBEDDINGS: Sequence[str] = ("cl_scratch_v5",)


def parse_embedding_names(value: str | Iterable[str] | None) -> list[str]:
    """Normalize a comma-separated string or iterable of embedding names."""
    if value is None:
        return []
    if isinstance(value, str):
        parts = value.split(",")
    else:
        parts = list(value)
    return [str(x).strip() for x in parts if str(x).strip()]


def get_incre_embeddings() -> list[str]:
    """Return the active incremental embedding list from this config file."""
    return parse_embedding_names(INCRE_EMBEDDINGS)


def apply_incre_filter(registry: Dict[str, Dict[str, str]], explicit_names: Iterable[str] | None = None) -> Dict[str, Dict[str, str]]:
    """Filter a registry to explicit names or active INCRE_EMBEDDINGS.

    Unknown names are ignored here so benchmark scripts can keep their previous
    non-strict behavior. Callers that need strict validation can compare the
    returned keys with the requested list.
    """
    requested = parse_embedding_names(explicit_names) if explicit_names is not None else get_incre_embeddings()
    if not requested:
        return registry
    wanted = set(requested)
    return {name: cfg for name, cfg in registry.items() if name in wanted}


def build_primary_embeddings(base_dir: str, *, apply_incremental: bool = True) -> Dict[str, Dict[str, str]]:
    """Build {embedding_name: {path, key}} for primary pipelines.

    When ``INCRE_EMBEDDINGS`` is non-empty, the returned registry is restricted
    to that subset by default.
    """
    out = deepcopy(PRIMARY_EMBEDDING_SPECS)
    for name, cfg in out.items():
        cfg["path"] = f"{base_dir}/{cfg.pop('subpath')}"
    if apply_incremental:
        out = apply_incre_filter(out)
    return out


def merge_incremental_results(
    new_df: Any,
    csv_path: str | Path,
    key_columns: Sequence[str],
    *,
    write: bool = True,
) -> Any:
    """Merge newly evaluated rows into an existing benchmark CSV.

    Existing rows with the same key tuple as a new row are replaced; unrelated
    rows (for old embeddings/datasets/settings) are preserved. This enables
    incremental embedding-only reruns while downstream summaries/markdown are
    generated from the full merged table.
    """
    path = Path(csv_path)
    merged = new_df.copy()
    if path.exists():
        import pandas as pd

        old_df = pd.read_csv(path)
        keys = [c for c in key_columns if c in old_df.columns and c in new_df.columns]
        if keys and not new_df.empty:
            new_keys = new_df[keys].astype(str).agg("\x1f".join, axis=1)
            old_keys = old_df[keys].astype(str).agg("\x1f".join, axis=1)
            old_df = old_df.loc[~old_keys.isin(set(new_keys))]
        merged = pd.concat([old_df, new_df], ignore_index=True, sort=False)
    if write:
        path.parent.mkdir(parents=True, exist_ok=True)
        merged.to_csv(path, index=False)
    return merged
