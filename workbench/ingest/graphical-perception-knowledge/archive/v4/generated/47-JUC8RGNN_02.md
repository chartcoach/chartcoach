---
id: use-box-plots-for-comparing-spread
title: "Use box plots to compare data spread across different categories or time periods"

tags:
  - impact:perceptual
  - impact:performance
  - chart:box-plot
  - task:compare
  - task:distribution
  - data:quantitative
  - visual:position
  - visual:length

sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "In an experiment comparing eight different time-series visualizations, box plots were the most accurate chart type (85.0% accuracy) for the task of identifying which month had the greatest 'spread' (absolute deviation)."

examples:
  - type: good
    description: A series of monthly box plots clearly shows that some months have a tall interquartile range (high spread) while others have a short one (low spread). The user can easily compare the heights of the boxes.
  - type: bad
    description: A standard line chart makes it very difficult to judge and compare the overall 'spread' of values within each month. The user has to mentally estimate the variation, which is an error-prone task.
---

## Guidance

When the primary task is to compare the statistical spread or variability of data across different groups or time intervals, use box plots.

## Why

Box plots are specifically designed to represent data distribution. They explicitly encode summary statistics related to spread, such as the interquartile range (IQR), which is represented by the height of the box. This offloads the difficult mental task of estimating variability from raw data points and transforms it into a simple perceptual task: comparing the lengths of the boxes. The study by Albers et al. (2014) found that box plots were significantly more effective for this task than other chart types, including line charts and various color-based encodings.

## When it applies

- The user needs to answer questions like, "Which category is most volatile?" or "In which month were the values most spread out?"
- The task is to compare distributions between several groups.
- The underlying data is quantitative.

## Exceptions

- **Showing Raw Data:** Box plots summarize the data and hide the specific shape of the distribution (e.g., they can't distinguish a bimodal distribution from a uniform one). If seeing the raw data points is critical, consider a violin plot or a strip plot instead.
- **Small Datasets:** Box plots can be misleading for very small datasets where the calculation of quartiles is not robust.

## Trade-offs

- **Loss of Detail:** Box plots hide the number of data points and the specific distribution shape within each group. They provide a summary at the cost of granular detail.
- **Familiarity:** While common in statistics, box plots may be unfamiliar to a general audience, potentially requiring a brief explanation or annotation.

## Signs of Trouble

- **Spread Misinterpretation:** Users looking at a line chart are incorrectly using the range (max - min) as a proxy for spread, or are unable to make consistent judgments about which period is more variable.
- **Analysis Paralysis:** Users are presented with a dense scatterplot or line chart and find it overwhelming to try and estimate and compare the spread between different groups.

## How to Improve

- **Quick Fix: Add a Benchmark.** On a line chart, you could add a shaded band representing one standard deviation around the mean. This provides a visual proxy for spread, though it's less direct than a box plot.
- **Comprehensive Approach: Redesign as a Box Plot.** Convert the visualization from a line chart or other raw data display to a series of box plots, one for each category or time period being compared. This directly supports the task of comparing spread and will yield more accurate results.