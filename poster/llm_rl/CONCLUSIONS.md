# Conclusions

## 1. Rollout/path information is bounded in fixed LLM RLVR

The bounded-information object is the rollout/path integral. For each prompt,
we separate raw path exposure from the part aligned with performance movement:

```text
P_i^H = sum_t H_b(p_i(t))
G_i^H = sum_t H_b(p_i(t)) * Delta p_i^+(t)
0 <= G_i^H <= 1 bit
```

In fixed LLM math RLVR, the binary verifier makes this path integral visible
through a Bernoulli projection: `H_b(p_i(t)) = h2(p_i(t)) <= 1` bit. In the
40-prompt run, the realized cumulative verifier projection is `265.5 / 640.0`
step-bits, or `41.5%` of the simple upper bound. The per-question `p_t`
trajectory figures make the projection concrete, while the useful finite score
is the performance-coupled integral `sum_t H_b(p_i(t)) Delta p_i^+(t)`.

Traditional RL provides the contrast: in Connect4/OpenSpiel self-play, the
environment keeps refreshing the rollout distribution near the current policy's
frontier, so terminal reward information is not capped by a fixed set of math
prompts in the same way.

## 2. The dataset is mostly additive

Self-transfer dominates cross-transfer:

```text
mean diagonal DeltaP_common = 0.0706
mean off-diagonal DeltaP_common = 0.0091
offdiag / diag = 0.129
near-additivity score = 0.871
```

Interpretation: training on a prompt mostly improves that prompt. Cross-prompt
interactions exist, but they are sparse and much weaker on average. This is the
empirical reason the dataset can often be approximated as a sum of prompt-local
information contributions.

## 3. RLVR shrinks rollout distributions

The shrinkage metric is model action entropy over sampled rollouts. It is not
the binary success entropy `h2(p)`.

```text
all-rollout action entropy: 0.281 -> 0.268 nats/token
correct-only action entropy: 0.217 -> 0.202 nats/token
```

The correct-only entropy is the cleaner seed-shrinkage diagnostic because it
conditions on successful trajectories. It shows that successful rollouts are
already lower entropy and become slightly sharper after training.

## 4. Cross-prompt transfer defines a geometry

Each source prompt has a transfer fingerprint:

```text
T_i = [DeltaP_i1, DeltaP_i2, ..., DeltaP_iN]
```

Similarity between these fingerprints gives a prompt-space geometry. In the
40x40 run, a 2D projection explains `48.3%` of transfer variance, while 16D
explains `95.3%`. This suggests that prompt interactions are not random noise;
they have a lower-dimensional structure that can be visualized and potentially
used for prompt selection.

## 5. Practical implication: prompt allocation

The transfer matrix can support curriculum or prompt sampling:

```text
score(source) = self_gain(source)
              + lambda * transfer_out(source)
              - mu * negative_transfer(source)
```

The current evidence says that prompt-local gains should remain the default
signal, while sparse positive transfer edges can be used to pick coverage
prompts or identify clusters of related problems.

## Caveats

- The 40x40 result is endpoint transfer, not a full per-step causal matrix.
- Correct-only action entropy is only available for sources that produce
  successful rollouts; support is `31 / 40` sources.
- The 787 MB full old-asset archive is kept locally and indexed here, but not
  committed into this branch.
- These figures are research/poster assets, not final camera-ready paper plots.
