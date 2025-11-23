---
id: optimize-nominal-color-hue
title: Maximize Perceptual Distance in Nominal Color Palettes
bibliography: references.bib
description: Optimize categorical color hues to ensure maximum discriminability between
  data classes.
labels:
- visual:color
- data:categorical
- impact:clarity
- task:distinguish
- chart:scatter
- chart:bar
---

## The Rule <!-- role: advice -->
Select color hues for nominal data that maximize the perceptual distance between every pair of categories, rather than relying on default or aesthetically chosen palettes.

## The Logic <!-- role: reason -->
Effective visualization of nominal data relies on the user's ability to distinguish between different categories purely through color.
*   **The Evidence:** In their review of graphical perception knowledge, Zeng and Battle [@zeng_review_2023] highlight that automated recommendation systems (like Voyager) can be improved by ingesting optimized palettes from experimental literature. They cite Fang et al. [@fang_categorical_2017], who demonstrate that algorithmically optimizing colormaps to maximize the minimal distance (using the CIEDE2000 metric) between colors significantly improves perceptual differentiation while maintaining necessary semantic constraints.

## Where to Apply <!-- role: context -->
This rule applies to visualizations mapping **nominal** (categorical) data to the **color hue** channel.
*   **User Goal:** Differentiating between distinct groups or classes (e.g., species in a scatterplot, lines on a metro map).
*   **Data Type:** Categorical/Nominal data with no inherent order.
*   **Audience:** Users who need to rapidly identify and separate groups within a dense dataset.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Visualizing Ordinal or Quantitative Data.
*   **Reason:** Nominal optimization focuses on distinctness (hue variation). Ordinal data requires a perceptual ordering (often luminance or saturation ramps), which purely distinct hues may obscure.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Semantic associations (e.g., "forests must be green") or brand consistency may be compromised if the optimization algorithm is not constrained to specific hue ranges.
*   **The Cost:** Generating an optimal palette requires computational effort (optimization algorithms) compared to picking a static list.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Selecting colors that look distinct in RGB space but are perceptually similar in human vision.
*   **Why it fails:** As noted by Fang et al. [@fang_categorical_2017], standard color spaces do not align with human perception; perceptually uniform metrics (like CIEDE2000) are required for true optimization.

## How to Check <!-- role: check -->
*   **Visual Sign:** Two or more categories look similar, or a category blends into the background color.
*   **The Test:** Check the perceptual distance ($D_{min}$) between the closest pair of colors. If they are difficult to distinguish at a glance, the palette has failed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use a pre-optimized categorical palette (e.g., from ColorBrewer or the palettes suggested in [@fang_categorical_2017]).
*   **Best Fix:** Run a constrained optimization algorithm (like a genetic algorithm) to generate a palette that maximizes separation for your specific number of data classes.
