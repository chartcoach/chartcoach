---
id: limit-area-charts-data-points
title: Use Stacked Columns for Few Dates
bibliography: references.bib
description: Use stacked column charts instead of area charts when there are fewer
  than ten dates.
labels:
- chart:area
- chart:bar
- data:temporal
- visual:density
- impact:readability
---

## The Rule <!-- role: advice -->
If you have fewer than ten dates (data points on the x-axis), consider using a stacked column chart instead of an area chart.

## The Logic <!-- role: reason -->
Area charts imply continuous change. When data points are sparse, the "slopes" between them can be misleading. Columns differ in how they handle labeling and distinct discrete values.
*   **The Principle:** Discrete vs. Continuous Representation.
*   **The Evidence:** [@muth_area_charts_2018] suggests that with fewer dates, labeling is improved in column charts, and readers have an easier time reading specific values.

## Where to Apply <!-- role: context -->
*   **User Goal:** Showing composition over a short period or specific intervals (e.g., annual reports for 5 years).
*   **Data Type:** Low-density time series (<10 points).
*   **Audience:** Readers who need to read exact values for specific years.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Irregular Intervals.
*   **Reason:** Column charts generally imply equal spacing. If your dates are 2017, 2030, 2050, and 2100, an area chart (which uses a continuous axis) will show the correct proportional distance between dates, whereas columns might not [@muth_area_charts_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** The "flow" aspect of the visualization.
*   **The Risk:** Columns can look cluttered if the gaps between them are too wide or too narrow relative to the data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Plotting 3 or 4 points as a jagged area chart.
*   **Why it fails:** It implies a trend knowledge between the points that doesn't exist and often looks visually awkward.

## How to Check <!-- role: check -->
*   **Visual Sign:** The area chart looks blocky, sharp-edged, or overly simple.
*   **The Test:** Count the x-axis labels. Are there fewer than 10?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the chart type to "Stacked Column."
*   **Best Fix:** Switch to Stacked Column and ensure direct labeling of the segments for better readability.
