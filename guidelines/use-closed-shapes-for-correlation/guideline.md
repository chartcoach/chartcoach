---
id: use-closed-shapes-for-correlation
title: Use Closed Shapes for Correlation Estimates
bibliography: references.bib
description: Use closed shapes (squares, triangles) rather than open shapes (asterisks,
  crosses) for scatterplots requiring trend estimation.
labels:
- chart:scatterplot
- task:correlate
- visual:shape
- impact:accuracy
- data:quantitative
- audience:analyst
- source:empirical
---

## The Rule <!-- role: advice -->
Use closed geometric shapes (such as squares, triangles, or circles) rather than open line-based shapes (such as asterisks, crosses, or plus signs) when plotting data in scatterplots intended for correlation or trend estimation.

## The Logic <!-- role: reason -->
Closed shapes possess a bounded region of space that facilitates "ensemble coding"—the brain's ability to extract summary statistics like average value or linear trend from a group of objects.
*   **The Principle:** Perceptual Robustness of Closed Figures.
*   **The Evidence:** Experimental results collated by @zeng_review_2023 show that scatterplots using closed shapes (e.g., triangles and squares) significantly outperform those using open shapes (e.g., asterisks and crosses) in both accuracy and speed for correlation tasks. Specifically, @burlinson_open_2018 demonstrates that participants were faster and more accurate at determining linear relationships when viewing closed symbols compared to open symbols.

## Where to Apply <!-- role: context -->
This advice applies to statistical data visualization where the user needs to assess the relationship between two quantitative variables.
*   **User Goal:** Estimating the strength or direction of a correlation (trend judgment).
*   **Data Type:** Bivariate quantitative data displayed as a scatterplot.
*   **Audience:** Users performing analytical tasks requiring rapid trend assessment.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-density plots with significant overplotting.
*   **Reason:** While closed shapes are better for perception, filled closed shapes can occlude each other more than open line-based shapes in extremely dense displays, potentially obscuring data density.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Closed shapes (especially if filled) typically consume more "ink" and visual weight than thin, open line segments.
*   **The Risk:** In multi-class scatterplots, using only closed shapes reduces the total number of distinct symbol shapes available (e.g., running out of distinct closed polygons).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a set of open symbols (like `+`, `x`, `*`) to represent different data series in a correlation plot.
*   **Why it fails:** @burlinson_open_2018 found that the combination of open shapes (e.g., asterisk and cross) resulted in the lowest accuracy and slowest performance for correlation tasks among tested designs.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the data points composed of line segments with no interior (e.g., `+`, `x`)?
*   **The Test:** Glancing at the plot, does the "cloud" of points feel faint or difficult to abstract into a single shape/line?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the marker style in your plotting library from markers like `cross` or `asterisk` to `square` or `circle`.
*   **Best Fix:** Use filled or outlined closed shapes (circles, squares, triangles) to maximize the "pop" of the trend.
