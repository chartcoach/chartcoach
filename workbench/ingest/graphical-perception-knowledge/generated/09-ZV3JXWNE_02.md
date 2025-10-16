---
id: parallel-coordinates-negative-correlation
title: "Recognize that parallel coordinates are more effective for negative correlation than for positive"
tags:
  - impact:perceptual
  - chart:parallel-coordinates
  - task:correlation
  - data:quantitative
evidence:
  strength: high
  summary: "Kay & Heer's (2016) Bayesian re-analysis of Harrison et al.'s (2014) data placed parallel coordinates in the 'high precision' group for visualizing negative correlation, but only in the 'medium precision' group for positive correlation. This indicates a significant performance difference based on the correlation's sign."
sources:
  - type: research
    ref: Kay & Heer, 2016
    url: https://doi.org/10.1109/TVCG.2015.2467671
    note: "The analysis in Figure 8 clearly separates 'parallel coordinates - negative' (high precision) from 'parallel coordinates - positive' (medium precision), demonstrating the performance asymmetry."
    role: primary
  - type: research
    ref: Harrison et al., 2014
    url: https://doi.org/10.1109/TVCG.2014.2346979
    note: "The original study providing the data that revealed this performance difference."
    role: supporting
---

## Guidance

When using parallel coordinates plots, be aware that they are highly effective for helping viewers perceive negative correlations but are significantly less effective for perceiving positive correlations.

## Why

The visual pattern for a strong negative correlation in a parallel coordinates plot is a very distinct and easily identifiable "X" crossing pattern between two axes. The pattern for a strong positive correlation—a series of parallel lines—is less distinct, and judging its strength (i.e., how parallel the lines are) is a more difficult perceptual task, leading to lower precision.

## When it applies

- When using parallel coordinates to explore relationships between multiple variables.
- When a key analysis task is to identify and compare the strength of negative correlations.

## Exceptions

- This guidance is specific to the task of judging correlation. Parallel coordinates plots have other uses, such as identifying clusters or outliers, where this specific asymmetry may be less relevant.

## Trade-offs

- **Inconsistent Performance:** If your dataset contains a mix of positive and negative correlations, a parallel coordinates plot will provide an inconsistent user experience, where negative correlations are easier to spot than positive ones.
- **Superior Alternatives:** A scatterplot matrix (SPLOM) provides a more consistent level of perceptual precision for judging both positive and negative correlations across all pairs of variables.

## Signs of Trouble

- **Missed Positive Correlations:** Users fail to identify strong positive correlations in the data when using a parallel coordinates plot, even when those same relationships are obvious in a scatterplot.
- **Inconsistent Judgments:** Users are adept at finding and ranking negative correlations but struggle with judging the strength of positive ones.

## How to Improve

- **Comprehensive Redesign: Use a Scatterplot Matrix (SPLOM).** If consistent performance for judging all correlation types is critical, the best approach is to replace the parallel coordinates plot with a scatterplot matrix. Each cell in the matrix provides a high-precision view of a single relationship.

- **Moderate Approach: Augment with Annotations.** If you must use parallel coordinates, consider automatically calculating and annotating pairs of axes with their correlation coefficient (e.g., `r = 0.8`). This compensates for the perceptual weakness in judging positive correlations by providing an explicit value.
