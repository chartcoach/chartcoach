---
id: avoid-area-charts-for-trend-estimation
title: Avoid Area Charts for Estimating Trends
bibliography: references.bib
description: Use scatterplots or line charts instead of area charts to prevent bias
  in trend estimation.
labels:
- chart:area-chart
- chart:line-chart
- chart:scatterplot
- task:correlate
- task:trend-estimation
- impact:accuracy
- impact:bias
---

## The Rule <!-- role: advice -->
Do not use area charts when the user needs to estimate trends, correlations, or regression lines. Use scatterplots or line charts instead.

## The Logic <!-- role: reason -->
Experimental comparisons show that area charts perform significantly worse than scatterplots and line charts for correlation tasks. Area charts introduce a perceptual distortion known as "within-the-area bias," where the visual weight of the filled region causes users to systematically underestimate the intercept of the trend.
*   **The Principle:** Within-the-Area Bias
*   **The Evidence:** The structured knowledge indicates that scatterplots and line charts share the top performance rank, while area charts are ranked significantly lower for correlation tasks [@zeng_review_2023] [@correll_regression_2017].

## Where to Apply <!-- role: context -->
This advice applies to bivariate visualizations where the user's primary goal is to identify the relationship (slope, intercept, or strength of correlation) between variables.
*   **User Goal:** Performing "regression by eye" or estimating the correlation between two variables.
*   **Data Type:** Quantitative Y-axis data plotted against Ordinal or Quantitative X-axis data.
*   **Audience:** Analysts or general audiences attempting to predict future values or understand relationships.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Volume or Part-to-Whole comparison.
*   **Reason:** If the goal is to emphasize the magnitude or accumulated volume of the data (e.g., "total sales volume") rather than the precise trend direction, the filled area provides the necessary visual weight that a line chart lacks.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the visual emphasis on the volume or magnitude of the values "under the curve."
*   **The Risk:** The chart may look less "solid" or substantial, potentially reducing the immediate visual impact of the data's magnitude.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding a fill to a line chart for purely aesthetic reasons (making it an area chart) without considering the analytical task.
*   **Why it fails:** This inadvertently triggers the "within-the-area bias," degrading the user's ability to accurately judge the trend line.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart represent a single series defined by a line with the space below it filled with color?
*   **The Test:** Ask a user to draw the "line of best fit" over the chart. If they consistently draw it lower than the mathematical average, the area fill is likely biasing their perception.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove the fill color opacity (set to 0%), leaving only the line (converting it to a standard line chart).
*   **Best Fix:** Convert the visualization to a scatterplot or a line chart, which have been proven to allow for more accurate trend estimation [@correll_regression_2017].
