---
id: expect-overestimation-in-point-graphs
title: Expect Overestimation Bias in Point Graphs
bibliography: references.bib
description: Users tend to slightly overestimate the mean value when viewing point
  graphs, contrasting with the underestimation in bar charts.
labels:
- chart:scatter
- chart:dot-plot
- task:aggregate
- visual:position
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Be aware that point marks (dot plots) cause users to slightly overestimate the mean, but prefer them over bars to avoid significant underestimation.

## The Logic <!-- role: reason -->
Unlike bar charts which pull the perceived mean downward, point marks (which use position rather than length/area) result in a perception that is either slightly higher than the mean or closer to the center, avoiding the "within-the-bar" bias.
*   **The Principle:** Overestimation Bias (vs. Underestimation). The lack of a filled area extending to the axis changes how the eye calculates the visual centroid.
*   **The Evidence:** In the collation by Zeng and Battle [@zeng_review_2023], findings from Godau et al. [@godau_perception_2016] indicate that while bars are underestimated, point graphs resulted in participants significantly overrating the mean (Design E-4).

## Where to Apply <!-- role: context -->
*   **User Goal:** Summary tasks where avoiding underestimation is critical.
*   **Data Type:** Univariate quantitative data plotted as points along an axis.
*   **Audience:** Users comparing the general performance of two groups (e.g., Point Graph vs. Bar Graph).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** In safety-critical contexts where overestimating a value (e.g., a risk factor or cost) is more dangerous than underestimating it.
*   **Reason:** The positive bias in point graphs might lead to optimistic interpretations that are unsafe in specific domains.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Point graphs may feel less "grounded" than bar charts and can be harder to scan if the points are sparse.
*   **The Risk:** You trade a strong negative bias (bars) for a slight positive bias (points), rather than achieving perfect accuracy.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assuming point graphs provide a perfectly neutral perception of the mean.
*   **Why it fails:** Godau et al. [@godau_perception_2016] showed that point graphs are not bias-free; they simply bias in the opposite direction (overestimation) compared to bars.

## How to Check <!-- role: check -->
*   **Visual Sign:** A strip plot or dot plot used to show a distribution.
*   **The Test:** Check if the data contains outliers at the high end; point graphs may exacerbate the visual pull of high outliers compared to anchored bars.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a median or mean line to the point graph.
*   **Best Fix:** Use a visualization that aggregates the data mathematically (like a box plot or error bar) rather than relying on the user's visual aggregation.
