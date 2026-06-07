# Figure Catalog

This catalog explains every bundled figure asset. The short `FIGURE_INDEX.md`
is for navigation; this file is for captions and interpretation.

### Poster assets

Path: `assets/poster/rlvr_distributional_shrinkage_poster.png`

Caption: RLVR as Distributional Shrinkage.

Meaning: One-slide summary of the story: bounded rollout/path information,
the LLM binary-verifier projection of that information, mostly additive data,
rollout entropy shrinkage, and transfer geometry.

Supports: Main poster narrative.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/poster_final_40row/rlvr_distributional_shrinkage_poster.png`

Path: `assets/poster/rlvr_story_overview.png`

Caption: Six-panel overview of the RLVR information and geometry story.

Meaning: Compact overview generated from the story assets, useful for talks or
backup slides.

Supports: Quick communication of the same story when the full poster is too
dense.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/rlvr_story_overview.png`

## assets/figures/traditional_rl/openspiel_c4_mean_win_rate_by_condition.pdf

Path: `assets/figures/traditional_rl/openspiel_c4_mean_win_rate_by_condition.pdf`

Caption: Connect4/OpenSpiel traditional RL comparison.

Meaning: This is the traditional-RL anchor for the poster. Connect4 self-play
renews the rollout distribution as the policy changes, so terminal reward
variation can remain near the current frontier instead of being exhausted by a
fixed prompt set.

Supports: The AlphaZero-style contrast: LLM math RLVR has a fixed
prompt-verifier source, while self-play can keep the rollout/path information
integral growing by generating fresh games.

Source: `/mnt/shared-storage-user/sunyoubang/kaisen/infomation-bottleneck-rlvr-paper/figures/openspiel_c4_mean_win_rate_by_condition.pdf`

## assets/figures/geometry40/bounded_information_budget.png

Path: `assets/figures/geometry40/bounded_information_budget.png`

Caption: Bounded Bernoulli-verifier projection per source prompt.

Meaning: Blue bars show realized cumulative verifier uncertainty
`sum_t h2(p_i(t))`; gray bars show the per-step binary bound. This is not the
full definition of information. It is the LLM math verifier projection of the
rollout/path information integral.

Supports: Fixed-dataset LLM RLVR exposes a bounded binary projection of the
rollout/path information integral.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/bounded_information_budget.png`

## assets/figures/geometry40/p_small_multiples.png

Path: `assets/figures/geometry40/p_small_multiples.png`

Caption: Per-question pass-rate trajectories `p_i(t)` for the 40-prompt run.

Meaning: Each small panel tracks one prompt's rollout success rate during
isolated training. Since every curve stays inside `[0,1]`, the binary verifier
projection has entropy at most one bit per step; the useful finite score then
projects this exposure onto monotone performance movement.

Supports: LLM binary-verifier projection; prompt-local training dynamics.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/isolated40/aggregate/p_small_multiples.png`

## assets/figures/geometry40/information_vs_self_gain.png

Path: `assets/figures/geometry40/information_vs_self_gain.png`

Caption: Cumulative verifier uncertainty versus self performance gain.

Meaning: Shows whether prompts with larger realized verifier uncertainty also
produce stronger self improvement.

Supports: Relationship between the verifier projection of path information and
performance.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/information_vs_self_gain.png`

## assets/figures/geometry40/geometry40_info_budget_vs_self_gain.png

Path: `assets/figures/geometry40/geometry40_info_budget_vs_self_gain.png`

Caption: Information budget versus per-problem self gain.

Meaning: Same conceptual comparison as `information_vs_self_gain`, formatted
for the paper/poster bundle with problem IDs labeled for high-gain prompts.

Supports: Information budget as a predictor candidate, not a complete
explanation.

Source: `/mnt/shared-storage-user/sunyoubang/kaisen/infomation-bottleneck-rlvr-paper/figures/dapo17k/geometry40/geometry40_info_budget_vs_self_gain.png`

## assets/figures/geometry40/geometry40_self_gain_by_problem.png

Path: `assets/figures/geometry40/geometry40_self_gain_by_problem.png`

Caption: Per-problem self performance gain after isolated RL.

Meaning: Bars show `DeltaP_ii_common`, the improvement on prompt `i` after
training on prompt `i`, relative to a common initial baseline.

Supports: Prompt-local learning and diagonal dominance.

Source: `/mnt/shared-storage-user/sunyoubang/kaisen/infomation-bottleneck-rlvr-paper/figures/dapo17k/geometry40/geometry40_self_gain_by_problem.png`

## assets/figures/geometry40/geometry40_pass_rate_before_after_by_problem.png

Path: `assets/figures/geometry40/geometry40_pass_rate_before_after_by_problem.png`

Caption: Per-problem pass rate before and after isolated RL.

Meaning: Compares common initial pass rate with final pass rate after
self-training, making prompt-level performance movement visible.

Supports: Per-question performance improvement and bounded `p` evidence.

Source: `/mnt/shared-storage-user/sunyoubang/kaisen/infomation-bottleneck-rlvr-paper/figures/dapo17k/geometry40/geometry40_pass_rate_before_after_by_problem.png`

## assets/figures/geometry40/diag_vs_offdiag_transfer_histogram.png

Path: `assets/figures/geometry40/diag_vs_offdiag_transfer_histogram.png`

Caption: Self-transfer dominates cross-transfer.

Meaning: Histogram comparing diagonal transfer cells with off-diagonal transfer
cells. Diagonal gains are much larger on average.

Supports: Dataset is mostly additive; cross-prompt interaction is sparse.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/diag_vs_offdiag_transfer_histogram.png`

