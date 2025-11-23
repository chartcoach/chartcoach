---
id: use-dot-plots-for-group-averages
title: Use Dot Plots Instead of Bar Charts for Comparing Averages
bibliography: references.bib
description: When displaying the average of a set of values, dot plots allow for more
  accurate visual aggregation than bar charts.
labels:
- chart:dot-plot
- chart:bar
- task:compare
- task:aggregate
- visual:position
- visual:length
---

## The Rule <!-- role: advice -->
When the task requires viewers to estimate or compare the **average** value of a group of data points, visualize the data using dot plots (positional encoding) rather than bar charts (length/area encoding).

## The Logic <!-- role: reason -->
While bar charts are effective for comparing single values, they trigger a primitive heuristic when viewers try to aggregate multiple values: the "summed area" proxy.
*   **The Principle:** When looking at a group of bars, the visual system tends to sum the total area (or total length) of the bars rather than averaging their top positions. In contrast, dot plots force the viewer to rely on spatial position, allowing the visual system to effectively estimate the "center of mass" or average position.
*   **The Evidence:** Experiments showed that while single-value comparisons were accurate for both chart types, performance plummeted for bar charts when comparing averages of sets. Participants were significantly more accurate when using dot plots for the same multi-value data [@yuan_perceptual_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the arithmetic mean (average) of two or more groups of data.
*   **Data Type:** Sets of values where the individual data points are visible (distributions) or when the task involves mental aggregation.
*   **Audience:** General audiences who might intuitively rely on visual "weight" (area) rather than position.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Comparing single values (1 vs 1).
*   **Reason:** The paper confirms that for single-value comparisons, the hierarchy of precision holds true: bar charts (aligned scales) perform similarly to dot plots and are highly precise [@yuan_perceptual_2019].
*   **Scenario:** The goal is to compare totals/sums.
*   **Reason:** Since bar charts trigger a "summed area" bias, they are actually perceptually aligned with tasks requiring the comparison of cumulative totals.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Bar charts are more familiar to general audiences than dot plots.
*   **The Risk:** Viewers may initially find the "floating" nature of dots less grounded than bars if they are used to seeing magnitude represented by filled shapes.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using misaligned bars (stacked bar segments) or purely length-based encodings for averages.
*   **Why it fails:** Research shows that misaligned bars suffer from the same "summed extent" limitations as aligned bars when users try to extract averages [@yuan_perceptual_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do you have multiple bars representing a single group or category that the user must mentally average?
*   **The Test:** Ask a user to quickly identify which group has the higher average. If they hesitate or point to the group with more total "ink" rather than higher position, the chart is failing.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove the fill and sides of the bars, leaving only the top line or a symbol at the data value (converting it effectively into a dot plot/strip plot).
*   **Best Fix:** Redesign the visualization as a dot plot or strip plot, ensuring the dots represent the individual values clearly along the positional axis.
