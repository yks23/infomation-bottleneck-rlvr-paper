# LLM Math RL vs AlphaZero Slides

This directory is a self-contained slide bundle.

- `index.html`: animated browser version. Open this for the watermelon-to-seeds animation.
- `slides.pdf`: static PDF export for sharing or printing.
- `SLIDES.md`: speaker outline and figure notes.
- `assets/`: only the images referenced by `index.html`.

Main storyline:

1. AlphaZero keeps receiving high-variance self-play information.
2. Fixed math RL datasets have bounded rollout information.
3. Multi-prompt datasets are approximately additive when prompt interactions are weak.
4. Transfer measurements define a dataset geometry.
5. Fixed-dataset RL shrinks a broad distribution into many prompt-level seeds.
6. Diffusion DDPO shows the same information-channel view with continuous, multi-reward feedback.