## assets/figures/geometry40/additivity_summary_bars.png

Path: `assets/figures/geometry40/additivity_summary_bars.png`

Caption: Additivity summary: diagonal gain, off-diagonal gain, and positive
off-diagonal gain.

Meaning: Reduces the transfer matrix into three scalar comparisons showing the
small average cross-transfer relative to self-transfer.

Supports: Near-additivity.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/additivity_summary_bars.png`

## assets/figures/geometry40/geometry40_transfer_in_out_by_problem.png

Path: `assets/figures/geometry40/geometry40_transfer_in_out_by_problem.png`

Caption: TransferOut and TransferIn by prompt.

Meaning: TransferOut ranks source prompts by how much they improve other
targets; TransferIn ranks target prompts by how much other sources improve
them.

Supports: Sparse cross-transfer and curriculum/prompt allocation.

Source: `/mnt/shared-storage-user/sunyoubang/kaisen/infomation-bottleneck-rlvr-paper/figures/dapo17k/geometry40/geometry40_transfer_in_out_by_problem.png`

## assets/figures/geometry40/action_entropy_shrinkage_trajectories.png

Path: `assets/figures/geometry40/action_entropy_shrinkage_trajectories.png`

Caption: Rollout action entropy over RL steps.

Meaning: Shows all-rollout, correct-only, and incorrect-only action entropy
trajectories. This separates policy-distribution shrinkage from binary success
entropy.

Supports: RLVR as distributional shrinkage.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/action_entropy_shrinkage_trajectories.png`

## assets/figures/geometry40/correct_rollout_action_entropy_trajectories.png

Path: `assets/figures/geometry40/correct_rollout_action_entropy_trajectories.png`

Caption: Correct-rollout action entropy trajectories.

Meaning: Conditions action entropy on successful rollouts, giving the cleanest
diagnostic for whether correct solution trajectories are becoming sharper.

Supports: Low-entropy problem seed story.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/correct_rollout_action_entropy_trajectories.png`

## assets/figures/geometry40/correct_rollout_support.png

Path: `assets/figures/geometry40/correct_rollout_support.png`

Caption: Support for correct-only action entropy.

Meaning: Shows how many successful rollouts are available per step/source for
the conditional entropy estimate.

Supports: Caveat and reliability check for correct-only entropy.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/correct_rollout_support.png`

## assets/figures/geometry40/action_entropy_shrinkage_vs_training_gain.png

Path: `assets/figures/geometry40/action_entropy_shrinkage_vs_training_gain.png`

Caption: Action entropy shrinkage versus training gain.

Meaning: Scatterplot comparing entropy reduction with improvement in training
success rate.

Supports: Relationship between distributional shrinkage and learning progress.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/action_entropy_shrinkage_vs_training_gain.png`

## assets/figures/geometry40/cluster_heatmap.png

Path: `assets/figures/geometry40/cluster_heatmap.png`

Caption: Cluster-sorted 40x40 transfer heatmap.

Meaning: Visualizes directed endpoint transfer after reordering prompts by
transfer similarity.

Supports: Cross-prompt transfer geometry and block structure.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/cluster_heatmap.png`

## assets/figures/geometry40/directed_edges.png

