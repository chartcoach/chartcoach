---
id: position-labels-outside-pie
title: Label Small Slices Outside the Chart
bibliography: references.bib
description: Place labels for smaller slices outside the pie chart to accommodate
  long text and improve legibility.
labels:
- chart:pie
- visual:typography
- visual:position
- impact:legibility
---

## The Rule <!-- role: advice -->
Label smaller pie slices outside of the chart rather than inside the wedges.

## The Logic <!-- role: reason -->
Pie charts are notoriously hard to label because slices narrow toward the center. Placing labels outside is especially helpful when dealing with long labels that won't fit inside small colored areas [@muth_pie_charts_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Ensuring text is readable.
*   **Data Type:** Data with long category names or small percentages.
*   **Audience:** Any reader.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The slices are massive (e.g., 50/50 split).
*   **Reason:** There is ample room inside the slice, and placing it inside creates a cleaner silhouette.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The chart takes up more horizontal or vertical space to accommodate the external labels.
*   **The Risk:** The connection between label and slice might be lost if not properly aligned or linked.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Shrinking the font size to microscopic levels to fit text inside.
*   **Why it fails:** It makes the chart unreadable.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is text overlapping the edge of the chart or other text?
*   **The Test:** Can you read the label without zooming in?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Move the labels to the margin.
*   **Best Fix:** Use pointer lines or a connecting visual aid if the label is far from the slice [@muth_pie_charts_2018].
