---
id: use-box-plots-for-spread-comparison
title: "Use box plots to compare spread or variance across categories"
tags:
  - impact:perceptual
  - impact:performance
  - impact:cognitive
  - task:distribution
  - task:compare
  - chart:box-plot
  - chart:line
  - data:temporal
  - data:categorical
  - audience:general
  - medium:screen
evidence:
  strength: medium
  summary: "In a study comparing time-series visualizations, Albers et al. (2014, n=56) found that box plots were the most effective design for comparing the spread of values within monthly periods, achieving 85% accuracy. This was significantly higher than the next-best design (woven colorfield, 71%) and far superior to standard line charts (49%) (p < .0001)."
sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "Demonstrated that explicitly encoding a statistic related to spread (like IQR in a box plot) is far more effective for judging spread than relying on perceptual estimation from raw data displays like line charts (p < .0001)."
    role: primary
---
## Guidance

When users need to compare the spread, variance, or consistency of data across different categories or time periods, use box plots.

## Why

Judging "spread" from raw data displays like line charts is a difficult perceptual task that humans are not good at. Box plots solve this by explicitly computing and encoding statistics related to distribution—specifically the interquartile range (IQR), which is a robust measure of spread. This offloads the complex mental calculation from the user to the chart, resulting in significantly higher accuracy.

### Core Principle

When a task requires judging a specific, computable statistic (like spread or variance), it is more effective to encode that statistic directly rather than asking the viewer to estimate it from raw data.

## When it applies

- The user's task is to determine which category is more "variable," "volatile," "consistent," or "spread out."
- You need to show the distribution of values for multiple categories side-by-side.

## Exceptions

- If the audience is unfamiliar with box plots, they may require a brief explanation. However, their superior performance often justifies the small learning curve.
- If showing every single data point is critical and the distribution is small, a dot plot or strip plot might be an alternative.

## Trade-offs

- Box plots summarize the data, so they hide the specific shape of the distribution (e.g., they can't distinguish a bimodal distribution from a unimodal one). Violin plots are an alternative that addresses this, but may be more complex.
- Box plots are less effective for other tasks, such as finding specific maximum values, compared to a modified stock chart.

## Signs of Trouble

- **Confusing Range with Spread:** When viewing a line chart, users incorrectly assume the category with the highest maximum or widest range is also the one with the greatest spread.
- **Inability to Compare:** Users report that they "can't tell" which of two line chart segments is more variable.
- **Incorrect Judgements:** Formal testing reveals that user judgments about spread from raw data charts are no better than chance.

## How to Improve

- **Quick Fix: Add Reference Bands.** On a line chart, add shaded bands for the standard deviation or interquartile range around the mean. This provides a visual guide to the spread, though it can become cluttered.
- **Comprehensive Redesign: Switch to Box Plots.** Replace the line chart or other raw data display with a series of box plots, with one box plot for each category or time period being compared. This is the most effective way to support this specific task.
