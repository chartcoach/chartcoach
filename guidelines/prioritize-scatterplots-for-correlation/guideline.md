---
id: prioritize-scatterplots-for-correlation
title: Prioritize Scatterplots for Precise Correlation Estimates
bibliography: references.bib
description: Use scatterplots as the standard for correlation tasks due to their high,
  symmetric perceptual precision.
labels:
- chart:scatterplot
- task:correlate
- visual:position
- impact:precision
- data:quantitative
---

## The Rule <!-- role: advice -->
Use scatterplots as the primary visualization choice when users need to accurately judge the correlation between two quantitative variables.

## The Logic <!-- role: reason -->
Scatterplots allow for correlation judgments that consistently follow Weber’s Law, meaning human perception of correlation behaves linearly and predictably with the data's statistical properties. According to research collated by [@zeng_review_2023], scatterplots provide a high baseline of precision (low Just Noticeable Difference or JND). Evidence from [@harrison_ranking_2014] demonstrates that scatterplots perform robustly for both positive and negative correlations, unlike other chart types that suffer from performance asymmetries.

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to estimate the strength of a relationship (r-value) or compare correlations between two datasets.
*   **Data Type:** Bivariate quantitative data.
*   **Audience:** General and expert users, as the perceptual mechanism is fundamental.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset is extremely large causing severe overplotting.
*   **Reason:** While the perceptual law holds, the visual encoding becomes occluded. Density plots or binned scatterplots may be required, though they were not tested in this specific ranking.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Scatterplots consume significant screen space to maintain the aspect ratio required for accurate judgment.
*   **The Risk:** Using alternative compact charts (like radar or donuts) to save space will significantly degrade the user's ability to detect correlation differences.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using "Donut Charts" or "Radar Charts" to show correlation in dashboards to save space.
*   **Why it fails:** The experimental rankings show these radial transforms result in significantly higher JNDs (lower precision) compared to standard Cartesian scatterplots [@harrison_ranking_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using angle, area, or slope to represent the relationship between two variables?
*   **The Test:** If you replace the chart with a scatterplot, does the relationship become immediately clearer?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the chart type to a standard point-mark scatterplot.
*   **Best Fix:** Ensure the scatterplot axes are scaled appropriately to avoid distorting the perceived correlation.
