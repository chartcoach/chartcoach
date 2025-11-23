---
id: encode-summary-statistics-with-color
title: Use Color for Aggregate Summary Tasks
bibliography: references.bib
description: When the user needs to estimate means or variance across a collection,
  color often outperforms position.
labels:
- visual:color
- visual:position
- task:summarize
- task:estimate
- impact:accuracy
- data:statistical
---

## The Rule <!-- role: advice -->
When the primary task is estimating the mean or variance of a dataset (rather than finding specific values), encode the data using color rather than position.

## The Logic <!-- role: reason -->
Research suggests a trade-off in ensemble coding abilities. While position is superior for identifying specific values (range, extrema, outliers), the visual system extracts mean and variance more accurately from color distributions [@szafir_four_2016].
*   **The Principle:** Feature Integration vs. Shape Boundaries
*   **The Evidence:** Experiments comparing scatterplots (position) to heatmaps/color arrays (color) show that color facilitates summation at low spatial frequencies, acting like a perceptual histogram, while position emphasizes boundaries [@szafir_four_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Quickly estimating the average value or the stability (variance) of a dataset.
*   **Data Type:** Large collections of data points where individual values matter less than the aggregate property.
*   **Audience:** Analysts looking for "gist" or general trends in dense data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to find the minimum, maximum, or range of the data.
*   **Reason:** Position is significantly more accurate than color for identifying extrema and range [@szafir_four_2016].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision of individual data points.
*   **The Risk:** Users cannot accurately read specific values back from the visualization (color saturation is poor for precise value extraction).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a scatterplot for every task.
*   **Why it fails:** While scatterplots are versatile, they may obscure the "average" signal in noise when the user strictly wants to know "is group A higher on average than group B?"

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using a scatterplot when the insight is purely about the average?
*   **The Test:** Ask a user to estimate the average value. If they try to calculate it point-by-point rather than "seeing" the average instantly, consider color.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a redundant color encoding to the positional plot.
*   **Best Fix:** Switch to a heatmap or dense pixel display if the task is purely summary-based.
