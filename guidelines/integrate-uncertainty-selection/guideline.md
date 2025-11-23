---
id: integrate-uncertainty-selection
title: Select by Integrating Probability Density
bibliography: references.bib
description: When brushing uncertain data, use probability integration rather than
  simple geometric containment.
labels:
- chart:interaction
- task:select
- task:brush
- data:uncertain
- impact:accuracy
---

## The Rule <!-- role: advice -->
When a user selects a region (brushes) on a plot of uncertain data, calculate the integral of each data point's probability density function (PDF) within the selection bounds. Select the data point only if the probability contained within the brush exceeds a high threshold (e.g., 95%).

## The Logic <!-- role: reason -->
In uncertain data, a point is not a singularity; it is a distribution with infinite extent.
*   **The Principle:** Statistical Significance.
*   **The Evidence:** [@feng_matching_2010] argues that a simple "inside/outside" test is invalid because the distribution spills out of the selection box. Integrating the PDF ensures the viewer selects the data only when the brush covers the meaningful bulk of the distribution, forcing the user to use larger brushes for more uncertain data.

## Where to Apply <!-- role: context -->
*   **User Goal:** Filtering or highlighting subsets of data.
*   **Data Type:** Data with modeled statistical uncertainty (e.g., Normal distributions).
*   **Audience:** Interactive visualization users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Real-time interaction on low-power devices with massive datasets.
*   **Reason:** Numerical integration (or Error Function lookups) for every point per frame can be computationally expensive compared to simple geometric collision detection.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Interaction speed (potential lag).
*   **The Risk:** Users may be confused why a point that visually appears "inside" the box is not selected (because the brush didn't capture enough of its wide distribution).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Expanding the brush box by a fixed pixel amount.
*   **Why it fails:** This assumes uniform uncertainty across all data points.
*   **The Wrong Fix:** Selecting if *any* part of the distribution touches the brush.
*   **Why it fails:** This leads to massive over-selection of irrelevant, uncertain data.

## How to Check <!-- role: check -->
*   **Visual Sign:** Draw a small box inside a large, blurry (uncertain) data point.
*   **The Test:** If the point is selected despite the box only covering a small fraction of the blur, the rule is broken. The point should only select when the box covers ~95% of the visible blur.

## How to Fix <!-- role: fix -->
*   **Best Fix:** For normal distributions, use the error function (`erf`) to calculate the area under the curve within the selection bounds. Set a selection threshold of $A > 0.95$.
