# SDXL Prompt-Balanced TRL DDPO Report

- Prompts: 10 prompts; see `all_rollouts_manifest.parquet` for prompt text.
- Model: SDXL base.
- Online RL: Hugging Face TRL `DDPOTrainer` with LoRA; SDXL-specific code is a pipeline adapter, not a custom PPO/DDPO loop.
- Conditions: No-RL, ImageReward-only, PickScore-only, ImageReward+PickScore.
- Evaluation: ImageReward, PickScore, HPSv2.1, calibrated with the fixed offline calibration pool.

## Main Result

Best final held-out HPSv2 z: PS-only = -0.0947.

## Final Cross-Reward Matrix

| train | imagereward | pickscore | hpsv2 |
|---|---|---|---|
| No-RL | -0.1153 | -0.4470 | -0.1861 |
| IR-only | -0.1501 | -0.3804 | -0.1288 |
| PS-only | -0.0784 | -0.3601 | -0.0947 |
| IR+PS | -0.0755 | -0.3487 | -0.0958 |

## Figures

- `figures/hpsv2_curve.png`
- `figures/cross_reward_matrix_final_z.png`
- `figures/reward_disagreement.png`
- `figures/final_image_grid.png`

## Interpretation Guardrails

- This is a small prompt-balanced experiment, so it can test reward-generalization behavior more reliably than a one-prompt smoke run, but it is still not broad prompt-distribution generalization.
- If IR+PS beats both single-reward runs on HPSv2, the result supports the multi-reward-as-richer-channel story.
- If IR+PS does not beat both, the report should frame it as evidence that reward aggregation or prompt choice needs refinement, not as a failed infrastructure run.
