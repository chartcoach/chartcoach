---
id: limit-parallel-coordinates-usage
title: Avoid Parallel Coordinates for Positive Correlations
bibliography: references.bib
description: Parallel coordinates perform poorly for positive correlations but excel
  at negative ones due to specific visual features.
labels:
- chart:parallel-coordinates
- task:correlation
- visual:angle
- impact:accuracy
- data:multivariate
---

## The Rule <!-- role: advice -->
Do not use parallel coordinates plots to depict positive correlations; reserve them for negatively correlated data or re-orient axes to create negative correlations.

## The Logic <!-- role: reason -->
There is a striking perceptual asymmetry in parallel coordinates. Humans are much better at judging the "X" intersections created by negative correlations than the parallel slopes created by positive correlations.
*   **The Principle:** **Visual Feature Salience.** For negative correlations ($r \approx -1$), lines intersect at a single point, creating distinct triangular shapes. For positive correlations ($r \approx 1$), lines become parallel, making deviations harder to detect (higher JND) [@harrison_ranking_2014].
*   **The Evidence:** Experiments showed that parallel coordinates depicting negative data performed significantly better than those depicting positive data, rivaling the performance of scatterplots. Conversely, positive correlation performance was poor [@harrison_ranking_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying relationships in multivariate data.
*   **Data Type:** High-dimensional data where axes are placed side-by-side.
*   **Audience:** Analysts looking for inverse relationships.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** You cannot control the axis order or the data contains a mix of unknown positive and negative correlations.
*   **Reason:** While less precise for positive correlations, the chart is still valid for identifying clusters or outliers, just not for precise correlation estimation.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may need to flip axes explicitly to convert positive correlations into visually negative ones (intersections).
*   **The Risk:** Confusion if the axis direction is inverted (e.g., "up" means "low value") without clear labeling.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Keeping axes in a default alphabetical or arbitrary order.
*   **Why it fails:** This maximizes the chance of displaying positive correlations as parallel lines, which have high perceptual error rates [@harrison_ranking_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do you see mostly parallel lines between two axes?
*   **The Test:** Can you easily tell the difference between a strong relationship ($r=0.7$) and a weak one ($r=0.4$) in those parallel lines? (Likely not).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Flip one of the axes so the relationship appears as an intersection ("X" shape) rather than parallel lines.
*   **Best Fix:** Implement algorithms to automatically maximize "negative" (intersecting) layouts by reordering or flipping axes.