Path: `assets/figures/geometry40/directed_edges.png`

Caption: Directed transfer graph.

Meaning: Nodes are prompts; directed edges show positive transfer from source
training prompts to target evaluation prompts.

Supports: Sparse cross-prompt interaction graph.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/directed_edges.png`

## assets/figures/geometry40/seed_geometry_sharpness_embedding.png

Path: `assets/figures/geometry40/seed_geometry_sharpness_embedding.png`

Caption: Problem seeds in transfer geometry.

Meaning: Embeds prompts using transfer fingerprints. Color indicates action
entropy shrinkage, linking seed geometry with shrinkage.

Supports: Prompt-space geometry and seed-sharpness story.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/seed_geometry_sharpness_embedding.png`

## assets/figures/geometry40/anchor_knn_graph.png

Path: `assets/figures/geometry40/anchor_knn_graph.png`

Caption: Anchor-transfer kNN graph.

Meaning: Uses transfer fingerprints to define a symmetric neighborhood graph
between prompts.

Supports: Scalable prompt-space visualization using sparse/anchor transfer
measurements.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/anchor_knn_graph.png`

## assets/figures/geometry40/anchor_embedding.png

Path: `assets/figures/geometry40/anchor_embedding.png`

Caption: Anchor-transfer embedding.

Meaning: 2D embedding from transfer-distance fingerprints, intended as a
visual prompt map.

Supports: Dataset geometry.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/anchor_embedding.png`

## assets/figures/geometry40/svd_spectrum.png

Path: `assets/figures/geometry40/svd_spectrum.png`

Caption: Singular spectrum of the transfer matrix.

Meaning: Shows that transfer fingerprints are lower-dimensional than the raw
40x40 matrix.

Supports: Low-rank prompt geometry.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/qwen25-geometry40-20260607_180845/story_assets_40row/figures/svd_spectrum.png`

## assets/figures/dapo17k_sweep/p_small_multiples.png

Path: `assets/figures/dapo17k_sweep/p_small_multiples.png`

Caption: DAPO17k per-question pass-rate trajectories `p_t`.

Meaning: Larger-sweep view of prompt-level success-rate dynamics. This is the
older evidence for the finite LLM binary-verifier projection.

Supports: Binary-verifier projection across a broader prompt sweep.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/p_small_multiples.png`

## assets/figures/dapo17k_sweep/completed_problem_H_p_subplots_latest.png

Path: `assets/figures/dapo17k_sweep/completed_problem_H_p_subplots_latest.png`

Caption: Completed-problem `H(p_t)` and `p_t` subplots.

Meaning: Places verifier entropy and success-rate trajectories side by side,
making the finite binary-information proxy visually explicit.

Supports: Finite binary projection of rollout/path information.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/completed_problem_H_p_subplots_latest.png`

## assets/figures/dapo17k_sweep/H_heatmap.png

Path: `assets/figures/dapo17k_sweep/H_heatmap.png`

Caption: DAPO17k verifier entropy heatmap.

Meaning: Heatmap of `H(p_t)` across prompts and steps, showing where binary
verifier uncertainty is concentrated.

Supports: Binary-verifier projection and prompt heterogeneity.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/H_heatmap.png`

## assets/figures/dapo17k_sweep/action_entropy_per_token_heatmap.png

Path: `assets/figures/dapo17k_sweep/action_entropy_per_token_heatmap.png`

Caption: DAPO17k action entropy per-token heatmap.

Meaning: Shows model rollout/action entropy rather than binary verifier
entropy.

Supports: Separation between rollout entropy and verifier entropy.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/action_entropy_per_token_heatmap.png`

## assets/figures/dapo17k_sweep/completed_problem_H_p_action_entropy_subplots_latest.png

Path: `assets/figures/dapo17k_sweep/completed_problem_H_p_action_entropy_subplots_latest.png`

Caption: Completed-problem verifier entropy, success rate, and action entropy.

Meaning: Combines the three central per-prompt trajectories used in the story:
`H(p_t)`, `p_t`, and rollout action entropy.

Supports: Unified view of binary-verifier projection and distributional
shrinkage.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/completed_problem_H_p_action_entropy_subplots_latest.png`

## assets/figures/dapo17k_sweep/initial_final_relationships.png

Path: `assets/figures/dapo17k_sweep/initial_final_relationships.png`

Caption: Initial versus final relationships in the DAPO17k sweep.

Meaning: Summarizes how starting difficulty/information relates to final
performance and dynamics.

