---
id: prefer-angle-over-area
title: Prefer Angle Over Area for Part-to-Whole Comparisons
bibliography: references.bib
description: When choosing between pie charts, treemaps, and bubble charts, pie charts
  offer better accuracy.
labels:
- chart:pie
- chart:treemap
- chart:bubble
- visual:angle
- visual:area
- task:sort
---

## The Rule <!-- role: advice -->
If you must use a part-to-whole visualization, use a pie chart (angle) rather than a treemap or bubble chart (area).

## The Logic <!-- role: reason -->
While position encodings are superior to both, angle encodings are significantly more accurate than area encodings.
*   **The Evidence:** Findings collated in [@zeng_review_2023] from [@heer_crowdsourcing_2010] show that Angle (E-6) is ranked significantly higher than Area-Rect (E-8), Treemap (E-9), and Area-Circle (E-7).
*   **The Hierarchy:** The study establishes a performance hierarchy where Angle > Area.

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating proportions or comparing parts of a whole when a bar chart is not an option.
*   **Data Type:** Quantitative proportions summing to a total.
*   **Audience:** General audiences familiar with pie charts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the dataset has a high cardinality (many slices).
*   **Reason:** While angle is better than area for simple comparisons, pie charts become unreadable with too many categories, whereas treemaps (E-9) can handle hierarchical density better despite lower accuracy.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Pie charts often require more space to label clearly compared to treemaps.
*   **The Risk:** You are still choosing a suboptimal encoding; position (bar charts) would be more accurate than angle.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a bubble chart (E-7) to show market share or proportions.
*   **Why it fails:** Area-Circle (E-7) is consistently ranked at the bottom of the accuracy list in the provided dataset.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using size (area) to represent value without a common axis?
*   **The Test:** If you switch the chart to a pie chart, are the differences easier to distinguish? (Evidence suggests they will be).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the bubble or treemap visualization to a pie chart (E-6).
*   **Best Fix:** Change the visualization to a bar chart (E-1) for maximum accuracy.
