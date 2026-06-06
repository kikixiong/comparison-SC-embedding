# Gene-Prompt Expression Completion

This benchmark now follows the fixed project configuration you provided (no recursive auto-discovery):
- Base data root: `/bigdata2/hyt/projects/scbenchmark`
- Datasets: `adamson`, `dixit`, `norman`
- Embeddings: `minus`, `baseline`, `scGPT_human`, `v4_bias_rec_best`, `v4_plain_best`, `v4_type_pe_best`, `scconcept`, `scconcept_encoded`

## Usage
```bash
nohup python scripts/gene_prompt_completion/run_gene_prompt_completion_all.py --data-dir /bigdata2/hyt/projects/scbenchmark/data/cellxgene --datasets test_data --max-cells 5000 --models ridge_pair --split-modes cell_holdout --target-size 64 --prompt-ratios 0.1 --seeds 0 > logs/gene_prompt_completion_ridge_pair.log 2>&1 &
```

You can restrict with `--datasets` and `--embeddings` (comma-separated names from the fixed list).

## Incremental embedding reruns

The usage command does not change for incremental runs. When `INCRE_EMBEDDINGS` in `scripts/common/embedding_config.py` is non-empty, the runner evaluates only those embedding names and merges the resulting rows into the existing CSV outputs. In this mode the config-level incremental list takes precedence over the default `--embeddings` list so new checkpoints can be evaluated without re-running old embeddings.

The conference markdown is regenerated from the merged `gene_prompt_completion_all_results.csv` after the CSV merge; markdown is never patched incrementally. Set `INCRE_EMBEDDINGS = ()` for a full fixed-list rerun.


## Outputs
- `run_plan.csv`
- `gene_prompt_completion_all_results.csv`
- `gene_prompt_completion_gene_metrics.csv`
- `prompt_target_manifest.csv`
- `gene_prompt_completion_report.md`

## Conference-style summary tables
After a run, the runner also writes:
- `gene_prompt_completion_conference_tables.md`: one compact markdown file comparing the fixed embeddings side by side with best/baseline highlighting.
- Conservative ridge_pair-vs-baseline diagnostics are included inside the markdown when the required model rows are present.

You can rebuild these tables from an existing results CSV without rerunning the benchmark:
```bash
python scripts/gene_prompt_completion/gene_prompt_conference_tables.py \
  --results results/gene_prompt_completion/gene_prompt_completion_all_results.csv \
  --out-dir results/gene_prompt_completion
```
