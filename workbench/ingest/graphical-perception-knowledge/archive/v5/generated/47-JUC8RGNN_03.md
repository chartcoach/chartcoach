---
id: use-box-plots-for-spread
title: "Use box plots to compare data spread across categories"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:box-plot
  - task:distribution
  - task:compare
  - data:quantitative
  - data:temporal
  - audience:expert
  - visual:length
  - medium:static
  - medium:screen
evidence:
  strength: medium
  summary: "An experiment on comparing data spread (absolute deviation) across time periods found that box plots were the most effective method, achieving 85% accuracy. This performance significantly surpassed all other tested chart types, including line charts (49%) and colorfields (58%)."
sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "Primary experiment showing box plots are superior for comparing statistical spread, as they encode it directly."
    role: primary
---

## Guidance

For tasks that require comparing the statistical spread, variance, or consistency of data across different groups or time periods, use box plots.

## Why

Box plots are specifically designed to encode a measure of spread (the interquartile range) directly through the height of the central box. This transforms what would be a difficult visual summarization task (mentally calculating variance from raw data) into a much simpler and more accurate perceptual task: comparing the lengths of several boxes.

### Core Principle

Directly encode the statistical property of interest to make its comparison perceptually trivial for the viewer.

## When it applies

- The primary goal is to determine which category or group has more or less variance in its data.
- When comparing the consistency or stability of a measure across different groups.

## Exceptions

- **Audience Familiarity:** Box plots are a statistical abstraction and may not be familiar to all audiences. If the audience is not statistically literate, the chart may be misinterpreted or confusing.
- **Distribution Shape:** Box plots hide the specific shape of the data's distribution, such as whether it is bimodal (has two peaks). If the underlying distribution shape is important, a violin plot or histogram should be considered instead.

## Trade-offs

- **Loss of Detail:** Using a box plot completely hides the raw data, making it impossible to see individual data points, the number of data points, or the shape of the distribution within the range.
- **Potential for Misinterpretation:** Viewers unfamiliar with box plots may misinterpret the different components (median line, box, whiskers).

## Signs of Trouble

- **Incorrect Heuristics:** When looking at a line chart, viewers incorrectly assume that a "spiky" section has more spread than a "smooth" section, without accounting for differences in the mean.
- **Inability to Compare:** Viewers are unable to reliably rank categories by their data variance when presented with raw data plots.

## How to Improve

- **Moderate Approach:** Replace other chart types (like line charts or bar charts of averages) with a series of box plots, with one plot for each category or time period being compared.
- **Comprehensive Approach:** Enhance the box plot by also showing the raw data. Create a "raincloud plot" by pairing each box plot with a strip plot or beeswarm plot (to show individual data points) and/or a violin plot (to show the distribution shape). This provides both the clear summary of spread and the context of the raw data.
