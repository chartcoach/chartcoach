---
id: scaffold-complexity
title: Increase Chart Complexity Progressively
bibliography: references.bib
description: Don't start with complex scatter plots. Introduce simple charts first
  to teach the reader how to read the data.
labels:
- chart:scatter
- chart:line
- visual:complexity
- impact:storytelling
- audience:novice
---

## The Rule <!-- role: advice -->
Do not immediately present complex charts (like scatter plots or 2D histograms) to a general audience. Instead, introduce the topic with simple visualizations first, and increase complexity step-by-step.

## The Logic <!-- role: reason -->
Complex charts can feel overwhelming to readers. By "scaffolding" the information—starting with a simple line chart, moving to an arrow plot, and finally showing the scatter plot—you ensure readers understand the context. Even if they don't "make it all the way to the last chart," they will have grasped the main message from the simpler versions [@muth_chart_types_guide_2025].

## Where to Apply <!-- role: context -->
*   **User Goal:** Explaining a complex relationship (correlation) or high-dimensional data.
*   **Data Type:** Correlations, multi-variable datasets (e.g., CO2 emissions vs time vs country).
*   **Audience:** Mainstream audience or readers unfamiliar with statistical plots.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The audience consists of experts or scientists.
*   **Reason:** They likely possess the "science-y" literacy to read scatter plots or heatmaps immediately without the intro [@muth_chart_types_guide_2025].

## The Price <!-- role: costs -->
*   **The Sacrifice:** It takes more space and time to tell the story because you are creating a sequence of charts instead of just one.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing a dense scatter plot immediately and relying on a text caption to explain it.
*   **Why it fails:** Readers may tune out before reading the caption because the visual is "overwhelming" [@muth_chart_types_guide_2025].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is your first chart a scatter plot with many dots?
*   **The Test:** Show the chart to a non-expert. Do they look confused? If yes, break it down.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Break the visualization into a sequence: 1. Simple trend (Line), 2. Specific comparison (Arrow/Slope), 3. Full context (Scatter).
