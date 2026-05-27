# Information Bottleneck x RLVR Reading List

This folder collects OpenReview papers related to information theory, information bottlenecks, entropy, feedback granularity, and RLVR.

Sources: NeurIPS 2025 and ICLR 2026 OpenReview accepted-paper metadata. ICML 2026 currently has no accepted records in OpenReview metadata.

## Start Here

### 1. [Hybrid Reinforcement: when reward is sparse, better to be dense](https://openreview.net/forum?id=0CajQNVKyB)
- Venue: iclr26 / ICLR 2026 Poster
- Score: 0.215049 | Themes: `core_rlvr_feedback_bottleneck;reward_granularity_dense_feedback`
- Keywords: core_rlvr_feedback_bottleneck: verifiable reward, binary feedback, sparse verifier; reward_granularity_dense_feedback: dense reward, hybrid reward, reward model, verifier
- Abstract: Post-training for reasoning in large language models has increasingly relied on verifiable rewards: deterministic checkers that provide $0$–$1$ correctness signals. While reliable, such binary feedback is brittle—many tasks admit partially correct or alternative answers that verifiers under-credit, and the resulting all-or-nothing supervision limits learning. Reward models offer richer, continuous feedback, which can serve as a complementary supervisory signal to verifiers. We introduce HERO (Hybrid Ensemble Reward Optimization), a reinforcement learning framework that integrates sparse verifier signals with dense reward model scores in a...

### 2. [Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward](https://openreview.net/forum?id=sE8DCSJTzd)
- Venue: iclr26 / ICLR 2026 Poster
- Score: 0.186061 | Themes: `core_rlvr_feedback_bottleneck;information_entropy_theory;exploration_rollout_diversity`
- Keywords: core_rlvr_feedback_bottleneck: verifiable reward, rlvr; information_entropy_theory: entropy, policy entropy; exploration_rollout_diversity: exploration, policy optimization
- Abstract: This paper examines the exploration–exploitation trade-off in reinforcement learning with verifiable rewards (RLVR), a framework for improving the reasoning of Large Language Models (LLMs). Recent studies suggest that RLVR can elicit strong mathematical reasoning in LLMs through two seemingly paradoxical mechanisms: \textit{spurious rewards}, which suppress exploitation by rewarding outcomes unrelated to the ground truth, and \textit{entropy minimization}, which suppresses exploration by pushing the model toward more confident and deterministic outputs, highlighting a puzzling dynamic: both discouraging exploitation and discouraging...

### 3. [Lookahead Tree-Based Rollouts for Enhanced Trajectory-Level Exploration in Reinforcement Learning with Verifiable Rewards](https://openreview.net/forum?id=4nLvUk8edu)
- Venue: iclr26 / ICLR 2026 Poster
- Score: 0.185152 | Themes: `core_rlvr_feedback_bottleneck;exploration_rollout_diversity`
- Keywords: core_rlvr_feedback_bottleneck: verifiable reward, rlvr; exploration_rollout_diversity: exploration, rollout, policy optimization
- Abstract: Reinforcement Learning with Verifiable Rewards (RLVR), particularly with algorithms like Group Relative Policy Optimization (GRPO), has proven highly effective in enhancing the reasoning capabilities of large language models. However, a critical bottleneck in current pipelines lies in the limited diversity of sampled trajectories during group rollouts. Homogeneous trajectories and their associated rewards would diminish the return signals for policy updates, thereby hindering effective policy learning. This lack of diversity stems primarily from token-level stochastic sampling, where local variations are likely to collapse into near-...

### 4. [EEPO: Exploration-Enhanced Policy Optimization via Sample-Then-Forget](https://openreview.net/forum?id=ObF4WIMkY6)
- Venue: iclr26 / ICLR 2026 Poster
- Score: 0.180449 | Themes: `core_rlvr_feedback_bottleneck;information_entropy_theory;exploration_rollout_diversity`
- Keywords: core_rlvr_feedback_bottleneck: verifiable reward, rlvr; information_entropy_theory: entropy; exploration_rollout_diversity: exploration, rollout, policy optimization
- Abstract: Balancing exploration and exploitation remains a central challenge in reinforcement learning with verifiable rewards (RLVR) for large language models (LLMs). Current RLVR methods often overemphasize exploitation, leading to entropy collapse, diminished exploratory capacity, and ultimately limited performance gains. Although techniques that increase policy stochasticity can promote exploration, they frequently fail to escape dominant behavioral modes. This creates a self-reinforcing loop—repeatedly sampling and rewarding dominant modes—that further erodes exploration. We introduce **E**xploration-**E**nhanced **P**olicy **O**ptimization...

