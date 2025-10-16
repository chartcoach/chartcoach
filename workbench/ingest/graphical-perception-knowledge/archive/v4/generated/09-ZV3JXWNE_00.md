---
id: use-scatterplot-for-correlation
title: "Use scatterplots to show the relationship between two quantitative variables"
tags:
  - impact:perceptual
  - chart:scatter
  - task:correlation
  - data:quantitative
sources:
  - type: research
    ref: Kay & Heer, 2016
    url: https://doi.org/10.1109/TVCG.2015.2467671
    note: "Primary source providing strong evidence. Found scatterplots offer high precision and low individual variance for both positive and negative correlations."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Meta-analysis (Table 9) confirms scatterplots are a top choice for correlation tasks based on a review of the literature."
  - type: research
    ref: Harrison et al., 2014
    url: https://doi.org/10.1109/TVCG.2014.2346979
    note: "Original study whose data was re-analyzed by Kay & Heer (2016)."
---

## Guidance

For visualizing and assessing the correlation between two continuous variables, a scatterplot is the most effective and reliable choice.

## Why

Scatterplots offer the highest perceptual precision for estimating correlation compared to other common chart types. Research shows they perform robustly for both positive and negative correlations and exhibit low variance in performance among different viewers, making them a consistently understandable choice.

## When it applies

- When the primary task is to assess the strength and direction of the relationship between two quantitative variables.

## Exceptions

- If one of the variables is time, a line chart might be more conventional, although a scatterplot can still be effective for showing correlation against time.
- For very large datasets, overplotting can obscure the distribution. In these cases, use techniques like transparency (alpha), sampling, or binning (e.g., a 2D histogram or heatmap).

## Trade-offs

- For a high number of variables, a scatterplot matrix (SPLOM) can become large and difficult to navigate. In these cases, a parallel coordinates plot might be better for exploratory analysis, but not for judging specific correlations.

## Signs of Trouble

- **Wrong Tool for the Job:** Another chart type (like a parallel coordinates plot, stacked area chart, or radar chart) is being used to make a claim about correlation.
- **Inconsistent Judgements:** Viewers draw different conclusions about the strength or direction of the trend shown in the chart.

## How to Improve

- **Comprehensive Redesign: Switch to a Scatterplot.** If another chart type is being used to show correlation, replace it with a scatterplot to improve perceptual accuracy and consistency. For multiple variables, use a scatterplot matrix.