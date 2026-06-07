# SDXL DDPO Reward-Generalization Experiment Conclusions

Date: 2026-06-07

## 1. Executive Summary

目前可以得出一个有用但需要谨慎表述的结论：

> 在 SDXL + TRL DDPO 的小规模 online RL 实验中，单 prompt 结果不稳定且容易误导；扩展到 10 个 prompt 后，online RL 在最终评估上整体优于 No-RL/base。多 reward 训练没有严格赢过最好的单 reward 条件，但它给出了最均衡的 reward profile：IR 和 PS 训练 reward 最高，held-out HPSv2 几乎追平 PS-only，并且三 reward 平均最好。

因此，当前实验支持下面这个更稳妥的论文叙事：

> Multi-reward feedback improves reward balance and reduces dependence on a single reward channel. In a small prompt-balanced SDXL DDPO experiment, multi-reward training matches the strongest single-reward baseline on held-out HPSv2 while achieving better cross-reward balance.

当前实验还不能强声称：

> IR+PS 一定比所有 single-reward policy 更泛化。

原因是：在 10-prompt final eval 上，PS-only 的 HPSv2 略高于 IR+PS，二者差距约 0.001 z，基本可以视为打平，但不是严格胜出。

## 2. Experimental Setup Used for the Main Conclusion

主实验使用：

- Base model: SDXL base
- Online RL algorithm: Hugging Face TRL `DDPOTrainer`
- Trainable parameters: LoRA
- Reward conditions:
  - `No-RL`: only sampling/evaluation, no policy update
  - `IR-only`: optimize ImageReward
  - `PS-only`: optimize PickScore
  - `IR+PS`: optimize the mean of calibrated ImageReward and PickScore
- Held-out evaluator: HPSv2.1
- Prompt count: 10 prompts
- Seeds: 2 seeds per condition
- Training length: 10 epochs
- Per training condition: 10 prompt-balanced rollout batches per epoch, batch size 2
- Final eval: 4 images per prompt per condition, 40 images per condition

Important output paths:

- Main report: `report/sdxl_ddpo_10prompt_report.md`
- Rollout statistics report: `report/rollout_reward_stats_report.md`
- Main figures: `report/figures/main/`
- Rollout-stat figures: `report/figures/rollout_reward_stats/`
- Tables: `report/tables/`

## 3. Main Final-Eval Result

Final cross-reward matrix, calibrated z:

| Train condition | ImageReward | PickScore | HPSv2 |
|---|---:|---:|---:|
| No-RL | -0.1153 | -0.4470 | -0.1861 |
| IR-only | -0.1501 | -0.3804 | -0.1288 |
| PS-only | -0.0784 | -0.3601 | -0.0947 |
| IR+PS | -0.0755 | -0.3487 | -0.0958 |

Interpretation:

- All RL conditions improve held-out HPSv2 over No-RL at final eval.
- PS-only is the best final HPSv2 condition by a tiny margin.
- IR+PS is almost tied with PS-only on HPSv2.
- IR+PS is best on ImageReward and PickScore at final eval.
- IR+PS gives the best three-reward average:
  - No-RL: -0.2495
  - IR-only: -0.2198
  - PS-only: -0.1777
  - IR+PS: -0.1733

The strongest supported claim is therefore not "multi-reward dominates single reward", but:

> Multi-reward training produces the best cross-reward balance while preserving held-out HPSv2 performance comparable to the strongest single-reward policy.

Useful figure references:

- `report/figures/main/cross_reward_matrix_final_z.png`
- `report/figures/rollout_reward_stats/final_eval_reward_mean_z.png`
- `report/figures/rollout_reward_stats/final_objective_vs_hpsv2.png`

## 4. Why the 10-Prompt Result Matters

The earlier one-prompt experiments did not support a clean online-RL-over-base story.

Single prompt, 3 epochs, final HPSv2:

| Train condition | HPSv2 |
|---|---:|
| No-RL | 0.7355 |
| IR-only | 0.4469 |
| PS-only | 0.5988 |
| IR+PS | 0.5095 |

Single prompt, 20 epochs, final HPSv2:

| Train condition | HPSv2 |
|---|---:|
| No-RL | 0.8100 |
| IR-only | 0.5124 |
| PS-only | 0.6964 |
| IR+PS | 0.7762 |

This means:

- A single prompt can be dominated by the base model's initial quality.
- More DDPO epochs do not automatically improve held-out reward.
- Reward optimization on one prompt can move the policy away from the base image distribution in a way that hurts held-out HPSv2.
- Single-prompt experiments are useful for debugging the RL loop, but they are too small for a stable generalization claim.

After increasing to 10 prompts, the final HPSv2 ordering changes:

| Train condition | HPSv2 |
|---|---:|
| No-RL | -0.1861 |
| IR-only | -0.1288 |
| PS-only | -0.0947 |
| IR+PS | -0.0958 |

