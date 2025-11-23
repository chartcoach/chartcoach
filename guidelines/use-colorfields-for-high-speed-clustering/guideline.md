---
id: use-colorfields-for-high-speed-clustering
title: Use Colorfields For High-Speed Time Series Scanning
bibliography: references.bib
description: Colorfields (1D heatmaps) allow for faster visual clustering of time
  series data compared to line charts or horizon graphs.
labels:
- chart:colorfield
- chart:heatmap
- task:cluster
- task:filter
- visual:color
- impact:speed
- data:time-series
---

## The Rule <!-- role: advice -->
Use colorfields (1D color density strips) rather than line charts or horizon graphs to maximize user speed when the task involves clustering or filtering time series based on general similarity.

## The Logic <!-- role: reason -->
Colorfields encode value intensity through color saturation or hue, reducing the visual signal to a single dense strip. This allows the eye to process aggregate patterns and "texture" more rapidly than tracking the positional path of a line chart. Empirical evidence reviewed by Zeng and Battle [@zeng_review_2023] indicates that colorfields outperformed both line charts and horizon graphs in task completion time for similarity searches, particularly when time-warping (non-linear alignment) was a factor [@gogolou_comparing_2019].

*   **The Principle:** Aggregate Pattern Perception
*   **The Evidence:** [@zeng_review_2023], [@gogolou_comparing_2019]

## Where to Apply <!-- role: context -->
*   **User Goal:** Triaging large datasets to find groups of similar behavior or outliers.
*   **Data Type:** High-frequency time series data where general morphology is more important than precise peak values.
*   **Audience:** Users needing to scan many data streams simultaneously (e.g., monitoring dashboards).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The users need to judge similarity based on precise amplitude (height) or vertical offsets.
*   **Reason:** Colorfields are less effective at communicating exact magnitudes or vertical shifts (Z-normalization invariance). In these cases, Line Charts perform equally well or better and offer more precision [@gogolou_comparing_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to read exact y-axis values.
*   **The Risk:** Users may perceive signals as "similar" because they share color density, even if the specific shape details (like sharp spikes vs. smooth hills) differ.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a rainbow color scale to add "precision" to the colorfield.
*   **Why it fails:** This introduces perceptual artifacts where changes in hue (e.g., yellow to green) are perceived as structural boundaries in the data that don't actually exist.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the visualization rely on a line tracing a path across time?
*   **The Test:** If you squint, can you still identify the "hot spots" or dense regions? If not, and you are using a line chart, consider converting to a colorfield for overview tasks.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Fill the area under the curve and reduce the height of the charts to create a "pseudo-colorfield."
*   **Best Fix:** Implement a true Colorfield using a single-hue or divergent color scale (e.g., Blue-White-Red) to map values directly to color intensity.
