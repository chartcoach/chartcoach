---
id: use-wrapped-bars-for-ranking
title: Use Wrapped Bar Charts for Ranking Long Lists
bibliography: references.bib
description: For ranking tasks involving long lists, wrapped bar charts offer the
  best balance of accuracy and efficiency compared to scrolled or packed alternatives.
labels:
- chart:wrapped-bar
- chart:bar
- task:rank
- task:sort
- impact:accuracy
- data:quantitative
- complexity:intermediate
---

## The Rule <!-- role: advice -->
When visualizing a long ranked list where the user needs to identify the rank of specific items, split the list into multiple columns (wrap the bars) rather than using a single scrolling column or packing bubbles.

## The Logic <!-- role: reason -->
Wrapped bar charts provide the highest accuracy for ranking tasks compared to other compact visualizations like packed bars, piled bars, or treemaps.
*   **The Principle:** Wrapped bars maintain the length encoding and a shared baseline (per column), which preserves the ability to judge magnitude accurately. Unlike scrolled charts, they display the entire dataset at once, eliminating the interaction cost of scrolling.
*   **The Evidence:** In controlled experiments, wrapped bars (E-3) achieved the highest accuracy ranking for determining item rank, outperforming scrolled lists (E-1) and significantly outperforming packed (E-4) and piled (E-5) bars [@mylavarapu_ranked-list_2019]. This performance led reviewers to identify them as the "overall most balanced choice" for ranked lists [@zeng_review_2023].

## Where to Apply <!-- role: context -->
This advice applies to static dashboards or reports where screen space is fixed but data density is high.
*   **User Goal:** Determining the specific rank or position of an item within a larger set.
*   **Data Type:** Quantitative ranked lists containing between 75 and 300 items.
*   **Audience:** General analysts needing to assess individual item performance within a large group.

## When to Break It <!-- role: exceptions -->
Do not use wrapped bars if the primary task is estimating the average value of the group.
*   **Scenario:** The user needs to find the mean or understand the overall distribution.
*   **Reason:** Scrolled bar charts (E-1) and Zvinca (dot) plots (E-6) significantly outperform wrapped bars for aggregation tasks in terms of accuracy [@mylavarapu_ranked-list_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose a single common baseline for the *entire* dataset; bars in different columns cannot be compared as instantly as bars in a single column.
*   **The Risk:** Comparisons between items in different columns are slightly more cognitively demanding than in a single linear list.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using "Packed Bars" or "Bubble Charts" to fit data on one screen.
*   **Why it fails:** Packed layouts (E-4) performed poorly in accuracy for ranking tasks because they discard the common baseline and spatial order [@mylavarapu_ranked-list_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart require a scrollbar to see the bottom 50% of items? Or are items packed into a rectangle without aligned starting points?
*   **The Test:** Ask a user to quickly point to the item ranked #40. If they have to scroll or search a packed cluster, the design has failed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the container height to remove scrolling (if possible).
*   **Best Fix:** Re-implement the chart to "wrap" to a new column after $N$ items, ensuring each column shares a local baseline.
