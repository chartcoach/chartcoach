---
id: prefer-stacked-bars-or-novel-circular-charts-over-pie-and-treemap-for-part-to-whole-sorting
title: Prefer stacked bars or novel circular part-to-whole charts over pie and treemap
  for part-to-whole sorting
bibliography: references.bib
description: For sorting/estimating part-to-whole shares across multiple categories,
  stacked bars and certain circular variants yield better accuracy than pie, and pie
  beats treemap.
labels:
- chart:stacked-bar
- chart:pie
- chart:treemap
- chart:part-to-whole
- task:sort
- visual:angle
- visual:area
- visual:length
- visual:color
- impact:accuracy
- data:quantitative
- data:categorical
- audience:general
- comparison:chart-type
---

## Prefer stacked bars or circular variants for accurate part-to-whole sorting <!-- role: advice -->

Prefer a stacked bar chart or a circular part-to-whole variant (straight-line circular or circular slices) instead of a pie chart when you need higher accuracy for sorting/estimating part-to-whole percentages across multiple categories. Avoid treemaps for this same part-to-whole sorting use case.

## Accuracy advantages in part-to-whole estimation across chart types <!-- role: reason -->

Accuracy differs by chart type for part-to-whole judgments even when the task and number of parts are held constant, so choosing the chart type can change error rates for the same underlying values.

**Mechanism:** When the chart form better supports comparing segment magnitudes for the asked-for slice, viewers make smaller estimation errors during part-to-whole judgments.

**Evidence:** In part-to-whole sorting/estimation with five slices, stacked bars and the two circular variants were ranked ahead of the pie chart for accuracy, and the treemap ranked last; additionally, circular slices performed significantly better than the pie chart, and the pie chart performed significantly better than the treemap under the study’s tests [@kosaraImpactDistributionChart2019; @zengReviewCollationGraphical2023].

**Notes:** The accuracy ranking here is specific to the evaluated part-to-whole judgment task and the tested chart set.

## Context for choosing a part-to-whole chart for sorting/estimation <!-- role: context -->

- **User Goal:** Estimate and compare category shares as percentages of a whole.
- **Task:** Sort/compare part-to-whole values across categories (part-to-whole judgment framed as a “sort” task).
- **Data:** One quantitative measure split into nominal categories (five parts in the evaluated setting).
- **Chart Setting:** Static chart, color hue used to identify the target slice/category.
- **Audience:** General audiences performing quick judgments.
- **Success Criterion:** Lower error (higher accuracy) in reported percentages.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** You are not doing part-to-whole sorting/estimation (for example, your task is not a part-to-whole percentage judgment). **Why:** The evidence only covers the part-to-whole “sort”/estimation task and does not justify generalizing to other tasks.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may need to switch away from a familiar pie/treemap form, which can increase design or stakeholder friction. **Risk:** Applying this as a universal rule can be misleading if your task differs from part-to-whole estimation/sorting. **Mitigation:** Treat this as a task-scoped default and confirm with a small task-matched check.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Replacing a pie chart with a treemap assuming it will automatically improve part-to-whole readability. **Why it fails:** In this task setting, treemaps were least accurate and were significantly worse than the pie chart.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Viewers frequently mis-estimate category shares or struggle to decide which slice is bigger when asked for a percentage. **Quick Check:** Compare at least one example using your current chart and a stacked bar (or one of the circular variants) and see if the estimate errors visibly shrink in informal review. **Stronger Test:** Run a small, task-matched pilot where people report the percent for a highlighted category and compare absolute errors across chart types.

## Fix: What to do instead <!-- role: fix -->

- Switch from pie/treemap to a stacked bar chart for the same part-to-whole breakdown.
- If you are exploring circular alternatives, use a circular part-to-whole variant like “circular slices” or “straight-line circular” instead of a traditional pie.
- If you must keep a pie-like form, avoid treemap as the substitute for this task and keep the pie over treemap.
- Validate the choice with a small, task-matched accuracy check using your real category labels and value ranges.
