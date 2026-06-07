"""Shared frozen embedding loaders and AnnData-to-cell-embedding builders."""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import numpy as np
import pandas as pd


DEFAULT_BASE_DIR = "/root/autodl-tmp/projects/comparison-SC-embedding/scbenchmark"


def log(msg: str) -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def import_anndata():
    try:
        import anndata as ad  # type: ignore
        return ad
    except ImportError as exc:
        raise ImportError("anndata is required to read --h5ad files. Install anndata or run in an environment that provides it.") from exc


def read_h5ad(path: str | Path):
    ad = import_anndata()
    return ad.read_h5ad(str(path))


def load_vocab(path: str | Path) -> Dict[str, int]:
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return {str(k): int(v) for k, v in raw.items()}


def load_embedding_registry(registry_path: str | None, base_dir: str | None, embedding_names: str | Iterable[str] | None) -> Dict[str, Dict[str, Any]]:
    """Load an embedding registry JSON or fall back to scripts/common embedding specs."""
    import sys
    common_root = Path(__file__).resolve().parents[1]
    if str(common_root) not in sys.path:
        sys.path.append(str(common_root))
    from common.embedding_config import build_primary_embeddings, parse_embedding_names

    if registry_path:
        with open(registry_path, "r", encoding="utf-8") as f:
            registry = json.load(f)
        if not isinstance(registry, dict):
            raise ValueError("--embedding-registry must be a JSON object keyed by embedding name")
    else:
        resolved_base = base_dir or DEFAULT_BASE_DIR
        registry = build_primary_embeddings(resolved_base, apply_incremental=False)

    names = parse_embedding_names(embedding_names)
    if names:
        missing = [n for n in names if n not in registry]
        if missing:
            raise KeyError(f"Requested embedding name(s) absent from registry: {missing}. Available: {sorted(registry)}")
        registry = {n: registry[n] for n in names}
    return registry


def resolve_vocab_path(cfg: Mapping[str, Any], cli_vocab: str | None, base_dir: str | None) -> Path:
    candidates = [cli_vocab, cfg.get("vocab_path"), cfg.get("vocab")]
    if base_dir:
        candidates.append(str(Path(base_dir) / "vocab.json"))
    for c in candidates:
        if c and Path(c).exists():
            return Path(c)
    raise FileNotFoundError("Could not resolve vocabulary JSON. Provide --vocab-path, registry vocab_path, or --base-dir pointing to a directory with vocab.json.")


def load_gene_embedding_matrix(cfg: Mapping[str, Any]) -> np.ndarray:
    path = Path(str(cfg.get("path", "")))
    if not path.exists():
        raise FileNotFoundError(f"Embedding file not found: {path}")
    typ = str(cfg.get("type", path.suffix.lstrip("."))).lower()
    if typ in {"checkpoint", "pt", "pth"} or path.suffix in {".pt", ".pth"}:
        import torch
        obj = torch.load(path, map_location="cpu", weights_only=False)
        keys = [cfg.get("key"), "encoder.embedding.weight", "module.embedding.weight", "embedding.weight"]
        containers = [obj]
        for nested in ("state_dict", "model_state_dict", "model"):
            if isinstance(obj, dict) and isinstance(obj.get(nested), dict):
                containers.append(obj[nested])
        for container in containers:
            if not isinstance(container, dict):
                continue
            for key in keys:
                if key and key in container:
                    val = container[key]
                    if hasattr(val, "detach"):
                        val = val.detach().cpu().numpy()
                    return np.asarray(val, dtype=np.float32)
        raise KeyError(f"No embedding weight key found in {path}; tried {keys}")
    if path.suffix == ".npy":
        return np.load(path).astype(np.float32)
    if path.suffix == ".npz":
        arr = np.load(path)
        key = str(cfg.get("array_key", "embedding"))
        if key not in arr:
            key = arr.files[0]
        return arr[key].astype(np.float32)
    if path.suffix in {".csv", ".tsv"}:
        sep = "\t" if path.suffix == ".tsv" else ","
        return pd.read_csv(path, header=None, sep=sep).values.astype(np.float32)
    raise ValueError(f"Unsupported embedding file type for {path}")


def _as_csr(x: Any):
    try:
        from scipy import sparse
        return x.tocsr() if sparse.issparse(x) else sparse.csr_matrix(x)
    except ImportError as exc:
        raise ImportError("scipy is required to aggregate AnnData.X into cell embeddings.") from exc


