# Scripts Overview

This directory contains benchmark pipelines and supporting scripts, organized by task domain.

## Recommended primary pipelines

These are the current, structured benchmark workflows you should prefer for new runs and reporting:

- `batch-correction/`
  - scRNA integration / batch-correction benchmark.
  - Entry point: `run_batch_correction_all.py`.

- `gene_prompt_completion/`
  - Gene-prompt expression completion benchmark.
  - Entry point: `run_gene_prompt_completion_all.py`.

- `grn_inference/`
  - GeneLink-style GRN inference benchmark (TF→target supervised link prediction).
  - Entry point: `run_grn_inference_all.py`.

- `perturbation_regression/`
  - Conservative, leak-free perturbation-effect regression benchmark.
  - Entry point: `perturbation_regression_benchmark.py`.

- `transfer_v2/`
  - Cross-dataset GRN transfer benchmark (prepare → run → control diagnostics).
  - Typical flow:
    1. `transfer_v2_prepare.py`
    2. `analyze_grn_transferability_v2.py`
    3. `run_transfer_control_v2.py`


## Incremental embedding reruns

Primary benchmark runners, plus the legacy annotation and perturbation scripts, share `scripts/common/embedding_config.py`. When a new checkpoint is added under `save_pretrain/<embedding_name>/best_model.pt`, add its entry to `PRIMARY_EMBEDDING_SPECS` and set `INCRE_EMBEDDINGS` in the same config file to only the new embedding names.

With a non-empty incremental embedding list, runners evaluate only those embeddings, then merge new rows into the existing result CSVs by benchmark-setting keys. Existing rows for older embeddings are preserved. Markdown tables are **not** patched incrementally; they are regenerated from the merged CSVs after each run. Leave `INCRE_EMBEDDINGS = ()` for full reruns.

## Secondary / legacy scripts

These remain useful for historical reproduction, exploratory analysis, or one-off utilities, but are not the recommended default pipelines.

- `annotation/`
  - Legacy combined embedding benchmark script (`benchmark_embeddings.py`).

- `perturbation/`
  - Legacy multi-task perturbation benchmark (`perturbation_benchmark.py`).

- `grn_inference/legacy/`
  - Older GRN helpers and experiment setup scripts:
    - `grn_embedding_only.py`
    - `grn_beeline_full.py`
    - `setup_scgreat.py`

## Practical guidance

- If you are preparing figures/tables for current reporting, use the **primary pipelines** above.
- Use `legacy/` scripts only when you explicitly need to reproduce prior historical runs.
- Task-specific usage details and output formats are documented in each subdirectory's README.
