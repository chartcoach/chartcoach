---
id: use-scatterplots-for-correlation
title: "Use scatterplots to visualize bivariate correlation"
tags:
  - impact:perceptual
  - impact:logos
  - chart:scatter
  - task:correlation
  - data:quantitative
  - audience:general
  - medium:static
  - medium:interactive
evidence:
  strength: high
  summary: "A 2016 Bayesian re-analysis of data from Harrison et al. (2014) found that scatterplots offer the highest perceptual precision for judging correlation. They also have the lowest performance variability among individuals for both positive and negative correlations, making them the most robust and reliable choice."
sources:
  - type: research
    ref: Kay & Heer, 2016
    url: https://doi.org/10.1109/TVCG.2015.2467671
    note: "Primary study. Bayesian re-analysis of Harrison et al. (2014) data, establishing a partial ranking. Found scatterplots to be in the 'high precision' group with low inter-subject variance (Figures 8 & 9)."
    role: primary
  - type: research
    ref: Harrison et al., 2014
    url: https://doi.org/10.1109/TVCG.2014.2346979
    note: "The original experiment whose data was re-analyzed. It provided the initial rankings that Kay & Heer refined."
    role: supporting
---

## Guidance

To enable viewers to accurately assess the relationship (correlation) between two quantitative variables, use a scatterplot.

## Why

Scatterplots provide the highest perceptual precision for judging correlation compared to many other common chart types, including bar charts, line charts, and radial charts. They also exhibit the least amount of performance variation between different people, making them a robust and reliable choice for a general audience.

### Core Principle

Humans are best at judging correlation from the shape, orientation, and tightness of a cloud of points (as in a scatterplot). This is a more direct perceptual task than interpreting correlation from overlaid lines, varying bar lengths, or segment areas, which can be ambiguous.

## When it applies

- When the primary goal is to show the strength and direction of the relationship between two continuous variables.
- When you need a reliable visualization that performs consistently well for a wide range of viewers.

## Exceptions

- If one of the variables is time, a line chart is a strong, conventional alternative for showing trends, though a scatterplot can still be effective.
- When visualizing a large number of variable pairs simultaneously, a correlation matrix (heatmap) offers a more compact overview, though it is less precise for judging the correlation in any single pair.

## Trade-offs

- Scatterplots can suffer from overplotting when data density is high. This can obscure the true correlation by hiding the number of points in a dense area. This often requires mitigation techniques like adjusting point transparency (alpha-blending), sampling the data, or switching to a 2D density plot or heatmap.

## Signs of Trouble

- **Misleading Patterns:** Viewers consistently misjudge the strength or direction of a correlation when it's shown in a non-scatterplot format (e.g., a stacked bar chart or radar chart).
- **High Variance:** Different team members arrive at wildly different conclusions about the same data when using an alternative chart type.
- **Ambiguous Encodings:** The chart uses visual channels like angle (pie/donut chart) or area (stacked area chart) to implicitly encode correlation, which are known to be difficult for humans to judge accurately.

## How to Improve

- **Quick Fix: Add an Annotation.** If you must use a less effective chart type, add the correlation coefficient (e.g., "Pearson's r = -0.85") as a direct text annotation to provide an unambiguous, quantitative escape hatch for the user.

- **Comprehensive Redesign: Switch to a Scatterplot.** Replace the existing visualization (e.g., parallel coordinates, radar chart) with a scatterplot. This provides the most perceptually accurate representation of the correlation, ensuring most viewers will interpret it correctly.
