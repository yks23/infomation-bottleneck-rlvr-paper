# Poster Text

## Title

RLVR as Distributional Shrinkage

## Subtitle

Bounded verifier information drives policy updates; rollout action entropy
shrinks into problem-conditioned seeds; cross-prompt transfer reveals their
geometry.

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

Finite verifier signal gives a per-step upper bound:

```text
H_i(t) = h2(p_i(t)) <= 1 bit
A_i = sum_t H_i(t)
```

Observed cumulative verifier uncertainty:

```text
265.5 / 640.0 step-bits = 41.5% of bound
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
