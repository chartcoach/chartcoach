---
id: use-index-charts-to-compare-relative-change
title: Normalize Time Series with an Index Chart for Relative Change
bibliography: references.bib
description: Use an interactive index chart to compare relative changes across time
  series with different baselines.
labels:
- chart:line
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:analyst
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When baseline magnitudes differ but relative change matters, normalize series to a chosen index point and plot them as an index chart.

## The Logic <!-- role: reason -->

Normalization enables meaningful comparison of growth/decline rates across series whose raw levels differ widely, shifting attention to percentage change rather than absolute price/level.

- **The Principle:** Normalize to support like-for-like comparison across heterogeneous baselines
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare growth rates or relative performance over time
- **Data Type:** Multiple time series with different starting levels (e.g., stock prices)
- **Audience:** Analysts and decision-makers exploring performance

## When to Break It <!-- role: exceptions -->

- **Scenario:** The absolute magnitude is the question (e.g., “Which is larger today?”)
- **Reason:** Indexing hides absolute level differences [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Loses absolute scale context
- **The Risk:** Viewers may misinterpret indexed values as raw values if labeling is unclear

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Plotting raw values on the same axis and claiming “comparability”
- **Why it fails:** Different baselines dominate perception and obscure relative change [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** One series visually dwarfs others due solely to scale, not growth
- **The Test:** Re-expressing the series as % change should materially change readability; if it does, an index chart is likely warranted

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a normalization toggle (“Index to date…”)
- **Best Fix:** Use an index chart with a clear selected base point and labeling that communicates “% change since…” [@heerTourVisualizationZoo2010]
