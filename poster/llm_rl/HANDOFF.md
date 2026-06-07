# LLM RL Poster Handoff

Use this file as the integration entrypoint. It is intentionally shorter than
`FIGURE_CATALOG.md`.

## One-Sentence Story

The central object is a bounded rollout/path information integral; in fixed
LLM RLVR, the binary verifier gives a finite observable projection of that
integral, RL shrinks rollout distributions into problem-conditioned seeds, and
sparse cross-prompt transfer defines the geometry between seeds.

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
LLM Bernoulli projection sum_t h2(p_t): 265.5 / 640.0 step-bits = 41.5%
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

1. `assets/figures/traditional_rl/openspiel_c4_mean_win_rate_by_condition.pdf`
   - Caption: Connect4/OpenSpiel traditional RL comparison.
   - Use for: AlphaZero-style self-play can renew rollout information, unlike a fixed prompt set.

2. `assets/figures/geometry40/p_small_multiples.png`
   - Caption: Per-prompt pass-rate trajectories `p_i(t)` in the 40-prompt run.
   - Use for: finite LLM verifier projection of the path integral.

3. `assets/figures/geometry40/bounded_information_budget.png`
   - Caption: Realized cumulative verifier uncertainty versus per-step bound.
   - Use for: bounded Bernoulli projection in fixed-dataset LLM RLVR.

4. `assets/figures/geometry40/diag_vs_offdiag_transfer_histogram.png`
   - Caption: Self-transfer dominates off-diagonal transfer.
   - Use for: dataset is mostly additive.

5. `assets/figures/geometry40/correct_rollout_action_entropy_trajectories.png`
   - Caption: Action entropy of successful rollouts during RL.
   - Use for: rollout distribution shrinkage.

6. `assets/figures/geometry40/cluster_heatmap.png`
   - Caption: Cluster-sorted directed transfer matrix.
   - Use for: prompt transfer geometry.

7. `assets/figures/geometry40/seed_geometry_sharpness_embedding.png`
   - Caption: Problem seeds embedded by transfer fingerprints.
   - Use for: geometric visualization.

8. `assets/figures/geometry40/svd_spectrum.png`
   - Caption: Low-rank structure of the transfer matrix.
   - Use for: dimensionality of prompt geometry.

## Minimal Table Set

- `assets/tables/geometry40/story_numbers.csv`
  - Main numbers for poster and text.
- `assets/tables/geometry40/bounded_information_by_source.csv`
  - Per-source Bernoulli projection, action entropy, and self gain.
- `assets/tables/geometry40/geometry40_self_gain_by_problem.csv`
  - Per-prompt self gain.
- `assets/tables/geometry40_endpoint/delta_p_common_initial_matrix.csv`
  - Main directed transfer matrix.
- `assets/tables/geometry40_endpoint/endpoint_transfer_records.csv`
  - Long-form row-per-cell transfer table.

## Text To Reuse

Short abstract:

```text
We view RL as converting rollout/path information into performance movement.
In fixed-dataset LLM RLVR, the binary verifier gives a finite Bernoulli
projection of the path integral, while RL sharpens the model's rollout
distribution into lower-entropy problem-conditioned seeds. Connect4 self-play
is the traditional-RL contrast: it renews the rollout distribution, so terminal
reward information is not capped by a fixed question set. On a 40-prompt LLM
geometry run, self-transfer dominates cross-transfer (offdiag/diag = 0.129),
suggesting the dataset is mostly additive. Sparse positive cross-transfer still
reveals a low-dimensional prompt geometry: 2D explains 48.3% and 16D explains
95.3% of transfer variance.
```

Bounded-information sentence:

```text
The bounded-information object is the rollout/path integral. In LLM math RLVR,
the binary verifier gives an observable Bernoulli projection: h2(p_i(t)) is at
most one bit per training step, and the 40-prompt run realizes 265.5 of 640.0
possible step-bits before projecting useful information onto performance
movement through sum_t h2(p_i(t)) Delta p_i^+(t).
```

Traditional RL contrast:

```text
Connect4/OpenSpiel shows the AlphaZero-style contrast: self-play renews the
rollout distribution as the policy changes, keeping reward variation near the
current frontier instead of exhausting a fixed prompt-verifier source.
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
