# Poster Text

## Title

RLVR as Distributional Shrinkage

## Subtitle

Bounded rollout/path information drives policy updates; binary verifiers expose
a finite LLM projection; rollout action entropy shrinks into
problem-conditioned seeds; cross-prompt transfer reveals their geometry.

## Core Hypothesis

Before RL:

```text
broad rollout/action distribution pi_0(y | x_i)
```

After RL:

```text
low-entropy problem seed s_i
```

Between seeds:

```text
transfer geometry T_ij = p_j(after training on i) - p_j(base)
```

Shrinkage is measured by action entropy of model rollouts. The cleanest seed
diagnostic conditions on successful rollouts.

## Panel 1: Bounded Information

The main object is a rollout/path information integral:

```text
P_i^H = sum_t H_b(p_i(t))
G_i^H = sum_t H_b(p_i(t)) Delta p_i^+(t)
```

For a binary verifier, LLM math RLVR exposes the Bernoulli projection:

```text
H_b(p_i(t)) = h2(p_i(t)) <= 1 bit
0 <= G_i^H <= 1 bit
```

Observed cumulative verifier projection:

```text
265.5 / 640.0 step-bits = 41.5% of bound
```

Traditional RL contrast:

```text
Connect4 self-play renews rollout information.
Fixed math prompts mostly exhaust a finite source.
```

## Panel 2: Dataset Is Mostly Additive

Self-transfer dominates cross-transfer:

```text
diag DeltaP = 0.0706
offdiag DeltaP = 0.0091
offdiag / diag = 0.129
additivity score = 0.871
```

## Panel 3: Rollout Entropy Shrinks

Successful trajectories become sharper under RL:

```text
H_action | correct: 0.217 -> 0.202 nats/token
correct-only shrink = 0.0151
all-rollout shrink = 0.0128
```

## Bottom Panels

Transfer geometry:

```text
directed graph: train source i, evaluate target j
```

Seed space:

```text
problem seeds embedded by transfer fingerprints
```

Low-rank structure:

```text
2D explained variance = 0.483
16D explained variance = 0.953
```

## Takeaway

RLVR turns broad rollout distributions into a constellation of low-entropy
problem seeds. Most dataset mass is additive; sparse cross-transfer defines the
seed geometry.
