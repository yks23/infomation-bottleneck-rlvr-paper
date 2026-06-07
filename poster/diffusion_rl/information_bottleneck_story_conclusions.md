# Information-Bottleneck Story for the SDXL DDPO Experiments

Date: 2026-06-07

Reference paper:

`/root/Information-bottleneck-RL/docs/Analysing_Information_Bottleneck_in_Reinforcement_Learning_from_Verifiable_Rewards (1).pdf`

## 1. Core Story

结合论文的信息瓶颈视角，目前这组 SDXL DDPO 实验最适合讲下面这个 story：

> Online diffusion RL 的有效性不只取决于 reward 是否 dense，也不只取决于 rollout 数量，而取决于 reward channel 对同一 prompt 下不同 rollouts 是否提供了可区分、非塌缩的反馈信息。单 prompt 实验因为 prompt 太少、base 质量过强，容易落入低有效信息或 reward-alignment 不稳定的区域；扩展到 10 prompts 后，rollout feedback 更接近模型能力边界，RL 才开始稳定优于 No-RL。多 reward 训练进一步提供更丰富的反馈通道，使 policy 在 ImageReward 和 PickScore 上更均衡，同时在 held-out HPSv2 上接近最强 single-reward baseline。

这比“IR+PS 一定赢过 single reward”更贴合当前数据，也更契合论文的核心观点：

> RLVR 的瓶颈不是 reward 稀疏本身，而是 reward-induced feedback information 的塌缩。

在我们的 diffusion setting 中，对应关系是：

| Paper RLVR concept | Diffusion experiment analogue |
|---|---|
| problem `x` | text prompt |
| trajectory `tau` | generated image / denoising trajectory outcome |
| verifier outcome `O` | reward model score transformed to bounded `r01` |
| binary/graded verifier | ImageReward, PickScore, HPSv2 |
| prompt-level rollout group | multiple generated images for the same prompt |
| high-information prompt | reward scores are neither saturated nor identical across images |
| low-information prompt | all samples get nearly same reward, or reward is too easy/too hard |

## 2. Paper Definitions Used Here

The paper defines a reward channel as:

```text
R: (x, tau) -> O
```

For a prompt-level rollout group, the paper focuses on three quantities.

Outcome entropy:

```text
H_B(O | x) = h(p_bar)
```

where `p_bar` is the average bounded reward for the rollout group. This is high when feedback is near the mixed regime, roughly `p_bar ~= 0.5`, and low when almost all outcomes are failure-like or success-like.

Reward separation:

```text
S_rel(x) = mean_i (r_i - p_bar)^2
```

This measures whether the reward channel can distinguish different rollouts for the same prompt. If all rollouts get the same reward, group-relative advantages vanish.

Accessible feedback information:

```text
I_acc(x) = H_B(O | x) * S_rel(x) / (S_rel(x) + eps)
```

This is not a new training objective. It is a diagnostic for how much usable feedback the current policy and current reward channel expose.

For this experiment, I used:

- `r01 = sigmoid(calibrated_z)` as the bounded reward proxy.
- prompt-level groups from final eval: 10 prompts x 4 images per condition.
- `IR+PS combined = 0.5 * (r01_IR + r01_PS)` as the bounded proxy for the multi-reward training channel.

Important limitation:

> The current DDPO training script did not sample `K > 1` images for the same prompt inside every training update. During training, each prompt often appears once per seed per rollout step. Therefore, the cleanest prompt-group information analysis is the final eval analysis, not an exact online measurement of per-update `I_acc`.

This limitation matters for the next experiment design.

## 3. Information Metrics from the 10-Prompt Final Eval

Final prompt-group information for the active training channel:

| Condition | Active channel | p_bar | H bits | S_rel | I_acc |
|---|---|---:|---:|---:|---:|
| IR-only | ImageReward | 0.4659 | 0.9540 | 0.0182 | 0.9264 |
| PS-only | PickScore | 0.4215 | 0.9454 | 0.0126 | 0.9064 |
| IR+PS | IR+PS combined | 0.4543 | 0.9636 | 0.0139 | 0.9335 |

Key observations:

- All three active channels have high outcome entropy, close to 1 bit.
- This means the final prompt set is not in an all-fail or all-success regime.
- `IR+PS combined` has the highest `I_acc` among active training channels.
- `IR+PS combined` also has the highest entropy, because its average bounded reward is closest to the mixed frontier.

This directly supports the information-bottleneck story:

