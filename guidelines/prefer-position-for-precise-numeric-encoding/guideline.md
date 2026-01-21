---
id: prefer-position-for-precise-numeric-encoding
title: Encode Numbers with Position First
bibliography: references.bib
description: Use spatial position as the primary encoding for numerical values to
  maximize decoding accuracy.
labels:
- chart:bar
- task:compare
- visual:position
- impact:clarity
- data:numerical
- audience:novice
- complexity:foundational
---

## The Rule <!-- role: advice -->

Encode numerical values using spatial position (e.g., aligned axes in bar charts, line charts, scatter plots) whenever you need accurate reading.

## The Logic <!-- role: reason -->

Spatial position is the most accurately decoded visual channel for numbers compared to alternatives like angle, length, area, volume, or saturation, improving comprehension and decision-making.

- **The Principle:** Graphical perception favors position for quantitative decoding
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Read and compare numeric values precisely; spot trends and outliers reliably
- **Data Type:** Quantitative measures (single or multiple series)
- **Audience:** General audiences and analysts

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must increase data density in very small multiples where standard position-based plots won’t fit
- **Reason:** More compact encodings may preserve resolution better at small sizes (see horizon graphs) [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** More screen space than dense encodings (e.g., horizon graphs)
- **The Risk:** Overplotting when many series share the same axes

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to area, volume, or saturation encodings to “save space” while still expecting precise comparisons
- **Why it fails:** These channels are less accurately decoded than position [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers must “eyeball” sizes/brightness instead of reading off a consistent scale
- **The Test:** Ask whether two close values can be distinguished without guessing; if not, you likely avoided position unnecessarily

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a shared axis and align marks to a common baseline
- **Best Fix:** Change to a position-based chart type (bar/line/scatter) appropriate to the task [@heerTourVisualizationZoo2010]
