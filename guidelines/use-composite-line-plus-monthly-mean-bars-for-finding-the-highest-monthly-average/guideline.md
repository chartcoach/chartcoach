---
id: use-composite-line-plus-monthly-mean-bars-for-finding-the-highest-monthly-average
title: Use a composite line chart with monthly mean bars to identify the month with
  the highest average
bibliography: references.bib
description: For month-level average comparisons in time series, overlay monthly mean
  bars on the raw line to improve accuracy.
labels:
- chart:line
- chart:bar
- task:aggregate
- visual:position
- visual:length
- impact:accuracy
- data:temporal
- audience:general
- granularity:monthly
---

## Use a line-plus-monthly-mean composite for monthly average comparisons <!-- role: advice -->

Use a composite chart that overlays a raw time-series line with per-month mean bars when viewers must choose which month has the highest average.

## Why the line-plus-mean overlay helps average judgments <!-- role: reason -->

Adding an explicit per-group mean reduces the need for viewers to mentally average many points, while retaining the raw series for contextual checking.

**Mechanism:** The mean is presented as a single, comparable mark per month, which supports more direct comparisons than visually aggregating many daily points.

**Evidence:** For the monthly-average identification task, the line-plus-monthly-mean composite (E-4) ranked highest in accuracy and significantly outperformed several alternatives (including the plain line chart E-1). [@albersTaskdrivenEvaluationAggregation2014; @zengReviewCollationGraphical2023]

**Notes:** This guideline targets month-binned comparisons; it does not assume the same benefit at other time granularities.

## When monthly averages must be compared across time windows <!-- role: context -->

- **User Goal:** Pick the month with the highest average level in a time series.
- **Task:** Aggregate (mean) comparison across discrete time windows.
- **Data:** Temporal quantitative values with an ordinal time axis and a meaningful windowing (e.g., months).
- **Chart Setting:** Static chart where the time window (month) is known and fixed.
- **Audience:** General audiences who may not want to compute averages mentally.
- **Success Criterion:** Higher accuracy in selecting the correct month.

## When not to rely on a line-plus-monthly-mean composite <!-- role: exceptions -->

**Break it when:** The time window of comparison is not months (or not pre-defined). **Why:** The mean bars encode a specific aggregation window, so mismatched windows can mislead or fail to support the intended comparison.

## Tradeoffs of adding monthly mean bars <!-- role: costs -->

**Sacrifice:** Additional visual complexity and layering compared with a single line.\
**Risk:** Viewers may overweight the aggregated bars and ignore relevant within-month variation.\
**Mitigation:** Keep the raw line visible so within-window variability remains inspectable.

## Common ways this goes wrong in practice <!-- role: mistakes -->

**Mistake:** Showing only the raw line and expecting viewers to reliably identify the highest average month. **Why it fails:** Accuracy was lower for the plain line condition than for the composite that explicitly encoded monthly means.

## Quick tests for whether the composite is working <!-- role: check -->

**Failure Sign:** People disagree frequently about which month has the highest average after brief viewing.\
**Quick Check:** Ask a few readers to answer the “highest average month” question; if responses vary widely, the mean may not be legible enough.\
**Stronger Test:** Run a small A/B comparison between a plain line and the composite for the same question and measure accuracy.

## What to do instead if the composite cannot be used <!-- role: fix -->

- Use a chart that explicitly encodes per-month summary statistics rather than relying on visual averaging.
- Use a discretely aggregated per-month color encoding that directly represents the monthly mean if a color-based design is required.
- Reduce the task to a smaller set of candidate months before showing the time series, so fewer averages must be compared.
