---
id: use-scatterplots-for-correlation-judgments-across-correlation-strengths
title: Use scatterplots for correlation judgments across a wide range of correlation
  strengths
bibliography: references.bib
description: When the task is to judge correlation strength, prefer scatterplots over
  the other tested chart forms across multiple correlation magnitudes.
labels:
- chart:scatter
- task:correlate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- metric:jnd
- complexity:intermediate
---

## Prefer scatterplots for correlation judgment <!-- role: advice -->

Use a scatterplot with two quantitative variables mapped to horizontal and vertical position when viewers need to judge correlation strength.

## Why scatterplots support correlation judgment well <!-- role: reason -->

Correlation judgment depends on how precisely viewers can discriminate differences in correlation; lower just-noticeable difference (Just Noticeable Difference, JND) indicates higher perceptual precision for that judgment.

**Mechanism:** Mapping two quantitative variables to position on orthogonal axes provides a visual pattern that viewers can discriminate with relatively small changes in correlation, yielding lower JNDs across multiple tested correlation strengths.

**Evidence:** Across multiple tested correlation levels (e.g., r around 0.1, 0.3, 0.5, 0.7, 0.9 with both signs), the ranked JND outcomes place scatterplots at or near the top compared to the other represented forms in the extracted rankings. [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023]

**Notes:** This guideline uses JND-based ranks for the correlate task as the effectiveness signal.

## Where this applies <!-- role: context -->

- **User Goal:** Judge how strongly two quantitative variables are related.
- **Task:** Correlate (perceptual discrimination of correlation strength).
- **Data:** Two quantitative fields with an underlying correlation (positive or negative) where correlation magnitude may vary.
- **Chart Setting:** Static, standard display where a single view must support correlation judgment.
- **Audience:** General audiences (no special statistical training assumed).
- **Success Criterion:** Lower discrimination threshold for correlation differences (lower JND).

## When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot plot individual observations (e.g., privacy, extreme overplotting, or unavailable point-level data). **Why:** The guideline assumes the viewer can see the positional pattern created by many points.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Scatterplots can require more space and may be harder to read when points overlap heavily.\
**Risk:** If the display prevents seeing point structure, the perceptual advantage may not materialize.\
**Mitigation:** Ensure the plot makes individual point distribution legible enough for pattern perception.

## Common mistakes to avoid <!-- role: mistakes -->

**Mistake:** Switching to a non-bivariate form (e.g., an ordered series-style display) for correlation judgment by default. **Why it fails:** The extracted rankings show higher JND (worse precision) than scatterplots for correlation discrimination.

## Quick checks <!-- role: check -->

**Failure Sign:** Viewers disagree widely about which of two relationships is more correlated when differences are small.\
**Quick Check:** Show two nearby correlation cases and see whether people consistently pick the stronger one.\
**Stronger Test:** Run a small discrimination pilot mirroring the “which is more correlated” comparison task and compare error/JND-like thresholds across candidate charts.

## What to do instead if you can't use a scatterplot <!-- role: fix -->

- Use a parallel-coordinates-style view only if you can validate that it supports your correlation judgments for your correlation direction and range.
- Use an ordered line-style view only if your data can be meaningfully ordered and you test that viewers can still discriminate correlation differences adequately.
- Reduce the scope of the question (e.g., only strong correlations) and validate the chosen form with a quick user check.
- Provide multiple coordinated views (e.g., include a scatterplot alongside an alternative) when correlation judgment is critical but constraints prevent relying on one form.
