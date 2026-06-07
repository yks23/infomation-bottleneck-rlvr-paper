# Conclusions

## 1. Verifier information is bounded

For a fixed finite prompt set, the binary verifier gives a per-step information
budget:

```text
H_i(t) = h2(p_i(t)) <= 1 bit
A_i = sum_t H_i(t) <= T_i
```

In the 40-prompt run, the realized cumulative verifier uncertainty is
`265.5 / 640.0` step-bits, or `41.5%` of the simple upper bound. This supports
the paper story that a fixed RLVR dataset has a finite information budget.
The per-question `p_t` trajectory figures make the bound concrete: every
trajectory stays in `[0,1]`, so each step contributes at most one verifier bit
via `h2(p_t)`.

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
