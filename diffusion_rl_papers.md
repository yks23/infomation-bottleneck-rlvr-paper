# Diffusion x Reinforcement Learning Papers

筛选位置：`project/information-bottleneck-rlvr` 与其依赖的本地 OpenReview metadata（`dev/metadata`）。

备注：当前 `papers.csv` / `papers.jsonl` 是围绕 RLVR 信息瓶颈生成的阅读列表，直接搜索 `diffusion / denoising / score-based` 没有命中。因此下面的候选主要来自同一批本地 OpenReview 元数据，筛选口径是标题或关键词中包含 diffusion/score-based，并且摘要、标题或关键词中包含 reinforcement learning / offline RL / policy / planning / control / reward / trajectory 等信号。

## 最相关

1. [Accelerating Diffusion Planners in Offline RL via Reward-Aware Consistency Trajectory Distillation](https://openreview.net/forum?id=hRuTBS07C7)  
   ICLR 2026. 用 reward-aware consistency distillation 加速 offline RL 中的 diffusion planner，目标是单步采样生成更高 reward 的 action trajectory。

2. [Don’t Trade Off Safety: Diffusion Regularization for Constrained Offline RL](https://openreview.net/forum?id=eSIRst0WVy)  
   NeurIPS 2025. 用 diffusion model 捕捉 offline data 中的 behavior policy，再抽取简化 policy 做安全约束下的 offline RL。

3. [State-Covering Trajectory Stitching for Diffusion Planners](https://openreview.net/forum?id=GEzd5K5s5u)  
   NeurIPS 2025. 针对 diffusion planner 受限于 offline dataset 覆盖度的问题，提出 reward-free trajectory stitching 来增强长时序规划。

4. [Dichotomous Diffusion Policy Optimization](https://openreview.net/forum?id=R8y089OGoo)  
   ICLR 2026. 直接研究如何用 RL 稳定训练大 diffusion policy，场景包括自动驾驶和机器人。

5. [Prior-Guided Diffusion Planning for Offline Reinforcement Learning](https://openreview.net/forum?id=lC4WKmTScD)  
   NeurIPS 2025. 用 learnable prior 替代 diffusion planner 的标准 Gaussian prior，做 return-guided offline RL planning。

6. [STITCH-OPE: Trajectory Stitching with Guided Diffusion for Off-Policy Evaluation](https://openreview.net/forum?id=AghtKxDf7f)  
   NeurIPS 2025. 用 denoising diffusion 生成目标策略下的 synthetic trajectories，服务高维长时序 off-policy evaluation。

7. [Tree-Guided Diffusion Planner](https://openreview.net/forum?id=I1C0a01BZu)  
   NeurIPS 2025. 把 test-time planning 表述为 tree search + diffusion trajectory generation，处理非凸、多 reward、不可微约束的控制问题。

8. [Compositional Monte Carlo Tree Diffusion for Extendable Planning](https://openreview.net/forum?id=om2CpclG4y)  
   NeurIPS 2025. 将 Monte Carlo Tree Diffusion 从单条 trajectory search 扩展到 plan composition，解决更长 horizon 的 planning。

9. [Fast Monte Carlo Tree Diffusion: 100× Speedup via Parallel and Sparse Planning](https://openreview.net/forum?id=JRVZTACwb0)  
   NeurIPS 2025. 针对 MCTD 推理慢的问题，提出 parallel / sparse MCTD，在保留 tree-based diffusion planning 的同时提速。

10. [One-Step Flow Q-Learning: Addressing the Diffusion Policy Bottleneck in Offline Reinforcement Learning](https://openreview.net/forum?id=60VgwdzxDM)  
    ICLR 2026. 面向 offline RL 中 diffusion policy 推理慢的瓶颈，用 one-step flow Q-learning 改善效率。

11. [Continuous Q-Score Matching: Diffusion Guided Reinforcement Learning for Continuous-Time Control](https://openreview.net/forum?id=o8F5lNOTG6)  
    NeurIPS 2025. 明确把 diffusion/score matching 和 continuous-time control RL 联系起来。

12. [GenPO: Generative Diffusion Models Meet On-Policy Reinforcement Learning](https://openreview.net/forum?id=BmRNz1TpCc)  
    NeurIPS 2025. 直接讨论 generative diffusion model 与 on-policy RL 的结合。

13. [Exploratory Diffusion Model for Unsupervised Reinforcement Learning](https://openreview.net/forum?id=k0Kb1ynFbt)  
    ICLR 2026. 用 diffusion model 拟合多样 replay-buffer distribution，提供 density estimate 和 score-based intrinsic reward，用于无监督 RL 探索。

14. [Horizon Imagination: Efficient On-Policy Rollout in Diffusion World Models](https://openreview.net/forum?id=Obefq4k8iG)  
    ICLR 2026. 用 diffusion world model 做更高效的 on-policy rollout。

15. [ADG: Ambient Diffusion-Guided Dataset Recovery for Corruption-Robust Offline Reinforcement Learning](https://openreview.net/forum?id=8fECf5YbJY)  
    NeurIPS 2025. 面向 corrupted offline RL dataset，用 ambient diffusion 做数据恢复和鲁棒 offline RL。

16. [Beyond Penalization: Diffusion-based Out-of-Distribution Detection and Selective Regularization in Offline Reinforcement Learning](https://openreview.net/forum?id=a4DbIONcpb)  
    ICLR 2026. 用 diffusion-based OOD detection / selective regularization 改善 offline RL。

17. [Structural Information-based Hierarchical Diffusion for Offline Reinforcement Learning](https://openreview.net/forum?id=SbGtQpm2vP)  
    NeurIPS 2025. 层次化 diffusion 用于 offline RL。

18. [Forecasting in Offline Reinforcement Learning for Non-stationary Environments](https://openreview.net/forum?id=24UJqxw1kv)  
    NeurIPS 2025. 用 conditional diffusion-based candidate state generation 处理非平稳环境下的 offline RL。

## 机器人 / 控制方向相关

1. [Real-Time Execution of Action Chunking Flow Policies](https://openreview.net/forum?id=UkR2zO5uww)  
   NeurIPS 2025. 面向 diffusion/flow-based VLA 和机器人控制，解决 action chunking policy 的实时执行问题。

2. [Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy](https://openreview.net/forum?id=oDoPiR8wZJ)  
   NeurIPS 2025. Diffusion/flow-based policy 在机器人 manipulation 中根据任务难度动态调整推理预算。

3. [DynaGuide: Steering Diffusion Polices with Active Dynamic Guidance](https://openreview.net/forum?id=XOw7Yf8qN3)  
   NeurIPS 2025. 用外部 dynamics model 在 diffusion denoising 过程中引导 off-the-shelf diffusion policy。

4. [Constrained Diffusers for Safe Planning and Control](https://openreview.net/forum?id=tahkGZjjWA)  
   NeurIPS 2025. 在 diffusion planning/control 中加入约束 Langevin sampling 和 control barrier functions。

5. [Contractive Diffusion Policies](https://openreview.net/forum?id=iKJbmx1iuQ)  
   ICLR 2026. 从 contraction theory 角度改善 diffusion policy 在 continuous control 中的鲁棒性。

6. [Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition](https://openreview.net/forum?id=TnLFRhLuZ6)  
   ICLR 2026. 在 test time 组合多个 diffusion/flow robot policy 的 distributional scores，提升策略表现。

## Diffusion LLM / reward alignment 相关

1. [d1: Scaling Reasoning in Diffusion Large Language Models via Reinforcement Learning](https://openreview.net/forum?id=7ZVRlBFuEv)  
   NeurIPS 2025. 用 RL 扩展 diffusion LLM 的 reasoning 能力。

2. [SPG: Sandwiched Policy Gradient for Masked Diffusion Language Models](https://openreview.net/forum?id=18j5Q49GwN)  
   ICLR 2026. 针对 masked diffusion language model 的 RL alignment，提出 Sandwiched Policy Gradient。

3. [Fine-Tuning Discrete Diffusion Models with Policy Gradient Methods](https://openreview.net/forum?id=rXFzVRZsbt)  
   NeurIPS 2025. 用 policy gradient fine-tune discrete diffusion model。

4. [MRO: Enhancing Reasoning in Diffusion Language Models via Multi-Reward Optimization](https://openreview.net/forum?id=ZTfqehfcEJ)  
   NeurIPS 2025. 多 reward optimization 改善 diffusion language model 的 reasoning。

5. [Inpainting-Guided Policy Optimization for Diffusion Large Language Models](https://openreview.net/forum?id=haVf5e4Q6C)  
   ICLR 2026. diffusion LLM 的 policy optimization 方向。

## 不是标准 RL，但可作延伸

1. [Value Matching: Scalable and Gradient-Free Reward-Guided Flow Adaptation](https://openreview.net/forum?id=7iXt44Actj)  
   ICLR 2026. Flow/diffusion model 的 black-box reward optimization，与 stochastic optimal control / RL 有交集。

2. [Test-Time Scaling of Diffusion Models via Noise Trajectory Search](https://openreview.net/forum?id=fnkkY7UGRl)  
   NeurIPS 2025. 将 diffusion denoising 视作 MDP / contextual bandit / MCTS 搜索问题。

3. [Diffusion Tree Sampling: Scalable inference-time alignment of diffusion models](https://openreview.net/forum?id=3D88hCO0Gd)  
   NeurIPS 2025. 用 tree search 和 terminal reward 做 diffusion model 的 inference-time reward alignment。

4. [Training-Free Reward-Guided Image Editing via Trajectory Optimal Control](https://openreview.net/forum?id=YL2NgqN3Vh)  
   ICLR 2026. 更偏生成模型 reward guidance，但方法上连接 trajectory optimal control。