Supports: Difficulty and information-efficiency analysis.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/initial_final_relationships.png`

## assets/figures/dapo17k_sweep/sweep_curves.png

Path: `assets/figures/dapo17k_sweep/sweep_curves.png`

Caption: Aggregate DAPO17k sweep curves.

Meaning: Shows aggregate training/evaluation curves over the sweep.

Supports: Background evidence for prompt-level RLVR dynamics.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/sweep_curves.png`

## assets/figures/dapo17k_sweep/valid_subplots_overview_latest.png

Path: `assets/figures/dapo17k_sweep/valid_subplots_overview_latest.png`

Caption: Validation overview subplots.

Meaning: Larger dashboard overview of validation behavior across prompts.

Supports: Data-quality and broader-sweep context.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/valid_subplots_overview_latest.png`

## assets/figures/dapo200/H_heatmap.png

Path: `assets/figures/dapo200/H_heatmap.png`

Caption: DAPO200 verifier entropy heatmap.

Meaning: Heatmap of binary verifier uncertainty over a 200-problem sweep.

Supports: Scalability of binary-verifier projection diagnostics.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo200-lr6e6-r32-s50-combined-20260526/final_044405/H_heatmap.png`

## assets/figures/dapo200/p_small_multiples.png

Path: `assets/figures/dapo200/p_small_multiples.png`

Caption: DAPO200 per-question pass-rate trajectories.

Meaning: Shows many prompt-level `p_t` curves in one sweep, useful as
large-scale finite-projection evidence.

Supports: Binary-verifier projection at larger prompt count.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo200-lr6e6-r32-s50-combined-20260526/final_044405/p_small_multiples.png`

## assets/figures/dapo200/action_entropy_per_token_heatmap.png

Path: `assets/figures/dapo200/action_entropy_per_token_heatmap.png`

Caption: DAPO200 action entropy per-token heatmap.

Meaning: Larger-sweep rollout entropy diagnostic.

Supports: Distributional shrinkage at larger prompt count.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo200-lr6e6-r32-s50-combined-20260526/final_044405/action_entropy_per_token_heatmap.png`

## assets/figures/dapo200/initial_final_relationships.png

Path: `assets/figures/dapo200/initial_final_relationships.png`

Caption: DAPO200 initial-final relationships.

Meaning: Relates initial prompt state to final performance and information
metrics.

Supports: Difficulty and prompt heterogeneity.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo200-lr6e6-r32-s50-combined-20260526/final_044405/initial_final_relationships.png`

## assets/figures/dapo200/sweep_curves.png

Path: `assets/figures/dapo200/sweep_curves.png`

Caption: DAPO200 aggregate sweep curves.

Meaning: Aggregate dynamics from the 200-problem run.

Supports: Larger-scale context for the poster claims.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo200-lr6e6-r32-s50-combined-20260526/final_044405/sweep_curves.png`

## assets/figures/pair10/pair10_dynamics_overview.png

Path: `assets/figures/pair10/pair10_dynamics_overview.png`

Caption: Pair10 dynamics overview.

Meaning: Pilot view comparing two-prompt dynamics against single-prompt runs.

Supports: Early additivity and interaction diagnostics.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/paper_assets_pair10_20260527/figures/pair10_dynamics_overview.png`

## assets/figures/pair10/pair10_Hdmaxp_bar.png

Path: `assets/figures/pair10/pair10_Hdmaxp_bar.png`

Caption: Pair10 `H * dmaxp` bar summary.

Meaning: Summarizes information-weighted performance movement for the pair10
pilot.

Supports: Early performance-coupled information metric.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/paper_assets_pair10_20260527/figures/pair10_Hdmaxp_bar.png`

## assets/figures/pair10/pair10_var_endpoint_bar.png

Path: `assets/figures/pair10/pair10_var_endpoint_bar.png`

Caption: Pair10 variance endpoint bar.

Meaning: Uses `p(1-p)` as an unsmoothed verifier-uncertainty proxy for endpoint
comparisons.

Supports: Alternative feature map for the finite LLM verifier projection.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/paper_assets_pair10_20260527/figures/pair10_var_endpoint_bar.png`

## assets/figures/pair10/pair_Hdmaxp_cumulative_dynamics_20260527.png

Path: `assets/figures/pair10/pair_Hdmaxp_cumulative_dynamics_20260527.png`

Caption: Cumulative pair `H * dmaxp` dynamics.

Meaning: Tracks cumulative performance-coupled information through time in a
two-prompt setting.

Supports: Pairwise additivity and information accumulation.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/pair_Hdmaxp_cumulative_dynamics_20260527.png`

