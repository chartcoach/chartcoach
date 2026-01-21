---
id: use-stacked-graphs-only-for-additive-nonnegative-series
title: Use Stacked Graphs Only for Additive, Non-Negative Time Series
bibliography: references.bib
description: Use stacked area graphs only when series are non-negative and their sum
  is meaningful.
labels:
- chart:stacked-area
- task:part-to-whole
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Use stacked graphs only when values are non-negative and interpreting the aggregate (the sum) is meaningful.

## The Logic <!-- role: reason -->

Stacked graphs visually encode a summation of time-series values; if summation is invalid or negatives exist, the visual representation becomes misleading or unusable.

- **The Principle:** Match aggregation semantics to the chart’s implicit arithmetic
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** See total volume over time and how categories contribute to that total
- **Data Type:** Multiple non-negative series where addition is meaningful (counts, totals)
- **Audience:** Broad audiences; dashboards with drill-down

## When to Break It <!-- role: exceptions -->

- **Scenario:** Data includes negative values
- **Reason:** Stacked graphs do not support negative numbers [@heerTourVisualizationZoo2010]
- **Scenario:** The series should not be summed (e.g., temperatures)
- **Reason:** The aggregate has no meaning and invites false inference [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Precise comparison of individual series trends away from the baseline
- **The Risk:** Trends for upper layers become hard to interpret because their baseline moves [@heerTourVisualizationZoo2010]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using stacking to “fit more lines” even when totals are meaningless
- **Why it fails:** The chart communicates an aggregate story that isn’t true [@heerTourVisualizationZoo2010]
- **The Wrong Fix:** Expecting viewers to compare upper bands accurately
- **Why it fails:** Off-baseline reading is perceptually difficult [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers argue about whether a category is rising/falling because its boundary is hard to read
- **The Test:** Hide all but one series; if the perceived trend changes substantially, stacking is impairing interpretation [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add interactive search/filtering to isolate series when needed [@heerTourVisualizationZoo2010]
- **Best Fix:** Switch to small multiples or an aligned multi-line view when individual trend comparison is primary [@heerTourVisualizationZoo2010]
