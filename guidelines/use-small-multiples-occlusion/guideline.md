---
id: use-small-multiples-occlusion
title: Use Small Multiples to Resolve Occlusion
bibliography: references.bib
description: Separate overlapping time-series into individual charts to improve legibility.
labels:
- chart:line
- chart:small-multiples
- visual:layout
- task:compare
- impact:clarity
---

## The Rule <!-- role: advice -->
When multiple time-series curves overlap and reduce legibility, use "small multiples" to show each series in its own chart rather than forcing them into a single plot.

## The Logic <!-- role: reason -->
Overlapping curves in a single space create visual clutter that obscures trends.
*   **The Principle:** Spatial Separation vs. Superposition
*   **The Evidence:** Placing multiple series in the same space can produce overlapping curves that reduce legibility. Separating them into standard small multiples allows for accurate observation of overall trends and seasonal patterns within each category without visual interference [@heer_tour_2010].

## Where to Apply <!-- role: context -->
*   **User Goal:** analyzing trends across many different categories simultaneously.
*   **Data Type:** Multiple time-series (e.g., unemployment by industry).
*   **Audience:** Analysts needing to see clear trends for individual categories.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When direct comparison of absolute magnitude at a specific time point is the primary task.
*   **Reason:** Superposition (single chart) is better for comparing the exact intersection points of two lines.

## The Price <!-- role: costs -->
*   **The Sacrifice:** It requires more screen space or results in smaller individual charts.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "spaghetti chart" with 10+ colored lines.
*   **Why it fails:** It becomes impossible to trace individual lines or identify distinct patterns.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are lines crossing over each other so frequently that you lose track of which color belongs to which label?
*   **The Test:** Can you instantly identify the seasonal peak of the third series without tracing it with your finger?

## How to Fix <!-- role: fix -->
*   **Best Fix:** Plot each category in a separate chart, but ensure they share the same axes scales for comparability [@heer_tour_2010].