## assets/figures/pair10/pair_Hdmaxp_subadditivity_bar_20260527.png

Path: `assets/figures/pair10/pair_Hdmaxp_subadditivity_bar_20260527.png`

Caption: Pair subadditivity bar for `H * dmaxp`.

Meaning: Compares joint pair training with the sum of isolated prompt
quantities.

Supports: Dataset additivity/subadditivity.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/pair_Hdmaxp_subadditivity_bar_20260527.png`

## assets/figures/pair10/pair_Hdp_per_question_delta_20260527.png

Path: `assets/figures/pair10/pair_Hdp_per_question_delta_20260527.png`

Caption: Per-question pair delta for `H * dp`.

Meaning: Shows which prompt in a pair accounts for the measured information-
weighted performance change.

Supports: Prompt-level decomposition of pair dynamics.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/pair_Hdp_per_question_delta_20260527.png`

## assets/figures/pair10/pair_Hsum_Hdp_dynamics_20260527.png

Path: `assets/figures/pair10/pair_Hsum_Hdp_dynamics_20260527.png`

Caption: Pair `Hsum` and `H * dp` dynamics.

Meaning: Compares raw verifier-information exposure with performance-coupled
information movement.

Supports: Distinction between bounded exposure and useful improvement.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/dapo17k_infogain_dashboard_latest/pair_Hsum_Hdp_dynamics_20260527.png`

## assets/figures/transfer_matrix8/delta_p_common_baseline.png

Path: `assets/figures/transfer_matrix8/delta_p_common_baseline.png`

Caption: 8x8 endpoint transfer matrix.

Meaning: Earlier small-matrix experiment: train on source prompt `i`, evaluate
target prompt `j`, and plot common-baseline `DeltaP_ij`.

Supports: Cross-prompt transfer matrix concept.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/transfer-matrix8-20260603-173013/analysis/delta_p_common_baseline.png`

## assets/figures/transfer_matrix8/positive_delta_p_common_baseline.png

Path: `assets/figures/transfer_matrix8/positive_delta_p_common_baseline.png`

Caption: Positive part of the 8x8 endpoint transfer matrix.

Meaning: Clips negative transfer to zero to emphasize sparse positive transfer
edges.

Supports: Sparse transfer and prompt coverage.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/transfer-matrix8-20260603-173013/analysis/positive_delta_p_common_baseline.png`

## assets/figures/transfer_matrix8/self_normalized_delta_p_common_baseline.png

Path: `assets/figures/transfer_matrix8/self_normalized_delta_p_common_baseline.png`

Caption: Self-normalized 8x8 transfer matrix.

Meaning: Normalizes each row by its self-transfer scale so diagonal entries
serve as a comparable reference.

Supports: Relative cross-transfer strength.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/transfer-matrix8-20260603-173013/analysis/self_normalized_delta_p_common_baseline.png`

## assets/figures/transfer_matrix8/info_weighted_positive_common.png

Path: `assets/figures/transfer_matrix8/info_weighted_positive_common.png`

Caption: Information-weighted positive 8x8 transfer matrix.

Meaning: Weights positive endpoint transfer by source-side information exposure.

Supports: Linking the source-side Bernoulli projection to transfer geometry.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/transfer-matrix8-20260603-173013/analysis/info_weighted_positive_common.png`

## assets/figures/perstep_transfer/perstep_cos_bar.png

Path: `assets/figures/perstep_transfer/perstep_cos_bar.png`

Caption: Per-step alignment cosine by source-target pair.

Meaning: Measures whether source-side information signal and target-side
performance improvement move in the same direction over training steps.

Supports: Per-step alignment and causal-candidate screening.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/perstep-transfer-20260603-185621/analysis/perstep_cos_bar.png`

## assets/figures/perstep_transfer/perstep_transfer_ratio_bar.png

Path: `assets/figures/perstep_transfer/perstep_transfer_ratio_bar.png`

Caption: Per-step transfer ratio by source-target pair.

Meaning: Diagonal-normalized transfer score for selected pair candidates.

Supports: Cross-prompt covariance-like alignment metric.

Source: `/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/perstep-transfer-20260603-185621/analysis/perstep_transfer_ratio_bar.png`
