---
id: avoid-area-charts-small-differences
title: Avoid Area Charts for Small Differences
bibliography: references.bib
description: Switch to line charts when value differences are subtle to allow axis
  truncation.
labels:
- chart:area
- chart:line
- data:quantitative
- visual:scale
- impact:accuracy
---

## The Rule <!-- role: advice -->
Do not use area charts if the differences between your values are very small. Use a line chart instead.

## The Logic <!-- role: reason -->
Area charts visualize volume, which necessitates that the y-axis starts at zero. Line charts visualize position and trend, allowing the axis to be truncated (zoomed in) to highlight small variances.
*   **The Principle:** Axis Scaling and Baseline Zero.
*   **The Evidence:** [@muth_area_charts_2018] notes that because area charts must start at zero, they cannot be stretched to show "tiny differences" effectively.

## Where to Apply <!-- role: context -->
*   **User Goal:** Highlighting subtle fluctuations or small performance gaps between categories.
*   **Data Type:** Time series data with low variance relative to the total magnitude.
*   **Audience:** Analysts looking for precise deviations.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** 100% Stacked Charts (sometimes).
*   **Reason:** If you are showing shares rather than absolute values, the full 0-100% scale is usually expected, though small changes remain hard to see.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The visual metaphor of "volume" or "total accumulation."
*   **The Risk:** Moving to a line chart with a truncated axis can exaggerate trends if not clearly labeled, though it is necessary for seeing small differences.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using an area chart but cutting the y-axis (not starting at zero).
*   **Why it fails:** This distorts the visual area, making the data ratio spatially incorrect. Area charts must start at zero [@muth_area_charts_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** The chart looks like flat, nearly parallel ribbons with no visible change.
*   **The Test:** Can you easily see the difference between time point A and B? If you have to squint, the scale is too compressed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the chart type to a Line Chart.
*   **Best Fix:** Use a Line Chart and adjust the y-axis range to encompass only the relevant data values (don't start at zero) to emphasize the variation.
