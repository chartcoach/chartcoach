---
id: minimize-encoding-range-to-reduce-centroid-bias
title: Minimize Encoding Range to Reduce Centroid Bias
bibliography: references.bib
description: Restrict the contrast range of size or lightness in scatterplots to prevent
  the weighted average illusion.
labels:
- chart:scatter
- visual:size
- visual:color
- task:aggregate
- impact:bias
- complexity:intermediate
---

## The Rule <!-- role: advice -->
Restrict the **range** of your visual encoding (the difference between the smallest/lightest and largest/darkest marks) in trivariate scatterplots to minimize bias in mean position estimation.

## The Logic <!-- role: reason -->
The "Weighted Average Illusion" creates a systematic bias where the perceived mean is pulled toward "heavy" (large or dark) data points. Experimental results from Hong et al. [@hong_weighted_2022], collated in the review by Zeng and Battle [@zeng_review_2023], indicate that **wide encoding ranges** (high contrast) significantly increase this bias. When the difference between the minimum and maximum visual intensity is large (e.g., tiny dots vs. huge bubbles), the user's attention is disproportionately captured by the heavy marks, skewing their perception of the group's location.

*   **The Principle:** Feature-Based Attention / Ensemble Coding Bias
*   **The Evidence:** [@hong_weighted_2022] via [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Assessing the general distribution or correlation of X and Y without being misled by the third variable (Z).
*   **Data Type:** Trivariate scatterplots where the third variable (Z) is correlated with position (X or Y).
*   **Audience:** Users performing aggregate tasks (e.g., "What is the general trend?").

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset contains critical outliers that must be highlighted.
*   **Reason:** A narrow range might make critical high-value data points indistinguishable from the rest of the dataset.
*   **Scenario:** The visualization is intended for dramatic effect rather than statistical precision.
*   **Reason:** High contrast (wide range) is more visually engaging, even if it distorts the spatial mean.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Reduced discriminability.
*   **The Risk:** By narrowing the range (e.g., making the smallest dot 5px and the largest 10px, rather than 2px and 20px), users may struggle to tell the difference between medium and high values.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "0 to Max" scale for size where the smallest value is 0 pixels.
*   **Why it fails:** This creates the widest possible range, maximizing the bias.
*   **The Wrong Fix:** Using pure white to pure black for lightness.
*   **Why it fails:** High contrast creates a strong "pull" toward the black points.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the largest points dominate the screen real estate? Are the lightest points nearly invisible?
*   **The Test:** Calculate the ratio between your maximum and minimum visual values. If the size ratio is extreme (e.g., > 10:1 area), bias is likely high.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the minimum size of the smallest dots or darken the lightest colors (clamp the lower bound).
*   **Best Fix:** Use a `log` scale or a compressed `linear` range for the third dimension to reduce the visual dominance of high values.