> The 10-prompt setup produces a high-information feedback regime; the multi-reward channel has the richest active feedback signal by the paper's `I_acc` diagnostic.

Supporting files:

- `report/tables/information_bottleneck/final_active_training_channel_information.csv`
- `report/figures/information_bottleneck/final_active_channel_information.png`
- `report/figures/information_bottleneck/final_iacc_channel_heatmap.png`

## 4. Why Single-Prompt RL Failed to Tell the Right Story

The earlier single-prompt experiments used:

```text
a young badger delicately sniffing a yellow rose, richly textured oil painting
```

For this prompt, No-RL/base was already very strong:

| Single-prompt run | No-RL HPSv2 | IR-only HPSv2 | PS-only HPSv2 | IR+PS HPSv2 |
|---|---:|---:|---:|---:|
| 3 epochs | 0.7355 | 0.4469 | 0.5988 | 0.5095 |
| 20 epochs | 0.8100 | 0.5124 | 0.6964 | 0.7762 |

From the paper's perspective, this is exactly why single-prompt RL is a bad unit for the main claim:

- It is not a stable estimate of prompt-level feedback information.
- It can be dominated by whether the base model already produces a high-reward sample.
- More epochs do not necessarily increase usable information.
- If reward feedback is not aligned with held-out HPSv2, RL can move the policy away from the base distribution and reduce held-out score.

The paper emphasizes that the unit of information is conditional on the prompt group, not marginal across an arbitrary dataset. With one prompt, we cannot distinguish:

- low-information saturation,
- reward-model mismatch,
- seed/sample variance,
- actual RL failure.

Therefore, the correct conclusion from the single-prompt experiment is:

> Single prompt is sufficient to debug the DDPO loop, but insufficient to evaluate the information-bottleneck hypothesis.

## 5. Why 10 Prompts Changed the Result

Final 10-prompt cross-reward matrix, calibrated z:

| Condition | ImageReward | PickScore | HPSv2 |
|---|---:|---:|---:|
| No-RL | -0.1153 | -0.4470 | -0.1861 |
| IR-only | -0.1501 | -0.3804 | -0.1288 |
| PS-only | -0.0784 | -0.3601 | -0.0947 |
| IR+PS | -0.0755 | -0.3487 | -0.0958 |

In the 10-prompt setup:

- All RL conditions improve final held-out HPSv2 over No-RL.
- PS-only is slightly best on HPSv2.
- IR+PS nearly ties PS-only on HPSv2.
- IR+PS is best on ImageReward and PickScore.
- IR+PS is best on the mean of all three rewards.

Information-bottleneck interpretation:

> Increasing prompt diversity moved the experiment away from a single-prompt idiosyncrasy and toward a frontier-like regime where reward feedback has high entropy and nonzero separation. In that regime, online RL can convert reward feedback into held-out reward gains.

This is a direct analogue of the paper's claim that fixed datasets can contain too-easy or too-hard examples, while learning improves when the training distribution contains prompts near the model's capability frontier.

## 6. What Multi-Reward Adds in Information Terms

The paper argues that richer verifiers and hybrid reward schemes do not merely change scalar reward values. They change the partition of trajectory space induced by the feedback channel.

Our experiment supports that weaker but important claim.

Final active-channel `I_acc`:

| Active training channel | I_acc |
|---|---:|
| ImageReward only | 0.9264 |
| PickScore only | 0.9064 |
| IR+PS combined | 0.9335 |

The multi-reward channel has the highest accessible information diagnostic. But it does not strictly win held-out HPSv2:

| Condition | HPSv2 z |
|---|---:|
| PS-only | -0.0947 |
| IR+PS | -0.0958 |

This is not a contradiction. It shows that:

> Information amount and reward alignment are different. More accessible feedback can improve cross-reward balance, but held-out HPSv2 depends on whether the training channel is aligned with HPSv2.

In this prompt set, PickScore appears highly aligned with HPSv2. IR+PS adds information from ImageReward, improving balance, but the extra information is not purely HPS-aligned.

The most accurate conclusion is:

> Multi-reward feedback increases usable and balanced feedback, but the best held-out reward depends on the alignment between the training reward channel and the held-out evaluator.

Useful figures:

- `report/figures/information_bottleneck/final_active_channel_information.png`
- `report/figures/information_bottleneck/active_iacc_vs_hpsv2.png`
- `report/figures/rollout_reward_stats/final_objective_vs_hpsv2.png`

## 7. How This Fits the Paper's Hypothesis

