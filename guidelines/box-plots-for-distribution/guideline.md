---
id: box-plots-for-distribution
title: Use Box Plots for Characterizing Distribution
bibliography: references.bib
description: Box plots outperform point, line, and color visualizations for characterizing
  the spread and distribution of data.
labels:
- chart:box-plot
- task:characterize-distribution
- visual:position
- visual:length
- data:statistical
- impact:clarity
---

## The Rule <!-- role: advice -->
Use Box Plots when the user needs to understand the spread, variance, or distribution of data over time.

## The Logic <!-- role: reason -->
Box plots visually abstract the data into summary statistics (IQR, median), allowing users to compare variance directly without processing individual data point positions.
*   **The Evidence:** The Box Plot (E-3) ranked #1 for the "characterize-distribution" task in the data collated by [@zeng_review_2023].
*   **The Comparison:** E-3 significantly outperformed the Composite Graph (E-4), Colorfield (E-5), and Line Graph (E-1) for this specific task [@albers_task-driven_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Assessing reliability, volatility, or consistency of a metric over time.
*   **Data Type:** Aggregated time-series data (e.g., daily distribution of hourly values).
*   **Audience:** Users with statistical literacy who understand quartiles and medians.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the audience is the general public or has low statistical literacy.
*   **Reason:** While not explicitly tested in this specific result set, box plots are often less intuitive to lay audiences than simple range bars or point clouds.
*   **Scenario:** When looking for anomalies.
*   **Reason:** Interestingly, while Box Plots show outliers, they were not the top performer for the "find-anomalies" task compared to Event Striping (E-7) [@albers_task-driven_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Temporal resolution of the underlying raw signal. Box plots aggregate data into bins (buckets), hiding the specific waveform of the time series.
*   **The Risk:** Misinterpretation of the "box" as a continuous block rather than a probability density.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a standard Line Graph (E-1) to judge spread.
*   **Why it fails:** Judging distribution from a line graph requires the user to visually integrate the "wiggle" of the line, which is cognitively demanding and less accurate than seeing the pre-calculated range of a box plot.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using a single line to represent data that varies significantly within the time step?
*   **The Test:** Ask, "Can the user tell if the data was tight or spread out on this specific day?" If the answer is no, apply a box plot or range encoding.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add error bars or specific range bars (Modified Stock Chart E-2).
*   **Best Fix:** Implement a full Box Plot (E-3) to show the Interquartile Range (IQR).
