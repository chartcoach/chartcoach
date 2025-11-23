---
id: emphasize-perpendicular-dispersion-scatterplots
title: Emphasize the Perpendicular Width of the Point Cloud
bibliography: references.bib
description: Design scatterplots to highlight the dispersion of points perpendicular
  to the regression line, as this is the primary visual proxy humans use to estimate
  correlation.
labels:
- chart:scatter
- task:correlation
- visual:position
- visual:shape
- impact:accuracy
- audience:general
---

## The Rule <!-- role: advice -->
When designing scatterplots for correlation tasks, explicitly maximize the visibility of the point cloud's "thickness" (dispersion) perpendicular to the regression line. Ensure the "minor axis" of the data shape is the most salient visual feature.

## The Logic <!-- role: reason -->
Humans do not perceive the statistical concept of correlation ($r$) directly. Instead, they use visual features as proxies to make heuristic judgments.
*   **The Principle:** Visual Proxies for Correlation.
*   **The Evidence:** @yang_correlation_2019 identified 49 candidate visual features and found that four specific features best predicted human judgment:
    1.  The standard deviation of perpendicular distances to the regression line (`dist_line_sd`).
    2.  The area of the prediction ellipse (`ellipse_area`).
    3.  The length of the minor axis of the prediction ellipse (`ellipse_minor`).
    4.  The perpendicular side of the confidence bounding box (`conf_bounding_box_perp`).
    These features all relate to the geometric *density* and *width* of the point cloud. If these features are obscured, perception of correlation fails.

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating the strength of a relationship between two variables or comparing the correlation of two different datasets.
*   **Data Type:** Bivariate quantitative data (standard scatterplot data).
*   **Audience:** Any user relying on rapid visual inspection to gauge statistical relationships.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Outlier Detection.
*   **Reason:** If the user's goal is to find specific anomalies rather than judge the overall relationship, emphasizing the aggregate "cloud shape" might distract from individual deviant points.
*   **Scenario:** Sparse Data.
*   **Reason:** With very few data points ($N < 10$), a "cloud" or "ellipse" shape does not visually form, rendering these geometric proxies unstable or invisible.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Individual point resolvability. To emphasize the aggregate shape (the "ellipse"), you may need to use smaller points or opacity, which makes identifying specific values harder.
*   **The Risk:** Users may perceive a "tight" relationship solely because the chart is physically small or compressed, even if the statistical variance is high (if axis scales are not handled carefully).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Drawing the regression line without showing the points clearly.
*   **Why it fails:** The regression line shows the *trend* (slope) but eliminates the *dispersion* information (`dist_line_sd`) that users actually rely on to judge the strength of the correlation @yang_correlation_2019.
*   **The Wrong Fix:** Using large, opaque markers in dense datasets.
*   **Why it fails:** This creates a "blob" where the internal density and the precise width of the minor axis are obscured by overplotting, making the correlation appear higher or lower than it is.

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you draw an imaginary ellipse around the data? Is the "short side" (width) of that ellipse clearly defined?
*   **The Test:** Look at the chart and try to estimate the "fatness" of the cloud. If the edges of the cloud are fuzzy or the center is a solid block of color, the visual proxy is broken.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Adjust marker opacity (alpha blending) and size so the density gradient perpendicular to the trend is visible.
*   **Best Fix:** Ensure the aspect ratio and axis scales preserve the geometric integrity of the `ellipse_minor` (the width of the cloud) so it reflects the statistical dispersion accurately.
