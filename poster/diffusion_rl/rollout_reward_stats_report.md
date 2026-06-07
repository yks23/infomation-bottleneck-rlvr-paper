# SDXL 10-Prompt Rollout Reward Statistics

## Scope

- `all_rollouts`: balanced trajectory samples. For each condition and prompt this has 44 images: 10 rollout steps x 2 seeds x 2 images plus the final eval, or 11 No-RL eval steps x 2 seeds x 2 images.
- `final_eval`: only the last eval sample for each condition, 4 images per prompt and 40 images per condition.
- Variance is score dispersion across prompts, seeds, and sampled images. It is not only estimator noise.

## All-Rollout Calibrated z Mean

| condition | IR | PS | HPSv2 |
|---|---|---|---|
| No-RL | -0.1327 | -0.4546 | -0.1680 |
| IR-only | -0.1283 | -0.4523 | -0.1778 |
| PS-only | -0.0937 | -0.4265 | -0.1581 |
| IR+PS | -0.1110 | -0.4298 | -0.1648 |

## All-Rollout Calibrated z Variance

| condition | IR | PS | HPSv2 |
|---|---|---|---|
| No-RL | 0.7180 | 0.3580 | 0.4381 |
| IR-only | 0.7131 | 0.4386 | 0.4928 |
| PS-only | 0.7318 | 0.4401 | 0.4943 |
| IR+PS | 0.7073 | 0.4267 | 0.4814 |

## Final-Eval Calibrated z Mean

| condition | IR | PS | HPSv2 |
|---|---|---|---|
| No-RL | -0.1153 | -0.4470 | -0.1861 |
| IR-only | -0.1501 | -0.3804 | -0.1288 |
| PS-only | -0.0784 | -0.3601 | -0.0947 |
| IR+PS | -0.0755 | -0.3487 | -0.0958 |

## Final-Eval Calibrated z Variance

| condition | IR | PS | HPSv2 |
|---|---|---|---|
| No-RL | 0.6861 | 0.3689 | 0.3964 |
| IR-only | 0.6415 | 0.4670 | 0.3892 |
| PS-only | 0.7051 | 0.5475 | 0.4827 |
| IR+PS | 0.6877 | 0.5031 | 0.4275 |

## Single vs Multi Reward

- IR-only improves HPSv2 over No-RL on 7/10 prompts, average delta +0.0573 z.
- PS-only improves HPSv2 over No-RL on 7/10 prompts, average delta +0.0914 z.
- IR+PS improves HPSv2 over No-RL on 7/10 prompts, average delta +0.0903 z.
- IR+PS beats the better single-reward run on 3/10 prompts at final eval; average gap to best single is -0.0484 HPSv2 z.
- Best final `(IR + PS) / 2` train-objective balance: IR+PS = -0.2121.
- Best final all-reward mean `(IR + PS + HPSv2) / 3`: IR+PS = -0.1733.
- Across all rollout steps, IR+PS average HPSv2 delta vs No-RL is +0.0032 z; final eval delta is +0.0903 z. This means the gain appears late in the short DDPO run, not uniformly across the whole trajectory.

## Figures

- `all_rollouts_reward_mean_z.png` / `.pdf`
- `all_rollouts_reward_variance_z.png` / `.pdf`
- `final_eval_reward_mean_z.png` / `.pdf`
- `final_eval_reward_variance_z.png` / `.pdf`
- `final_prompt_hpsv2_delta_vs_no_rl.png` / `.pdf`
- `all_rollouts_prompt_hpsv2_delta_vs_no_rl.png` / `.pdf`
- `final_prompt_hpsv2_heatmap.png` / `.pdf`
- `ir_ps_vs_best_single_final_hpsv2.png` / `.pdf`
- `reward_correlation_heatmaps.png` / `.pdf`
- `final_objective_vs_hpsv2.png` / `.pdf`

## Interpretation

- The 10-prompt run supports the basic online-RL-over-base story at final eval: every RL condition improves held-out HPSv2 mean over No-RL.
- The multi-reward condition is not a clean held-out HPSv2 winner over the best single reward. It is better framed as the most balanced condition: it has the best final IR and PS means, nearly ties PS-only on HPSv2, and gives the best average over IR/PS/HPSv2.
- PS-only remains a strong baseline on this prompt set. The next lever is not more code, but reward weighting or early stopping; IR+PS peaks at an earlier checkpoint in the existing curve.