### 5. [No Prompt Left Behind: Exploiting Zero-Variance Prompts in LLM Reinforcement Learning via Entropy-Guided Advantage Shaping](https://openreview.net/forum?id=kiXFIESZKv)
- Venue: iclr26 / ICLR 2026 Poster
- Score: 0.17917 | Themes: `core_rlvr_feedback_bottleneck;information_entropy_theory;exploration_rollout_diversity`
- Keywords: core_rlvr_feedback_bottleneck: verifiable reward, rlvr, zero-variance, all responses; information_entropy_theory: entropy; exploration_rollout_diversity: policy optimization
- Abstract: Reinforcement Learning with Verifiable Rewards (RLVR) is a powerful framework for improving the reasoning abilities of Large Language Models (LLMs). However, current methods such as GRPO rely only on problems where the model responses to the same input differ in correctness, while ignoring those where all responses receive the same reward — so-called zero-variance prompts. In this work, we argue that such prompts are not useless but can, in fact, provide meaningful feedback for policy optimization. To this end, we introduce Reinforcement Learning with Zero-Variance Prompts (RL-ZVP), a novel algorithm that extract learning signals from...

### 6. [Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn Search Agents](https://openreview.net/forum?id=qkWP6phrvZ)
- Venue: iclr26 / ICLR 2026 Poster
- Score: 0.177616 | Themes: `core_rlvr_feedback_bottleneck;information_entropy_theory;reward_granularity_dense_feedback;exploration_rollout_diversity`
- Keywords: core_rlvr_feedback_bottleneck: advantage collapse, identical rewards, reward sparsity; information_entropy_theory: information gain; reward_granularity_dense_feedback: dense reward, reward model, fine-grained; exploration_rollout_diversity: rollout, policy optimization
- Abstract: Large language model (LLM)-based agents are increasingly trained with reinforcement learning (RL) to enhance their ability to interact with external environments through tool use, particularly in search-based settings that require multi-turn reasoning and knowledge acquisition. However, existing approaches typically rely on outcome-based rewards that are only provided exclusively upon generating the final answer. This reward sparsity becomes particularly problematic in multi-turn settings, where long trajectories exacerbate three critical issues: (i) advantage collapse, where all rollouts receive identical rewards and provide no useful...

### 7. [Smarter Not Harder: Generative Process Evaluation with Intrinsic-Signal Driving and Ability‑Adaptive Reward Shaping](https://openreview.net/forum?id=LZZENDlZt9)
- Venue: iclr26 / ICLR 2026 Poster
- Score: 0.176208 | Themes: `core_rlvr_feedback_bottleneck;reward_granularity_dense_feedback;exploration_rollout_diversity`
- Keywords: core_rlvr_feedback_bottleneck: sparse feedback; reward_granularity_dense_feedback: reward model, process reward, reward shaping; exploration_rollout_diversity: exploration
- Abstract: Large reasoning models (LRMs) have shown strong performance in complex mathematical reasoning when optimized via reinforcement learning (RL). However, conventional outcome-only reward provides sparse feedback, leading to inefficient optimization. In this work, we investigate whether generative process reward models (GenPRMs) can accelerate RL training of LRMs by improving the utilization of reasoning trajectories. We first analyze critical limitations in existing GenPRMs, including their heavy reliance on reasoning ability during correctness judgment, and suppression of exploration as well as vulnerability to reward hacking during reward...

### 8. [Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards](https://openreview.net/forum?id=Z5sWYACAop)
- Venue: iclr26 / ICLR 2026 Poster
- Score: 0.164019 | Themes: `core_rlvr_feedback_bottleneck;exploration_rollout_diversity`
- Keywords: core_rlvr_feedback_bottleneck: verifiable reward; exploration_rollout_diversity: rollout, sampling efficiency, rollout allocation, policy optimization
- Abstract: Sampling efficiency is a key bottleneck in reinforcement learning with verifiable rewards. Existing group-based policy optimization methods, such as GRPO, allocate a fixed number of rollouts for all training prompts. This uniform allocation implicitly treats all prompts as equally informative, and could lead to inefficient computational budget usage and impede training progress. We introduce VIP, a Variance-Informed Predictive allocation strategy that allocates a given rollout budget to the prompts in the incumbent batch to minimize the expected gradient variance of the policy update. At each iteration, VIP uses a lightweight Gaussian...

