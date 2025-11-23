---
id: stack-charts-vertically-for-summary-comparison
title: Stack Charts Vertically to Compare Averages and Ranges
bibliography: references.bib
description: Arrange small multiple bar charts vertically (stacked) rather than overlaying
  them when comparing summary statistics.
labels:
- chart:bar
- chart:small-multiples
- task:aggregate
- task:compare
- task:determine-range
- visual:position
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Arrange bar charts vertically (one on top of the other) when the user needs to compare summary statistics like the mean or the range of two datasets. Do not superpose (overlay) them.

## The Logic <!-- role: reason -->
Vertical stacking allows the viewer to perform "global" visual comparisons rather than "focal" item-by-item comparisons. As collated by Zeng et al. [@zeng_review_2023], experiments by Jardine et al. [@jardine_perceptual_2020] indicate that viewers use perceptual proxies—such as estimating the "mean length" or the "hull area" of the entire chart—to judge averages and ranges. Vertical alignment facilitates slicing downward to extract these global lengths or areas more precisely than overlaid or horizontal arrangements.

*   **The Principle:** Global Perceptual Proxies
*   **The Evidence:** [@jardine_perceptual_2020] via [@zeng_review_2023]

## Where to Apply <!-- role: context -->
This advice applies when the analytic task involves assessing the properties of the set as a whole, rather than individual data points.

*   **User Goal:** Comparing aggregate values (e.g., "Which group has a higher average?") or variability (e.g., "Which group has a wider range?").
*   **Data Type:** Multiple series of quantitative values across nominal categories (e.g., bar charts).
*   **Audience:** General audiences performing visual analysis tasks.

## When to Break It <!-- role: exceptions -->
The ranking of visualization effectiveness flips when the task changes from "global" summary to "local" point identification.

*   **Scenario:** Finding the specific item that changed the most (Maximum Delta) or judging Correlation.
*   **Reason:** As noted in the literature review by Jardine et al. [@jardine_perceptual_2020], superposed (overlaid) or animated charts perform better for item-level comparisons because they support focal processing.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Vertical stacking consumes significant vertical screen space, which may require scrolling if many charts are involved.
*   **The Risk:** If the charts are too far apart vertically, the eye cannot easily "slice" through them to compare the hull areas.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Superposing (overlaying) two bar charts on top of each other using transparency or different colors.
*   **Why it fails:** Jardine et al. [@jardine_perceptual_2020] found that superposition was the least effective design (ranking 4th out of 4) for comparing means and ranges, likely because the visual clutter forces the eye into "focal" mode, inhibiting the ability to see the shape of the data distribution as a whole.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are two sets of bars occupying the exact same x/y pixel space (overlapping)?
*   **The Test:** Ask, "Am I trying to see which whole group is larger, or which specific bar is larger?" If it's the whole group, separate them vertically.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Move the charts to separate rows (facet by row) so they sit one above the other sharing a common X-axis.
*   **Best Fix:** Implement a "Stacked" small multiple layout as defined in the experimental setup of Jardine et al. [@jardine_perceptual_2020] (Design E-1).
