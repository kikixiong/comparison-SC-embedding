# Legacy perturbation benchmark

`perturbation_benchmark.py` is the legacy embedding-only perturbation benchmark covering classification, perturbation-effect similarity, direction prediction, and cell-type-specific delta regression. For current conservative reporting, prefer `scripts/perturbation_regression/` where applicable.

## Usage

```bash
python scripts/perturbation/perturbation_benchmark.py
```

## Incremental embedding reruns

This script now uses the shared registry in `scripts/common/embedding_config.py`. When `INCRE_EMBEDDINGS` is non-empty, the same command evaluates only that embedding subset and merges new rows into `perturbation_results.csv` by benchmark setting. Existing rows for older embeddings are preserved.

Set `INCRE_EMBEDDINGS = ()` for a full rerun. If you generate markdown or downstream summaries from this CSV, regenerate them from the merged CSV rather than editing markdown incrementally.
