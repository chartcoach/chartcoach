---
id: use-scatterplots-for-correlation-discrimination-as-baseline
title: Use scatterplots as the default high-precision choice for correlation discrimination
bibliography: references.bib
description: Scatterplots provide among the lowest JNDs and symmetric performance
  across positive and negative correlations for correlation discrimination tasks.
labels:
- chart:scatter
- task:compare
- visual:position
- impact:accuracy
- data:quantitative
- audience:practitioner
- baseline:weber-model
---

## Default to scatterplots when the task is discriminating correlation strength <!-- role: advice -->

Use a scatterplot when viewers must judge which relationship is more correlated, especially when you need consistent performance for both positive and negative correlations.

## Why scatterplots support precise and sign-symmetric correlation judgments <!-- role: reason -->

Scatterplots directly encode two variables as position, producing a visual pattern whose tightness changes smoothly with correlation magnitude. That consistent geometric change can support stable discrimination thresholds across correlation signs.

**Mechanism:** A direct position-based encoding yields a coherent “spread around a line” cue whose discriminability can remain similar when the sign flips, helping maintain low JND across conditions.

**Evidence:** The paper’s fitted Weber models show scatterplots have among the lowest JNDs across tested visualizations, and scatterplot performance did not significantly differ between positive and negative correlations in discrimination precision [@harrisonRankingVisualizationsCorrelation2014a]. In the overall Weber-model-based ranking, scatterplot variants appear at or near the top compared with other tested visualizations [@harrisonRankingVisualizationsCorrelation2014a].

**Notes:** The guidance is about discrimination precision (JND), not about estimating the exact numeric correlation value.

## When scatterplots are the right default <!-- role: context -->

- **User Goal:** Reliably compare correlation strengths across multiple relationships.
- **Task:** Forced-choice discrimination or informal comparison of “more vs less correlated.”
- **Data:** Two quantitative variables; moderate sample size/density similar to the paper’s setting (100 points in fixed-size panels).
- **Chart Setting:** Static view or small multiples where consistent comparison matters.
- **Audience:** Broad audiences with mixed statistical training.
- **Success Criterion:** Low JND and stable performance across correlation direction.

## When not to default to scatterplots <!-- role: exceptions -->

**Break it when:** Your use case cannot represent individual points or requires a different structural constraint than point-based bivariate display. **Why:** The paper’s evidence compares specific chart families; the scatterplot advantage is established within that tested set and task.

## Tradeoffs of defaulting to scatterplots <!-- role: costs -->

**Sacrifice:** Scatterplots may not align with tools or conventions that push other chart types for two-column data. **Risk:** Overreliance on scatterplots can crowd a dashboard if many relationships must be shown simultaneously. **Mitigation:** Use small multiples or reserve scatterplots for the comparisons where correlation discrimination is most critical.

## Common mistakes when using scatterplots for correlation judgments <!-- role: mistakes -->

- **Mistake:** Switching away from scatterplots to a more familiar chart type without checking discrimination precision. **Why it fails:** Several common alternatives in the paper show substantially higher JNDs or sign asymmetries.
- **Mistake:** Assuming that if a chart “shows a trend,” it supports fine discrimination of correlation differences. **Why it fails:** The paper’s JND results show large variation in precision across visualizations that can all depict trends.

## Quick checks for choosing scatterplots appropriately <!-- role: check -->

**Failure Sign:** Users disagree frequently on which of two relationships is more correlated. **Quick Check:** Compare the candidate chart’s predicted/known JND against the scatterplot’s JND at your target r range. **Stronger Test:** Run a small forced-choice comparison study (two charts, same r values) and measure JND via a short staircase.

## What to do instead when scatterplots are not feasible <!-- role: fix -->

- Use the paper’s Weber-model ranking to pick the next-best visualization×direction for your correlation range.
- If correlation sign varies, select a chart with demonstrated low JND for both signs or use sign-specific chart choices.
- If you must use a line-family chart, consider ordering choices that improve discriminability within that family (validated by JND).
- If a chosen chart produces chance-level discrimination for your sign/range, switch chart families rather than tuning cosmetic parameters.
