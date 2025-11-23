---
id: use-diverging-scales-for-high-freq-patterns
title: Use Diverging Colormaps for Complex Patterns
bibliography: references.bib
description: For identifying structures or gradients in high-frequency (noisy) spatial
  data, diverging colormaps perform best.
labels:
- chart:continuous-map
- task:correlate
- task:aggregate
- visual:color-diverging
- data:spatial-frequency
- complexity:high
---

## The Rule <!-- role: advice -->
Apply diverging colormaps (such as Coolwarm or Spectral) when visualizing continuous maps containing high spatial frequency or "noisy" data, specifically for tasks involving pattern recognition or gradient comparison.

## The Logic <!-- role: reason -->
Complex spatial data requires high "perceptual resolution" to resolve shapes and structures.
*   **The Principle:** Shape-from-Shading. Diverging scales often vary luminance in two directions (e.g., dark-light-dark or distinct hue-divergence), which assists the visual system in resolving high-frequency textures and gradients.
*   **The Evidence:** Zeng and Battle [@zeng_review_2023] synthesized findings showing that for "aggregate" and "correlate" tasks on high-frequency data (labeled Aggregate-2 and Correlate-2 in the dataset), diverging scales like Coolwarm (E-6) and Spectral (E-7) significantly outperformed sequential scales. Reda et al. [@reda_graphical_2018] specifically note that these schemes provide "maximal perceptual resolution."

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying structures, gradients, clusters, or matching terrain profiles (Pattern Perception).
*   **Data Type:** High spatial frequency data (e.g., rugged terrain maps, noisy sensor data, complex medical imaging).
*   **Audience:** Analysts looking for anomalies or structural correlations in dense data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data has very low spatial frequency (smooth, broad variations).
*   **Reason:** In low-frequency conditions (Aggregate-1), the evidence shows no significant performance difference between colormaps. A simple sequential scale may be aesthetically preferable.
*   **Scenario:** The data does not have a meaningful midpoint (e.g., zero or average).
*   **Reason:** Diverging scales imply a critical center point; applying them to strictly positive sequential data can be misleading.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Simplicity. Diverging scales are more complex to interpret if the center point is arbitrary.
*   **The Risk:** Misinterpretation of the "neutral" color (often white or gray) as "no data" rather than a median value.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "Spiral" or "Cubehelix" scheme for high-frequency pattern tasks.
*   **Why it fails:** Despite being theoretically sound for monotonicity, Reda et al. [@reda_graphical_2018] found these performed poorly for resolving fine details in complex maps compared to diverging schemes.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the map look like "static" or noise where you expect to see structure?
*   **The Test:** Calculate the spatial frequency or entropy of the image. If high, check if the colormap is Sequential.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Swap a sequential scale (e.g., Blues) for a diverging one (e.g., Red-Blue) centered on the data mean.
*   **Best Fix:** Use the "Coolwarm" colormap, which was the top-performing design for high-frequency gradient and pattern tasks in the source experiments [@reda_graphical_2018].
