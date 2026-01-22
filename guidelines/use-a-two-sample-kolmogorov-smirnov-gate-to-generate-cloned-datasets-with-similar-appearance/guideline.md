---
id: use-a-two-sample-kolmogorov-smirnov-gate-to-generate-cloned-datasets-with-similar-appearance
title: "Use a two-sample Kolmogorov\u2013Smirnov gate to generate cloned datasets\
  \ with similar appearance"
bibliography: references.bib
description: "Maintain distributional similarity in x and y by accepting perturbations\
  \ only when two-sample Kolmogorov\u2013Smirnov tests remain below a chosen threshold."
labels:
- chart:scatter
- task:anonymize
- visual:position
- impact:privacy
- data:quantitative
- audience:expert
- custom:distributional-similarity
- complexity:advanced
---

## Enforce x- and y-distribution similarity with Kolmogorov–Smirnov tests <!-- role: advice -->

When you want a visually similar “cloned” scatterplot, accept perturbations only if two-sample Kolmogorov–Smirnov (K–S) test results for both x and y remain below your similarity threshold.

## Why distributional gating preserves overall structure while changing points <!-- role: reason -->

A distributional test constrains changes at the level of the empirical distributions, which limits how far the overall shape can drift even as individual points move, producing outputs that resemble the original more than shape-coerced variants do.

**Mechanism:** The K–S constraint rejects proposals that noticeably alter the cumulative distribution of x or y, thereby keeping marginal distributions close and preserving a similar-looking scatter structure.

**Evidence:** Using K–S tests inside the acceptance gate (requiring both x and y K–S statistics below 0.05) produced “cloned” datasets with similar appearance while still changing individual points [@matejkaSameStatsDifferent2017]. This use was motivated as a way to support anonymization by altering points while keeping overall structure similar [@matejkaSameStatsDifferent2017].

**Notes:** The approach can preserve additional summary properties (such as standard deviations) alongside resemblance when combined with other constraints [@matejkaSameStatsDifferent2017].

## When the goal is similarity rather than dramatic visual differences <!-- role: context -->

- **User Goal:** Modify sensitive data points while keeping the plot’s overall structure similar.
- **Task:** Create a “mirror” or “clone” dataset that resembles the original in distribution.
- **Data:** 2D quantitative scatter data where marginal distributions are meaningful.
- **Chart Setting:** Publication or sharing contexts where exact points should change but the general pattern should remain.
- **Audience:** Analysts or reviewers comparing original vs shared data.
- **Success Criterion:** The clone looks similar to the original, and the K–S similarity criteria (and any other chosen constraints) pass.

## When not to use marginal K–S constraints as your main similarity criterion <!-- role: exceptions -->

**Break it when:** Visual similarity depends primarily on joint structure rather than x and y marginals. **Why:** A marginal distribution constraint does not directly encode joint patterns beyond what the acceptance gate enforces [@matejkaSameStatsDifferent2017].

## Tradeoffs of K–S-based cloning constraints <!-- role: costs -->

**Sacrifice:** The added constraints can reduce the range of possible outputs and slow the search. **Risk:** Outputs may preserve marginals yet still change relationships that matter for interpretation if those are not also constrained. **Mitigation:** Pair the K–S gate with any additional statistics you require to remain stable [@matejkaSameStatsDifferent2017].

## Common mistakes when generating “cloned” datasets <!-- role: mistakes -->

**Mistake:** Assuming matching a few summary statistics guarantees a similar-looking dataset. **Why it fails:** Very different plots can share the same basic summaries, so distributional similarity needs explicit enforcement when similarity is the goal [@matejkaSameStatsDifferent2017].

## Quick tests for “clone” quality <!-- role: check -->

**Failure Sign:** The clone passes simple summaries but looks clearly different from the original. **Quick Check:** Run two-sample K–S tests on x and y and verify both are below the chosen threshold. **Stronger Test:** Compare overlaid plots of original and clone to see whether the overall structure aligns while individual points differ [@matejkaSameStatsDifferent2017].

## What to do instead when the clone is too different or too similar <!-- role: fix -->

- Tighten or relax the K–S threshold to control how much the distributions may change.
- Add additional preserved measures (such as correlation) if relationships must remain stable.
- Reduce the perturbation step size if the process frequently proposes changes that fail the similarity gate.
- Increase iterations so the algorithm can find acceptable alternatives under the similarity constraint [@matejkaSameStatsDifferent2017].
