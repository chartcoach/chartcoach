---
id: maintain-chronological-axes
title: Sort Time-Series Chronologically
bibliography: references.bib
description: Prevent misleading trend interpretation by ensuring time-based axes follow
  chronological order, not magnitude.
labels:
- chart:bar
- data:temporal
- visual:position
- impact:accuracy
- task:identify-trend
---

## The Rule <!-- role: advice -->
Always order time-based axes chronologically. Never sort data points by magnitude (e.g., highest to lowest) when the x-axis represents time or dates.

## The Logic <!-- role: reason -->
Readers instinctively interpret the x-axis as a timeline. When data is sorted by magnitude instead of time, users incorrectly interpret the resulting slope as a temporal trend (e.g., "cases are decreasing") rather than a distribution of magnitudes. Chronological ordering also allows users to identify complex distribution shapes, such as bi-modality, which are destroyed by magnitude sorting.
*   **The Principle:** Temporal spatial mapping.
*   **The Evidence:** In a study of COVID-19 charts, participants viewing a magnitude-sorted chart incorrectly classified the trend as decreasing, whereas those viewing the chronological redesign correctly identified the bi-modal shape of the data [@burns_how_2020].

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying trends, patterns, or distribution shapes over time.
*   **Data Type:** Time-series data, specifically bar charts representing counts per day or week.
*   **Audience:** General public and policy makers.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Pareto Analysis.
*   **Reason:** If the explicit goal is to identify the "top N" days regardless of when they occurred, and the axis is clearly labeled as categorical ranks rather than a timeline.

## The Price <!-- role: costs -->
*   **The Sacrifice:** It becomes harder to instantly identify exactly which specific date had the absolute highest or lowest value without scanning the entire chart.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Sorting bars by height to make the chart look "cleaner" or to highlight the worst days first.
*   **Why it fails:** It creates an "illusion of causality" or a false trend (e.g., a smooth downward curve) that does not exist in reality [@burns_how_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Check the axis labels. Are the dates jumping around (e.g., May 2nd, then April 28th)?
*   **The Test:** Ask a user to describe the "trend." If they describe a monotonic increase or decrease, but the dates are scrambled, the design is misleading.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Re-sort the dataset by the date column before plotting.
*   **Best Fix:** Ensure the x-axis is explicitly typed as a continuous date/time field in your visualization tool to force chronological ordering.
