---
id: account-for-overestimation-when-reading-average-from-bar-charts
title: Account for systematic overestimation when estimating an average from bar charts
bibliography: references.bib
description: Average positions read from bar charts can be systematically overestimated
  in aggregate judgments.
labels:
- chart:bar
- task:aggregate
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- bias:overestimate
- complexity:advanced
---

## Account for bar-average overestimation in aggregate judgments <!-- role: advice -->

When viewers estimate an average from a bar chart, assume the perceived average will be biased upward relative to the true average. Treat bar-based average judgments as potentially systematically overestimated rather than only noisy.

## Why bar averages skew upward <!-- role: reason -->

Even when a chart uses a widely trusted quantitative encoding, the perceived average can shift consistently away from the true value. This creates a predictable direction of bias that can affect aggregate judgments.

**Mechanism:** The perceived average of a set of bars can shift upward relative to the true average, producing consistent signed error in aggregate judgments.

**Evidence:** In an aggregate task using bars (quantitative data encoded by length with a nominal x-axis), average position estimates were significantly overestimated using a linear mixed-effects analysis. [@xiongBiasedAveragePosition2020; @zengReviewCollationGraphical2023]

**Notes:** This guideline concerns bias direction (systematic overestimation) for average estimation, not general bar-chart effectiveness across tasks.

## When this applies to your chart and task <!-- role: context -->

- **User Goal:** Estimate or recall an average level from a set of bars.
- **Task:** Aggregate (average position estimation).
- **Data:** Quantitative values distributed across a categorical/nominal x-axis.
- **Chart Setting:** A single bar series shown in one plot.
- **Audience:** Any audience making quick visual average judgments.
- **Success Criterion:** Minimizing directional bias in the perceived average.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The user is not estimating an average/aggregate from the bar set. **Why:** The evidence summarized here is specific to average position estimation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Adding guardrails for averaging can add visual or explanatory overhead. **Risk:** Viewers may infer that all bar interpretations are unreliable, even when the task is not averaging. **Mitigation:** Limit bias mitigation to workflows where the mean is the decision-relevant quantity.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming average-of-bars judgments will be unbiased because bars are familiar and “precise.” **Why it fails:** The observed error is directional (systematic overestimation) in aggregate judgments.

## Quick tests <!-- role: check -->

**Failure Sign:** People consistently report the average level of the bars higher than the true average. **Quick Check:** Collect a handful of average estimates from representative viewers and inspect whether signed errors are mostly positive. **Stronger Test:** Run a small pilot and test whether mean signed error is above zero.

## What to do instead <!-- role: fix -->

- Add an explicit average cue (e.g., an average indicator) to reduce reliance on mental averaging from bar heights.
- Provide the numeric average next to the chart when mean accuracy matters.
- Separate tasks that require recalling averages across series into views that do not require memory of bar-set averages.
- Validate the design by measuring signed error for average judgments in a brief task-focused evaluation.
