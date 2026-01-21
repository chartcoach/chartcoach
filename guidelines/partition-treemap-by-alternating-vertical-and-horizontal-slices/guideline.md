---
id: partition-treemap-by-alternating-vertical-and-horizontal-slices
title: Alternate Vertical and Horizontal Cuts by Tree Level
bibliography: references.bib
description: Lay out treemap rectangles by slicing along one axis per level, alternating
  axes as you recurse.
labels:
- chart:treemap
- task:layout
- visual:position
- impact:efficiency
- data:hierarchical
- audience:expert
- source:shneiderman-1992
---

## The Rule <!-- role: advice -->

Generate treemaps by slicing the parent rectangle into child rectangles proportionally, alternating the cut direction at each depth (e.g., vertical at even levels, horizontal at odd levels).

## The Logic <!-- role: reason -->

Alternating slice direction provides a simple recursive layout that avoids computationally intensive bin-packing while still filling space and preserving proportional areas through ratio-based partitioning.

- **The Principle:** Recursive slice-and-dice space partitioning
- **The Evidence:** Shneiderman specifies vertical partitions at even levels and horizontal at odd levels, using `x3 = x1 + (Size(child)/Size(root))*(x2-x1)` and recursing with flipped axes [@shneidermanTreeVisualizationTreemaps1992].

## Where to Apply <!-- role: context -->

- **User Goal:** Fast rendering of large trees with many nodes.
- **Data Type:** Arbitrary trees where each node has a weight (pre-aggregated for internal nodes).
- **Audience:** Implementers building treemap visualizations.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need a layout strategy that avoids extreme thin rectangles for readability.
- **Reason:** The paper’s algorithm optimizes simplicity and speed, not rectangle aspect ratios [@shneidermanTreeVisualizationTreemaps1992].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some rectangles can become long, thin “slices,” reducing legibility.
- **The Risk:** Small leaves may become too small to represent, especially with large value ranges [@shneidermanTreeVisualizationTreemaps1992].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Introducing bin-packing to “fit rectangles better” as a first step.
- **Why it fails:** It increases computational complexity, undermining the rapid, linear-time goal Shneiderman emphasizes [@shneidermanTreeVisualizationTreemaps1992].

## How to Check <!-- role: check -->

- **Visual Sign:** Rendering time grows rapidly with node count, or layout code is complex and non-recursive.
- **The Test:** Confirm the algorithm visits each node once (linear in number of nodes) as described [@shneidermanTreeVisualizationTreemaps1992].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Implement the described recursive slice-and-dice with an `axis` flag that flips each level.
- **Best Fix:** Ensure partition boundaries are computed purely from size ratios and the current rectangle width/height [@shneidermanTreeVisualizationTreemaps1992].
