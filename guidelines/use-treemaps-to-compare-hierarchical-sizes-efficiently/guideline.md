---
id: use-treemaps-to-compare-hierarchical-sizes-efficiently
title: Use Treemaps to Compare Hierarchical Sizes in Limited Space
bibliography: references.bib
description: Use treemaps to show hierarchical containment while enabling rapid comparison
  of node sizes.
labels:
- chart:treemap
- task:compare
- visual:area
- impact:space-efficiency
- data:hierarchical
- audience:analyst
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Use a treemap when you need a space-efficient hierarchy view where node area communicates size.

## The Logic <!-- role: reason -->

Treemaps are enclosure diagrams that recursively subdivide area into rectangles, making the size of any node quickly visible; squarified treemaps improve readability and size estimation compared to naive subdivision.

- **The Principle:** Space-filling enclosure supports rapid size comparison across hierarchy
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify largest components and how they nest within groups
- **Data Type:** Hierarchical data with a quantitative “size” per node
- **Audience:** Analysts; readers comfortable with area-based comparison

## When to Break It <!-- role: exceptions -->

- **Scenario:** The hierarchy relationships (paths) must be traced explicitly
- **Reason:** Treemaps emphasize containment and size over link structure [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Path clarity and sometimes label readability for small rectangles
- **The Risk:** Very small nodes become illegible

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using naive “slice-and-dice” rectangles that create extreme aspect ratios
- **Why it fails:** Squarified treemaps improve readability and size estimation [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Many rectangles are long/thin, and labels don’t fit
- **The Test:** If most leaves have extreme aspect ratios, you likely need a squarified approach [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the treemap layout to a squarified algorithm
- **Best Fix:** Use padding or other enclosure emphasis thoughtfully to support hierarchy reading while keeping rectangles readable [@heerTourVisualizationZoo2010]
