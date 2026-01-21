---
id: use-parallel-coordinates-to-show-many-variables-compactly
title: Use Parallel Coordinates to Visualize Many Variables at Once
bibliography: references.bib
description: Use parallel coordinates to display multivariate records compactly and
  reveal crossings indicative of correlation.
labels:
- chart:parallel-coordinates
- task:explore
- visual:position
- impact:space-efficiency
- data:multivariate
- audience:analyst
- complexity:advanced
---

## The Rule <!-- role: advice -->

Use parallel coordinates when you need to show many variables simultaneously and compare individual records across dimensions.

## The Logic <!-- role: reason -->

Parallel coordinates plot values on parallel axes and connect each record with a polyline; line crossings can indicate inverse correlation, and reordering axes plus interactive filtering supports pattern finding.

- **The Principle:** Encode multivariate profiles as polylines across aligned axes
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Explore multivariate patterns, tradeoffs, and correlations across many variables
- **Data Type:** Multivariate tables with many columns (dimensions)
- **Audience:** Analysts comfortable with dense displays

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary need is to see pairwise relationships with point clouds (shape, clusters)
- **Reason:** Parallel coordinates emphasize record profiles and crossings rather than 2D point distributions [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Immediate interpretability for casual audiences
- **The Risk:** Visual clutter with many records unless filtering is available

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a fixed axis order even when patterns are unclear
- **Why it fails:** Reordering dimensions is a key aid to pattern finding [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** The chart looks like an unreadable bundle and no filtering exists
- **The Test:** If filtering along one or more dimensions is impossible, the display won’t support effective querying [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Allow interactive filtering (brushing) on axes to reduce clutter
- **Best Fix:** Support axis reordering plus filtering to reveal correlations and patterns [@heerTourVisualizationZoo2010]
