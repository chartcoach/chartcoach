---
id: use-parallel-coordinates-for-multivariate-exploration
title: "Use parallel coordinates for multivariate cluster and anomaly detection"
tags:
  - impact:perceptual
  - chart:parallel-coordinates
  - task:cluster
  - task:find-anomalies
  - task:retrieve-value
  - data:quantitative
sources:
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Meta-analysis (Table 9) identifies parallel coordinates as an effective choice for cluster, find anomalies, and retrieve value tasks, citing Kanjanabose et al. 2015 [42]."
---

## Guidance

Consider using a parallel coordinates plot for the exploratory analysis of multivariate data, especially for tasks that involve identifying clusters of similar items, finding outliers (anomalies), and retrieving the values of a specific item across multiple dimensions.

## Why

In a parallel coordinates plot, each data item is represented as a line connected across multiple parallel axes. This structure allows for unique patterns to emerge: clusters of similar items form visible "bundles" of lines with similar paths, while anomalies often appear as lines that follow a path dramatically different from the main bundles. This makes it a powerful tool for discovering structure in high-dimensional datasets.

## When it applies

- When analyzing datasets with multiple quantitative variables (typically 4 or more).
- When the goal is exploratory: to understand relationships between many variables, find natural groupings of data points, or spot unusual data points.

## Exceptions

- **Do not use for correlation.** Parallel coordinates are notoriously poor for accurately judging the correlation between any two variables. For that task, use a scatterplot or scatterplot matrix.
- The order of the axes dramatically impacts which patterns are visible. Therefore, parallel coordinates are most effective in an interactive environment where the user can reorder axes.

## Trade-offs

- The chart can become cluttered and unreadable with a very large number of data points (lines), a problem known as overplotting.
- Interpretation is highly dependent on the order of the axes. A meaningful pattern between two variables might be completely invisible if their axes are not adjacent.

## Signs of Trouble

- **Correlation Claims:** A parallel coordinates plot is being presented as the primary evidence for a strong or weak correlation between two variables.
- **Static and Arbitrary:** The visualization is static, and the axes are in an arbitrary order, likely hiding more patterns than it reveals.
- **Overplotting:** The plot is a solid mass of color, making it impossible to discern individual lines or bundles.

## How to Improve

- **Quick Fix: Add Interactivity.** If possible, allow users to reorder axes and brush/highlight lines. Brushing enables a user to select a subset of lines and see their path across all axes, which is crucial for exploration.
- **Moderate approach: Reduce Overplotting.** Use transparency (alpha blending) to reveal the density of lines and make bundles more apparent. For very large datasets, consider sampling the data or using binned parallel coordinates.
- **Comprehensive approach: Supplement with Other Views.** Combine a parallel coordinates plot with other views, such as a scatterplot matrix (SPLOM). Use the parallel coordinates for an overview and identifying clusters, then use the SPLOM to accurately investigate the specific correlations between pairs of variables.