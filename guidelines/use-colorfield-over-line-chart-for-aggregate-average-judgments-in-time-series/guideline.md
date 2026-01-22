---
id: use-colorfield-over-line-chart-for-aggregate-average-judgments-in-time-series
title: Use a colorfield encoding instead of a line chart for aggregate average judgments
  in time series
bibliography: references.bib
description: For finding the time range with the highest average in a time series,
  a colorfield value encoding yields higher accuracy than a line chart.
labels:
- chart:line
- chart:heatmap
- task:aggregate
- visual:color
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- study:between-subjects
---

## Prefer a colorfield for maximum-average-in-range decisions <!-- role: advice -->

Use a colorfield where time is on the horizontal axis and value is encoded by color when the task is to choose which time segment has the highest average. Prefer this over a standard line chart for this aggregate judgment task.

## Why colorfields help average-over-range judgments <!-- role: reason -->

Encoding values as color supports direct comparison of average “intensity” (overall color) within each time segment, rather than requiring readers to integrate many positional samples along a line. This shifts the judgment from aggregating many pointwise readings to comparing summary appearance across segments.

**Mechanism:** Color-encoded regions can be visually summarized across a defined time segment, while a line chart requires piecing together many positional values to estimate an average.

**Evidence:** In an aggregate task (select the month with the highest average) using time-series data, a color-hue encoding over time (colorfield) was more accurate than a line chart (positionY over time), with a significant difference reported via ANOVA (p < 0.001) and a direct significant pair (colorfield > line) in the recorded results [@correllComparingAveragesTime2012; @zengReviewCollationGraphical2023].

**Notes:** This guideline is only about accuracy for the aggregate task reported, not about other tasks (e.g., retrieving exact values).

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Decide which time segment (pre-defined bins such as months) has the highest average value.
- **Task:** Aggregate (average-over-range) judgment.
- **Data:** One quantitative measure indexed by an ordered temporal or ordinal sequence.
- **Chart Setting:** Static display where the viewer can compare multiple pre-defined ranges along one timeline.
- **Audience:** General audiences performing quick analytic judgments.
- **Success Criterion:** Higher task accuracy for selecting the maximum-average segment.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** The decision requires reading or comparing precise individual values at specific times. **Why:** This guideline only has evidence for an aggregate average judgment task, not for value-reading tasks.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose support for precise pointwise reading that a line chart commonly enables. **Risk:** Readers may over-trust color differences as exact numeric differences even when the mapping is continuous. **Mitigation:** Treat this as a task-specific choice and validate with the intended task (aggregate selection) rather than general readability.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Switching to a colorfield for any time-series task without confirming it is an average-over-range decision. **Why it fails:** The evidence only supports improved accuracy for the aggregate task recorded, not for other tasks.

## Quick tests before you ship <!-- role: check -->

**Failure Sign:** People disagree widely on which time segment has the highest average when using a line chart. **Quick Check:** Ask a few readers to pick the maximum-average segment from both a line chart and a colorfield and compare correctness rates. **Stronger Test:** Run a small A/B test measuring accuracy on the same aggregate question across the two encodings.

## What to do instead if this rule doesn’t fit <!-- role: fix -->

- Keep the line chart when the primary need is reading exact values at specific time points.
- Provide two coordinated views: one optimized for aggregate judgments (colorfield) and one for pointwise reading (line chart).
- Change the task framing to explicitly focus on aggregate comparisons (segment-based questions) if aggregate insight is the goal.
- If the time segments are not pre-defined, restructure the analysis so segments are defined before using a colorfield for segment-wise comparison.
