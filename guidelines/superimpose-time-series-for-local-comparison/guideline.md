---
id: superimpose-time-series-for-local-comparison
title: Superimpose Time Series for Local Value Comparisons
bibliography: references.bib
description: Use shared-space line charts or braided graphs when users need to compare
  values at specific time points.
labels:
- chart:line-chart
- chart:braided-graph
- task:compare
- task:find-extremum
- visual:position
- data:temporal
- impact:efficiency
---

## The Rule <!-- role: advice -->
Superimpose multiple time series in a shared coordinate space (such as a standard multi-line chart or braided graph) when the primary task is finding specific values or comparing magnitudes at a single point in time.

## The Logic <!-- role: reason -->
Shared-space techniques reduce the distance the eye must travel to compare vertical positions. When series are overlaid, the visual comparison is immediate and local.
*   **The Principle:** Local Visual Span optimization.
*   **The Evidence:** Research by Javed et al. [@javed_graphical_2010] demonstrates that shared-space techniques (Simple Line Graphs and Braided Graphs) significantly outperform split-space techniques (Small Multiples and Horizon Graphs) in completion time for "Maximum" (find extremum) tasks. As collated by Zeng et al. [@zeng_review_2023], designs E-1 (Simple Line) and E-2 (Braided) are ranked highest for finding extrema.

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to determine which series has the highest or lowest value at a specific timestamp (e.g., "Which stock price was highest on Tuesday?").
*   **Data Type:** Multiple quantitative time series (typically fewer than 8-10 to avoid excessive clutter).
*   **Audience:** Users performing detailed value extraction rather than trend scanning.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High Data Density / Clutter.
*   **Reason:** If there are too many lines (e.g., >10) or if the lines frequently cross and overlap, occlusion makes it impossible to trace individual lines. In these cases, the "visual clutter" penalty outweighs the "shared space" benefit.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Legibility of individual trend shapes. Overlapping lines obscure the holistic shape of any single series.
*   **The Risk:** Occlusion may hide data points where lines intersect or cluster tightly.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using Small Multiples for point-wise comparison.
*   **Why it fails:** It forces the user's eye to jump back and forth between separate charts to compare the Y-position of a specific time point, increasing cognitive load and time.

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you easily see which line is "on top" at any given X-coordinate?
*   **The Test:** Point to a specific date on the X-axis. Can you instantly rank the series from highest to lowest without moving your eyes to different panels?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Merge separate charts into a single multi-line chart.
*   **Best Fix:** If lines overlap significantly but the task remains local comparison, use a **Braided Graph** (Design E-2 in [@zeng_review_2023]), which uses depth-ordering and fill to clarify overlaps while maintaining a shared axis.
