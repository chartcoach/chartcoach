---
id: limit-total-colors
title: Minimize Total Color Count
bibliography: references.bib
description: Reduce the number of colors to 3 or 4 to prevent cognitive overload for
  colorblind readers.
labels:
- visual:color
- impact:clarity
- impact:accessibility
- custom:cognitive-load
---

## The Rule <!-- role: advice -->
Limit your palette to three or four colors maximum. If you have more categories, group less important ones together or use non-color cues.

## The Logic <!-- role: reason -->
The more colors used, the harder they are to distinguish for everyone, but the difficulty scales disproportionately for colorblind users.
*   **The Principle:** Cognitive Load reduction.
*   **The Evidence:** Green-blind data analyst Lee Durbin states in [@muth_colorblindness_2020] that seeing more than 3 or 4 colors causes him to "tune out" unless other indicators are present.

## Where to Apply <!-- role: context -->
*   **User Goal:** Quick scanning and category identification.
*   **Data Type:** Categorical data with many items (e.g., a pie chart with 10 slices).
*   **Audience:** Busy readers or those with vision deficiencies.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** A continuous heatmap or complex choropleth map.
*   **Reason:** These rely on gradients rather than distinct categorical hues.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to assign a unique identity to every single minor category.
*   **The Risk:** Grouping data into "Others" might hide specific, smaller insights.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assigning 10 different distinct hues to a bar chart.
*   **Why it fails:** It creates a "confetti" effect where distinguishing between "shade of blue #3" and "shade of purple #2" becomes impossible.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you relying on a legend with more than 5 items?
*   **The Test:** Count the distinct hues. If >4, ask if all are necessary.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Color only the most important values/categories and turn everything else gray.
*   **Best Fix:** Switch the chart type to one that labels data directly (like a bar chart) so color is not the primary identifier [@muth_colorblindness_2020].
