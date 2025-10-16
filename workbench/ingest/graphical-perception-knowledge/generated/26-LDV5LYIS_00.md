---
id: use-scatterplots-for-correlation
title: "Use Scatterplots Over Parallel Coordinates for Assessing Correlation"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:scatter
  - chart:parallel-coordinates
  - task:correlation
  - data:quantitative
  - visual:position
  - medium:static
  - medium:screen
  - audience:general

evidence:
  strength: medium
  summary: "Li et al. (2010, n=25) found scatterplots are significantly more accurate and faster for judging correlation than parallel coordinate plots. Users could distinguish twice as many correlation levels with scatterplots and were less biased in their judgments."

sources:
  - type: research
    ref: Li, Martens, & van Wijk, 2010
    url: https://doi.org/10.1057/ivs.2008.13
    note: "Controlled experiment (n=25) showed that users can distinguish twice as many correlation levels with scatterplots compared to parallel coordinate plots. Scatterplots were also significantly faster and less prone to bias (p<0.05)."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This paper's methodology for collating graphical perception knowledge was used to structure the findings from the primary source."
    role: related

tools: []

examples: []
---

## Guidance

To help viewers accurately and efficiently assess the relationship between two quantitative variables, use a scatterplot instead of a parallel coordinate plot.

## Why

Scatterplots leverage the direct, two-dimensional mapping of variables to position, which is a highly effective channel for perceiving correlation. Experiments show that viewers can distinguish about twice as many different levels of correlation with scatterplots compared to parallel coordinate plots. They also perform the task more quickly and with less bias.

### Core Principle

Match the visual structure to the analytical task. For assessing bivariate correlation, a direct 2D spatial mapping is perceptually superior to encoding variables on separate parallel axes, which requires interpreting patterns of crossing lines.

## When it applies

- When the primary goal is for the user to understand the strength and direction of the correlation between two continuous variables.
- When comparing the effectiveness of different chart types for a correlation task.

## Exceptions

- Parallel coordinate plots are designed for showing relationships across *many* variables (>2), not just two. If the task is to compare multivariate patterns or identify clusters across multiple dimensions, a parallel coordinate plot may be appropriate. However, assessing the specific correlation between any two individual variables will remain difficult.

## Trade-offs

- A single scatterplot can only show the relationship between two variables at a time. To compare many variables, you would need a scatterplot matrix (SPLOM), which takes up significantly more space than a single parallel coordinate plot.

## Signs of Trouble

- **Slow Interpretation:** Viewers take a long time to determine the correlation from a chart, often tracing lines back and forth in a parallel coordinate plot.
- **Misinterpreted Strength:** Users consistently over- or under-estimate the strength of a relationship.
- **Negative Bias:** When using a parallel coordinate plot, users report seeing negative correlations where none exist or exaggerate the strength of weak negative ones.

## How to Improve

- **Quick Fix:** If you must use a parallel coordinate plot, add a clear annotation stating the calculated correlation coefficient (e.g., "Pearson's r = 0.85"). This provides an "escape hatch" from the difficult perceptual task by giving the user the exact answer.
- **Comprehensive Approach:** Replace the parallel coordinate plot with a scatterplot for the two variables of interest. If multiple variables are involved and pairwise correlations are important, use a scatterplot matrix (SPLOM) to allow for clear and accurate correlation assessment for every pair.
