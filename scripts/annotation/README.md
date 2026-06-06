# Legacy annotation benchmark

`benchmark_embeddings.py` is the legacy combined benchmark for cell-type annotation and perturbation classification. For new reporting, prefer the primary task-specific pipelines in `scripts/README.md`, but this script remains useful for reproducing historical annotation tables.

## Usage

```bash
python scripts/annotation/benchmark_embeddings.py
```

To rebuild the annotation conference markdown from an existing merged CSV without rerunning embeddings:

```bash
python scripts/annotation/benchmark_embeddings.py \
  --csv-to-md results/annotation/benchmark_results.csv \
  --annotation-output-dir results/annotation
```

## Incremental embedding reruns

This legacy script now shares `scripts/common/embedding_config.py` with the primary runners. When `INCRE_EMBEDDINGS` is non-empty, the same command evaluates only those embedding names, merges rows into:

- `results/annotation/benchmark_results.csv`
- `results/perturbation/benchmark_results.csv`

After merging the annotation CSV, `annotation_conference_tables.md` is regenerated from the merged CSV. Markdown is not patched incrementally. Set `INCRE_EMBEDDINGS = ()` for a full rerun.

Geneformer (`GF-12L95M`) is skipped during checkpoint-only incremental runs unless it is explicitly listed in `INCRE_EMBEDDINGS`.
