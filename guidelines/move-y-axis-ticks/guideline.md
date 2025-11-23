---
id: move-y-axis-ticks
title: Move Axis Ticks to the Data
bibliography: references.bib
description: Move axis labels to the right (or top) if that is where the important
  data ends.
labels:
- visual:position
- chart:line
- visual:layout
---

## The Rule <!-- role: advice -->
Move your axis labels to the other side of the chart (from left to right, or bottom to top) if those regions contain the relevant data points.

## The Logic <!-- role: reason -->
Placing axis ticks closer to the data points they measure makes it easier for the eye to estimate values. For example, if a line chart ends on the right side, placing the Y-axis on the right allows readers to quickly verify the final value without scanning back across the entire chart width [@muth_text_in_data_visualizations_2022].

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating the value of the most recent data point.
*   **Data Type:** Line charts or time series where the latest data is on the right.
*   **Audience:** General readers.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the user's primary goal is to compare the *start* of the trend (left side) rather than the end.
*   **Reason:** Proximity should prioritize the most important data region.

## The Price <!-- role: costs -->
*   **The Sacrifice:** It breaks the convention of the "standard" left-aligned Y-axis.
*   **The Risk:** Readers conditioned to look left might momentarily search for the scale.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** keeping the axis on the left but drawing long gridlines across the whole chart.
*   **Why it fails:** While helpful, the eye still has to travel the full width of the chart to match the line to the number.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is there a large gap between your data and your axis labels?
*   **The Test:** Look at the last data point. How far do you have to move your eye to find the number it corresponds to?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** In chart settings, switch Y-axis position to "Right."