The paper's central hypothesis:

> RLVR may be bottlenecked by the information content of rollout feedback.

Our diffusion result gives an analogous finding:

> Diffusion RL reward optimization is bottlenecked not just by reward density, but by whether reward models provide informative prompt-level distinctions among sampled images.

Evidence supporting this:

1. Single prompt was unstable and misleading.
   - No-RL was already strong.
   - RL did not beat base even with more epochs.
   - This is consistent with low or poorly aligned realized feedback, not simply insufficient compute.

2. 10 prompts produced a usable RL-over-base signal.
   - All RL conditions beat No-RL on final HPSv2.
   - This is consistent with prompt diversity increasing realized feedback potential.

3. Final prompt-group entropy is high.
   - Active channels have `H ~= 0.945` to `0.964` bits.
   - This is close to the paper's maximum-information regime at `p ~= 0.5`.

4. Final prompt-group separation is nonzero.
   - Active channels have `S_rel ~= 0.0126` to `0.0182`.
   - Reward models distinguish sampled images within the same prompt.

5. Multi-reward has the highest active-channel `I_acc`.
   - IR+PS combined: `I_acc = 0.9335`
   - ImageReward only: `I_acc = 0.9264`
   - PickScore only: `I_acc = 0.9064`

6. Multi-reward produces the best cross-reward balance.
   - Best final ImageReward.
   - Best final PickScore.
   - Nearly tied final HPSv2.
   - Best average over IR, PS, and HPSv2.

This supports a paper-compatible conclusion:

> Hybrid reward channels can expose richer usable feedback than a single reward channel. In our SDXL DDPO experiment, this extra information manifests as better cross-reward balance rather than a strict held-out HPSv2 win.

## 8. What We Should Not Overclaim

The current experiments do not prove:

- Multi-reward always improves held-out generalization.
- IR+PS is strictly better than PS-only.
- The information bottleneck hypothesis is fully validated for diffusion RL.
- More rollout samples alone would solve the problem.
- Our current DDPO update implements the paper's prompt-group `K`-rollout analysis exactly.

The last point is important. The paper's prompt-group theory assumes multiple rollouts for the same prompt at the same policy state. Our current final eval has this structure, but the training loop was optimized for fast small-scale DDPO and often had one image per prompt per seed during a training rollout batch.

So the clean claim is:

> The experiments are consistent with the information-bottleneck story and provide a diffusion-domain analogue, but the next experiment should explicitly sample `K > 1` images per prompt per update to test the theory more directly.

## 9. Figure Guide

A figure-by-figure guide is useful because the current report has three kinds of figures: reward-performance figures, rollout-statistics figures, and information-bottleneck figures.

### 9.1 Information-bottleneck figures

`report/figures/information_bottleneck/final_active_channel_information.png`

- What it shows: the paper-style information diagnostics for each condition's active training channel.
- Panels:
  - `Outcome entropy`: prompt-group `H_B(O|x)` in bits.
  - `Reward separation`: prompt-group `S_rel`, measuring whether rollouts under the same prompt receive distinguishable rewards.
  - `Accessible information`: `I_acc`, combining entropy and separation.
- How to read it: higher `H` means the reward channel is closer to the mixed frontier instead of all-fail/all-success; higher `S_rel` means the reward model separates images within the same prompt; higher `I_acc` means the channel provides more usable feedback.
- Main takeaway: `IR+PS` has the highest active-channel `I_acc`, supporting the claim that multi-reward feedback exposes richer usable information.

`report/figures/information_bottleneck/active_iacc_vs_hpsv2.png`

- What it shows: each training condition plotted by active-channel `I_acc` on the x-axis and final held-out HPSv2 z-score on the y-axis.
- How to read it: if information amount alone determined held-out performance, points with larger `I_acc` would always have higher HPSv2. The plot tests that relation.
- Main takeaway: `IR+PS` has the highest `I_acc`, but `PS-only` slightly edges it on HPSv2. This supports the nuanced claim that information amount matters, but reward-evaluator alignment also matters.

`report/figures/information_bottleneck/final_iacc_channel_heatmap.png`

- What it shows: final prompt-group `I_acc` for every training condition and every reward channel, including the combined `IR+PS` channel.
- How to read it: rows are policies trained with different objectives; columns are reward/evaluator channels. Larger values mean that channel still distinguishes prompt-level rollouts with high accessible information.
- Main takeaway: `IR+PS` maintains high information across multiple channels, which supports the cross-reward-balance story.

