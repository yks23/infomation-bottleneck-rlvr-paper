# Poster Entrypoints

Primary integrated poster:

- `vertical_integrated_poster/vertical_information_integral_poster.png`
- `vertical_integrated_poster/vertical_information_integral_poster.pdf`
- `vertical_integrated_poster/build_vertical_poster.py`

Minimal website:

- `../website/index.html`

Core story:

```text
AlphaZero-like self-play keeps sampling near a renewable 50/50 frontier.
Its rollout/path information integral can keep growing with training time.

Fixed LLM math RLVR has a finite prompt-verifier source.
Questions tend to become all-right or all-wrong, so the useful middle-band
information is finite across the dataset.

RL then acts as distributional sharpening:
a broad rollout distribution shrinks into problem-conditioned seeds.
The cross-prompt transfer matrix defines distances between those seeds.
```

Supporting bundles:

- `connectfour/`: traditional RL / OpenSpiel Connect4 evidence.
- `llm_rl/`: 40-prompt LLM RLVR transfer geometry and action-entropy evidence.
- `diffusion_rl/`: diffusion RL reward-channel evidence.
- `information_bottleneck_rlvr_poster.tex`: earlier horizontal LaTeX draft.