This supports the practical conclusion:

> Prompt diversity is necessary even for a minimal online diffusion RL experiment. A one-prompt setup can validate infrastructure, but a prompt-balanced setup is needed to observe a meaningful RL-over-base signal.

Useful figure references:

- `report/figures/main/hpsv2_curve.png`
- `report/figures/main/final_image_grid.png`

## 5. Mean and Variance Across Multiple Rollouts

Across all rollout samples, calibrated z means were:

| Train condition | ImageReward | PickScore | HPSv2 |
|---|---:|---:|---:|
| No-RL | -0.1327 | -0.4546 | -0.1680 |
| IR-only | -0.1283 | -0.4523 | -0.1778 |
| PS-only | -0.0937 | -0.4265 | -0.1581 |
| IR+PS | -0.1110 | -0.4298 | -0.1648 |

Across all rollout samples, calibrated z variances were:

| Train condition | ImageReward | PickScore | HPSv2 |
|---|---:|---:|---:|
| No-RL | 0.7180 | 0.3580 | 0.4381 |
| IR-only | 0.7131 | 0.4386 | 0.4928 |
| PS-only | 0.7318 | 0.4401 | 0.4943 |
| IR+PS | 0.7073 | 0.4267 | 0.4814 |

Interpretation:

- The all-rollout mean is much less separated than the final-eval mean.
- This suggests that reward improvement appears late in the short DDPO run rather than being uniformly present through the whole trajectory.
- PS-only has the best all-rollout HPSv2 mean, but the gain is small.
- IR+PS has lower HPSv2 variance than PS-only in final eval and all-rollout stats, while keeping similar final HPSv2 mean.
- The variance does not show catastrophic collapse. It mainly reflects prompt difficulty, seed variation, and image-level diversity.

Useful figure references:

- `report/figures/rollout_reward_stats/all_rollouts_reward_mean_z.png`
- `report/figures/rollout_reward_stats/all_rollouts_reward_variance_z.png`
- `report/figures/rollout_reward_stats/final_eval_reward_variance_z.png`

## 6. Per-Prompt Behavior

At final eval:

- IR-only improves HPSv2 over No-RL on 7/10 prompts.
- PS-only improves HPSv2 over No-RL on 7/10 prompts.
- IR+PS improves HPSv2 over No-RL on 7/10 prompts.
- IR+PS beats the better of IR-only and PS-only on 3/10 prompts.
- IR+PS average HPSv2 delta vs No-RL is +0.0903 z.
- IR+PS average gap to the best single-reward condition is -0.0484 z.

This gives a nuanced conclusion:

> Multi-reward training improves over base on most prompts, but it is not uniformly better than choosing the stronger single reward per prompt.

Prompt-level observations:

- `parti_00422` is the original badger/rose prompt. No-RL is already very strong there, and RL often hurts final HPSv2. This explains why the single-prompt experiment was misleading.
- `parti_00308` and `parti_00973` are difficult cases where RL does not consistently improve HPSv2.
- `parti_00233`, `parti_00300`, `parti_00555`, `parti_00674`, `parti_00708`, `parti_00861`, and `parti_00995` mostly benefit from RL.

Useful figure references:

- `report/figures/rollout_reward_stats/final_prompt_hpsv2_delta_vs_no_rl.png`
- `report/figures/rollout_reward_stats/final_prompt_hpsv2_heatmap.png`
- `report/figures/rollout_reward_stats/ir_ps_vs_best_single_final_hpsv2.png`

## 7. Single Reward vs Multi Reward

The data supports three separate statements:

### 7.1 Single-reward training works

Both IR-only and PS-only improve final held-out HPSv2 over No-RL:

- IR-only: -0.1288 vs No-RL -0.1861
- PS-only: -0.0947 vs No-RL -0.1861

This means the DDPO loop is not merely changing images arbitrarily; optimizing reward does transfer partially to held-out HPSv2.

### 7.2 PS-only is a strong baseline

PS-only is the best final HPSv2 condition:

- PS-only HPSv2: -0.0947
- IR+PS HPSv2: -0.0958

The difference is tiny, but the ordering matters for claims. We should not say multi-reward strictly wins on held-out HPSv2.

### 7.3 Multi-reward is the most balanced

IR+PS is best on the two training reward channels:

- IR+PS ImageReward: -0.0755
- PS-only ImageReward: -0.0784
- IR+PS PickScore: -0.3487
- PS-only PickScore: -0.3601

IR+PS also has the best all-reward mean:

- IR+PS: -0.1733
- PS-only: -0.1777
- IR-only: -0.2198
- No-RL: -0.2495

The best interpretation is:

> Multi-reward optimization trades a tiny amount of held-out HPSv2 peak performance for better cross-reward balance.

This is still valuable for an information-bottleneck or reward-generalization argument, because it suggests that using multiple reward channels can avoid optimizing one reward in isolation.

Useful figure references:

