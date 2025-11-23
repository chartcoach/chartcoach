---
id: overlay-charts-for-magnitude-deltas
title: Overlay Charts to Compare Magnitude Changes
bibliography: references.bib
description: Superimpose data series to effectively identify maximum value changes.
labels:
- chart:bar
- chart:line
- chart:donut
- task:compare
- task:aggregate
- visual:position
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Superimpose comparative data series within the same coordinate space (overlaying them) rather than separating them into small multiples.

## The Logic <!-- role: reason -->
Placing data series on top of one another (superposition) significantly improves a user's ability to identify the "biggest mover" or maximum difference (delta) between the series. Empirical rankings show that overlaid designs consistently outperform juxtaposed designs (both stacked and adjacent) for identifying aggregate differences across bar charts, line charts, and donut charts.
*   **The Principle:** Just Noticeable Difference (JND) / Visual Scannability
*   **The Evidence:** In a review by [@zeng_review_2023] collating data from [@ondov_face_2019], overlaid designs (E-4, E-8, E-11) ranked highest for aggregate tasks across multiple chart types, showing significant performance benefits over separated layouts.

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying the largest change (delta) or difference between two datasets (e.g., "Which category grew the most?").
*   **Data Type:** Quantitative data series (Bar, Line, or Donut/Arc charts) sharing the same scale.
*   **Audience:** Analysts or general users needing to spot magnitude differences quickly.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The task is specifically to estimate the overall **correlation** between two bar chart series, rather than specific value changes.
*   **Reason:** Evidence from [@ondov_face_2019] indicates that mirrored layouts (E-3) can outperform overlaid layouts (E-4) specifically for correlation tasks in bar charts.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual clutter and potential occlusion if the data points overlap heavily without transparency (though the study used specific rendering to mitigate this).
*   **The Risk:** Users may struggle to read the exact value of the underlying layer if the top layer completely obscures it.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using vertically stacked small multiples (one chart above another).
*   **Why it fails:** Theoretical and experimental rankings consistently place stacked layouts (E-1) at the bottom for performance in finding value differences [@ondov_face_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the two series presented in separate frames (side-by-side or top-to-bottom)?
*   **The Test:** Can you see the gap between the two values directly, or does your eye have to jump between two different axes?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Move the second data series onto the same axis as the first.
*   **Best Fix:** Design an overlaid chart (e.g., bullet chart or multi-series line chart) where the shared axis eliminates the need for eye travel.
