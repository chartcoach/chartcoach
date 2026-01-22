---
id: use-box-plot-per-month-to-characterize-monthly-distributions
title: Use per-month box plots to characterize monthly distributions
bibliography: references.bib
description: For distribution characterization across months, box plots support higher
  accuracy than several alternative time-series designs.
labels:
- chart:boxplot
- task:characterize-distribution
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- granularity:monthly
---

## Use per-month box plots for month-by-month distribution characterization <!-- role: advice -->

Use box plots grouped by month when the task is to characterize or compare distributions across months rather than to read individual daily values.

## Why box plots help distribution characterization across time windows <!-- role: reason -->

Box plots explicitly summarize key distributional features within each time window, making between-window comparisons of distribution shape and spread more direct than scanning raw points.

**Mechanism:** The display compresses each month into summary marks representing distribution structure, reducing the perceptual workload of interpreting many points.

**Evidence:** For the distribution-characterization task, the box-plot design (E-3) ranked highest in accuracy and significantly outperformed multiple alternatives (including the composite line-plus-bars E-4 and the plain line E-1). [@albersTaskdrivenEvaluationAggregation2014; @zengReviewCollationGraphical2023]

**Notes:** This guideline supports distribution understanding at the month level; it is not intended for identifying specific days.

## When the goal is to understand within-month distribution differences <!-- role: context -->

- **User Goal:** Compare how values are distributed across months.
- **Task:** Characterize distribution across discrete time windows.
- **Data:** Temporal quantitative data that can be grouped into months.
- **Chart Setting:** Static dashboard or report where summary is acceptable.
- **Audience:** General audiences needing an overview.
- **Success Criterion:** Higher accuracy in distribution-focused judgments.

## When not to use box plots for the primary view <!-- role: exceptions -->

**Break it when:** The audience must identify individual day-level events or exact daily extrema. **Why:** Box plots de-emphasize the raw sequence and do not directly show which day produced a value.

## Tradeoffs of box plots for time series <!-- role: costs -->

**Sacrifice:** Loss of day-to-day temporal continuity and patterns (e.g., trends within a month).\
**Risk:** Readers may assume the visualization contains all information needed about temporal behavior when it is intentionally summarized.\
**Mitigation:** Pair with a raw-series view if day-to-day structure may matter.

## Common distribution-encoding mistakes <!-- role: mistakes -->

**Mistake:** Using only a raw line chart to ask distribution characterization questions. **Why it fails:** Accuracy was lower than for per-month box plots in the evaluated distribution task.

## Quick checks for distribution comprehension <!-- role: check -->

**Failure Sign:** People describe trends over time when asked about distributional differences between months.\
**Quick Check:** Ask readers to describe what changes from month to month; if they cannot mention spread or central tendency, the distribution summary may be unclear.\
**Stronger Test:** Give a short quiz about which month has the “widest spread” or “most variable” distribution and measure accuracy.

## What to do instead if box plots are not acceptable <!-- role: fix -->

- Use another per-month summary design that directly encodes distribution-relevant summaries rather than raw points.
- Provide a paired view: one summarized view for distribution tasks and one raw-series view for sequence tasks.
- Reduce temporal resolution (e.g., show weekly aggregates) if month-level box plots feel too abstract for the audience.
