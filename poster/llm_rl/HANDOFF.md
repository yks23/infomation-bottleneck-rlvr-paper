# LLM RL Poster Handoff

Use this file as the integration entrypoint. It is intentionally shorter than
`FIGURE_CATALOG.md`.

## One-Sentence Story

RLVR turns broad rollout distributions into lower-entropy problem-conditioned
seeds; a fixed verifier gives a bounded information budget, most prompt gains
are additive, and sparse cross-prompt transfer defines the geometry between
seeds.

## Main Poster Files

- Poster PNG: `assets/poster/rlvr_distributional_shrinkage_poster.png`
- Poster PDF: `assets/poster/rlvr_distributional_shrinkage_poster.pdf`
- Overview PNG: `assets/poster/rlvr_story_overview.png`

## Core Numbers To Quote

From `assets/tables/geometry40/story_numbers.csv`:

```text
40 x 40 source-target matrix
positive transfer cells: 608 / 1600
significant transfer cells: 42
bounded verifier information: 265.5 / 640.0 step-bits = 41.5%
mean diagonal DeltaP_common: 0.0706
mean off-diagonal DeltaP_common: 0.0091
offdiag / diag: 0.129
near-additivity score: 0.871
all-rollout action entropy: 0.281 -> 0.268 nats/token
correct-only action entropy: 0.217 -> 0.202 nats/token
correct-only entropy support: 31 / 40 sources
2D transfer explained variance: 0.483
16D transfer explained variance: 0.953
```

## Minimum Figure Set For A Paper/Slide

1. `assets/figures/geometry40/p_small_multiples.png`
   - Caption: Per-prompt pass-rate trajectories `p_i(t)` in the 40-prompt run.
   - Use for: bounded verifier information evidence.

2. `assets/figures/geometry40/bounded_information_budget.png`
   - Caption: Realized cumulative verifier uncertainty versus per-step bound.
   - Use for: finite information budget.

3. `assets/figures/geometry40/diag_vs_offdiag_transfer_histogram.png`
   - Caption: Self-transfer dominates off-diagonal transfer.
   - Use for: dataset is mostly additive.

4. `assets/figures/geometry40/correct_rollout_action_entropy_trajectories.png`
   - Caption: Action entropy of successful rollouts during RL.
   - Use for: rollout distribution shrinkage.

5. `assets/figures/geometry40/cluster_heatmap.png`
   - Caption: Cluster-sorted directed transfer matrix.
   - Use for: prompt transfer geometry.

6. `assets/figures/geometry40/seed_geometry_sharpness_embedding.png`
   - Caption: Problem seeds embedded by transfer fingerprints.
   - Use for: geometric visualization.

7. `assets/figures/geometry40/svd_spectrum.png`
   - Caption: Low-rank structure of the transfer matrix.
   - Use for: dimensionality of prompt geometry.

## Minimal Table Set

- `assets/tables/geometry40/story_numbers.csv`
  - Main numbers for poster and text.
- `assets/tables/geometry40/bounded_information_by_source.csv`
  - Per-source verifier information, action entropy, and self gain.
- `assets/tables/geometry40/geometry40_self_gain_by_problem.csv`
  - Per-prompt self gain.
- `assets/tables/geometry40_endpoint/delta_p_common_initial_matrix.csv`
  - Main directed transfer matrix.
- `assets/tables/geometry40_endpoint/endpoint_transfer_records.csv`
  - Long-form row-per-cell transfer table.

## Text To Reuse

Short abstract:

```text
We view RLVR as distributional shrinkage. For each prompt, the verifier exposes
a bounded binary information budget, while RL sharpens the model's rollout
distribution into a lower-entropy problem-conditioned seed. On a 40-prompt
geometry run, self-transfer dominates cross-transfer (offdiag/diag = 0.129),
suggesting the dataset is mostly additive. Sparse positive cross-transfer still
reveals a low-dimensional prompt geometry: 2D explains 48.3% and 16D explains
95.3% of transfer variance.
```

Bounded-information sentence:

```text
Because each prompt success rate p_i(t) lies in [0,1], the verifier entropy
h2(p_i(t)) is at most one bit per training step; in the 40-prompt run, the
realized cumulative verifier uncertainty is 265.5 of 640.0 possible step-bits.
```

Additivity sentence:

```text
The mean self-transfer is 0.0706, while the mean off-diagonal transfer is
0.0091, so most dataset information behaves approximately additively and
cross-prompt effects are sparse.
```

Geometry sentence:

```text
Each source prompt is represented by its transfer fingerprint over targets;
distances between these fingerprints define a prompt-space geometry that can
support clustering, coverage, and curriculum allocation.
```

## Where To Look Next

- Full figure explanations: `FIGURE_CATALOG.md`
- Short navigation index: `FIGURE_INDEX.md`
- Exact source path for every bundled asset: `ASSET_MANIFEST.csv`
- Larger local old-asset index: `assets/manifests/all_existing_assets/manifest.csv`
