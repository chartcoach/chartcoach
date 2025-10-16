---
id: avoid-area-charts-for-trend-estimation
title: "Avoid area charts for estimating trends accurately"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:area
  - chart:line
  - chart:scatter
  - task:trend
  - task:correlation
  - data:quantitative
  - data:temporal
  - visual:area
  - visual:position
  - audience:general
  - medium:static
  - access:cognitive-load-risk
sources:
  - type: research
    ref: Correll & Heer, 2017
    url: https://doi.org/10.1145/3025453.3025922
    note: "Found that area charts introduce a systematic under-estimation of trend intercepts (a 'within-the-area' bias), leading to less accurate trend estimation compared to scatter plots or line charts."
---
## Guidance

Avoid using area charts when the primary goal is for viewers to estimate or judge trends in the data. Line charts and scatter plots lead to more accurate perceptual estimates of trends.

## Why

Area charts create a "within-the-area" perceptual bias. Viewers tend to systematically underestimate the trend's intercept because they perceive points within the filled area as more likely or representative. This leads to less accurate trend estimations compared to visually symmetric charts like line graphs or scatter plots, where there is no filled region to create such a bias.

## When it applies

- When visualizing bivariate data, especially time-series, where understanding the trend is a key objective.
- When the viewer's task is to judge the slope, intercept, or overall trajectory of the data by eye.
- When the accuracy of trend perception is more important than showing a part-to-whole relationship or total volume.

## Exceptions

- When the main goal is to show the cumulative total or volume over time, and trend estimation is a secondary, less critical task. For example, in a stacked area chart showing the composition of a total over time.
- When using a streamgraph (a type of area chart) to show changes in distribution over time, though be aware that estimating the trend of any single category remains challenging.

## Trade-offs

- **Clarity vs. Volume:** Area charts effectively convey volume and a sense of cumulative quantity. Switching to a line chart improves trend estimation accuracy but loses this explicit visual representation of volume. The line chart focuses purely on the trend of the data points.

## Signs of Trouble

- **Underestimation Bias:** Users consistently interpret the trend as being lower or having a lower intercept than it actually does. For example, they might estimate a starting value of 80 when it is actually 100.
- **Misjudged Intercept:** When asked to estimate the starting point or general level of a trend in an area chart, viewers' estimates are systematically low.
- **Focus on Volume, not Trend:** User discussions about an area chart center exclusively on the total volume, while missing or misinterpreting the underlying rate of change.

## How to Improve

- **Quick Fix: Add a Trend Line.** Overlay an explicit, statistically calculated trend line onto the area chart. This provides a clear visual guide, helping to counteract the chart's inherent perceptual bias, but does not fully eliminate it.

- **Moderate Redesign: Switch to a Line Chart.** Change the chart type from an area chart to a line chart. This is a simple change in most visualization tools and is highly effective at removing the "within-the-area" bias, leading to more accurate trend perception.

- **Comprehensive Redesign: Use a Scatter Plot.** If the data is not a strictly continuous series, or if you want to avoid the implication of connection between points, use a scatter plot. This removes the bias and provides a neutral representation of the data points, allowing for unbiased trend estimation.