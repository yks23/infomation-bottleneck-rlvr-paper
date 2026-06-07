# Figure And Table Index

## Poster

- `assets/poster/rlvr_distributional_shrinkage_poster.png`
  Main poster image.
- `assets/poster/rlvr_distributional_shrinkage_poster.pdf`
  Main poster PDF.
- `assets/poster/rlvr_story_overview.png`
  Six-panel overview generated from the story assets.

## Primary 40x40 Figures

- `assets/figures/geometry40/bounded_information_budget.png`
  Bounded verifier-information budget per source.
- `assets/figures/geometry40/geometry40_self_gain_by_problem.png`
  Per-problem self performance gain after isolated RL.
- `assets/figures/geometry40/geometry40_pass_rate_before_after_by_problem.png`
  Initial/common pass rate versus final self-trained pass rate.
- `assets/figures/geometry40/diag_vs_offdiag_transfer_histogram.png`
  Diagonal/self transfer compared with off-diagonal transfer.
- `assets/figures/geometry40/geometry40_transfer_in_out_by_problem.png`
  TransferOut and TransferIn marginals.
- `assets/figures/geometry40/correct_rollout_action_entropy_trajectories.png`
  Correct-only action entropy trajectories.
- `assets/figures/geometry40/action_entropy_shrinkage_trajectories.png`
  All-rollout, correct-only, and incorrect-only action entropy trajectories.
- `assets/figures/geometry40/cluster_heatmap.png`
  Cluster-sorted transfer matrix.
- `assets/figures/geometry40/directed_edges.png`
  Directed transfer graph.
- `assets/figures/geometry40/seed_geometry_sharpness_embedding.png`
  Prompt seed embedding by transfer fingerprints.
- `assets/figures/geometry40/svd_spectrum.png`
  Transfer-matrix singular spectrum.

## Older Supporting Figures

- `assets/figures/dapo17k_sweep/*`
  Earlier DAPO17k information-gain dashboard figures.
- `assets/figures/dapo200/*`
  DAPO200 sweep figures.
- `assets/figures/pair10/*`
  Pair10/additivity pilot figures.
- `assets/figures/transfer_matrix8/*`
  Earlier 8x8 transfer matrix figures.
- `assets/figures/perstep_transfer/*`
  Per-step alignment figures.

## Key Tables

- `assets/tables/geometry40/story_numbers.csv`
  One-row numeric summary used in the poster.
- `assets/tables/geometry40/bounded_information_by_source.csv`
  Per-source information, action entropy, and self-gain summary.
- `assets/tables/geometry40/action_entropy_by_step.csv`
  Per-step action entropy split into all/correct/incorrect rollouts.
- `assets/tables/geometry40/geometry40_self_gain_by_problem.csv`
  Per-problem self gain.
- `assets/tables/geometry40_endpoint/delta_p_common_initial_matrix.csv`
  Main directed transfer matrix.
- `assets/tables/geometry40_endpoint/R_normalized_info_weighted_positive_common_matrix.csv`
  Self-normalized information-weighted positive transfer matrix.
- `assets/tables/geometry40_endpoint/delta_p_permutation_p_value_matrix.csv`
  Permutation p-values for endpoint transfer.
- `assets/tables/transfer_matrix8/*`
  Earlier 8x8 endpoint transfer tables.
- `assets/tables/perstep_transfer/*`
  Per-step alignment matrices and summaries.

## Full Local Asset Index

The full local old-asset bundle is indexed but not committed in full:

- `assets/manifests/all_existing_assets/manifest.csv`
- `assets/manifests/all_existing_assets/summary_counts.csv`
- `assets/manifests/all_existing_assets/source_roots.txt`

Use these files to find the larger local copy at:

```text
artifacts/rlvr_existing_figures_tables_20260607
```
