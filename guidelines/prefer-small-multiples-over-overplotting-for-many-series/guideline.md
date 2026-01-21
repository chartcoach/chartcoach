---
id: prefer-small-multiples-over-overplotting-for-many-series
title: Use Small Multiples to Avoid Overlapping Time-Series Lines
bibliography: references.bib
description: Split many time series into small multiples to reduce overlap and improve
  trend reading.
labels:
- chart:small-multiples
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:analyst
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When multiple time series overlap in a shared plot, split them into small multiples so each series has its own chart.

## The Logic <!-- role: reason -->

Overlapping curves reduce legibility; small multiples preserve a consistent visual form while eliminating occlusion, making both overall trends and local patterns easier to see.

- **The Principle:** Reduce occlusion and preserve comparability through repeated, separated views
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare trends across many categories without line collisions
- **Data Type:** Many time series (often category-split)
- **Audience:** Analysts exploring patterns; readers scanning categories

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary question requires direct within-axis comparison at shared scale (e.g., crossovers at exact dates)
- **Reason:** Separate panels can make some point-to-point comparisons slower [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** More screen space than a single combined chart
- **The Risk:** If scales are not clearly handled (e.g., normalization choices), viewers may miscompare magnitudes [@heerTourVisualizationZoo2010]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping one crowded plot and relying on color/legend to disambiguate
- **Why it fails:** Occlusion remains; readability collapses with many series [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Lines frequently cross/overlap and individual series cannot be traced end-to-end
- **The Test:** Try tracing one category with your finger; if you lose it, use small multiples [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Facet the chart by category into a grid of identical mini line charts
- **Best Fix:** Use small multiples with normalization when appropriate to emphasize within-category patterns (as shown for unemployment by industry) [@heerTourVisualizationZoo2010]