### 9. [CORE: Concept-Oriented Reinforcement for Bridging the Definition–Application Gap in Mathematical Reasoning](https://openreview.net/forum?id=pRSRiXdpkm)
- Venue: iclr26 / ICLR 2026 Poster
- Score: 0.158133 | Themes: `core_rlvr_feedback_bottleneck;reward_granularity_dense_feedback;exploration_rollout_diversity`
- Keywords: core_rlvr_feedback_bottleneck: verifiable reward, rlvr; reward_granularity_dense_feedback: fine-grained, verifier; exploration_rollout_diversity: rollout
- Abstract: Large language models (LLMs) often solve challenging math exercises yet fail to apply the concept right when the problem requires genuine understanding. Popular Reinforcement Learning with Verifiable Rewards (RLVR) pipelines reinforce final answers but provide little fine-grained conceptual signal, so models improve at pattern reuse rather than conceptual applications. We introduce $\textit{CORE}$ (Concept-Oriented REinforcement), an RL training framework that turns explicit concepts into a controllable supervision signal. Starting from a high-quality, low-contamination textbook resource that links verifiable exercises to concise concept...

### 10. [Supervised Reinforcement Learning: From Expert Trajectories to Step-wise Reasoning](https://openreview.net/forum?id=Uro84w2xz5)
- Venue: iclr26 / ICLR 2026 Poster
- Score: 0.156267 | Themes: `core_rlvr_feedback_bottleneck;exploration_rollout_diversity`
- Keywords: core_rlvr_feedback_bottleneck: verifiable reward, rlvr; exploration_rollout_diversity: rollout
- Abstract: Large Language Models (LLMs) often struggle with problems that require multi-step reasoning. For small-scale open-source models, Reinforcement Learning with Verifiable Rewards (RLVR) fails when correct solutions are rarely sampled even after many attempts, while Supervised Fine-Tuning (SFT) tends to overfit long demonstrations through rigid token-by-token imitation. To address this gap, we propose Supervised Reinforcement Learning (SRL), a framework that reformulates problem solving as generating a sequence of logical ``actions''. SRL trains the model to generate an internal reasoning monologue before committing to each action. It provides...

### 11. [Temperature as a Meta-Policy: Adaptive Temperature in LLM Reinforcement Learning](https://openreview.net/forum?id=AoTHU2OmS6)
- Venue: iclr26 / ICLR 2026 Poster
- Score: 0.183255 | Themes: `exploration_rollout_diversity`
- Keywords: exploration_rollout_diversity: exploration, rollout, adaptive sampling, temperature, policy optimization
- Abstract: Temperature is a crucial hyperparameter in large language models (LLMs), controlling the trade-off between exploration and exploitation during text generation. High temperatures encourage diverse but noisy outputs, while low temperatures produce focused outputs but may cause premature convergence. Yet static or heuristic temperature schedules fail to adapt to the dynamic demands of reinforcement learning (RL) throughout training, often limiting policy improvement. We propose Temperature Adaptive Meta Policy Optimization (TAMPO), a new framework that recasts temperature control as a learnable meta-policy. TAMPO operates through a...

### 12. [Perception-Aware Policy Optimization for Multimodal Reasoning](https://openreview.net/forum?id=izbBqTL8vb)
- Venue: iclr26 / ICLR 2026 Poster
- Score: 0.175833 | Themes: `core_rlvr_feedback_bottleneck;information_entropy_theory;reward_granularity_dense_feedback;exploration_rollout_diversity`
- Keywords: core_rlvr_feedback_bottleneck: verifiable reward, rlvr; information_entropy_theory: entropy; reward_granularity_dense_feedback: reward model; exploration_rollout_diversity: rollout, policy optimization
- Abstract: Reinforcement Learning with Verifiable Rewards (RLVR) has proven to be a highly effective strategy for empowering Large Language Models (LLMs) with long chain-of-thought reasoning abilities. However, its design and optimizations remain tailored to purely textual domains, resulting in suboptimal performance when applied to multimodal reasoning tasks. In particular, we observe that a major source of error (67%) in current multimodal reasoning lies in the perception of visual inputs. To address this bottleneck, we propose PAPO, a novel policy gradient algorithm that encourages the model to generate visually grounded reasoning without external...

## Theme Views

