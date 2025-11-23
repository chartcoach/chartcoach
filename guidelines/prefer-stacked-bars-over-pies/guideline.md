---
id: prefer-stacked-bars-over-pies
title: Prefer Stacked Bars Over Pie Charts For Accuracy
bibliography: references.bib
description: Stacked bar charts offer higher accuracy than standard pie charts for
  sorting tasks.
labels:
- chart:bar
- chart:pie
- task:sort
- visual:length
- visual:angle
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Use stacked bar charts instead of standard pie charts when accuracy in sorting segments is required.

## The Logic <!-- role: reason -->
Length encodings generally support more precise comparisons than angle encodings.
*   **The Evidence:** According to the collation by @zeng_review_2023, the experiment by @kosara_impact_2019 ranked Stacked Bars (E-4) in the top tier for sorting accuracy, outperforming standard Pie Charts (E-1).

## Where to Apply <!-- role: context -->
*   **User Goal:** Ranking or sorting components within a whole.
*   **Data Type:** Quantitative part-to-whole data.
*   **Audience:** Users performing analytical tasks requiring precision.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When rapid scanning speed is prioritized over absolute precision.
*   **Reason:** The study @kosara_impact_2019 indicated that Stacked Bars (E-4) were slower to read than Circular Slice designs (E-2).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Stacked bars may take longer to scan visually compared to circular designs.
*   **The Risk:** Users may perceive the linear layout as less "part-to-whole" than a circular layout.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a standard Donut Chart without considering arc length/area properties.
*   **Why it fails:** The study specifically tested "Circular Slices" (E-2) and "Straight-Line Circular" (E-3) designs, not necessarily generic donut charts.

## How to Check <!-- role: check -->
*   **Visual Sign:** A standard Pie Chart is used for data where slices are very similar in size.
*   **The Test:** Can the user instantly tell which of two similar slices is larger?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Convert the Pie Chart to a Stacked Bar Chart.
*   **Best Fix:** Ensure the Stacked Bar uses clear length encoding to maximize the accuracy advantage found in the study.