- `report/figures/rollout_reward_stats/final_objective_vs_hpsv2.png`
- `report/figures/rollout_reward_stats/reward_correlation_heatmaps.png`
- `report/figures/main/ir_ps_cross_reward_curve.png`

## 8. What This Says About Reward Hacking

The current evidence does not show obvious catastrophic reward hacking.

Reasons:

- Final image grids are visually coherent.
- RL improves held-out HPSv2 over No-RL on average in the 10-prompt run.
- IR+PS improves both training rewards and nearly matches the best held-out HPSv2 result.
- Reward disagreement does not explode in a way that would suggest one reward is being gamed while the others collapse.

However, there is evidence of reward-specific behavior:

- IR-only is not consistently best on ImageReward in final eval.
- PS-only is strongest on held-out HPSv2, which may mean PickScore is closer to HPSv2 on this prompt set.
- Single-prompt RL can hurt held-out HPSv2 even after 20 epochs.

So the safe conclusion is:

> We do not see severe reward hacking in the 10-prompt run, but we do see reward-channel dependence. Multi-reward helps balance channels, but reward weighting and early stopping still matter.

Useful figure references:

- `report/figures/main/final_image_grid.png`
- `report/figures/main/reward_disagreement.png`
- `report/figures/rollout_reward_stats/reward_correlation_heatmaps.png`

## 9. Relation to the Information-Bottleneck Hypothesis

The original hypothesis is roughly:

> More informative reward feedback should produce better online RL behavior and better generalization to held-out reward models.

The current experiments partially support this.

Supported:

- Single-prompt reward feedback is too narrow and unstable.
- Adding prompt diversity improves held-out reward behavior.
- Multiple reward channels produce a more balanced solution than a single reward channel.
- IR+PS reaches the best final combined reward objective and nearly matches the best held-out HPSv2 result.

Not fully supported yet:

- IR+PS does not strictly beat PS-only on final held-out HPSv2.
- The experiment has only 10 prompts and 2 seeds.
- HPSv2 is only one held-out evaluator.
- We have not yet shown the result holds across broader prompt distributions or different model families.

Best current formulation:

> The experiments support a weaker but defensible information-feedback claim: reward diversity improves cross-reward consistency and avoids relying on a single reward channel. The stronger claim that multi-reward feedback always improves held-out reward generalization remains open.

## 10. Recommended Framing for a Paper or Internal Report

A good title-level claim would be:

> Prompt-balanced online diffusion RL benefits from reward diversity: multi-reward DDPO improves cross-reward balance and matches the strongest single-reward baseline on held-out HPSv2.

A strong but still honest abstract sentence:

> In a 10-prompt SDXL DDPO experiment, optimizing either ImageReward or PickScore improves held-out HPSv2 over the base sampler, while combining ImageReward and PickScore yields the best cross-reward balance and nearly identical held-out HPSv2 to the best single-reward run.

Avoid saying:

- "Multi-reward outperforms all single rewards."
- "This proves multi-reward reduces reward hacking."
- "Single prompt is sufficient for online diffusion RL conclusions."
- "The result generalizes to SD3.5 or broad prompt distributions."

Say instead:

- "Multi-reward improves reward balance."
- "10-prompt prompt-balanced RL gives a more reliable signal than single-prompt RL."
- "Held-out HPSv2 improves over No-RL for all RL conditions in the 10-prompt run."
- "PS-only remains a strong baseline, so reward weighting and early stopping are important."

## 11. Practical Next Steps

The next experiments should focus on tightening the story rather than rewriting the RL algorithm.

Recommended:

1. Early stopping analysis from existing checkpoints.
   - IR+PS peaks earlier than final in the HPSv2 curve.
   - Report both best-checkpoint and final-checkpoint results.

2. Reward-weight sweep.
   - Try `0.25 IR + 0.75 PS`, `0.5 IR + 0.5 PS`, and `0.75 IR + 0.25 PS`.
   - Since PS-only is close to best HPSv2, a PS-heavy mixture may keep HPSv2 while improving IR/PS balance.

3. Increase prompt count modestly.
   - 20 to 50 prompts would be much more convincing than 10 while still remaining small.
   - Keep seeds at least 2.

4. Add confidence intervals.
   - Bootstrap over prompts, not just images.
   - Prompt-level uncertainty is the meaningful uncertainty source here.

5. Keep SD3.5 as offline/eval unless there is a ready online RL implementation.
   - The current online result is specifically SDXL + DDPO.

## 12. Bottom Line

The current experiments are enough to support this conclusion:

> Online DDPO on SDXL can improve held-out reward over the base sampler when evaluated on a small prompt-balanced set. Multi-reward training is not a strict held-out HPSv2 winner over the best single reward in this run, but it gives the most balanced reward profile and nearly matches the strongest single-reward baseline. This makes multi-reward DDPO a promising but not yet fully proven approach for reward-generalized diffusion RL.