### core_rlvr_feedback_bottleneck

- [Hybrid Reinforcement: when reward is sparse, better to be dense](https://openreview.net/forum?id=0CajQNVKyB) (iclr26, score=0.215049)
- [Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward](https://openreview.net/forum?id=sE8DCSJTzd) (iclr26, score=0.186061)
- [Lookahead Tree-Based Rollouts for Enhanced Trajectory-Level Exploration in Reinforcement Learning with Verifiable Rewards](https://openreview.net/forum?id=4nLvUk8edu) (iclr26, score=0.185152)
- [EEPO: Exploration-Enhanced Policy Optimization via Sample-Then-Forget](https://openreview.net/forum?id=ObF4WIMkY6) (iclr26, score=0.180449)
- [No Prompt Left Behind: Exploiting Zero-Variance Prompts in LLM Reinforcement Learning via Entropy-Guided Advantage Shaping](https://openreview.net/forum?id=kiXFIESZKv) (iclr26, score=0.17917)
- [Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn Search Agents](https://openreview.net/forum?id=qkWP6phrvZ) (iclr26, score=0.177616)
- [Smarter Not Harder: Generative Process Evaluation with Intrinsic-Signal Driving and Ability‑Adaptive Reward Shaping](https://openreview.net/forum?id=LZZENDlZt9) (iclr26, score=0.176208)
- [Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards](https://openreview.net/forum?id=Z5sWYACAop) (iclr26, score=0.164019)
- [CORE: Concept-Oriented Reinforcement for Bridging the Definition–Application Gap in Mathematical Reasoning](https://openreview.net/forum?id=pRSRiXdpkm) (iclr26, score=0.158133)
- [Supervised Reinforcement Learning: From Expert Trajectories to Step-wise Reasoning](https://openreview.net/forum?id=Uro84w2xz5) (iclr26, score=0.156267)
- [Perception-Aware Policy Optimization for Multimodal Reasoning](https://openreview.net/forum?id=izbBqTL8vb) (iclr26, score=0.175833)
- [Trust, But Verify: A Self-Verification Approach to Reinforcement Learning with Verifiable Rewards](https://openreview.net/forum?id=gA3fFAEXNT) (nips25, score=0.166606)

### information_entropy_theory

- [Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward](https://openreview.net/forum?id=sE8DCSJTzd) (iclr26, score=0.186061)
- [EEPO: Exploration-Enhanced Policy Optimization via Sample-Then-Forget](https://openreview.net/forum?id=ObF4WIMkY6) (iclr26, score=0.180449)
- [No Prompt Left Behind: Exploiting Zero-Variance Prompts in LLM Reinforcement Learning via Entropy-Guided Advantage Shaping](https://openreview.net/forum?id=kiXFIESZKv) (iclr26, score=0.17917)
- [Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn Search Agents](https://openreview.net/forum?id=qkWP6phrvZ) (iclr26, score=0.177616)
- [Perception-Aware Policy Optimization for Multimodal Reasoning](https://openreview.net/forum?id=izbBqTL8vb) (iclr26, score=0.175833)
- [Beyond Pass@ 1: Self-Play with Variational Problem Synthesis Sustains RLVR](https://openreview.net/forum?id=Wjf3OMJxpn) (iclr26, score=0.154051)
- [CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models](https://openreview.net/forum?id=5rXN5knHKW) (iclr26, score=0.152825)
- [DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Tree-based Search](https://openreview.net/forum?id=Kx0G6v2c2S) (iclr26, score=0.152592)
- [Quantile Advantage Estimation: Stabilizing RLVR for LLM Reasoning](https://openreview.net/forum?id=WDP5b3mtFV) (iclr26, score=0.152168)
- [RiskPO: Risk-based Policy Optimization with Verifiable Reward for LLM Post-Training](https://openreview.net/forum?id=KjHB7rebQO) (iclr26, score=0.146676)
- [Controllable Exploration in Hybrid-Policy RLVR for Multi-Modal Reasoning](https://openreview.net/forum?id=5wxyCidRsK) (iclr26, score=0.141045)
- [TraPO: A Semi-Supervised Reinforcement Learning Framework for Boosting LLM Reasoning](https://openreview.net/forum?id=3K1y4KbWAx) (iclr26, score=0.137734)

### reward_granularity_dense_feedback

- [Hybrid Reinforcement: when reward is sparse, better to be dense](https://openreview.net/forum?id=0CajQNVKyB) (iclr26, score=0.215049)
- [Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn Search Agents](https://openreview.net/forum?id=qkWP6phrvZ) (iclr26, score=0.177616)
- [Smarter Not Harder: Generative Process Evaluation with Intrinsic-Signal Driving and Ability‑Adaptive Reward Shaping](https://openreview.net/forum?id=LZZENDlZt9) (iclr26, score=0.176208)
- [CORE: Concept-Oriented Reinforcement for Bridging the Definition–Application Gap in Mathematical Reasoning](https://openreview.net/forum?id=pRSRiXdpkm) (iclr26, score=0.158133)
- [Perception-Aware Policy Optimization for Multimodal Reasoning](https://openreview.net/forum?id=izbBqTL8vb) (iclr26, score=0.175833)
- [Trust, But Verify: A Self-Verification Approach to Reinforcement Learning with Verifiable Rewards](https://openreview.net/forum?id=gA3fFAEXNT) (nips25, score=0.166606)
- [FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable Reasoning](https://openreview.net/forum?id=jhqqoimoWt) (iclr26, score=0.153682)
- [DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Tree-based Search](https://openreview.net/forum?id=Kx0G6v2c2S) (iclr26, score=0.152592)
- [SSVPO: Effective Step-Level Credit Assignment for RL Training of Language Models](https://openreview.net/forum?id=g33DGvnHYd) (iclr26, score=0.151049)
- [Process-Verified Reinforcement Learning for Theorem Proving via Lean](https://openreview.net/forum?id=P00k4DFaXF) (iclr26, score=0.14934)
- [Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning](https://openreview.net/forum?id=4DJoBOQNd0) (iclr26, score=0.14879)
- [Optimizing Anytime Reasoning via Budget Relative Policy Optimization](https://openreview.net/forum?id=jFaFCc5978) (nips25, score=0.145109)

### exploration_rollout_diversity

- [Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward](https://openreview.net/forum?id=sE8DCSJTzd) (iclr26, score=0.186061)
- [Lookahead Tree-Based Rollouts for Enhanced Trajectory-Level Exploration in Reinforcement Learning with Verifiable Rewards](https://openreview.net/forum?id=4nLvUk8edu) (iclr26, score=0.185152)
- [EEPO: Exploration-Enhanced Policy Optimization via Sample-Then-Forget](https://openreview.net/forum?id=ObF4WIMkY6) (iclr26, score=0.180449)
- [No Prompt Left Behind: Exploiting Zero-Variance Prompts in LLM Reinforcement Learning via Entropy-Guided Advantage Shaping](https://openreview.net/forum?id=kiXFIESZKv) (iclr26, score=0.17917)
- [Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn Search Agents](https://openreview.net/forum?id=qkWP6phrvZ) (iclr26, score=0.177616)
- [Smarter Not Harder: Generative Process Evaluation with Intrinsic-Signal Driving and Ability‑Adaptive Reward Shaping](https://openreview.net/forum?id=LZZENDlZt9) (iclr26, score=0.176208)
- [Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards](https://openreview.net/forum?id=Z5sWYACAop) (iclr26, score=0.164019)
- [CORE: Concept-Oriented Reinforcement for Bridging the Definition–Application Gap in Mathematical Reasoning](https://openreview.net/forum?id=pRSRiXdpkm) (iclr26, score=0.158133)
- [Supervised Reinforcement Learning: From Expert Trajectories to Step-wise Reasoning](https://openreview.net/forum?id=Uro84w2xz5) (iclr26, score=0.156267)
- [Temperature as a Meta-Policy: Adaptive Temperature in LLM Reinforcement Learning](https://openreview.net/forum?id=AoTHU2OmS6) (iclr26, score=0.183255)
- [Perception-Aware Policy Optimization for Multimodal Reasoning](https://openreview.net/forum?id=izbBqTL8vb) (iclr26, score=0.175833)
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](https://openreview.net/forum?id=jGbRWwIidy) (iclr26, score=0.163814)

## Files

- `../data/papers.csv`: sortable spreadsheet-style index.
- `../data/papers.jsonl`: machine-readable records.
- `../scripts/download_pdfs.py`: downloads selected PDFs by rank or all records.
- `../data/pdfs/`: default output folder for downloaded PDFs.

## Download Examples

```sh
python3 scripts/download_pdfs.py --rank 1 --rank 2 --rank 3
python3 scripts/download_pdfs.py --all
```