### 9.2 Main reward-performance figures

`report/figures/main/hpsv2_curve.png`

- What it shows: held-out HPSv2 calibrated z-score over DDPO eval steps.
- How to read it: compare whether RL conditions move above No-RL and whether the best checkpoint differs from the final checkpoint.
- Main takeaway: `IR+PS` reaches a strong HPSv2 checkpoint before the final step, while final HPSv2 is nearly tied between `PS-only` and `IR+PS`. This motivates early-stopping analysis.

`report/figures/main/cross_reward_matrix_final_z.png`

- What it shows: final cross-reward matrix. Rows are train conditions; columns are reward evaluators.
- How to read it: a good generalizing policy should not only improve its own training reward, but also avoid collapsing on other reward channels.
- Main takeaway: `IR+PS` is best on ImageReward and PickScore and nearly tied with `PS-only` on HPSv2, making it the most balanced condition.

`report/figures/main/ir_ps_cross_reward_curve.png`

- What it shows: the trajectory of the `IR+PS` policy evaluated by ImageReward, PickScore, and HPSv2.
- How to read it: this tests whether optimizing the combined reward improves both training channels while preserving held-out reward.
- Main takeaway: the combined policy has a cross-reward trajectory rather than only optimizing one reward channel.

`report/figures/main/reward_disagreement.png`

- What it shows: the mean disagreement among calibrated ImageReward, PickScore, and HPSv2 scores.
- Metric: `std(z_IR, z_PS, z_HPSv2)` per image, averaged by condition and step.
- How to read it: larger disagreement suggests reward channels are giving more conflicting judgments.
- Main takeaway: the run does not show a catastrophic reward-disagreement explosion, but single-reward policies can still move reward channels differently.

`report/figures/main/final_image_grid.png`

- What it shows: final generated images for No-RL, IR-only, PS-only, and IR+PS.
- How to read it: this is a qualitative sanity check against obvious reward hacking or image collapse.
- Main takeaway: final images are visually coherent, so the reward changes are not explained by obvious image failure.

### 9.3 Rollout mean/variance figures

`report/figures/rollout_reward_stats/all_rollouts_reward_mean_z.png`

- What it shows: mean calibrated reward z-scores across all collected rollout samples, not only final eval.
- How to read it: this summarizes the entire short DDPO trajectory.
- Main takeaway: all-rollout means are closer together than final-eval means, suggesting that much of the gain appears late in training.

`report/figures/rollout_reward_stats/all_rollouts_reward_variance_z.png`

- What it shows: variance of calibrated reward z-scores across all rollout samples.
- How to read it: variance here reflects prompt difficulty, seed variation, and image-level diversity, not just estimator noise.
- Main takeaway: RL changes reward dispersion, but there is no obvious variance collapse that would indicate trivial image/reward collapse.

`report/figures/rollout_reward_stats/final_eval_reward_mean_z.png`

- What it shows: final-eval reward means for ImageReward, PickScore, and HPSv2.
- How to read it: this is the cleanest final comparison among train conditions.
- Main takeaway: all RL conditions improve HPSv2 over No-RL; `IR+PS` is best on IR and PS; `PS-only` and `IR+PS` are nearly tied on HPSv2.

`report/figures/rollout_reward_stats/final_eval_reward_variance_z.png`

- What it shows: final-eval reward variances for each condition and reward evaluator.
- How to read it: compare whether a condition's mean gain comes with much larger score dispersion.
- Main takeaway: `IR+PS` keeps HPSv2 variance below `PS-only` while nearly matching its HPSv2 mean, which supports the balanced-feedback interpretation.

`report/figures/rollout_reward_stats/final_objective_vs_hpsv2.png`

- What it shows: final `(IR + PS) / 2` train-objective balance on the x-axis versus final held-out HPSv2 on the y-axis.
- How to read it: this separates "doing well on the training reward mixture" from "doing well on held-out HPSv2".
- Main takeaway: `IR+PS` has the best training-objective balance, while `PS-only` is marginally better on HPSv2. This shows the distinction between feedback richness and evaluator alignment.

### 9.4 Prompt-level figures

`report/figures/rollout_reward_stats/final_prompt_hpsv2_delta_vs_no_rl.png`

- What it shows: per-prompt final HPSv2 delta against No-RL for IR-only, PS-only, and IR+PS.
- How to read it: positive bars mean the RL policy improved over No-RL for that prompt.
- Main takeaway: each RL condition improves HPSv2 on 7/10 prompts, but the winning condition varies by prompt.

