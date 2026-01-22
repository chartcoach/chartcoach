---
id: use-scatterplots-not-parallel-coordinates-for-correlation-judgment
title: Use a scatterplot (not parallel coordinates) to judge correlation between two
  quantitative variables
bibliography: references.bib
description: For visual correlation judgments, scatterplots yield higher accuracy
  than parallel coordinate plots.
labels:
- chart:scatter
- chart:parallel-coordinates
- task:correlate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- comparison:chart-type
---

## Prefer scatterplots over parallel coordinates for correlation judgments <!-- role: advice -->

Use a scatterplot when the user needs to judge correlation between two quantitative variables, instead of a parallel coordinate plot. Prefer the scatterplot even when both views are available for the same data.

## Scatterplots provide a more discriminable correlation signal than parallel coordinates <!-- role: reason -->

Correlation judgments depend on how clearly the visualization makes the direction and strength of association perceptually available. A scatterplot presents correlation as a spatial pattern in 2D position, which supports more reliable discrimination of correlation levels than the line-crossing patterns that arise in parallel coordinate plots.

**Mechanism:** Position-based 2D point clouds make trend direction and tightness easier to visually separate into distinct correlation levels than overlapped line segments between two axes.

**Evidence:** In a controlled experiment varying visualization method, sample size, and observation time, correlation judgments were more accurate with scatterplots than with parallel coordinate plots for the correlate task. [@zengReviewCollationGraphical2023; @liJudgingCorrelationScatterplots2010]

**Notes:** This guideline covers only bivariate correlation judgment (two variables at a time), not other multivariate analysis tasks.

## When this applies: bivariate visual correlation judgment <!-- role: context -->

- **User Goal:** Decide whether two quantitative variables are positively correlated, negatively correlated, or uncorrelated (and how strongly).
- **Task:** Correlate.
- **Data:** Two quantitative fields; correlation strength is the primary question.
- **Chart Setting:** Static view where the user inspects a single bivariate relationship.
- **Audience:** General audiences who can interpret basic statistical charts.
- **Success Criterion:** Higher correctness of the correlation judgment.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task is not correlation judgment between two quantitative variables. **Why:** The evidence is only for the correlate task, so the comparison may not hold for other tasks.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose the “consistent axis” layout style that parallel coordinate plots provide when extending to many variables. **Risk:** Treating this as a blanket ban on parallel coordinates can block workflows where users need coordinated multivariate browsing rather than a single correlation estimate. **Mitigation:** Evaluate task-by-task if correlation judgment is not the main goal.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a parallel coordinate plot for bivariate correlation judgment because it is already used elsewhere in a multivariate dashboard. **Why it fails:** Correlation judgment accuracy is lower than with a scatterplot for this task.

## Quick tests <!-- role: check -->

**Failure Sign:** Users disagree about the sign or strength of correlation for the same pair of variables when using the parallel coordinate plot.\
**Quick Check:** Show the same bivariate data as a scatterplot and see if correlation judgments become more consistent.\
**Stronger Test:** Run a small timed study where users judge correlation sign/strength on both views and compare accuracy.

## What to do instead <!-- role: fix -->

- Replace the bivariate parallel coordinate view with a scatterplot for correlation judgment steps.
- Add a scatterplot-on-demand option when the user selects two variables from a parallel coordinate plot workflow.
- If you must keep the parallel coordinate plot, pair it with a scatterplot for the same two variables during correlation-focused analysis.
