# Diffusion Generative Models with RL / Reward / Preference Experiments

这份列表专门收集“图像/视频/视觉生成 diffusion 或 flow matching 模型”的 RL、reward optimization、preference alignment、DPO/GRPO、test-time reward search 相关论文。

区别于 `diffusion_rl_papers.md`：这里不重点看 diffusion policy 做机器人控制，也不重点看 offline RL planning；重点是 image/video generation 的生成质量、偏好对齐、奖励引导和人类/模型反馈。

## 最贴近：T2I/T2V diffusion 的 RLHF / GRPO / DPO / reward alignment

1. [Consistent Noisy Latent Rewards for Trajectory Preference Optimization in Diffusion Models](https://openreview.net/forum?id=qGihS60jfT)  
   ICLR 2026. 面向 text-to-image 和 text-to-video diffusion。核心问题是 reward model 评估中间 noisy latent 不稳定，以及不同 timestep 的 preference ranking 不一致。提出 Score-based Latent Reward Model，让 reward 更适合扩散轨迹级优化。很适合看“diffusion 生成轨迹如何做 reward / preference optimization”。

2. [DenseGRPO: From Sparse to Dense Reward for Flow Matching Model Alignment](https://openreview.net/forum?id=nIwFge9nW0)  
   ICLR 2026. 明确是 text-to-image generation + reinforcement learning + GRPO。它指出现有 GRPO 对 flow matching / diffusion alignment 往往只有 terminal reward，导致中间 denoising step 的 credit assignment 很粗。提出 step-wise dense reward，评估每一步 denoising 对最终偏好的贡献。这个和 RLVR 里的“稀疏 reward 变 dense reward”非常呼应。

3. [Towards Better Optimization For Listwise Preference in Diffusion Models](https://openreview.net/forum?id=ippWaS9PG9)  
   ICLR 2026. 从 RLHF/DPO 角度看 T2I diffusion alignment。它认为 pairwise preference 不充分，真实人类反馈常常是 listwise/ranking，于是提出 Diffusion-LPO，把 listwise preference 用进 diffusion model 的 preference optimization。

4. [Value Gradient Guidance for Flow Matching Alignment](https://openreview.net/forum?id=6MmOy2Ji8V)  
   NeurIPS 2025. 用 optimal control / reward fine-tuning 的视角对齐 flow matching generative models，实验包括 Stable Diffusion 3。适合看“生成模型 reward alignment 和最优控制/RL 的理论连接”。

5. [Diffusion Blend: Inference-Time Multi-Preference Alignment for Diffusion Models](https://openreview.net/forum?id=M2DXbwO8le)  
   ICLR 2026. 明确说 RL algorithms 已用于 diffusion models 的 aesthetic quality、text-image consistency 等 reward alignment，但单一 reward 和固定 KL 太限制。它关注 inference-time 多偏好对齐：给多个 reward basis，推理时组合不同用户偏好。

6. [Adaptive Divergence Regularized Policy Optimization for Fine-tuning Generative Models](https://openreview.net/forum?id=aXO0xg0ttW)  
   NeurIPS 2025. 面向 generative models / flow matching / text-to-image generation 的 RL fine-tuning。关键词包括 reinforcement learning、adaptive regularization、advantage estimation、exploration-exploitation trade-off。适合看“把生成模型当 policy 来 fine-tune”的方法。

## 图像编辑 / 个性化 / 视觉质量偏好

1. [Training-Free Reward-Guided Image Editing via Trajectory Optimal Control](https://openreview.net/forum?id=YL2NgqN3Vh)  
   ICLR 2026. 不训练模型，而是在 diffusion / flow reverse process 里做 reward-guided editing。把编辑过程表述为 trajectory optimal control：既要保留源图语义，又要提高目标 reward。

2. [Personalized Image Editing in Text-to-Image Diffusion Models via Collaborative Direct Preference Optimization](https://openreview.net/forum?id=BBZEcVu1nA)  
   NeurIPS 2025. 用 Collaborative DPO 让 T2I diffusion 的 image editing 适配用户个性化审美偏好。适合看“personalized preference + DPO + image editing”。

3. [Diffusion Negative Preference Optimization Made Simple](https://openreview.net/forum?id=CU5EHe1KUt)  
   ICLR 2026. 针对 text-to-image generation 的 preference alignment，关注 negative preference，即不仅学习“喜欢什么”，还主动抑制“不希望出现什么”。

4. [DP²O-SR: Direct Perceptual Preference Optimization for Real-World Image Super-Resolution](https://openreview.net/forum?id=45bQUVXmwl)  
   NeurIPS 2025. 用 Direct Preference Optimization 做真实图像超分的 perceptual quality alignment。虽然是 super-resolution，不是通用 T2I，但很适合作为“视觉生成质量 reward/preference”的案例。

5. [Doctor Approved: Generating Medically Accurate Skin Disease Images through AI-Expert Feedback](https://openreview.net/forum?id=IPxOoU8aqt)  
   NeurIPS 2025. 医学皮肤病图像生成，讨论 RL/DPO/human feedback 的成本问题，并用 AI-expert feedback 改善 diffusion 合成图像的医学准确性。适合看“领域专家反馈如何约束视觉生成”。

## 视频生成 / 自动驾驶视觉生成

1. [Dual-IPO: Dual-Iterative Preference Optimization for Text-to-Video Generation](https://openreview.net/forum?id=mu8sO1Vw0C)  
   ICLR 2026. Text-to-video diffusion transformer 的 preference alignment。交替优化 reward model 和 video generation model，reward 关注 subject consistency、motion smoothness、aesthetic quality 等。

2. [RLGF: Reinforcement Learning with Geometric Feedback for Autonomous Driving Video Generation](https://openreview.net/forum?id=EATkC9iHE3)  
   NeurIPS 2025. 很贴“video diffusion + RL experiment”。它用 latent-space AD perception model 给 video diffusion model 提供几何 reward，改善自动驾驶视频生成中的几何一致性和下游 3D 检测效果。

## Test-time reward search / inference-time alignment

1. [Test-Time Scaling of Diffusion Models via Noise Trajectory Search](https://openreview.net/forum?id=fnkkY7UGRl)  
   NeurIPS 2025. 把 diffusion denoising 看成 MDP，terminal reward 来自最终样本质量，讨论 MCTS、contextual bandit、epsilon-greedy 等搜索。很适合看“扩散生成过程能不能像 RL 搜索一样 test-time scaling”。

2. [Diffusion Tree Sampling: Scalable inference-time alignment of diffusion models](https://openreview.net/forum?id=3D88hCO0Gd)  
   NeurIPS 2025. 用 tree search 和 terminal reward 做 diffusion model 的 inference-time reward alignment。相比普通 guidance，它复用过去采样结果，在 diffusion chain 上回传 terminal reward。

3. [$\Psi$-Sampler: Initial Particle Sampling for SMC-Based Inference-Time Reward Alignment in Score Models](https://openreview.net/forum?id=slVqJAI5sT)  
   NeurIPS 2025. 用 SMC 做 score-based generative model 的 inference-time reward alignment，任务包括 layout-to-image、quantity-aware generation、aesthetic-preference generation。

4. [Sample Reward Soups: Query-efficient Multi-Reward Guidance for Text-to-Image Diffusion Models](https://openreview.net/forum?id=MNVxrgRcJV)  
   ICLR 2026. Training-free / black-box multi-reward guidance，用 reward-guided search gradients 做 T2I diffusion 的 Pareto sampling，目标是降低多个 black-box reward 的查询成本。

5. [GLASS Flows: Efficient Inference for Reward Alignment of Flow and Diffusion Models](https://openreview.net/forum?id=vH7OAPZ2dR)  
   ICLR 2026. 关注 inference-time reward adaptation 的采样效率，在大规模 text-to-image 模型上做实验。

## 可以作为补充但不是最核心

1. [Value Matching: Scalable and Gradient-Free Reward-Guided Flow Adaptation](https://openreview.net/forum?id=7iXt44Actj)  
   ICLR 2026. 任务包括 image generation 和 molecular design。更偏通用 flow/diffusion reward optimization，但与 RL 和 stochastic optimal control 关系明确。

2. [CPO: Condition Preference Optimization for Controllable Image Generation](https://openreview.net/forum?id=ToEgGjClB9)  
   NeurIPS 2025. ControlNet / controllable image generation 的 preference optimization，偏 DPO 和 controllability，不是典型 RL，但和视觉生成 preference alignment 相关。

3. [Selftok-Zero: Reinforcement Learning for Visual Generation via Discrete and Autoregressive Visual Tokens](https://openreview.net/forum?id=YktFxpaEmR)  
   NeurIPS 2025. 它讨论为什么 diffusion-based visual generation 的实际 generation trajectories 难以直接 reward，转而从 discrete/autoregressive visual tokens 做 RL。适合作为“为什么 diffusion 做 RL 不容易”的反例/动机。

## 推荐阅读顺序

1. 先看 DenseGRPO：最像“RLVR 的 dense reward 问题迁移到 T2I diffusion/flow”。
2. 再看 Consistent Noisy Latent Rewards：解决 diffusion 中间轨迹 reward 不稳定的问题。
3. 然后看 Diffusion-LPO / Diffusion Blend / VGG-Flow：补齐 preference optimization、multi-reward 和 optimal-control 视角。
4. 如果关注视频，直接读 Dual-IPO 和 RLGF。
5. 如果关注不用训练、只在推理时找更好样本，读 Test-Time Scaling、Diffusion Tree Sampling、$\Psi$-Sampler、Sample Reward Soups。