`report/figures/rollout_reward_stats/all_rollouts_prompt_hpsv2_delta_vs_no_rl.png`

- What it shows: per-prompt HPSv2 delta against No-RL averaged across all rollout samples.
- How to read it: compare this with the final-prompt delta figure to see whether gains are present throughout training or mainly at the end.
- Main takeaway: all-rollout prompt gains are weaker than final-eval gains, again suggesting late-training improvement.

`report/figures/rollout_reward_stats/final_prompt_hpsv2_heatmap.png`

- What it shows: final HPSv2 z-score for every prompt and condition.
- How to read it: columns are prompts, rows are train conditions; color indicates held-out HPSv2 quality.
- Main takeaway: prompt difficulty and prompt-specific reward alignment are large sources of variation, which is why one-prompt conclusions are unreliable.

`report/figures/rollout_reward_stats/ir_ps_vs_best_single_final_hpsv2.png`

- What it shows: per-prompt comparison of `IR+PS` final HPSv2 against the better of `IR-only` and `PS-only`.
- How to read it: points above the diagonal mean `IR+PS` beats the best single-reward policy for that prompt.
- Main takeaway: `IR+PS` wins on 3/10 prompts against the best single reward, so the correct claim is balance and robustness, not strict dominance.

`report/figures/rollout_reward_stats/reward_correlation_heatmaps.png`

- What it shows: correlations among ImageReward, PickScore, and HPSv2 scores for rollout images under each condition.
- How to read it: high correlation means reward channels judge sampled images similarly; lower correlation means reward channels expose different partitions of image space.
- Main takeaway: reward models are related but not identical channels, which is exactly why combining them can change the feedback information available to RL.

## 10. Recommended Paper-Style Framing

A good paragraph for the experiment section:

> We interpret reward models as feedback channels over prompt-conditioned image rollouts. Following the information-bottleneck view of RLVR, a reward channel is useful when it maintains both high outcome entropy and nonzero reward separation within a prompt group. In a one-prompt SDXL DDPO run, online RL did not reliably improve held-out HPSv2 over the base sampler, indicating that single-prompt feedback can be dominated by prompt-specific saturation and reward mismatch. After moving to a 10-prompt prompt-balanced setup, all RL conditions improved final HPSv2 over No-RL. The hybrid ImageReward+PickScore channel achieved the highest final accessible-information diagnostic among active training channels and the best cross-reward balance, while nearly matching the strongest single-reward baseline on held-out HPSv2. These results support the view that richer reward feedback improves the usable information available to diffusion RL, although held-out performance also depends on reward-evaluator alignment.

A compact claim:

> Multi-reward DDPO does not simply add more reward values; it changes the feedback channel by making more rollout distinctions available. In our 10-prompt SDXL experiment, that richer channel produces the most balanced reward profile and matches the best single-reward held-out result.

Avoid:

> Multi-reward proves better generalization.

Use:

> Multi-reward improves cross-reward consistency and preserves held-out performance.

## 11. Concrete Next Experiment to Fully Match the Paper

To make the next experiment maximally aligned with the paper, change the rollout design:

```text
For each update:
  sample B prompts
  for each prompt, sample K images
  compute IR, PS, and HPS diagnostic scores per image
  compute H_B, S_rel, I_acc per prompt group
  train on IR-only, PS-only, IR+PS
  track I_acc over checkpoints
```

Recommended minimal setup:

- SDXL only
- 10 to 20 prompts
- `K = 4` images per prompt per update
- 2 seeds
- reward conditions: IR-only, PS-only, IR+PS
- held-out evaluator: HPSv2
- report:
  - `I_acc` trajectory
  - final HPSv2
  - cross-reward matrix
  - prompt-level delta vs No-RL
  - correlation between early `I_acc` and later reward improvement

The decisive test would be:

> Do prompts/checkpoints with larger prompt-group `I_acc` show larger subsequent reward improvement?

That is the most direct empirical bridge to the paper.

## 12. Bottom Line

The current result should be framed as:

> A small diffusion-RL analogue of the RLVR information-bottleneck hypothesis. Single-prompt feedback is too narrow and unstable. Prompt-balanced RL creates a higher-information regime where online DDPO improves over No-RL. Multi-reward feedback has the highest accessible-information diagnostic and produces the best cross-reward balance, but held-out HPSv2 is controlled by both information amount and reward alignment, so PS-only remains a strong baseline.

This is a defensible, paper-consistent story.
