---
id: bar-chart-proximity-jnd
title: Minimize Distance Between Compared Bars
bibliography: references.bib
description: Place bars close together to lower the Just Noticeable Difference threshold
  and improve comparison accuracy.
labels:
- chart:bar
- task:compare
- task:sort
- visual:position
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Place bars that need to be compared immediately adjacent to one another. Do not separate them with large gaps or intervening bars.

## The Logic <!-- role: reason -->
The ability to distinguish differences in bar height—the Just Noticeable Difference (JND)—is significantly affected by the separation distance between the bars. Research indicates a strong positive correlation between distance and JND: the farther apart the bars are, the larger the difference in height must be for a user to notice it. Interestingly, the absolute height of the bars does not significantly affect JND, likely because bars are judged along a common aligned scale.

*   **The Principle:** Distance-Dependent JND
*   **The Evidence:** [@lu_modeling_2022], included in the review by [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing specific values (e.g., "Is A taller than B?") or sorting items mentally.
*   **Data Type:** Quantitative data displayed on a common scale (Bar Charts).
*   **Audience:** General audiences needing to make accurate pairwise comparisons.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Grouped Bar Charts (Clustered Bars).
*   **Reason:** You may need to separate clusters (e.g., by year) to maintain the semantic structure of the data, even if it makes comparing a bar in Cluster A to a bar in Cluster B harder.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Ordering flexibility. You must sort the data by the comparison logic (e.g., descending values) or semantic grouping rather than arbitrary ordering.
*   **The Risk:** If the dataset is large, relevant bars might inevitably be far apart if not filtered.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Increasing the width of the bars to make them "easier to see."
*   **Why it fails:** The evidence suggests distance is the primary driver of error in bar charts, not the object intensity (height/size) or width.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the two most critical bars for the user separated by more than 2-3 other bars?
*   **The Test:** Can you determine which bar is taller without tracing a line with your finger or eye across the gap?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reorder the dataset so compared items are neighbors (e.g., sort by value).
*   **Best Fix:** Use interaction techniques (like highlighting or tooltips) to visually bridge the gap or display the delta if reordering is impossible.
