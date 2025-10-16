---
id: use-scatterplots-for-correlation
title: "Use scatterplots to visualize bivariate correlation"
tags:
  - impact:perceptual
  - chart:scatter
  - chart:parallel-coordinates
  - task:correlation
  - data:quantitative
  - visual:position
  - medium:static
  - medium:screen
evidence:
  strength: medium
  summary: "A 2016 Bayesian re-analysis of correlation perception data found that scatterplots offer the highest precision for judging both positive and negative correlation, with the lowest variance in performance between individual viewers."
sources:
  - type: research
    ref: "Kay & Heer, 2016"
    url: "https://doi.org/10.1109/TVCG.2015.2467671"
    note: "Primary re-analysis finding scatterplots to be the most precise and reliable visualization for correlation tasks across nine common chart types."
    role: primary
  - type: research
    ref: "Harrison et al., 2014"
    url: "https://doi.org/10.1109/TVCG.2014.2346979"
    note: "The original experimental data that was re-analyzed. The re-analysis led to different, more nuanced conclusions."
    role: related
---

## Guidance

When the primary goal is for the audience to assess the strength and direction of a relationship between two quantitative variables, use a scatterplot.

## Why

Scatterplots allow for the most precise human perception of correlation compared to many other common chart types like bar charts, line charts, or radial charts. They leverage position on a 2D plane, which is a highly effective visual channel for this task. The research shows they perform consistently well for both positive and negative correlations and exhibit low variance in performance across different viewers, making them a robust and reliable choice.

### Core Principle

Humans judge quantities more accurately by comparing positions along a common scale than by comparing less effective visual channels like angle, area, or color. For correlation, this principle translates to perceiving the shape and density of a point cloud encoded by position.

## When it applies

- When the primary task is to assess the strength and direction of a linear relationship between two continuous variables.
- When you need a visualization that works reliably for both positive and negative correlations.
- When designing for a general audience, as scatterplots show the lowest performance variability among individuals.

## Exceptions

- **Severe Overplotting:** If the dataset is very large and points overlap significantly, a simple scatterplot can become an unreadable blob. In this case, the guidance is still to use a position-based encoding, but with modifications.
- **Categorical Data:** This guidance applies to two quantitative variables. For other data types, different charts are more appropriate.

## Trade-offs

- A standard scatterplot does not explicitly show summary statistics like a regression line or confidence intervals, which may need to be added as a separate layer.
- While parallel coordinates can also be effective (especially for negative correlation), scatterplots are more consistently high-performing for both positive and negative correlations.

## Signs of Trouble

- **Wrong Tool for the Job:** A chart that uses a less effective channel for correlation (like angle in a pie chart or length in a stacked bar chart) is used to show a relationship between two variables.
- **Inconsistent Performance:** A chosen chart type (e.g., parallel coordinates) works well for negative correlations but poorly for positive correlations, leading to potential misinterpretation depending on the data.
- **Viewer Confusion:** The audience has difficulty determining if a relationship is strong or weak, or positive or negative.

## How to Improve

- **Quick Fix: Add an Annotation.** If you must use a less effective chart type, add a clear annotation stating the correlation coefficient (e.g., "Pearson's r = -0.85"). This provides the information directly, bypassing the perceptual challenge.

- **Moderate Approach: Modify the Scatterplot.** For datasets with overplotting, switch from solid points to hollow circles, reduce point opacity (alpha), or sample the data. This preserves the scatterplot format while mitigating density issues.

- **Comprehensive Approach: Replace the Chart.** Switch the visualization to a scatterplot. Ensure the aspect ratio is appropriate (often close to 1) to avoid distorting the perceived correlation strength. For very dense data, use a 2D histogram (heatmap) or contour plot, which still use the 2D plane but aggregate the points.