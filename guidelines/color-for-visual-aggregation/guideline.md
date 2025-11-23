---
id: color-for-visual-aggregation
title: Use Color for Visual Aggregation Tasks
bibliography: references.bib
description: When explicit statistical encoding is not possible, color encodings support
  average estimation better than position encodings.
labels:
- chart:heatmap
- chart:colorfield
- task:summarize
- visual:color
- data:timeseries
---

## The Rule <!-- role: advice -->
When you cannot explicitly compute and plot a summary statistic (e.g., due to space or unknown tasks), use color encodings (like colorfields) rather than position encodings (line charts) to help users estimate averages over a range.

## The Logic <!-- role: reason -->
The human visual system can preattentively summarize color over a region (ensemble statistics) more effectively than it can average positional variance in a noisy line.
*   **The Principle:** Ensemble Statistics / Preattentive Summarization.
*   **The Evidence:** [@albers_task-driven_2014] found that standard Colorfields outperformed Line Graphs for the task of identifying the month with the highest average sales, as the color encoding allows viewers to make judgments over a field.

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating the "average" or general state of a dense time series.
*   **Data Type:** High-frequency time series where a line chart would suffer from extreme jitter or overplotting.
*   **Audience:** Users looking for trends and heat-maps rather than exact values.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to compare values with high precision.
*   **Reason:** Color has low perceptual fidelity for point comparison. If precision is required, position is superior.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to see exact peaks, valleys, and shapes of the data.
*   **The Risk:** Color perception is non-linear; users may misinterpret the magnitude of differences compared to positional length.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a line chart for very dense data (e.g., pixel-wide data points).
*   **Why it fails:** The visual noise ("hairiness") of the line makes it difficult for the eye to estimate the center of mass (average).

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the line chart so jagged that it looks like a solid block of ink?
*   **The Test:** Squint at the chart. If the line chart just looks like a fuzzy blur, a colorfield might provide a cleaner summary of the density/average.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Convert the dense line chart into a 1D heatmap (colorfield).
*   **Best Fix:** Use "Color Weaving" or similar high-density techniques if preserving some distributional information is required.
