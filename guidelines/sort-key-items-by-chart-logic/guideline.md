---
id: sort-key-items-by-chart-logic
title: Sync Key Order with Chart Order
bibliography: references.bib
description: Order color key items to match the visual arrangement or hierarchy of
  the data in the chart.
labels:
- visual:order
- visual:legend
- impact:cognition
- data:categorical
---

## The Rule <!-- role: advice -->
Sort the items in your color key to match the order they appear in the visualization (e.g., biggest to smallest) or their natural logical order.

## The Logic <!-- role: reason -->
Readers reading left-to-right naturally look for the top-left chart element first; the key should reflect this expectation. If categories have different sizes (like in a pie chart or bubble chart), listing the "biggest" category first in the key reduces search time. If data has a natural order (e.g., "Left, Center, Right" or "2015, 2020, 2025"), the key must respect it to avoid confusion [@muth_color_keys_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Quickly finding the label for the most prominent data points.
*   **Data Type:** Pie charts, bubble charts, categorical choropleth maps, or stacked bars.
*   **Audience:** All audiences.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Alphabetical requirements.
*   **Reason:** If the user effectively uses the key as a dictionary to look up specific known terms (e.g., a list of 50 states), alphabetical sorting is superior to data-driven sorting.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Flexibility. You may need to manually reorder the key if the data changes.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Defaulting to alphabetical sorting for nominal categories like "Democrats" and "Republicans" when the chart is ordered by vote share.
*   **Why it fails:** It disconnects the visual hierarchy from the textual hierarchy.

## How to Check <!-- role: check -->
*   **Visual Sign:** The largest slice in the pie chart is blue, but the blue item is buried at the bottom of the legend.
*   **The Test:** Check the top-left or largest element in your chart. Is it the first item in your key?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually drag legend items to match the visual magnitude of the data.
*   **Best Fix:** Sort the underlying data by value (descending) so the legend and chart automatically synchronize.
