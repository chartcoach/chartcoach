---
id: small-multiples-for-spatio-temporal-clustering
title: Prioritize Small Multiples for Spatio-Temporal Clustering
bibliography: references.bib
description: Small multiples allow for faster identification of clusters and distributions
  over time.
labels:
- chart:small-multiples
- chart:glyph-map
- task:cluster
- task:distribution
- data:spatio-temporal
- impact:efficiency
---

## The Rule <!-- role: advice -->
Use **Small Multiples** rather than superimposed Glyph Maps when the analysis task involves identifying clusters or characterizing the distribution of values over space and time.

## The Logic <!-- role: reason -->
Statistical analysis of user performance indicates that Small Multiples are significantly faster than Glyph Maps for high-level pattern recognition tasks like clustering and characterizing distributions. The spatial juxtaposition allows users to see the "shape" of the data evolving, whereas glyphs require localized serial processing.
*   **The Evidence:** Small Multiples (E-1) were found to be significantly faster than Glyph Maps (E-2) for `cluster` and `characterize-distribution` tasks [@zeng_review_2023; @pena-araya_comparison_2020].

## Where to Apply <!-- role: context -->
*   **User Goal:** Recognizing broad patterns, such as groups of regions behaving similarly or understanding the overall spread of data values.
*   **Data Type:** Quantitative data distributed across geographical regions and time steps.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The display medium is extremely small (e.g., a smartwatch or very small mobile view).
*   **Reason:** Small multiples may become illegible if the individual maps shrink beyond the point where regions are distinguishable.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Detail visibility. You trade the ability to see fine-grained local details (which a large single map offers) for a better global overview of temporal evolution.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Overloading a single map with proportional symbols (circles, bars) to show history.
*   **Why it fails:** Users struggle to mentally integrate the spatial distribution of these symbols into a coherent cluster; the "forest" is lost for the "trees."

## How to Check <!-- role: check -->
*   **Visual Sign:** If you are using a single map, are there overlapping symbols that obscure the underlying geography?
*   **The Test:** Can a user identify "which regions group together" in under 5 seconds?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If you must use a single map, ensure glyphs are minimal and do not overlap.
*   **Best Fix:** Switch to a Small Multiples layout (grid) where each cell represents a time step, maintaining constant geographic boundaries.
