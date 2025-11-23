---
id: emphasize-distribution-means
title: Emphasize Means in Density Plots
bibliography: references.bib
description: Brighten the centers of distributions to maintain pattern visibility
  in density plots.
labels:
- chart:scatter
- chart:parallel-coordinates
- visual:intensity
- impact:readability
- data:uncertain
- task:locate
---

## The Rule <!-- role: advice -->
When rendering density plots of uncertain data, artificially scale the intensity of the distribution's mean (center) to be brighter than the rest of the distribution.

## The Logic <!-- role: reason -->
While pure density plots are statistically accurate, they can make individual values difficult to distinguish and cause outliers to fade too much.
*   **The Principle:** Dual-frequency visual processing.
*   **The Evidence:** [@feng_matching_2010] suggests that scaling the mean introduces a "discrete, identifiable feature" that remains visible even within the blur of uncertainty. This allows the viewer to see the scale of the distribution (the blur) and the location of the data (the bright center) simultaneously.

## Where to Apply <!-- role: context -->
*   **User Goal:** Recovering the location of individual data points within a density plot.
*   **Data Type:** Small to medium datasets where distinct items still matter, but uncertainty needs to be shown.
*   **Audience:** Users who are familiar with standard scatter plots and need a bridge to density visualization.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Extremely large datasets (Massive overplotting).
*   **Reason:** If thousands of means overlap, the benefit of emphasis is lost, and the plot simply becomes a standard density map.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Statistical purity.
*   **The Risk:** The visualization no longer perfectly represents the Probability Density Function (PDF) because the peaks are artificially heightened for legibility.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Drawing an opaque dot over a transparent shape.
*   **Why it fails:** This occludes the density information underneath and re-introduces the clutter of standard scatter plots.

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you identify the center of a blurry blob?
*   **The Test:** Look at a single uncertain data point. It should look like a "star" or a "glow" with a hot core, rather than a flat, uniform cloud.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Overlay a semi-transparent point at the exact coordinates of the data sample on top of the density rendering.
*   **Best Fix:** Modify the pixel shader or rendering algorithm to multiply the intensity at the center of the kernel by a constant factor before accumulation.
