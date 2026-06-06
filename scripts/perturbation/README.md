# Legacy perturbation benchmark

`perturbation_benchmark.py` is the legacy embedding-only perturbation benchmark covering classification, perturbation-effect similarity, direction prediction, and cell-type-specific delta regression. For current conservative reporting, prefer `scripts/perturbation_regression/` where applicable.

## Usage

```bash
nohup python scripts/perturbation/perturbation_benchmark.py > logs/perturbation.log 2>&1 &
```

## Incremental embedding reruns

This script now uses the shared registry in `scripts/common/embedding_config.py`. When `INCRE_EMBEDDINGS` is non-empty, the same command evaluates only that embedding subset and merges new rows into `perturbation_results.csv` by benchmark setting. Existing rows for older embeddings are preserved.

Set `INCRE_EMBEDDINGS = ()` for a full rerun. After each successful CSV merge, `perturbation_conference_tables.md` is regenerated from the merged `perturbation_results.csv`, so full and incremental runs share the same markdown export path rather than patching markdown incrementally. In the generated tables, values better than `baseline` are black bold and row-best values are red bold.
