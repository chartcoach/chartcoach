---
id: augment-boxplots-distribution
title: Augment Boxplots with Raw Data or Density Curves
bibliography: references.bib
description: Boxplots hide distribution shapes; overlay points or use violin plots.
labels:
- chart:boxplot
- visual:distribution
- task:compare
- impact:clarity
- data:statistical
---

## The Rule <!-- role: advice -->
Do not use simple boxplots alone to communicate complex data distributions. Overlay the raw data points (jittered) or use a violin plot.

## The Logic <!-- role: reason -->
Boxplots summarize data into quartiles (25th, 50th, 75th percentiles). It is possible to generate widely distinct 1D distributions—such as a normal curve, a bi-modal distribution, or data concentrated entirely at the extremes—that produce identical boxplots (same median, IQR, and whiskers). The box visualizes the summary, not the reality.
*   **The Principle:** Non-parametric Ambiguity
*   **The Evidence:** [@matejka_same_2017]

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing distributions between groups.
*   **Data Type:** 1D distribution data.
*   **Audience:** Researchers or stakeholders needing to understand the "shape" of the data (e.g., is it polarized? is it uniform?).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Standardized reporting where only quartiles are legally or procedurally required.
*   **Reason:** Sometimes the goal is specifically to report the IQR, not the full distribution shape.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Jittered strips or violin plots take up more horizontal width than a simple boxplot.
*   **The Risk:** Showing all points can look "noisy" if the dataset is massive.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding "notches" to the boxplot.
*   **Why it fails:** Notches represent confidence intervals for the median, but they still do not reveal if the data is bi-modal (two humps) or uniform (flat).

## How to Check <!-- role: check -->
*   **Visual Sign:** You see a row of boxplots that look similar, but you suspect the underlying processes are different.
*   **The Test:** "Explode" the boxplot into a histogram or strip plot. Do the shapes look the same?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a layer of semi-transparent, jittered points on top of the boxplot.
*   **Best Fix:** Use a Violin Plot or a "Raincloud Plot" (half-violin + jittered points) to show the probability density alongside the statistical markers.
