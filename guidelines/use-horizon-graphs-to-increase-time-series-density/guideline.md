---
id: use-horizon-graphs-to-increase-time-series-density
title: Use Horizon Graphs to Compare Many Dense Time Series in Little Space
bibliography: references.bib
description: Use horizon graphs to preserve resolution while greatly increasing time-series
  data density.
labels:
- chart:horizon
- task:compare
- visual:color
- impact:space-efficiency
- data:temporal
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

When you must compare many time series in very small vertical space, use horizon graphs with banding and layering.

## The Logic <!-- role: reason -->

Horizon graphs increase data density by mirroring negative values and layering multiple value bands, preserving resolution while using substantially less space; they can outperform standard plots at small sizes despite a learning curve.

- **The Principle:** Increase data density via banded layering without sacrificing resolution
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Scan and compare many time series at once in constrained space
- **Data Type:** High-density time series, potentially with positive/negative values
- **Audience:** Analysts willing to learn a more complex encoding

## When to Break It <!-- role: exceptions -->

- **Scenario:** The audience is unfamiliar and the display size is not constrained
- **Reason:** Horizon graphs “take some time to learn,” and simpler charts may suffice [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Immediate interpretability compared to a standard line/area chart
- **The Risk:** Misreading banded color intensity if the banding scheme is unclear

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Shrinking standard area/line charts until axes and shapes are unreadable
- **Why it fails:** You lose effective resolution and comparability; horizon graphs are designed for this constraint [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Mini time-series charts become indistinguishable blobs when reduced in height
- **The Test:** Reduce the chart to its intended small size; if patterns disappear, consider horizon graphs [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Apply mirroring of negative values and a small number of bands
- **Best Fix:** Implement full horizon banding and layering with consistent band thresholds and a clear legend/explanation [@heerTourVisualizationZoo2010]
