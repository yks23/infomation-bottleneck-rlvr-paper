# SDXL 10-Prompt DDPO Report

This folder mirrors the key reports, figures, and CSV tables from:

`/cephfs/huangyu/data/ib_diff_rl_small/reports/sdxl_single_prompt_ddpo_trl/20260607_sdxl_ddpo_8gpu_10prompt_10ep_lr3e5_ckpt1`

## Reports

- `experiment_conclusions.md`: detailed conclusions and recommended framing.
- `information_bottleneck_story_conclusions.md`: paper-aligned information-bottleneck interpretation.
- `sdxl_ddpo_10prompt_report.md`: main DDPO cross-reward report.
- `rollout_reward_stats_report.md`: rollout mean/variance and single-vs-multi reward analysis.

## Figures

- `figures/main/`: original training/evaluation figures.
- `figures/rollout_reward_stats/`: additional rollout mean, variance, per-prompt delta, correlation, and objective-vs-HPS figures.
- `figures/information_bottleneck/`: prompt-group feedback information figures.

## Tables

- `tables/main/`: main reward curves and cross-reward matrix CSVs.
- `tables/rollout_reward_stats/`: rollout-level mean/variance, prompt-level deltas, and reward-correlation CSVs.
- `tables/information_bottleneck/`: prompt-group entropy, reward separation, and accessible-information CSVs.
