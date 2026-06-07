# Vertical Integrated Poster

This folder contains the primary vertical poster for the current story:

```text
AlphaZero-like self-play
-> renewable 50/50 rollout frontier
-> unbounded cumulative information integral

fixed LLM math RLVR
-> prompts collapse to all-right or all-wrong
-> finite useful Bernoulli projection on a fixed dataset

RL sharpening
-> broad rollout distribution shrinks into problem seeds
-> transfer matrix defines dataset geometry
```

Generated files:

- `vertical_information_integral_poster.png`
- `vertical_information_integral_poster.pdf`

Editable source:

- `build_vertical_poster.py`

Regenerate locally from the repository root:

```bash
python3 poster/vertical_integrated_poster/build_vertical_poster.py
```

Main evidence used:

- Connect4/OpenSpiel numbers from `poster/connectfour/5.31.md`
- 40-prompt LLM RLVR figures and numbers from `poster/llm_rl`
- Geometry figures from `poster/llm_rl/assets/figures/geometry40`

The poster is intentionally focused on the main AlphaZero-vs-LLM-math logic.
Diffusion RL assets remain in `poster/diffusion_rl` as supporting material, but
are not used in the vertical poster to keep the visual argument clean.
