# GeneLink-style GRN inference benchmark

This benchmark treats GRN inference as directed supervised TF→target link prediction.

## Inputs
Datasets must provide curated GRN edges as `Train_set.csv`, `Validation_set.csv`, and `Test_set.csv` (optionally `Target.csv` mapping integer indices to gene symbols). Positive labels come from curated edges; negatives are sampled from candidate TF×target pairs after excluding all known positives.

## Fixed embeddings
The runner uses the fixed `/bigdata2/hyt/projects/scbenchmark/save_pretrain/...` registry. It intentionally does not rediscover random result CSVs as embeddings.


## Incremental embedding reruns

The same command below can be reused. With `--embeddings fixed`, the fixed registry is filtered by `INCRE_EMBEDDINGS` in `scripts/common/embedding_config.py` when that list is non-empty, so only the new embedding subset is evaluated. New rows are merged into `grn_inference_all_results.csv` and the diagnostic CSVs; unrelated rows for previous embeddings are preserved.

Set `INCRE_EMBEDDINGS = ()` before running when you want the full fixed registry.

## Usage
```bash
python scripts/grn_inference/run_grn_inference_all.py \
  --base-dir . \
  --out-dir results/grn_inference \
  --datasets auto \
  --embeddings fixed \
  --models lr,mlp \
  --split-modes edge_holdout,cross_dataset_transfer,topology_matched_transfer \
  --negative-sampling random_negative,degree_matched_negative \
  --negative-ratios 1,5 \
  --seeds 0,1,2,3,4 \
  --resume
```

## Outputs
- `grn_inference_all_results.csv`
- `grn_inference_summary.csv`
- `edge_sampling_diagnostics.csv`
- `split_diagnostics.csv`
- `gene_coverage_diagnostics.csv`
- `missing_assets.csv`
- `sampled_edges/*.csv`
- `grn_inference_report.md`

AUPRC is the primary metric because true regulatory edges are sparse and class imbalance is central to GRN link prediction.
