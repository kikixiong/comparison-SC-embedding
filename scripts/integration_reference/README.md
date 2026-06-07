# Integration and Reference Mapping Benchmarks

These scripts evaluate **frozen, embedding-agnostic** representations. They do not fine-tune scGPT or any other backbone.

Embeddings can be supplied in two ways:

1. **Gene embeddings** from the existing embedding registry/checkpoint workflow. Cells are represented by the same expression-weighted average used by the annotation benchmark: matched gene vectors are averaged with expression weights.
2. **Precomputed cell embeddings** in `adata.obsm[...]` via `--obsm-key`. The scripts validate that the matrix is two-dimensional and has one row per AnnData cell.

Every run writes a config JSON, logs seed/input paths/embedding names, saves gene-coverage diagnostics, and uses identical cell subsets or splits across embeddings.

## Integration benchmark

Measures label preservation and batch mixing separately. Higher batch mixing is not automatically better if label preservation collapses.

```bash
python scripts/integration_reference/integration_benchmark.py \
  --h5ad data/my_dataset.h5ad \
  --embedding-registry configs/embedding_registry.json \
  --embedding-names baseline,scGPT_human,minus,cl_v6_fair \
  --vocab-path /path/to/vocab.json \
  --batch-key batch \
  --label-key cell_type \
  --out-dir results/integration_reference \
  --seed 42 \
  --max-cells 20000 \
  --min-cells-per-label 20 \
  --min-cells-per-batch 20
```

For precomputed cell embeddings:

```bash
python scripts/integration_reference/integration_benchmark.py \
  --h5ad data/my_dataset.h5ad \
  --embedding-registry configs/cell_embedding_registry.json \
  --embedding-names v4_plain_best \
  --obsm-key X_v4_plain_best \
  --batch-key batch \
  --label-key cell_type \
  --out-dir results/integration_reference \
  --seed 42
```

Outputs:

* `results/integration_reference/integration_metrics.csv`
* `results/integration_reference/integration_coverage.csv`
* `results/integration_reference/integration_config.json`
* `results/integration_reference/integration_report.md`
* `results/integration_reference/integration_conference_table.md`

## Reference mapping with held-out batch

Uses reference cells with known labels to predict query-cell labels. Metrics are reported both including and excluding query labels absent from the reference.

```bash
python scripts/integration_reference/reference_mapping_benchmark.py \
  --h5ad data/my_dataset.h5ad \
  --embedding-registry configs/embedding_registry.json \
  --embedding-names baseline,scGPT_human,minus,cl_v6_fair \
  --vocab-path /path/to/vocab.json \
  --reference-query-mode batch_heldout \
  --batch-key batch \
  --label-key cell_type \
  --out-dir results/integration_reference \
  --seed 42 \
  --k-values 1,5,10,20
```

Other split modes:

* `--reference-query-mode dataset_heldout --dataset-key dataset`
* `--reference-query-mode random_split --query-fraction 0.2`
* `--reference-query-mode custom_column --custom-column split_group --reference-value train --query-value test`

Outputs:

* `results/integration_reference/reference_mapping_metrics.csv`
* `results/integration_reference/reference_mapping_per_label.csv`
* `results/integration_reference/reference_mapping_confusion_matrix.csv`
* `results/integration_reference/reference_mapping_split_diagnostics.csv`
* `results/integration_reference/reference_mapping_coverage.csv`
* `results/integration_reference/reference_mapping_config.json`
* `results/integration_reference/reference_mapping_report.md`
* `results/integration_reference/reference_mapping_conference_table.md`

## Combined summary

```bash
python scripts/integration_reference/summarize_integration_reference.py \
  --results-dir results/integration_reference
```

Output:

* `results/integration_reference/combined_integration_reference_summary.md`

## Registry format

A registry is a JSON object keyed by embedding name. Checkpoint entries follow the existing repository convention:

```json
{
  "baseline": {
    "path": "/path/to/save_pretrain/baseline/best_model.pt",
    "key": "module.embedding.weight",
    "type": "checkpoint",
    "vocab_path": "/path/to/vocab.json"
  }
}
```

If `--embedding-registry` is omitted, the scripts reuse `scripts/common/embedding_config.py` and resolve paths from `--base-dir`, whose default mirrors the existing annotation/perturbation benchmark base directory (`/root/autodl-tmp/projects/comparison-SC-embedding/scbenchmark`).
