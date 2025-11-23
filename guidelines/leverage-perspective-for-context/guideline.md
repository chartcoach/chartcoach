---
id: leverage-perspective-for-context
title: Leverage Perspective as a Log-Like Scale
bibliography: references.bib
description: Use 3D perspective to create a single view that combines foreground detail
  (focus) with background history (context).
labels:
- chart:timeseries
- chart:bar
- visual:perspective
- task:monitor
- data:temporal
- impact:efficiency
---

## The Rule <!-- role: advice -->
Tilt time-series or bar charts in 3D to allocate more screen space to recent data (foreground) while compressing historical data (background).

## The Logic <!-- role: reason -->
Linear perspective naturally compresses distant objects, acting as a **visual log transformation** or a "focus + context" lens.
*   **The Principle:** **Perspective foreshortening**. Objects closer to the viewer appear larger, allowing detailed examination of recent performance, while distant objects provide the necessary long-term trend without consuming equal pixel space.
*   **The Evidence:** [@brath_3d_2014] illustrates that a tilted time series can show distinct daily movements in the foreground (with "30 times the 2D area") while simultaneously showing the long-term trend in the background. This potentially improves cognitive performance by eliminating the need to cross-reference separate "zoom" and "overview" charts.

## Where to Apply <!-- role: context -->
*   **User Goal:** Monitoring current performance in the context of long-term history.
*   **Data Type:** Long time series or wide-variation datasets.
*   **Audience:** Traders, dashboard monitors, or decision-makers needing immediate status updates without losing historical context.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Precise comparison between historical values and current values is required.
*   **Reason:** Perspective distorts size constancy. You cannot easily compare the height of a bar in the foreground to one in the background [@brath_3d_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Dimensional accuracy for distant data points.
*   **The Risk:** Users may perceive the chart as "chart junk" if the utility of the perspective compression is not explained or obvious.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Creating two separate charts (one zoomed in, one zoomed out).
*   **Why it fails:** This forces the user to visually switch back and forth (cross-referencing), increasing cognitive load compared to a single integrated view [@brath_3d_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are older data points taking up as much pixel space as the critical new data?
*   **The Test:** Check if you can see the "daily noise" in the data from 3 years ago. If you can, and you don't need to, you are wasting screen space.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Tilt the camera so the "current" data is closest to the viewport.
*   **Best Fix:** Adjust the field of view (FOV) to exaggerate the perspective, ensuring the foreground is large and readable while the background recedes significantly.
