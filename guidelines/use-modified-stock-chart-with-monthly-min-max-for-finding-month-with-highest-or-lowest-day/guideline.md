---
id: use-modified-stock-chart-with-monthly-min-max-for-finding-month-with-highest-or-lowest-day
title: Use a modified stock chart with monthly minima and maxima marks to find the
  month with the highest or lowest day
bibliography: references.bib
description: For month-level extrema searches in time series, explicitly encode monthly
  minima/maxima to improve accuracy.
labels:
- chart:line
- task:find-extremum
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- granularity:monthly
---

## Use monthly minima/maxima marks for month-level extrema questions <!-- role: advice -->

Use a time-series design that explicitly marks each month’s minimum and maximum when the task is to choose which month contains the highest day or the lowest day.

## Why explicit extrema marks improve extrema finding <!-- role: reason -->

Extrema-finding across months becomes a comparison among a small set of explicitly encoded values rather than a visual search through many daily points.

**Mechanism:** Explicit month-level extrema reduce search and memory demands by turning “scan many points” into “compare one extrema mark per month.”

**Evidence:** For finding the month with the lowest day (find-extremum-2), the modified stock chart with monthly extrema (E-2) ranked highest and significantly outperformed the plain line chart (E-1). [@albersTaskdrivenEvaluationAggregation2014; @zengReviewCollationGraphical2023]

**Notes:** This rule covers both maxima and minima tasks at the month scale; the evidence is strongest for the minima task in the extracted results.

## When users must identify the month containing an extreme day <!-- role: context -->

- **User Goal:** Identify which month contains the highest (or lowest) single-day value.
- **Task:** Find extremum across time windows.
- **Data:** Temporal quantitative series with meaningful discrete windows (months).
- **Chart Setting:** Static display where per-month extrema can be precomputed.
- **Audience:** General audiences performing quick lookups.
- **Success Criterion:** Higher accuracy for selecting the correct month.

## When not to precompute and encode extrema <!-- role: exceptions -->

**Break it when:** The audience needs to verify the exact day and context of the extreme rather than just which month contains it. **Why:** Emphasizing month-level extrema can downplay within-month structure that may matter for explanation.

## Tradeoffs of emphasizing extrema <!-- role: costs -->

**Sacrifice:** Extra marks/layers and potential clutter relative to a single line.\
**Risk:** Viewers may focus on extrema and miss other distributional properties within months.\
**Mitigation:** Keep the raw series visible alongside extrema marks.

## Common extrema-encoding failure modes <!-- role: mistakes -->

**Mistake:** Using only a raw line chart for month-level extrema selection. **Why it fails:** Accuracy was significantly lower than a design that explicitly encoded monthly extrema.

## Quick checks for extrema support <!-- role: check -->

**Failure Sign:** People consistently confuse months with similarly high/low values because the extreme is hard to spot.\
**Quick Check:** Ask a few readers to answer “which month has the lowest day?”; if they need to trace many points, extrema are not explicit enough.\
**Stronger Test:** Compare accuracy between the plain line and an extrema-marked design on the same stimuli.

## What to do instead if extrema marks are too cluttered <!-- role: fix -->

- Show only the per-month extrema values (and suppress the raw line) when context is not needed.
- Provide a separate view dedicated to extrema comparison across months.
- Reduce the number of months shown at once (e.g., filter to a quarter) before applying the extrema-finding task.
