---
id: use-dot-plots-for-aggregation
title: Use Zvinca (Dot) Plots for Aggregate Summaries
bibliography: references.bib
description: When users need to estimate averages or distributions in large lists,
  compact dot plots outperform bar charts in speed and accuracy.
labels:
- chart:dot-plot
- chart:zvinca-plot
- task:aggregate
- task:mean
- visual:position
- impact:efficiency
- data:quantitative
---

## The Rule <!-- role: advice -->
Use Zvinca plots (dense dot plots) instead of bar charts when the user's primary task is to estimate the average value (mean) or assess the distribution of a large list of items.

## The Logic <!-- role: reason -->
Dot plots reduce the ink-to-data ratio and allow for higher density without the visual clutter of bars. This clarity improves the perception of the aggregate whole.
*   **The Principle:** By removing the bar length and focusing on position, users can more easily process the "center of gravity" of the dataset.
*   **The Evidence:** Zvinca plots (E-6) ranked highest for accuracy in aggregation tasks, tying with scrolled bar charts but performing significantly faster [@mylavarapu_ranked-list_2019]. This aligns with findings in the broader review that position-based plots often excel at summary tasks [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Determining the average value or spotting outliers in a large collection.
*   **Data Type:** Large quantitative lists (e.g., 75+ items) where individual item identity is secondary to the group behavior.
*   **Audience:** Users performing statistical overview tasks.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to compare the exact difference between two specific items.
*   **Reason:** For pairwise comparisons (e.g., "Is A larger than B?"), standard bar charts (scrolled or wrapped) offer better accuracy than dot plots [@mylavarapu_ranked-list_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** The visual weight of individual items is reduced; single items are harder to click or hover over compared to thick bars.
*   **The Risk:** Novice users may find the dense dot representation less familiar than a standard bar chart.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "Piled Bar" chart to save space.
*   **Why it fails:** Piled bars (E-5) performed significantly worse than Zvinca plots for aggregation tasks [@mylavarapu_ranked-list_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using thick bars to represent hundreds of data points, causing the chart to grow extremely tall?
*   **The Test:** Check the aspect ratio. If the chart is mostly "ink" (bars) and requires heavy scrolling to find the middle value, it is inefficient for aggregation.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reduce bar width to thin lines.
*   **Best Fix:** Convert the mark type from `bar` to `point` or `circle` and align them on a single axis (Zvinca plot style).
