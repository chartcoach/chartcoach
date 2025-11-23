---
id: avoid-parallel-coordinates-positive-correlation
title: Avoid Parallel Coordinates for Positive Correlation
bibliography: references.bib
description: Parallel coordinates perform poorly for perceiving positive correlations
  compared to negative correlations.
labels:
- chart:parallel-coordinates
- task:correlate
- visual:orientation
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Do not use parallel coordinates to visualize positive correlations. Limit their use in correlation tasks to detecting negative relationships.

## The Logic <!-- role: reason -->
There is a drastic performance asymmetry in parallel coordinates depending on the direction of the correlation.
*   **The Principle:** **Directional Bias.** Parallel coordinates rely on line slope and crossing patterns. Negative correlations create a distinct "bowtie" crossing pattern that is highly perceptible, while positive correlations create parallel lines that are harder to distinguish.
*   **The Evidence:** In the collation by [@zeng_review_2023], Parallel Coordinates for negative correlation (Design E-8) ranked in the top tier (Rank 1). However, Parallel Coordinates for positive correlation (Design E-12) dropped to the bottom tier (Rank 4). [@kay_beyond_2016] confirms that while parallel coordinates are competitive with scatterplots for negative data, they are significantly worse for positive data.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing multiple variables where the primary relationships of interest are inverse (negative correlations).
*   **Data Type:** Multivariate quantitative data.
*   **Audience:** Expert users familiar with reading parallel coordinate patterns.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to trace individual data points across more than two dimensions (Multivariate analysis).
*   **Reason:** The primary goal shifts from "estimating correlation" (the scope of this evidence) to "tracking entity values," which parallel coordinates support better than pairwise scatterplots.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to uniformly visualize relationships; you must know the data structure (direction of correlation) *before* choosing the chart.
*   **The Risk:** Users may completely overlook strong positive correlations because the visual signal (parallel lines) is perceptually weak.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assuming parallel coordinates work equally well for all relationships.
*   **Why it fails:** The experimental ranking shows a massive degradation in JND (Just-Noticeable Difference) performance when switching from negative to positive correlation on the same chart type.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the lines between axes roughly parallel?
*   **The Test:** Can you easily distinguish between a correlation of $r=0.4$ and $r=0.7$ in the parallel view? (The evidence suggests you likely cannot).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Invert one of the axes. This transforms the visual pattern of a positive correlation into the "bowtie" pattern of a negative correlation, which is Rank 1 for perception.
*   **Best Fix:** Switch to a scatterplot matrix (SPLOM) if space permits.
