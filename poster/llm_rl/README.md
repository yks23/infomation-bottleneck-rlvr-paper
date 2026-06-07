# LLM RL Poster Bundle

This directory is a self-contained sharing bundle for the LLM RLVR poster story:

```text
finite verifier information
-> rollout/action entropy shrinkage
-> cross-prompt transfer geometry
-> curriculum / prompt allocation
```

Main poster:

- PNG: `assets/poster/rlvr_distributional_shrinkage_poster.png`
- PDF: `assets/poster/rlvr_distributional_shrinkage_poster.pdf`
- Six-panel overview: `assets/poster/rlvr_story_overview.png`

## Core Claim

RLVR can be viewed as distributional shrinkage. A base model starts with a broad
rollout/action distribution for each prompt. RL updates reduce uncertainty and
turn that broad distribution into lower-entropy, problem-conditioned seeds.
Cross-prompt transfer then defines a directed geometry between those seeds.

## Main 40x40 Result

The latest run trains on 40 source prompts and evaluates transfer to the same
40 target prompts:

```text
source x target cells: 40 x 40 = 1600
positive transfer cells: 608 / 1600
significant cells: 42
mean diagonal DeltaP_common: 0.0706
mean off-diagonal DeltaP_common: 0.0091
offdiag / diag: 0.129
near-additivity score: 0.871
```

The finite verifier-information proxy is bounded:

```text
sum_i sum_t h2(p_i(t)) = 265.5 step-bits
upper bound = 640.0 step-bits
realized fraction = 41.5%
```

Rollout shrinkage is measured using model action entropy, not binary success
entropy:

```text
all-rollout action entropy: 0.281 -> 0.268 nats/token
correct-only action entropy: 0.217 -> 0.202 nats/token
correct-only shrink: 0.0151 nats/token
correct-only support: 31 / 40 sources
```

The transfer matrix is low-rank enough to visualize:

```text
2D explained variance: 0.483
16D explained variance: 0.953
```

## Contents

- `CONCLUSIONS.md`: concise claims, caveats, and takeaways.
- `POSTER_TEXT.md`: text used for the poster story and talks.
- `FIGURE_INDEX.md`: grouped figure/table list with suggested usage.
- `ASSET_MANIFEST.csv`: selected assets and their original source paths.
- `assets/figures/geometry40`: primary 40x40 transfer geometry figures.
- `assets/figures/dapo17k_sweep`: older DAPO17k information-gain figures.
- `assets/figures/dapo200`: 200-problem sweep figures.
- `assets/figures/pair10`: pair/additivity pilot figures.
- `assets/figures/transfer_matrix8`: earlier 8x8 transfer matrix figures.
- `assets/figures/perstep_transfer`: per-step alignment figures.
- `assets/tables`: supporting CSV/JSON tables.
- `assets/manifests/all_existing_assets`: index of the larger local old-asset bundle.

The larger local bundle was not committed because it is about 787 MB. This
poster bundle keeps the branch lightweight while preserving source paths for
full local retrieval.
