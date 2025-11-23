---
id: prefer-lightness-over-size-for-centroid-estimation
title: Prefer Lightness Over Size for Centroid Estimation
bibliography: references.bib
description: Use lightness instead of size in trivariate scatterplots to improve accuracy
  when users need to estimate the mean position.
labels:
- chart:scatter
- visual:size
- visual:color
- task:aggregate
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
When designing trivariate scatterplots (X, Y, and a third variable), use **color lightness** rather than **mark size** if the user needs to accurately estimate the center (mean position) of the data points.

## The Logic <!-- role: reason -->
Users naturally misjudge the spatial mean of a scatterplot when the points vary in visual weight. This is known as the "Weighted Average Illusion" [@hong_weighted_2022]. According to data collated by Zeng and Battle [@zeng_review_2023], scatterplots using **size** (area) encodings resulted in significantly higher error rates for aggregation tasks compared to those using **lightness**. Large marks distort the perceived center of mass more aggressively than dark marks do, making lightness a safer choice for preserving spatial summary statistics.

*   **The Principle:** Weighted Average Illusion / Feature-Based Attention
*   **The Evidence:** [@hong_weighted_2022] via [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to determine the "average" location of the data (e.g., "Where is the center of the cluster?").
*   **Data Type:** Quantitative data mapped to X, Y, and a third quantitative variable.
*   **Audience:** General analysts or public audiences interpreting spatial distributions.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user specifically needs to find the *weighted* mean (e.g., "Where is the center of revenue?" rather than "Where is the center of stores?").
*   **Reason:** In this case, the "illusion" aligns with the analytical goal—the larger/darker points *should* pull the mean toward them.
*   **Scenario:** The user needs to read precise individual values for the third variable.
*   **Reason:** Size is generally more effective than lightness for distinguishing specific point values, even if it hurts ensemble (summary) perception.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the pop-out effect of size for individual outliers.
*   **The Risk:** Lightness scales can be harder to read precisely than size scales for individual point comparison (e.g., distinguishing 40% gray from 50% gray).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a bubble chart (size encoding) and adding a crosshair for the true mean.
*   **Why it fails:** The visual weight of the large bubbles will still cause a cognitive conflict, making the true mean look "wrong" to the user.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using circles of varying sizes to represent a third variable?
*   **The Test:** Ask a user to click where they think the "average" point is. If they click significantly closer to the largest bubbles than the geometric center, the design is biasing their perception.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the encoding of the third variable from `size` to `color` (specifically lightness/luminance).
*   **Best Fix:** If using size is mandatory, provide an explicit visual indicator (like a centroid mark or reference lines) to show the true spatial mean.
