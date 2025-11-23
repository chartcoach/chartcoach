---
id: quantitative-effectiveness-ranking
title: Encode Quantities Using Position First
bibliography: references.bib
description: Use position on a common scale as the primary encoding for quantitative
  data, following perceptual accuracy rankings.
labels:
- chart:scatter
- chart:bar
- visual:position
- visual:length
- visual:area
- visual:color
- data:quantitative
- impact:accuracy
---

## The Rule <!-- role: advice -->
When encoding quantitative data, prioritize **Position** (common scale) over all other visual variables. If position is unavailable, use Length, then Angle, then Slope, then Area. Avoid using Color or Density for precise quantitative comparison.

## The Logic <!-- role: reason -->
Human perceptual tasks are accomplished with varying degrees of accuracy. Effectiveness criteria are based on comparing the perceptual tasks required by alternative graphical languages.
*   **The Principle:** Accuracy Ranking of Quantitative Perceptual Tasks
*   **The Evidence:** Based on Cleveland and McGill's psychophysical results cited in [@mackinlay_automating_1986], tasks are ranked: Position > Length > Angle > Slope > Area > Volume > Color/Density.

## Where to Apply <!-- role: context -->
*   **User Goal:** Precise comparison of numerical values.
*   **Data Type:** Quantitative (ranges, numeric values).
*   **Audience:** Analytical audiences requiring high fidelity.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The "Position" channel is already used for a more important variable.
*   **Reason:** You typically only have two axes (x and y). Once those are used, you must move down the ranking list for tertiary variables.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Designs relying on position (like scatter plots or bar charts) can become cluttered if data density is high.
*   **The Risk:** Using lower-ranking channels (like Area in a bubble chart) significantly reduces the user's ability to accurately judge differences (e.g., a 10-fold range is perceivable, but precise comparison is difficult).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using circle size (Area) to encode the primary quantitative variable when an axis is available.
*   **Why it fails:** Area is ranked fifth in accuracy, far below Position and Length [@mackinlay_automating_1986].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using bubbles or color gradients to show the most important numbers?
*   **The Test:** Can you instantly tell if one value is 25% larger than another? If not, the encoding is likely too low on the effectiveness ranking.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add labels to the imprecise marks.
*   **Best Fix:** Change the chart type. Convert a bubble chart to a bar chart or scatter plot to utilize Position or Length.
