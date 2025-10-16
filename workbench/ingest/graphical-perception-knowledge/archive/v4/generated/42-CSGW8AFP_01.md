---
id: visualize-outlier-sensitive-trends
title: "Explicitly visualize trend lines when outliers are significant"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:ethical
  - impact:logos
  - chart:scatter
  - chart:line
  - task:trend
  - task:correlation
  - data:quantitative
  - data:outliers
  - audience:general
  - audience:expert
  - medium:static
sources:
  - type: research
    ref: Correll & Heer, 2017
    url: https://doi.org/10.1145/3025453.3025922
    note: "Found that viewers performing 'regression by eye' naturally down-weight or ignore outliers. Their visual estimates are closer to a robust fit (that excludes outliers) than a standard OLS fit (that includes them)."
---
## Guidance

When visualizing data with outliers that are analytically significant (i.e., they should be included in a trend model), you must explicitly plot the trend line. Do not rely on the viewer to perform "regression by eye."

## Why

Viewers naturally discount or ignore outliers when visually estimating trends. Their mental model of the trend will be robust to outliers, resembling a regression where outliers are removed (a "robust fit"). If those outliers are analytically important and should influence the trend (as in a standard Ordinary Least Squares regression), this creates a misunderstanding between the viewer's perception and the intended statistical model.

## When it applies

- When visualizing data that contains extreme values or outliers.
- When the analytical goal requires a model (like OLS regression) that is sensitive to these outliers.
- When it is critical that the audience understands the influence of extreme data points on the overall trend (e.g., how one large sale affects the average).

## Exceptions

- If the analytical goal is to perform a robust analysis and intentionally down-weight outliers. In this case, the audience's natural tendency aligns with the goal, though showing a calculated robust trend line would still be clearer.
- During early-stage exploratory analysis where the user's task is to identify and decide whether certain points should be treated as outliers.

## Trade-offs

- **Clutter vs. Precision:** Adding an explicit trend line adds visual complexity.
- **Flexibility vs. Specificity:** Relying on "regression by eye" allows for flexible interpretation, while plotting a specific trend line (e.g., OLS) imposes a single statistical model on the viewer, which may not always be desirable.

## Signs of Trouble

- **Divergent Conclusions:** A viewer looking at a scatter plot with outliers reaches a different conclusion about the trend than what a statistical OLS model indicates.
- **Ignoring Extremes:** Viewers describe the trend based only on the dense cluster of points, dismissing outliers as "errors" or "flukes" when they are in fact significant data points.
- **"Robust by Default" Perception:** The audience is unaware of how much a few extreme points are pulling the "true" average trend up or down.

## How to Improve

- **Quick Fix: Highlight the Outliers.** Use a different color, size, or shape to draw attention to the outlier points. This signals their potential importance, though it doesn't guarantee viewers will correctly incorporate them into their mental trend line.

- **Moderate Redesign: Add the OLS Trend Line.** Overlay a standard regression line (e.g., Ordinary Least Squares) that is calculated including the outliers. This makes the influence of the outliers on the overall trend explicit and clear.

- **Comprehensive Redesign: Show Both Models.** For more expert audiences, visualize both the robust trend line (ignoring outliers) and the OLS trend line (including outliers). Label them clearly (e.g., "Trend without extreme values" vs. "Overall trend including all data"). This powerfully communicates the precise impact of the outliers on the model.