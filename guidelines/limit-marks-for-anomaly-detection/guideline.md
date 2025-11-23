---
id: limit-marks-for-anomaly-detection
title: Limit Visible Marks for Anomaly Detection
bibliography: references.bib
description: Reduce the number of data points in ungrouped visualizations to improve
  search time for anomalies.
labels:
- chart:scatterplot
- chart:grid
- task:find-anomalies
- visual:density
- impact:efficiency
- data:quantitative
---

## The Rule <!-- role: advice -->
Reduce the total count of visible data points (set size) when the user's primary task is to find a specific target or anomaly within an ungrouped display.

## The Logic <!-- role: reason -->
Visual search time increases significantly as the number of distractor elements increases in random or ungrouped layouts. The evidence shows a direct negative correlation between set size and task performance.
*   **The Principle:** Serial Visual Search / Distractor Interference.
*   **The Evidence:** In the review by [@zeng_review_2023], data extracted from [@gramazio_relation_2014] demonstrates that for `find-anomalies` tasks, designs with lower cardinality (e.g., 36 or 64 items) consistently and significantly outperformed designs with high cardinality (e.g., 144, 196, or 484 items) in terms of response time.

## Where to Apply <!-- role: context -->
This applies to visualizations where data points are distributed randomly or without specific categorical spatial grouping.
*   **User Goal:** Rapidly identifying a unique target, outlier, or specific data point.
*   **Data Type:** Quantitative datasets visualized as scatterplots (points) or grids (area-rects).
*   **Audience:** Users performing time-sensitive monitoring or rapid data scanning.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data is spatially grouped by category (e.g., all red dots in one quadrant, blue in another).
*   **Reason:** As noted in the broader context of [@gramazio_relation_2014], spatial grouping allows users to filter out large chunks of data ("pre-attentive processing"), making the total set size less detrimental to search speed.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose data density and the ability to see the full context or "texture" of the entire dataset at once.
*   **The Risk:** Filtering data to reduce the count might hide relevant local patterns or non-target outliers that provide necessary context.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Reducing the *size* of the marks to fit more in, without reducing the *count*.
*   **Why it fails:** While mark size affects visibility, the sheer quantity of distinct objects (cardinality) drives the cognitive load in serial search tasks [@gramazio_relation_2014]. Small marks in high quantities remain difficult to scan.

## How to Check <!-- role: check -->
*   **Visual Sign:** The screen appears cluttered with hundreds of distinct items that lack a clear spatial structure.
*   **The Test:** Ask a user to find a specific "odd-one-out" item. If they have to scan item-by-item rather than glancing directly at the area, the set size is likely too high.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Filter or sample the data to show fewer points (e.g., reduce from 400 to <100).
*   **Best Fix:** If all data must be shown, introduce spatial grouping (e.g., small multiples or faceted grids) to break the large set into smaller, manageable perceptual groups.
