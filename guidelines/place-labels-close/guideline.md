---
id: place-labels-close
title: Place Labels Close to Data
bibliography: references.bib
description: Label visual elements directly to avoid forcing the reader to use a legend.
labels:
- visual:text
- visual:layout
- impact:efficiency
- impact:accessibility
- task:identify
---

## The Rule <!-- role: advice -->
Place labels as close as possible to the visual element they represent, rather than using a distant legend.

## The Logic <!-- role: reason -->
Separating labels from data forces the eye to travel back and forth, increasing cognitive load.
*   **The Principle:** Spatial Contiguity.
*   **The Evidence:** [@muth_better_charts_2017] argues that "we want to save our readers' time and energy and therefore don't want them to travel far distances with the eye."

## Where to Apply <!-- role: context -->
*   **User Goal:** Quick identification of categories.
*   **Data Type:** Line charts, scatter plots, or bar charts with multiple categories.
*   **Audience:** All audiences, especially those with attention constraints.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** extremely high-density charts or small multiples where space is non-existent.
*   **Reason:** Direct labels might occlude the data itself.

## The Price <!-- role: costs -->
*   **The Sacrifice:** It consumes "white space" within the chart area that might otherwise be clean.
*   **The Risk:** If not placed carefully, labels can overlap data points.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a default separate box legend below or to the side of the chart.
*   **Why it fails:** It forces the user to look away from the data to understand it.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is there a box with colored squares and text separate from the chart?
*   **The Test:** Track your eye movement. If you look left-right-left to identify a line, the design needs fixing.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Move the legend text next to the ends of the lines.
*   **Best Fix:** Eliminate the legend entirely and place text labels directly on top of or adjacent to the visual elements (lines, bars) they describe [@muth_better_charts_2017].
