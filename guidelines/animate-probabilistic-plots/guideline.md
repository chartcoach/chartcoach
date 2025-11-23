---
id: animate-probabilistic-plots
title: Animate Random Samples to Highlight Outliers
bibliography: references.bib
description: Use animation to cycle through random samples from probability distributions
  to reveal outliers.
labels:
- chart:scatter
- chart:parallel-coordinates
- visual:animation
- visual:motion
- impact:attention
- data:uncertain
- task:explore
---

## The Rule <!-- role: advice -->
For large uncertain datasets, use "probabilistic plots" that animate over time. continually replace the displayed points (or lines) with new random samples drawn from each data point's underlying probability distribution.

## The Logic <!-- role: reason -->
Static density plots tend to smooth out outliers, hiding them in the background.
*   **The Principle:** Preattentive processing of motion (flicker).
*   **The Evidence:** [@feng_matching_2010] demonstrates that regions of high certainty remain stable over time (solid), while uncertain regions or outliers appear briefly and disappear. This "intermittent flickering" signals the viewer to look at the outlier region, preventing outliers from being averaged out of existence.

## Where to Apply <!-- role: context -->
*   **User Goal:** Finding potential anomalies or outliers that might be missed in a static summary.
*   **Data Type:** Extremely large datasets where computing a full density plot is computationally expensive, or datasets with critical outliers.
*   **Audience:** Users performing exploratory data analysis (EDA) looking for "needles in a haystack."

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Static reporting (e.g., print media).
*   **Reason:** Animation is impossible in non-digital formats.
*   **Scenario:** Precise statistical comparison.
*   **Reason:** The constant flux makes it hard to compare exact densities side-by-side at any given second.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Temporal stability.
*   **The Risk:** The flickering can be distracting or annoying if not tuned correctly. False patterns may briefly appear due to random sampling coincidence.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing a single static sample of random points.
*   **Why it fails:** A single random sample may show false clusters or miss the average distribution entirely [@feng_matching_2010].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the plot moving? Do solid areas represent high probability?
*   **The Test:** Watch the plot for 10 seconds. Areas of high certainty should look like solid, stable structures. Uncertain outliers should flash in and out like sparks.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Implement a loop that draws $N$ samples using the Box-Muller transform (for normal distributions) and fades them out as new samples fade in.
