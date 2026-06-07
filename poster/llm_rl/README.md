# LLM RL Poster Bundle

This directory is a self-contained sharing bundle for the LLM RLVR poster story:

```text
bounded rollout/path information integral
-> finite verifier projection in LLM RLVR
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

The bounded-information object is the rollout/path-level information integral,
not `h2(p)` by itself. For a binary verifier, `h2(p_t)` or `p_t(1-p_t)` is the
observable Bernoulli projection of that path integral. The useful finite score
is the performance-coupled projection:

```text
P_i^H = sum_t H_b(p_i(t))
G_i^H = sum_t H_b(p_i(t)) * Delta p_i^+(t)
0 <= G_i^H <= 1 bit
```

Connect4/OpenSpiel is the traditional-RL anchor: self-play can keep refreshing
the rollout distribution near the current frontier, so its information integral
is not capped by a fixed prompt set in the same way as fixed-dataset LLM RLVR.

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

The LLM Bernoulli-verifier projection is bounded:

```text
sum_i sum_t h2(p_i(t)) = 265.5 step-bits
upper bound = 640.0 step-bits
realized fraction = 41.5%
```

The per-question `p_i(t)` trajectory figures are direct visual evidence for the
finite binary projection: `p_i(t)` always lives in `[0,1]`, so each verifier step
contributes at most one Bernoulli entropy bit. The poster should phrase this as
evidence about the LLM projection of the rollout/path integral, not as the full
definition of information.

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
- `HANDOFF.md`: shortest integration entrypoint for collaborators.
- `POSTER_TEXT.md`: text used for the poster story and talks.
- `FIGURE_INDEX.md`: grouped figure/table list with suggested usage.
- `FIGURE_CATALOG.md`: detailed caption, meaning, claim, and source for each figure.
- `ASSET_MANIFEST.csv`: selected assets and their original source paths.
- `assets/figures/geometry40`: primary 40x40 transfer geometry figures.
- `assets/figures/traditional_rl`: Connect4/OpenSpiel traditional RL anchor.
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
