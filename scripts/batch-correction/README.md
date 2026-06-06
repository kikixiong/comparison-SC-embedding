# Batch-correction / scRNA integration benchmark

Evaluates frozen gene embeddings by cell-level pooled representations, then checks both biology conservation and batch mixing.

## Why both matter
Good integration must preserve cell type (AvgBIO) while mitigating batch signal (AvgBATCH). UMAP is visualization only.

## Auto-discovery
`discover_project_assets(base_dir)` scans common embedding and dataset locations, and auto-detects `batch_key`/`label_key` from common `obs` names.

## One-command usage
```bash
nohup python scripts/batch-correction/run_batch_correction_all.py --base-dir . --out-dir results/batch-correction --datasets auto --embeddings auto > logs/batch_correction.log 2>&1 &
```

Use `--datasets` / `--embeddings` to restrict scope.

## Incremental embedding reruns

The same command above is still the normal entry point. If `INCRE_EMBEDDINGS` is non-empty in `scripts/common/embedding_config.py` (currently used for newly added checkpoints such as `cl_v6_fair`), `--embeddings auto` discovers only that incremental subset, evaluates those embeddings, and merges the new rows into the existing `batch_correction_all_results.csv`.

After the CSV merge, `batch_correction_conference_tables.md` is regenerated from the merged CSV; markdown is not updated incrementally. Set `INCRE_EMBEDDINGS = ()` for a full embedding rerun. If you want a non-incremental explicit subset with `--embeddings name1,name2`, first clear `INCRE_EMBEDDINGS` so the registry is not pre-filtered.

If `Immune_Human_openproblems` is present, it is prioritized first by default (`--priority-datasets`).

Convert an existing all-results CSV into the conference-style markdown tables without rerunning embeddings:
```bash
python scripts/batch-correction/run_batch_correction_all.py --csv-to-md results/batch-correction/batch_correction_all_results.csv --out-dir results/batch-correction
```

## Outputs
- `batch_correction_all_results.csv`
- `batch_correction_per_dataset_summary.csv`
- `batch_correction_rankings.csv`
- `batch_correction_report.md`
- `batch_correction_conference_tables.md`: compact paper-style tables comparing embeddings by dataset/correction method, with best values highlighted.
- `plots/*`

## Caveats
Do not claim success from batch mixing alone; check conservative score `min(AvgBIO, AvgBATCH)` and stability across seeds.

## Required scGPT-style datasets
Coverage claims require at least one of: **PBMC 10K**, **Immune Human** (prefer both). If missing, they are written to `missing_assets.csv` and report warns not to claim full scGPT-style coverage.
