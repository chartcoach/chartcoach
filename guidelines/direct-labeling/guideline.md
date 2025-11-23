---
id: direct-labeling
title: Label Data Directly
bibliography: references.bib
description: Place labels directly on lines or areas to eliminate the need for color
  legends.
labels:
- visual:text
- impact:readability
- impact:efficiency
- chart:line
- chart:pie
---

## The Rule <!-- role: advice -->
Remove separate color keys (legends) whenever possible. Place labels directly onto the lines, pie slices, or bar areas they describe.

## The Logic <!-- role: reason -->
Color keys are difficult for colorblind people to decipher because they require matching a small swatch in a legend to a shape in the chart (which may look different due to size). Direct labeling removes the cognitive task of color matching entirely [@muth_colorblindness_2020].
*   **The Principle:** Spatial Contiguity.
*   **The Evidence:** [@muth_colorblindness_2020] asserts that this tip "saves every one of your readers lots of time," not just those who are colorblind, by reducing eye travel.

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapid identification of data series.
*   **Data Type:** Line charts, area charts, pie charts.
*   **Audience:** All users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Highly clustered data points or lines that end at the exact same value.
*   **Reason:** There is physically no space for the text without overlapping.

## The Price <!-- role: costs -->
*   **The Sacrifice:** White space. Direct labels take up room on the canvas.
*   **The Risk:** Clutter if not managed well with leader lines.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a legend with very small color swatches.
*   **Why it fails:** Small areas of color are harder to distinguish than large areas.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the eye have to dart back and forth between the chart and a box on the side?
*   **The Test:** Remove the legend. Is the chart still readable? If yes, the legend was clutter. If no, add direct labels.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Move legend items to sit next to the end of the lines.
*   **Best Fix:** Use text labels matching the color of the data, positioned at the end of the series or on the largest segment of the area/pie.
