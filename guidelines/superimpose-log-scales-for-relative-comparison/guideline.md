---
id: superimpose-log-scales-for-relative-comparison
title: Superimpose Logarithmic Scales for Growth Rates
bibliography: references.bib
description: Use superimposed logarithmic scales rather than juxtaposed linear scales
  for comparing growth rates across time series with different magnitudes.
labels:
- chart:line-chart
- visual:scale
- task:correlate
- task:aggregate
- data:time-series
- impact:efficiency
---

## The Rule <!-- role: advice -->
When comparing trends or growth rates of multivariate time series with significantly different magnitudes, **superimpose the lines on a logarithmic scale**. Do not use juxtaposed (side-by-side) linear charts.

## The Logic <!-- role: reason -->
Juxtaposed charts force the eye to scan back and forth, increasing cognitive load and time. Superimposition allows for direct visual comparison of slopes. However, superimposing data with vastly different magnitudes (e.g., a stock at \$10 vs. \$1000) on a linear scale hides the behavior of the smaller series.
*   **The Principle:** Logarithmic scales linearize exponential changes; equal vertical distances represent equal percentage changes, making slopes directly comparable regardless of absolute magnitude.
*   **The Evidence:** Experimental results collated by Zeng and Battle [@zeng_review_2023] from Aigner et al. [@aigner_bertin_2011] show that superimposed logarithmic plots (E-2) significantly outperformed juxtaposed linear plots (E-1) in both task completion time and accuracy for correlation and aggregation tasks.

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying correlations in trends or estimating aggregate percentage changes between variables.
*   **Data Type:** Multivariate time series where the variables differ significantly in value domain (e.g., comparing Apple stock price vs. Microsoft stock price over decades).
*   **Audience:** Analysts or users capable of interpreting non-linear axes.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to read precise absolute values rather than relative changes.
*   **Reason:** Logarithmic scales distort the perception of absolute magnitude differences, making it difficult for users to estimate the raw numerical difference between two points.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Intuitive understanding of absolute units.
*   **The Risk:** Novice users may misinterpret the flattening of curves at the top of the scale as "slowing down" if they do not notice the log axis.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a linear scale with dual Y-axes (secondary axes) to superimpose the lines.
*   **Why it fails:** This introduces arbitrary crossing points that suggest false correlations and makes slope comparison geometrically invalid.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the lines placed in separate charts (side-by-side or stacked) even though the user needs to compare their slopes?
*   **The Test:** Check the range of your variables. If Variable A ranges 0-10 and Variable B ranges 1000-2000, and you are using linear scales, you are likely forced to separate them (juxtaposition). If you switch to Log, can you overlay them meaningfully?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the Y-axis scale type from `linear` to `log` and remove row/column faceting to overlay the lines in a single view.
*   **Best Fix:** Ensure the axis is clearly labeled as logarithmic to aid interpretation.
