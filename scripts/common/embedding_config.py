"""Shared embedding registry for primary benchmark pipelines."""
from __future__ import annotations

from copy import deepcopy
from typing import Dict


PRIMARY_EMBEDDING_SPECS: Dict[str, Dict[str, str]] = {
    "minus": {"subpath": "save_pretrain/minus/best_model.pt", "key": "module.embedding.weight"},
    "baseline": {"subpath": "save_pretrain/baseline/best_model.pt", "key": "module.embedding.weight"},
    "scGPT_human": {"subpath": "save_pretrain/scGPT_human/best_model.pt", "key": "encoder.embedding.weight"},
    "v4_bias_rec_best": {"subpath": "save_pretrain/v4_bias_rec_best/best_model.pt", "key": "embedding.weight"},
    "v4_plain_best": {"subpath": "save_pretrain/v4_plain_best/best_model.pt", "key": "embedding.weight"},
    "v4_type_pe_best": {"subpath": "save_pretrain/v4_type_pe_best/best_model.pt", "key": "embedding.weight"},
    "scconcept": {
        "subpath": "save_pretrain/scconcept/best_model.pt",
        "key": "gene_token_encoder.learnable_embs.hsapiens.weight",
    },
    "scconcept_encoded": {"subpath": "save_pretrain/scconcept_encoded/best_model.pt", "key": "embedding.weight"},
}


def build_primary_embeddings(base_dir: str) -> Dict[str, Dict[str, str]]:
    """Build {embedding_name: {path, key}} for primary pipelines."""
    out = deepcopy(PRIMARY_EMBEDDING_SPECS)
    for name, cfg in out.items():
        cfg["path"] = f"{base_dir}/{cfg.pop('subpath')}"
    return out
