---
id: avoid-treemaps-for-sorting
title: Avoid Treemaps For Value Sorting Tasks
bibliography: references.bib
description: Treemaps result in lower accuracy for sorting tasks compared to pie charts
  and stacked bars.
labels:
- chart:treemap
- chart:pie
- task:sort
- task:rank
- visual:area
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Do not use treemaps when the user needs to accurately sort or rank the parts of a whole.

## The Logic <!-- role: reason -->
Treemaps rely on 2D area comparisons that are often difficult for users to rank precisely.
*   **The Evidence:** In a review by @zeng_review_2023, data from @kosara_impact_2019 demonstrated that Treemaps (E-5) ranked lowest in sorting accuracy, performing significantly worse than standard Pie Charts (E-1) and Stacked Bars (E-4).

## Where to Apply <!-- role: context -->
*   **User Goal:** When the primary analytical task is to determine the order of segments from largest to smallest.
*   **Data Type:** Part-to-whole quantitative data.
*   **Audience:** General users needing to make precise comparisons between categories.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the data hierarchy (nested categories) is more important than the precise sorting of leaf nodes.
*   **Reason:** Treemaps are primarily designed for showing hierarchical structure, which pie charts and stacked bars cannot easily display.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to display hierarchical nesting that a treemap provides.
*   **The Risk:** By choosing a Pie Chart or Stacked Bar instead, you may lose space efficiency if there are many small categories.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a standard Pie Chart to fix the problem.
*   **Why it fails:** While @kosara_impact_2019 found Pie Charts (E-1) significantly better than Treemaps (E-5), they were still outperformed by Stacked Bars (E-4) in accuracy.

## How to Check <!-- role: check -->
*   **Visual Sign:** A rectangular layout where users are struggling to determine if one box is slightly larger than another.
*   **The Test:** Ask a user to quickly rank the top 5 categories in the visualization.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch to a Stacked Bar Chart (E-4).
*   **Best Fix:** Use a Stacked Bar Chart or a Circular Slice design (E-2), both of which ranked highest for sorting accuracy in the study.
