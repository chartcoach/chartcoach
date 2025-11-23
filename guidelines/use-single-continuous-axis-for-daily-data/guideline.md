---
id: use-single-continuous-axis-for-daily-data
title: Visualize 24-Hour Data on a Single Continuous Axis
bibliography: references.bib
description: A single 24-hour linear chart is more effective for identifying extrema
  than splitting data into two 12-hour charts.
labels:
- chart:bar
- task:find-extremum
- visual:position
- impact:efficiency
- data:temporal
- layout:juxtaposed
---

## The Rule <!-- role: advice -->
Plot 24-hour daily data on a single continuous axis rather than splitting it into juxtaposed 12-hour charts (AM/PM).

## The Logic <!-- role: reason -->
Splitting time series data into separate panels increases the cognitive load required to scan for global attributes.
*   **The Principle:** A single view eliminates the need for eye movements between separate charts to compare values or find a global maximum.
*   **The Evidence:** Experiments demonstrated that a single 24-hour linear chart (Design E-4) was significantly more efficient for finding the maximum value ("find-extremum" task) than juxtaposed 12-hour charts (Design E-3) [@waldner_comparison_2020]. The review of these findings highlights that while linear is generally better, the specific configuration of a single continuous axis yields the best results [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Finding the global maximum or minimum value in a day.
*   **Data Type:** Quantitative values distributed over a 24-hour period.
*   **Audience:** Users performing analysis tasks requiring a holistic view of the day.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Extreme horizontal space constraints.
*   **Reason:** If the display is too narrow to support 24 legible bars side-by-side, stacking two 12-hour charts might be necessary for readability, despite the performance cost.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Requires a wider aspect ratio to accommodate 24 bins comfortably.
*   **The Risk:** The chart may appear "wide" or "short" depending on the available screen real estate.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Splitting the chart into AM and PM rows to save horizontal space.
*   **Why it fails:** This forces the user to mentally integrate two separate visualizations to find the highest peak, slowing down the "find extremum" task [@waldner_comparison_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there two separate X-axes (one for AM, one for PM) or two separate clusters of bars?
*   **The Test:** Trace the path from 11:00 AM to 1:00 PM. If the eye has to jump to a different location or graph, the axis is not continuous.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Combine the data arrays and render them on one x-axis from 0 to 23.
*   **Best Fix:** Ensure the aspect ratio allows for a single linear bar chart spanning the full 24-hour cycle.
