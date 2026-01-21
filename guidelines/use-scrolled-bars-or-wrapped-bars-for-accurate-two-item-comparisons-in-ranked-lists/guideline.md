---
id: use-scrolled-bars-or-wrapped-bars-for-accurate-two-item-comparisons-in-ranked-lists
title: Use Scrolled Bars or Wrapped Bars for Accurate Two-Item Comparisons in Ranked
  Lists
bibliography: references.bib
description: For comparing two highlighted items in a ranked list, scrolled barcharts
  and wrapped bars are the most accurate options among the tested ranked-list visualizations.
labels:
- chart:bar
- task:compare
- task:sort
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- domain:ranked-list
---

## The Rule <!-- role: advice -->

When users must accurately compare two selected items in a ranked list, use scrolled barcharts or wrapped bars.

## The Logic <!-- role: reason -->

In the second “sort” condition (two-item comparison task), scrolled barchart (E-1) and wrapped bars (E-3) are the top accuracy group, and each significantly outperforms treemap (E-2) and the other dense layouts (E-4/E-5/E-6).

- **The Principle:** Preserve discriminable value judgments for pairwise comparisons.
- **The Evidence:** The extracted ranking for sort-2 accuracy places (E-3, E-1) as best; significance pairs show E-3 and E-1 beating E-2/E-4/E-5/E-6 [@mylavarapuRankedListVisualizationGraphical2019]. These results are part of the collation in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which of two items is larger and by how much (two-item comparison).
- **Data Type:** Ranked list with quantitative values.
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary goal is speed (minimizing time) rather than accuracy for comparisons.
- **Reason:** In the sort-2 time ranking, scrolled barchart (E-1) is the slowest, while Zvinca (E-6) is ranked fastest [@mylavarapuRankedListVisualizationGraphical2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Scrolled barcharts can cost time (scrolling/interaction), and wrapped bars can add scanning overhead across columns.
- **The Risk:** If time-to-answer is critical, these accuracy-leading choices may underperform faster alternatives.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using treemaps as the default for pairwise value comparison in ranked lists.
- **Why it fails:** Treemap (E-2) ranks below (E-3, E-1) for accuracy and is significantly worse than both in the extracted significance pairs [@mylavarapuRankedListVisualizationGraphical2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Users frequently invert which item is larger or give inconsistent magnitude estimates.
- **The Test:** A/B test scrolled vs wrapped vs treemap vs Zvinca for two-item prompts; compare normalized absolute error.

## How to Fix <!-- role: fix -->

- **Quick Fix:** If currently using treemap/packed/piled/Zvinca for comparisons, switch to wrapped bars.
- **Best Fix:** Provide scrolled barchart or wrapped bars as the “compare precisely” mode, and reserve faster-but-less-accurate options for overview tasks [@mylavarapuRankedListVisualizationGraphical2019; @zengReviewCollationGraphical2023].
