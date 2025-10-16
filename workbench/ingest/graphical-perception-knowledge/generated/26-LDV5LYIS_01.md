---
id: avoid-pcp-for-bivariate-correlation
title: "Avoid Parallel Coordinate Plots for Assessing Bivariate Correlation"

tags:
  - impact:perceptual
  - impact:cognitive
  - access:cognitive-load-risk
  - chart:parallel-coordinates
  - task:correlation
  - data:quantitative
  - medium:static
  - medium:screen
  - audience:general

evidence:
  strength: medium
  summary: "Li et al. (2010, n=25) found parallel coordinate plots (PCPs) are significantly less accurate and slower for judging correlation than scatterplots. PCPs also introduced a bias where users were more likely to perceive negative correlations."

sources:
  - type: research
    ref: Li, Martens, & van Wijk, 2010
    url: https://doi.org/10.1057/ivs.2008.13
    note: "Controlled experiment (n=25) demonstrated that PCPs led to lower accuracy, slower task completion, and a bias towards perceiving negative correlations when compared to scatterplots for judging correlation (p<0.05)."
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

Do not use a parallel coordinate plot (PCP) when the primary goal is for a user to accurately judge the correlation between two variables.

## Why

Judging correlation from a parallel coordinate plot relies on perceiving patterns from crossing lines, which is a perceptually difficult and error-prone task. Studies show that PCPs lead to significantly lower accuracy, slower task completion times, and can even introduce a bias towards seeing negative correlations when compared to the direct positional mapping of scatterplots.

### Core Principle

Choose visual encodings that minimize cognitive load and map directly to the analytical task. For assessing correlation, the angle and density of line crossings in a PCP are a much less effective and more biased encoding than the 2D position in a scatterplot.

## When it applies

- When your analysis or communication focuses on showing the strength or direction of a relationship between two specific quantitative variables.

## Exceptions

- This guideline applies specifically to the task of *judging correlation*. Parallel coordinate plots can be effective for other multivariate tasks, such as identifying clusters, filtering data across multiple dimensions, or spotting outliers in a high-dimensional dataset.

## Trade-offs

- By avoiding a PCP for a bivariate task, you lose the ability to show that same data in context with many other variables in a single compact chart. The most effective alternative for pairwise comparisons, a scatterplot matrix, requires more screen space.

## Signs of Trouble

- **User Confusion:** Viewers express difficulty or uncertainty when asked to describe the relationship between two axes in a parallel coordinate plot.
- **Line-Tracing Overload:** The plot is a dense "web" of crossing lines, making it impossible to discern a dominant trend between any two axes.
- **Inaccurate Takeaways:** Viewers incorrectly infer the strength or direction of a correlation, or exhibit a bias towards seeing negative correlations.

## How to Improve

- **Moderate Redesign:** If the two variables are the most important part of a multivariate display, pull them out and present them in a dedicated scatterplot, shown alongside the main parallel coordinate plot.
- **Comprehensive Redesign:** If the task is purely about bivariate correlation, replace the parallel coordinate plot with a scatterplot. If multiple pairwise comparisons are important, use a scatterplot matrix (SPLOM) to provide a clear, accurate view for each pair.