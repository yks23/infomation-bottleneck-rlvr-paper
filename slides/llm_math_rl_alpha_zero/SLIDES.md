# Class Presentation Slides

This folder contains a self-contained HTML slide deck for the class presentation:

- `index.html`: open this directly in a browser. Use left/right arrow keys to navigate.
- `assets/`: local figures copied from the RLVR final figure bundle.

Suggested title:

> 为什么学术界的大模型数学RL没有像AlphaZero那样轻易解决？

## Core Story

The central claim is:

> AlphaZero-style self-play keeps generating high-variance learning signals, while RL on a fixed math dataset has a finite information budget.

The talk should not begin with infrastructure or experiments. It should begin with the puzzle:

1. AlphaZero can improve by playing itself.
2. LLM math RL also has verifiers and rollouts.
3. So why does it not explode into fast self-improvement?

The answer in this deck is that fixed math datasets behave like bounded information reservoirs. A prompt either remains unsolved, or it gets solved and then stops producing useful reward variance.

## Slide-by-Slide Script

### 1. Opening Question

Introduce the question and presenters:

> 为什么学术界的大模型数学RL没有像AlphaZero那样轻易解决？

Presenters:

> 杨凯森，黄禹

Do not give the answer yet. This slide should only create the puzzle.

### 2. Two Tempting Explanations

List two common answers:

1. The action space is huge: Go has 361 board positions, while a model vocabulary can have 160k tokens.
2. Language has weak legality constraints: the model can emit invalid symbolic expressions.

These are real issues, but not the deepest bottleneck.

### 3. Why They Are Probably Not Core

Argue that both problems are engineerable:

- For math, the useful token alphabet can be compressed to hundreds of math-relevant tokens.
- Lean, parsers, compilers, and constrained decoding can reject illegal expressions.

### 4. Main Thesis

State the thesis:

> Academic LLM math RL usually experiments on a dataset of fixed size. For such a dataset, total rollout information is bounded.

Use:

- `assets/bounded_information_budget.png`

Message:

> For a fixed training set D = {q_1, ..., q_n}, RL repeatedly samples rollouts from the same problem/verifier sources. If each problem has a finite information integral C_i, then the dataset-level integral is bounded by sum_i C_i.

### 5. Information Metric

Define the objects before giving the metric:

- Problem: `q_i`
- Model at step `t`: `pi_t`
- One rollout: `tau_i(t) ~ pi_t(. | q_i)`
- Verifier reward: `R_i(t)=r(q_i, tau_i(t))`

Normalize reward by an affine transform to `[0,1]` before comparing variances, so reward scale does not dominate:

```text
R01_i(t) = (R_i(t) - R_min) / (R_max - R_min)
I_i(t) = V[R01_i(t)]
```

For binary verifier reward:

```text
I_i(t) = p_i(t)(1-p_i(t)) <= 1/4
```

The information integral is:

```text
A_i(T) = sum_{t=0}^{T-1} I_i(t)
A_D(T) = sum_{q_i in D} A_i(T)
```

### 6. AlphaZero / Connect Four

First ask how AlphaZero avoids this fixed-dataset exhaustion.

Background:

- Policy/value network proposes evaluations.
- MCTS searches from the current state.
- Self-play generates new games.
- The resulting wins/losses train the next network, which becomes the next opponent.

Use Connect Four as a small example:

- In self-play, the two players are usually close in strength.
- Outcomes stay close to half win / half lose.
- Therefore `p(win) ~= 1/2`, so `V[R] ~= 1/4`, the maximum binary-reward information.

### 7. Math Dataset With One Problem

Use:

- `assets/completed_problem_H_p_subplots_top50.png`

Message:

> This DAPO-17k completed sweep is many independent single-question runs. Each panel is a dataset with only one trained problem. Useful information appears only in the transition region; once `p_i(t)` approaches 0 or 1, `I_i(t)=p_i(t)(1-p_i(t))` goes to 0.

### 8. Math Dataset With Many Problems

Use:

- `assets/dapo17k_p_H_top30_multitask.png`

Message:

> The DAPO-17k sweep panel shows the first 30 prompt trajectories. The top half shows each prompt's pass-rate trajectory and the bottom half shows the corresponding information trajectory. The dataset behaves like many finite information pockets. Total information can grow with problem count, but it is still bounded for a fixed set.

### 9. Multi-Problem Additivity

Use:

- `assets/diag_vs_offdiag_transfer_histogram.png`
- `assets/additivity_summary_bars.png`

Message:

> Prompt interactions are not zero, but they are weak enough that adding relatively independent prompts increases the information budget approximately additively.

### 10. Distance Definition 1: Performance Vector

Use `assets/sparse_delta_p_common_heatmap.png`.

Define:

```text
x_i = (p_i1, p_i2, ..., p_in)
d_cos(i,j) = 1 - cos(x_i, x_j)
```

Here `p_ij` is the performance / improvement of target `j` after training source `i`. Each row is a prompt fingerprint. If two source prompts improve the same targets, their vectors point in the same direction. This gives an approximately undirected distance.

### 11. Distance Definition 2: Self-Normalized Directed Transfer

Use:

- `assets/sparse_positive_delta_p_common_heatmap.png`
- `assets/sparse_source_transfer_summary.png`
- `assets/anchor_knn_graph.png`

Define:

```text
R_ij = p_ij / p_ii
```

