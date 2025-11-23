---
id: ensure-equal-intervals-time-series
title: Ensure Equal Time Intervals for Stacked Columns
bibliography: references.bib
description: Avoid using stacked column charts for time series data if the dates have
  irregular intervals.
labels:
- chart:stacked-column
- data:temporal
- visual:distortion
- impact:accuracy
---

## The Rule <!-- role: advice -->
Only use stacked column charts for time data if your dates have exactly the same intervals (e.g., every year, every month). If intervals vary, use a chart with a continuous x-axis.

## The Logic <!-- role: reason -->
Column charts typically use discrete x-axes (ordinal or categorical). If you plot data with irregular gaps (e.g., 2010, 2011, 2015) as columns, they will appear visually equidistant. This distorts the perception of time and trends. Area charts or line charts possess continuous scales that correctly visualize the distance between different date intervals [@muth_stacked_columns_2018].

## Where to Apply <!-- role: context -->
*   **Data Type:** Time series data.
*   **Constraint:** Gaps in data collection or irregular reporting periods.
*   **Chart Type:** Stacked Column Chart.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The x-axis treats the events as categorical "Instances" rather than a timeline.
*   **Reason:** If the time delta is irrelevant to the analysis (e.g., comparing "First Attempt" vs "Second Attempt" regardless of when they happened).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Switching to a line or area chart might make it slightly harder to compare the cumulative totals of specific points compared to stacked columns.
*   **The Risk:** Using columns for irregular dates lies to the reader about the rate of change.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding empty columns for missing years to "pad" the spacing.
*   **Why it fails:** It creates visual noise and clutter.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the x-axis labels.
*   **The Test:** Calculate the difference between adjacent labels. Is it constant? (e.g., $t_2 - t_1 = t_3 - t_2$). If not, the chart is misleading.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the visualization type to an Area Chart or Line Chart.
*   **Best Fix:** Use an Area Chart if the comparison of the *total* volume over time is important, as it maintains the stacking metaphor on a continuous axis.
