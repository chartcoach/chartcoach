---
id: prefer-position-over-area-for-correlation
title: Prefer Position Over Area for Correlation
bibliography: references.bib
description: Area and angle-based encodings (donuts, stacked areas) yield lower precision
  for correlation tasks than position-based encodings.
labels:
- chart:donut
- chart:stacked-area
- task:correlate
- visual:area
- visual:angle
- impact:clarity
---

## The Rule <!-- role: advice -->
Avoid using donut charts, stacked area charts, or stacked bar charts to communicate correlation. Use position-based encodings (points or lines) instead.

## The Logic <!-- role: reason -->
Encodings that rely on area, angle, or length (in stacked contexts) significantly underperform compared to position on a common scale.
*   **The Principle:** **Encoding Effectiveness.** The human visual system estimates correlation more precisely through spatial position (scatterplots) than through variations in area or arc length.
*   **The Evidence:** According to the dataset in [@zeng_review_2023], designs using area (E-9, E-3), angle (E-11, E-5), and stacked length (E-10, E-4) consistently appear in lower tiers (Ranks 2, 3, and 4) compared to the top-tier position-based Scatterplots (Rank 1). For positive correlations specifically, donut (E-5) and stacked area (E-3) charts were in the lowest performance group (Rank 4) [@kay_beyond_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Assessing the relationship between two variables.
*   **Data Type:** Quantitative data being mapped to radial or stacked coordinate systems.
*   **Audience:** Any audience (the perceptual limitation is biological, not learned).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The correlation is merely a secondary decoration to a part-to-whole comparison.
*   **Reason:** If the primary task is "Summation" or "Part-to-Whole," stacked/area charts are appropriate. This rule applies strictly to the task of *correlation*.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Aesthetic variety. "Infographic" style charts often rely on donuts or radial areas which are less effective for this specific task.
*   **The Risk:** Users will perceive relationships as "noisy" or "weak" even when they are statistically strong, due to high JND thresholds in these chart types.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "Radar" or "Donut" chart to show how two variables move together.
*   **Why it fails:** The JND (Just Noticeable Difference) required to see changes in correlation is much higher in these forms than in Cartesian plots.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you encoding variables using slice width, slice size, or filled area size?
*   **The Test:** Ask a viewer to estimate the correlation coefficient. In area charts, their estimates will likely vary significantly from the truth compared to a scatterplot.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Unstack the data. Place visual marks side-by-side or superimposed on a standard x/y axis.
*   **Best Fix:** Convert the data to a Scatterplot (E-1) or Line Chart (E-2/E-6).