This is a direct measure of how much training source `i` transfers to target `j`, normalized by how much source `i` helps itself. It is naturally directed. For a symmetric distance, merge `R_ij` and `R_ji`.

### 12. Sharpness and Geometry

Use:

- `assets/sparse_action_entropy_per_token_heatmap.png`
- `assets/seed_geometry_sharpness_embedding.png`

Message:

- Action entropy measures shrinkage.
- Transfer vectors define a prompt geometry.
- The geometry tells us which prompts can help or fail to help each other.

### 13. Watermelon to Seeds

Use the right-side embedding from the previous slide as the seeds.

Message:

> The base model is a wide distribution. RL on a fixed dataset shrinks it into many sharp seeds, one per prompt or solution mode. These seeds inherit the transfer geometry measured above.

The HTML slide uses a simple animation: the watermelon shrinks and the geometry embedding appears as the final seed map.

### 14. Diffusion RL Experiment

Use:

- `assets/diffusion_final_image_grid.png`

Message:

> The diffusion version is the same information-bottleneck story with a different rollout object. A math problem becomes a text prompt, a rollout becomes a generated image / denoising trajectory, and a binary verifier becomes continuous reward channels such as ImageReward, PickScore, and HPSv2.

Formula:

```text
c_i -> x ~ pi_t(. | c_i) -> R(c_i, x)
I_i(t) = Var_x[R(c_i, x)]
```

Experiment setting:

- SDXL + TRL DDPO + LoRA.
- 10 prompt-balanced setup.
- Conditions: No-RL, IR-only, PS-only, IR+PS.
- Held-out evaluator: HPSv2.

### 15. Diffusion Information Results

Use:

- `assets/diffusion_cross_reward_matrix_final_z.png`
- `assets/diffusion_final_active_channel_information.png`
- `assets/diffusion_active_iacc_vs_hpsv2.png`

Message:

> Multi-reward feedback is a wider information channel. IR+PS is not strictly better than the strongest single reward on held-out HPSv2, but it gives the most balanced reward profile and the highest active accessible information.

Careful wording:

- All RL conditions improve held-out HPSv2 over No-RL in the final eval.
- PS-only is slightly best on HPSv2.
- IR+PS almost ties PS-only on HPSv2 and is best on ImageReward/PickScore balance.
- IR+PS has the highest prompt-group accessible information.

### 16. How to Get More Information

Three directions:

1. Add more relatively independent prompts.
2. Add richer reward signals per prompt: proof states, partial credit, Lean feedback, step rewards.
3. Move toward generative environments: theorem generation, diffusion-style generation, AI-created tasks.

The final point:

> As models get stronger, humans alone cannot keep supplying enough frontier tasks. We need AI-generated tasks and self-iteration.

### 17. Takeaway

Close with:

> AlphaZero is powerful because self-play keeps the information stream alive. Fixed-dataset math RL is a finite-information sharpening process.

Three words:

- Bounded
- Additive
- Geometric

## Figure Sources

The figures in `assets/` were copied from:

```text
/mnt/shared-storage-user/safewt-share/sunyoubang/verl-agent-run-logs/rlvr_final_figure_bundle_20260608_with_sparse8x4/figures
```

Key supporting figures:

- `train_to_p1_sweep_curves.png`: sweep curves showing that math prompts tend to remain unsolved or rapidly converge, leaving a narrow informative transition window.
- `completed_problem_H_p_subplots_top50.png`: DAPO-17k completed-prompt small multiples showing `H(p_t)` and `p_t` per prompt, cropped to top-50 panels for slide readability.
- `train_to_p1_H_curve.png`: information/entropy trajectory for the same process.
- `sparse_p_small_multiples.png`: per-prompt pass-rate trajectories.
- `sparse_H_small_multiples.png`: per-prompt information/variance trajectories.
- `dapo17k_p_H_top30_multitask.png`: slide-friendly p/H montage from the DAPO-17k sweep, cropped to the first 30 prompts.
- `diag_vs_offdiag_transfer_histogram.png`: diagonal vs off-diagonal transfer evidence.
- `additivity_summary_bars.png`: summary for weak interaction / approximate additivity.
- `sparse_delta_p_common_heatmap.png`: source-to-anchor transfer matrix.
- `sparse_positive_delta_p_common_heatmap.png`: positive part of the transfer panel.
- `sparse_source_transfer_summary.png`: source transfer-out summary.
- `anchor_knn_graph.png`: kNN graph built from anchor fingerprints.
- `directed_edges.png`: directed transfer edges.
- `sparse_action_entropy_per_token_heatmap.png`: action entropy shrinkage.
- `seed_geometry_sharpness_embedding.png`: prompt geometry visualization.
- `diffusion_final_image_grid.png`: SDXL DDPO final samples for No-RL, IR-only, PS-only, and IR+PS.
- `diffusion_cross_reward_matrix_final_z.png`: final cross-reward matrix for the diffusion DDPO experiment.
- `diffusion_final_active_channel_information.png`: prompt-group entropy, reward separation, and accessible information for active training channels.
- `diffusion_active_iacc_vs_hpsv2.png`: active-channel accessible information versus held-out HPSv2.

## Suggested 8-Minute Timing

- Slides 1-3: 1.5 min
- Slides 4-6: 2 min
- Slides 7-9: 1.5 min
- Slides 10-13: 2 min
- Slides 14-17: 1.5 min

For a shorter 5-minute version, skip slides 9, 11, and 15.
