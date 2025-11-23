---
id: simplify-map-legends
title: Simplify Map Legends for Readability
bibliography: references.bib
description: Design color keys to be quickly decipherable, showing extremes, centers,
  and consistent intervals.
labels:
- chart:map
- visual:legend
- impact:usability
- task:identify
---

## The Rule <!-- role: advice -->
Design color keys (legends) to be instantly decipherable.
*   For **Sequential**: Show lowest, highest, and 2-4 values in between.
*   For **Diverging**: Always display the center value.
*   Ensure values use consistent intervals (e.g., 0, 25, 50).

## The Logic <!-- role: reason -->
The key is the translator for the map. Overly complex or irregularly spaced keys confuse the reader. Consistent intervals in the key (0, 25, 50 vs 0, 13, 62) reduce cognitive load and make the scale easier to internalize [@muth_choroplethmaps_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Decoding the color values on the map.
*   **Data Type:** Any quantitative data mapped to color.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Quantile Scales.
*   **Reason:** If your map specifically uses quantiles (equal number of regions per color) rather than equal intervals, the legend numbers might be irregular, but this should be made clear.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You might have to round values in the legend, which is slightly less precise than the raw min/max of the data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Omitting the center value in a diverging scale.
*   **Why it fails:** Readers cannot locate the "neutral" or "zero" point.
*   **The Wrong Fix:** Showing only Min and Max.
*   **Why it fails:** Readers cannot estimate the non-linear distribution of colors in the middle.

## How to Check <!-- role: check -->
*   **The Test:** Look at the legend. Are the numbers easy to count by (e.g., by 10s, 25s, 100s)? If they are random (e.g., 4, 19, 77), the key is hard to read.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Round the values in your legend ticks to nice, readable numbers [@muth_choroplethmaps_2018].