def build_cell_embeddings_from_gene_embeddings(adata: Any, emb_matrix: np.ndarray, vocab: Mapping[str, int], embedding_name: str) -> Tuple[np.ndarray, pd.DataFrame]:
    """Expression-weighted cell embedding with explicit gene coverage diagnostics."""
    var_names = np.asarray([str(g) for g in adata.var_names])
    gene_to_var = {g: i for i, g in enumerate(var_names)}
    matched_pairs: List[Tuple[int, int]] = []
    missing_genes: List[str] = []
    for gene, emb_idx in vocab.items():
        if int(emb_idx) < 0 or int(emb_idx) >= emb_matrix.shape[0]:
            continue
        var_idx = gene_to_var.get(str(gene))
        if var_idx is None:
            missing_genes.append(str(gene))
        else:
            matched_pairs.append((var_idx, int(emb_idx)))

    n_adata_genes = int(adata.n_vars)
    matched_var_indices = np.array([p[0] for p in matched_pairs], dtype=np.int64)
    matched_emb_indices = np.array([p[1] for p in matched_pairs], dtype=np.int64)
    n_unique_matched = int(len(set(matched_var_indices.tolist())))
    n_adata_missing_from_embedding = int(n_adata_genes - n_unique_matched)
    if matched_var_indices.size == 0:
        raise ValueError(f"{embedding_name}: zero AnnData genes matched the embedding vocabulary; cannot build cell embeddings.")

    x = _as_csr(adata.X)[:, matched_var_indices]
    emb_dim = int(emb_matrix.shape[1])
    out = np.zeros((adata.n_obs, emb_dim), dtype=np.float32)
    counts = np.diff(x.indptr).astype(int)
    sums = np.asarray(x.sum(axis=1)).ravel().astype(np.float32)
    zero_cells = sums <= 0
    for i in range(adata.n_obs):
        start, end = x.indptr[i], x.indptr[i + 1]
        if start == end or sums[i] <= 0:
            continue
        cols = x.indices[start:end]
        vals = x.data[start:end].astype(np.float32)
        emb_idx = matched_emb_indices[cols]
        weights = vals / (vals.sum() + 1e-8)
        out[i] = (emb_matrix[emb_idx] * weights[:, None]).sum(axis=0)

    diag = pd.DataFrame({
        "embedding": embedding_name,
        "source": "gene_embedding",
        "cell_index": np.arange(adata.n_obs, dtype=int),
        "cell_id": np.asarray(adata.obs_names, dtype=str),
        "n_genes_adata": n_adata_genes,
        "n_genes_matched": n_unique_matched,
        "matched_gene_ratio": float(n_unique_matched / max(n_adata_genes, 1)),
        "n_adata_genes_missing_from_embedding": n_adata_missing_from_embedding,
        "per_cell_nonzero_matched_gene_count": counts,
        "cells_with_zero_matched_genes": int(zero_cells.sum()),
        "n_embedding_vocab_genes": int(len(vocab)),
        "n_missing_embedding_vocab_genes_from_adata": int(len(missing_genes)),
    })
    return out, diag


def load_precomputed_cell_embeddings(adata: Any, obsm_key: str, embedding_name: str) -> Tuple[np.ndarray, pd.DataFrame]:
    if obsm_key not in adata.obsm:
        raise KeyError(f"AnnData.obsm is missing key {obsm_key!r}. Available keys: {list(adata.obsm.keys())}")
    x = np.asarray(adata.obsm[obsm_key], dtype=np.float32)
    if x.ndim != 2:
        raise ValueError(f"adata.obsm[{obsm_key!r}] must be 2D, got shape {x.shape}")
    if x.shape[0] != adata.n_obs:
        raise ValueError(f"adata.obsm[{obsm_key!r}] has {x.shape[0]} rows but AnnData has {adata.n_obs} cells; cell order cannot be validated.")
    diag = pd.DataFrame({
        "embedding": embedding_name,
        "source": f"obsm:{obsm_key}",
        "cell_index": np.arange(adata.n_obs, dtype=int),
        "cell_id": np.asarray(adata.obs_names, dtype=str),
        "n_genes_adata": int(adata.n_vars),
        "n_genes_matched": np.nan,
        "matched_gene_ratio": np.nan,
        "n_adata_genes_missing_from_embedding": np.nan,
        "per_cell_nonzero_matched_gene_count": np.nan,
        "cells_with_zero_matched_genes": 0,
        "n_embedding_vocab_genes": np.nan,
        "n_missing_embedding_vocab_genes_from_adata": np.nan,
    })
    return x, diag


def get_cell_embeddings(adata: Any, embedding_name: str, cfg: Mapping[str, Any], *, obsm_key: str | None, vocab_path: str | None, base_dir: str | None) -> Tuple[np.ndarray, pd.DataFrame]:
    key = obsm_key or cfg.get("obsm_key")
    if key:
        return load_precomputed_cell_embeddings(adata, str(key), embedding_name)
    vocab_file = resolve_vocab_path(cfg, vocab_path, base_dir)
    vocab = load_vocab(vocab_file)
    emb = load_gene_embedding_matrix(cfg)
    return build_cell_embeddings_from_gene_embeddings(adata, emb, vocab, embedding_name)


def save_config(out_dir: str | Path, filename: str, args: Any, extra: Optional[Dict[str, Any]] = None) -> Path:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    payload = vars(args).copy() if hasattr(args, "__dict__") else dict(args)
    if extra:
        payload.update(extra)
    path = out / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, sort_keys=True, default=str)
    return path


def validate_obs_keys(adata: Any, keys: Sequence[str]) -> None:
    missing = [k for k in keys if k and k not in adata.obs]
    if missing:
        raise KeyError(f"AnnData.obs missing required key(s): {missing}. Available obs columns: {list(adata.obs.columns)}")
