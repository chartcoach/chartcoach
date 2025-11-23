---
id: increase-color-contrast-small-marks
title: Increase Color Contrast Steps for Small Marks
bibliography: references.bib
description: Small visualization marks require significantly larger color differences
  to be distinguishable compared to large patches.
labels:
- visual:color
- visual:size
- chart:scatterplot
- task:cluster
- impact:clarity
- data:nominal
---

## The Rule <!-- role: advice -->
Increase the perceptual distance (step size) between colors when mapping data to small or thin marks, such as scatterplot points or thin lines. Do not rely on standard color palettes designed for large maps or areas.

## The Logic <!-- role: reason -->
Perceived color difference varies inversely with mark size. As the size of a visual mark decreases, the human ability to discriminate between colors drops significantly.
*   **The Principle:** Size-Dependent Color Perception.
*   **The Evidence:** Research by Szafir shows that a 2° visual angle (standard color science patch) is insufficient for modeling visualization marks. A 0.5° scatterplot point requires a color difference ($\Delta E$) roughly 3 times larger than a large patch to be equally distinguishable [@szafir_modeling_2018]. This relationship is fundamental to the collation of graphical perception knowledge [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Distinguishing between categories (clusters) or reading specific values encoded by color.
*   **Data Type:** High-density datasets visualized with small geometries.
*   **Chart Types:** Scatterplots, thin line charts, or high-density dot plots.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Large Area Visualizations.
*   **Reason:** If the visualization uses large filled areas (e.g., heatmaps with large cells, bar charts with wide bars, or choropleth maps), the marks are large enough that standard color difference metrics (like CIELAB) are accurate, and subtle differences are perceptible [@szafir_modeling_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Reduced Encoding Capacity.
*   **The Risk:** By requiring larger differences between colors, you fit fewer distinct categories into the visualization before the colors become indistinguishable or the palette becomes garish.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using default "print" or "map" palettes (like standard ColorBrewer classes) on scatterplots.
*   **Why it fails:** Szafir found that 13 of 18 ColorBrewer sequential ramps failed to provide sufficient discriminability when applied to standard scatterplot point sizes (10px) [@szafir_modeling_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Adjacent categories in a scatterplot look identical or "blend" together when not directly adjacent.
*   **The Test:** Check the mark diameter. If points are small (e.g., <10px), verify if the color difference ($\Delta E$) is significantly higher than standard Just Noticeable Difference (JND) thresholds.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the point size (radius) of the marks.
*   **Best Fix:** Select a high-contrast palette specifically tuned for small marks, or reduce the number of color categories to allow for larger perceptual steps between them.
