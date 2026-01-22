---
id: use-stacked-bars-over-stacked-lines-or-areas-for-negative-correlation-judgment
title: Use stacked bar charts over stacked line or stacked area charts for judging
  negative correlation strength
bibliography: references.bib
description: For negative correlation judgment, stacked bar charts rank better (lower
  JND) than stacked area and stacked line charts in the extracted comparisons.
labels:
- chart:bar
- chart:area
- chart:line
- task:correlate
- visual:length
- visual:area
- impact:accuracy
- data:quantitative
- audience:general
- metric:jnd
- correlation:negative
- complexity:intermediate
---

## Prefer stacked bars for negative correlation discrimination among stacked variants <!-- role: advice -->

For judging negative correlation strength using stacked charts, use stacked bar charts rather than stacked line charts or stacked area charts.

## Why stacked bars can improve discrimination among stacked variants <!-- role: reason -->

When multiple chart variants depict the same underlying relationship, the discriminability of correlation changes depends on how the visual form supports small differences in correlation, captured by JND.

**Mechanism:** Among stacked variants for negative correlations, the stacked bar form supports finer perceptual discrimination of correlation differences than the stacked area and stacked line forms, leading to lower JND.

**Evidence:** Pairwise tests reported for negative correlations show stacked bar charts outperform stacked line and stacked area charts for correlation judgment (lower JND), and the extracted rankings place the stacked bar (negative) ahead of the stacked variants (negative). [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023]

**Notes:** This guideline is limited to the negative-correlation case and to comparisons among stacked variants.

## Where this applies <!-- role: context -->

- **User Goal:** Compare which of two relationships is more negatively correlated using stacked representations.
- **Task:** Correlate (discriminate correlation strength).
- **Data:** Two quantitative variables represented through stacked series-style encodings where correlation is negative.
- **Chart Setting:** Static display where the stacked form is required by constraints.
- **Audience:** General audiences.
- **Success Criterion:** Lower JND / more reliable discrimination.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The main requirement is to emphasize continuity or trend over an ordered dimension rather than correlation discrimination. **Why:** This guideline optimizes correlation discrimination, not trend reading.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Stacked bars can be visually dense and may reduce perceived continuity compared to lines/areas.\
**Risk:** If viewers focus on unrelated features, correlation discrimination can still suffer even with stacked bars.\
**Mitigation:** Keep the viewing task explicit (correlation comparison) and avoid unnecessary visual complexity.

## Common mistakes to avoid <!-- role: mistakes -->

**Mistake:** Using stacked area or stacked line charts as interchangeable with stacked bars for correlation judgment. **Why it fails:** The extracted evidence shows stacked variants differ meaningfully in correlation discrimination performance for negative correlations.

## Quick checks <!-- role: check -->

**Failure Sign:** People need large differences in correlation before they can reliably tell which is stronger.\
**Quick Check:** Run a small comparison task with two nearby negative correlations using stacked bar versus stacked area/line and see which yields more consistent answers.\
**Stronger Test:** Collect enough judgments to estimate a discrimination threshold and choose the stacked variant with the lower threshold.

## What to do instead <!-- role: fix -->

- Use a scatterplot if stacked presentation is not required.
- Use parallel coordinates as an alternative bivariate view for negative correlation discrimination if scatterplots are infeasible.
- Reduce reliance on stacking by separating series into small multiples if correlation judgment remains critical.
- Add a dedicated correlation-focused view alongside the stacked chart when stacking must be preserved for other reasons.
