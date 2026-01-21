---
id: penalize-high-cardinality-fields-on-color-shape-or-facets-in-recommendations
title: Penalize High-Cardinality Fields on Color, Shape, and Facets
bibliography: references.bib
description: Avoid recommendations that map many unique values to hard-to-discriminate
  channels or huge trellis layouts.
labels:
- chart:scatter
- task:explore
- visual:color
- impact:readability
- data:high-cardinality
- audience:analyst
- system:recommendation
---

## The Rule <!-- role: advice -->

Rank down (or avoid) recommendations that encode high-cardinality variables using color, shape, row, or column facets.

## The Logic <!-- role: reason -->

Compass accounts for cardinality because high-cardinality encodings can cause poor discrimination (color/shape) or massive sparse trellis plots (row/column), reducing interpretability—especially in a gallery [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Match channel capacity to variable cardinality
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Scan readable recommended charts quickly
- **Data Type:** Variables with many distinct values (e.g., long-tailed categories)
- **Audience:** Analysts browsing thumbnails

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user explicitly wants to enumerate categories (e.g., inspect all members) and has mechanisms to filter or page through results.
- **Reason:** Penalizing high-cardinality might hide a legitimate investigative need.

## The Price <!-- role: costs -->

- **The Sacrifice:** Some detailed breakdowns won’t be surfaced by default.
- **The Risk:** Users might miss rare-but-important categories unless they steer the system.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Automatically mapping any nominal field to color or facets regardless of distinct count.
- **Why it fails:** It yields charts that are hard to read and not scannable in a recommendation gallery [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Legends with too many entries or trellis grids that are huge and sparse.
- **The Test:** Count unique values; if the legend/trellis dominates the chart or becomes unreadable at thumbnail size, the mapping is inappropriate.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a cardinality-based penalty in the ranking score for color/shape/facets.
- **Best Fix:** Prefer aggregation, binning, or user-steered filtering before mapping high-cardinality fields to these channels [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
