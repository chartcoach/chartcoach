---
id: optimize-scatterplot-design-outlier-speed
title: Perceptually Optimize Scatterplots for Faster Outlier Detection
bibliography: references.bib
description: Perceptually optimized scatterplots allow users to spot anomalies significantly
  faster, though with a trade-off in accuracy.
labels:
- chart:scatterplot
- task:find-anomalies
- impact:speed
- visual:opacity
- visual:size
---

## The Rule <!-- role: advice -->
Apply perceptual optimization models (balancing contrast, overplotting, and separation) to scatterplots when the user must identify outliers rapidly.

## The Logic <!-- role: reason -->
Optimization algorithms that adjust marker opacity and size based on a cost function for "outlier perceivability" significantly reduce the time required to complete a task. As reviewed in @zeng_review_2023, the perceptually optimized design (E-1) outperformed standard defaults (E-2, E-3) in terms of completion time for finding anomalies @micallef_towards_2017. The optimization highlights structures that draw the eye quickly.

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapid screening or "triage" of data to find potential anomalies.
*   **Data Type:** Large datasets where manual parameter tuning is inefficient.
*   **Audience:** Users monitoring dashboards or real-time feeds where reaction time is critical.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Precision-critical analysis.
*   **Reason:** The optimized designs had a lower accuracy rate (success rate) than standard defaults. If missing an outlier is unacceptable, prioritize accuracy over speed @micallef_towards_2017.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Accuracy.
*   **The Risk:** Users may miss subtle outliers that standard defaults would have revealed, as the success rate for the optimized design was lower than for standard R/MATLAB plots.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using fixed, large markers for all datasets to make them "visible."
*   **Why it fails:** This causes overplotting which hides outliers located near the density distribution.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the plot maximize the contrast between the outlier and the background without saturating the dense regions?
*   **The Test:** Measure the time it takes to locate a known outlier; it should be immediate.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use an algorithm to automatically set alpha (opacity) and size based on data density.
*   **Best Fix:** Implement a cost-function based optimizer that specifically weights outlier perceivability (S_o) as described in @micallef_towards_2017.
