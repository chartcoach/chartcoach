---
id: mirror-bar-charts-comparison
title: Mirror Axes for Side-by-Side Bar Comparisons
bibliography: references.bib
description: Arrange comparative bar charts with mirrored axes to leverage bilateral
  symmetry detection.
labels:
- chart:bar
- task:compare
- task:correlation
- visual:position
- impact:accuracy
---

## The Rule <!-- role: advice -->
When placing two bar charts side-by-side for comparison, mirror their axes so the bars face each other (right-align the left chart, left-align the right chart).

## The Logic <!-- role: reason -->
The human visual system is highly sensitive to mirror symmetry, particularly near the focal point. Mirroring spatially juxtaposes the relevant data and utilizes this sensitivity, making it easier to detect differences (asymmetry) or similarities compared to standard repeated translations (standard side-by-side layouts) [@ondov_face_2019].

*   **The Principle:** Bilateral Symmetry Detection
*   **The Evidence:** Mirrored arrangements outperformed standard horizontal and vertical small multiples for identifying both the largest change (MaxDelta) and the highest correlation between datasets [@ondov_face_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing two specific datasets for either identifying outliers (biggest change) or estimating overall similarity (correlation).
*   **Data Type:** Bar charts representing two series of data.
*   **Audience:** General users, particularly in static media (like handouts) where animation is impossible.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Donut Charts or Slope Charts.
*   **Reason:** The experiments showed no significant performance benefit for "mirrored" layouts in donut or slope charts compared to standard adjacent layouts [@ondov_face_2019].
*   **Scenario:** Comparing more than two datasets.
*   **Reason:** Mirroring implies a bilateral relationship; it is difficult to scale this geometric arrangement to three or more series [@ondov_face_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Familiarity. Users may be less accustomed to "population pyramid" style layouts for general data than standard left-to-right bar charts.
*   **The Risk:** Axis Labeling. You must ensure the reversed axis (on the left chart) is clearly understood as increasing towards the center (or decreasing from the center, depending on implementation).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Stacking charts vertically (one above the other).
*   **Why it fails:** Vertical small multiples (stacked) yielded the lowest accuracy for comparison tasks in the study [@ondov_face_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do all bars grow from left to right?
*   **The Test:** Look at the space between the charts. If the bars are growing away from the center gap in the same direction, they are not mirrored. They should grow towards (or away from) a shared central spine.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Right-align the left-hand chart and remove the gap between the two charts.
*   **Best Fix:** Create a "diverging bar" or "population pyramid" style layout where the category labels sit in the center spine.
