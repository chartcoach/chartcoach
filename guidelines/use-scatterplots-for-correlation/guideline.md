---
id: use-scatterplots-for-correlation
title: Use Scatterplots for Bivariate Correlation
bibliography: references.bib
description: Scatterplots consistently outperform other chart types for accurately
  estimating correlation in both positive and negative directions.
labels:
- chart:scatterplot
- task:correlate
- visual:position
- impact:precision
- data:quantitative
- audience:general
---

## The Rule <!-- role: advice -->
Visualize bivariate correlation using scatterplots. Prioritize this chart type over line charts, parallel coordinates, or area-based visualizations when the user needs to estimate the strength of the relationship.

## The Logic <!-- role: reason -->
Scatterplots provide the highest precision and the lowest variance between individuals when estimating correlation.
*   **The Principle:** **Perceptual Precision.** According to experimental rankings, scatterplots (specifically design E-1 for positive and E-7 for negative) consistently appear in the top performance tier for Just-Noticeable Differences (JND) in correlation tasks.
*   **The Evidence:** The review by [@zeng_review_2023], synthesizing data from [@kay_beyond_2016], ranks scatterplots as the most effective visualization for this task. [@kay_beyond_2016] specifically notes that scatterplots are unique in combining high precision for *both* positively and negatively correlated data while maintaining low variation in performance across different users.

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurately estimating or comparing the correlation ($r$) between two quantitative variables.
*   **Data Type:** Bivariate quantitative data (Quantitative-1 vs. Quantitative-2).
*   **Audience:** General audiences and analysts, as the interpretation requires less individual adjustment than other types.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset is extremely large and suffers from severe overplotting.
*   **Reason:** While not explicitly tested in the ranking data provided, the perceptual advantages of position encoding degrade when points become a solid mass. However, the primary evidence suggests scatterplots remain robust across standard densities.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Space efficiency. Scatterplots generally require a square or nearly square aspect ratio to be most effective, whereas parallel coordinates or stacked bars can be compressed horizontally.
*   **The Risk:** Overplotting can obscure density if transparency or aggregation is not used.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using dual-axis line charts or parallel coordinates to save space.
*   **Why it fails:** As shown in the data, parallel coordinates perform significantly worse for positive correlations (dropping to the lowest rank), and line charts generally perform in the middle tier (Rank 3).

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using two separate axes to map two variables as points in 2D space?
*   **The Test:** If you swap the chart to a parallel coordinates plot, does the correlation look "stronger" or "weaker" erroneously? (Stick to the scatterplot for the ground truth).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the mark type to `point` and map the two variables to `positionX` and `positionY`.
*   **Best Fix:** Ensure the aspect ratio is close to 1:1 to avoid distorting the perception of the slope/cloud shape.
