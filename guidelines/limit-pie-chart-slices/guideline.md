---
id: limit-pie-chart-slices
title: Limit Pie Charts to Five Slices
bibliography: references.bib
description: To ensure readability and tidy labeling, avoid using pie charts for datasets
  with more than five categories.
labels:
- chart:pie
- visual:clutter
- task:simplification
- impact:clarity
- data:categorical
---

## The Rule <!-- role: advice -->
Do not include more than five values (slices) in a single pie chart.

## The Logic <!-- role: reason -->
Pie charts work best when showing how a whole divides into a *few* shares. When there are more than five shares, the labeling becomes untidy and the chart becomes difficult to read [@muth_pie_charts_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Creating a clean, readable overview of a composition.
*   **Data Type:** Categorical data with high cardinality.
*   **Audience:** Readers who need a quick summary without visual clutter.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** You are using an interactive tool where labels are hidden until hover (though this still strains visual processing).
*   **Reason:** Hiding labels solves the clutter, but not the slice size comparison issue.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot show every single data point individually.
*   **The Risk:** You may need to aggregate data, potentially obscuring granular details.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a legend or cramming labels with lines pointing to thin slices.
*   **Why it fails:** It increases cognitive load and visual messiness.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there more than 5 distinct colors or wedges?
*   **The Test:** Count the slices. If > 5, the rule is broken.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Group smaller slices into an "others" category.
*   **Best Fix:** Switch to a stacked column or stacked bar chart, which handles larger numbers of categories better [@muth_pie_charts_2018].
