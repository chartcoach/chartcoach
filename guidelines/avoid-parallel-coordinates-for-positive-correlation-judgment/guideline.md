---
id: avoid-parallel-coordinates-for-positive-correlation-judgment
title: Avoid parallel coordinates for judging positive correlation strength
bibliography: references.bib
description: Parallel coordinates perform worse (higher JND) for judging positive
  correlation than several alternatives in the extracted rankings.
labels:
- chart:parallel-coordinates
- task:correlate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- metric:jnd
- correlation:positive
- complexity:intermediate
---

## Avoid parallel coordinates when correlation is positive <!-- role: advice -->

Avoid parallel coordinates when viewers need to discriminate the strength of positive correlations between two quantitative variables.

## Why parallel coordinates can reduce precision for positive correlation <!-- role: reason -->

Correlation discrimination precision varies by chart form and correlation sign, and higher JND indicates poorer discrimination.

**Mechanism:** For positive correlations, the visual structure induced by parallel coordinates can make changes in correlation less discriminable, increasing the JND needed for reliable judgments.

**Evidence:** In the extracted JND rankings for the correlate task, the parallel-coordinates design for positive correlation is placed at the bottom (worst) among the compared designs at multiple tested correlation strengths. [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023]

**Notes:** This is a sign-specific guideline (positive correlation).

## Where this applies <!-- role: context -->

- **User Goal:** Decide which of two relationships is more strongly positively correlated.
- **Task:** Correlate (discriminate correlation differences).
- **Data:** Two quantitative variables where the expected relationship is positive (r > 0).
- **Chart Setting:** Static presentation where viewers must make comparative judgments.
- **Audience:** General audiences.
- **Success Criterion:** Low JND (high precision) for positive correlation judgments.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your primary goal is not correlation-strength discrimination (e.g., you need to show many dimensions in one view and correlation judgment is secondary). **Why:** This guideline is only about correlation discrimination performance, not multidimensional overview needs.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Avoiding parallel coordinates may reduce your ability to show many dimensions compactly in one figure.\
**Risk:** Forcing a bivariate alternative may hide other dimensions that matter to the analysis.\
**Mitigation:** Separate tasks: use a bivariate view for correlation judgment and another view for multivariate context.

## Common mistakes to avoid <!-- role: mistakes -->

**Mistake:** Using parallel coordinates as the default for showing “relationship strength” without considering correlation sign. **Why it fails:** The extracted evidence indicates substantially worse JND for positive correlation discrimination in that form.

## Quick checks <!-- role: check -->

**Failure Sign:** People frequently confuse moderate vs. strong positive correlation in your parallel-coordinates view.\
**Quick Check:** Ask a few readers which of two positive relationships is more correlated and see if answers are consistent.\
**Stronger Test:** Compare the same judgments using a scatterplot versus parallel coordinates and keep the form that yields more consistent discrimination.

## What to do instead <!-- role: fix -->

- Use a scatterplot to support correlation-strength discrimination for positive relationships.
- If you must use parallel coordinates, test axis arrangement strategies and verify that correlation discrimination meets your needs.
- Add a companion scatterplot for the key variable pair whose correlation viewers must judge.
- If correlation sign varies, provide separate views or annotations that clarify direction before asking for strength judgments.
