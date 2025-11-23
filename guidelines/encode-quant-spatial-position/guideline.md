---
id: encode-quant-spatial-position
title: Encode Numerical Data Using Spatial Position
bibliography: references.bib
description: Prioritize spatial position over other visual channels for accurate numerical
  decoding.
labels:
- chart:bar
- chart:scatter
- chart:line
- visual:position
- impact:accuracy
- data:numerical
---

## The Rule <!-- role: advice -->
Map your most important numerical data to spatial position (x, y coordinates) rather than visual variables like angle, area, volume, or color saturation.

## The Logic <!-- role: reason -->
Research in graphical perception demonstrates that the human visual system decodes spatial position more accurately than other visual attributes.
*   **The Principle:** Graphical Perception Accuracy
*   **The Evidence:** Experiments by psychologists and statisticians confirm that position leads to the most accurate decoding of numerical data compared to angle, length, area, volume, and color [@heer_tour_2010].

## Where to Apply <!-- role: advice -->
*   **User Goal:** When the viewer needs to read values precisely or compare magnitudes accurately.
*   **Data Type:** Quantitative (Numerical) data.
*   **Audience:** Any audience requiring precise data interpretation.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When visualizing geographical data (Maps).
*   **Reason:** Position is constrained by geography (latitude/longitude), requiring the use of other channels like color (choropleth) or size (graduated symbols) to encode data values [@heer_tour_2010].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Spatial position consumes the primary layout dimensions of the canvas, limiting the number of variables that can be encoded on shared axes compared to compact forms like color matrices.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using color saturation to encode primary numerical values in a non-spatial chart.
*   **Why it fails:** The eye is less sensitive to differences in saturation than differences in position [@heer_tour_2010].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using the x or y axis to represent categories while using bubble size or color shade to represent the main number?
*   **The Test:** Try to read the specific value of a data point. If you have to reference a color legend or estimate the area of a circle, you are not using position.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add labels to the non-positional elements to aid reading.
*   **Best Fix:** Switch to a bar chart, line chart, or scatter plot where the value directly determines the coordinate [@heer_tour_2010].
