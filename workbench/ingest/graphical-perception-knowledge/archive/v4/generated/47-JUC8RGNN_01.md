---
id: explicitly-encode-target-statistics
title: "To support comparing summary statistics, explicitly encode them in the chart"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:box-plot
  - chart:stock
  - chart:bar
  - chart:line.annotated
  - task:compare
  - task:summary-mean
  - task:distribution
  - task:find-extremum
  - task:determine-range
  - data:quantitative
  - data:temporal
  - visual:position
  - visual:shape
  - visual:color
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "Across multiple tasks (finding range, average, spread, outliers), chart designs that explicitly computed and encoded the target statistic consistently outperformed designs that required the user to mentally compute it from raw data. For example, box plots were best for spread, and composite graphs were best for averages."

examples:
  - type: good
    description: A composite graph explicitly shows monthly averages as bars overlaid on a line chart of raw data. This design had the highest accuracy for the 'compare averages' task in the study.
  - type: good
    description: A box plot explicitly encodes the median, interquartile range (IQR), and extrema (whiskers). This makes it highly effective for comparing spread and distributions.
  - type: bad
    description: A simple line chart requires the user to mentally estimate the average value of each month to compare them. This leads to lower accuracy and higher cognitive load compared to a chart that shows the averages explicitly.
---

## Guidance

When a user's task involves comparing summary statistics (like averages, spreads, or ranges) across different periods or categories, choose a visualization that explicitly computes and encodes those statistics rather than requiring the user to estimate them from raw data.

## Why

Offloading computational work from the user to the computer reduces cognitive load and improves accuracy. Instead of mentally estimating a complex property like 'spread' or 'average' from dozens of data points, the user can perform a much simpler perceptual task: comparing the length of two bars or the position of two points. Albers et al. (2014) demonstrated this principle's effectiveness: chart types that explicitly encoded the statistic relevant to the task (e.g., box plots for spread, event striping for outliers) were the top performers for that task.

## When it applies

- The user task is well-defined and involves comparing a specific summary statistic (mean, median, range, spread, number of outliers).
- Accuracy and speed of judgment are important.
- The task is a primary goal for the visualization, justifying the choice to dedicate visual encoding to that statistic.

## Exceptions

- **Exploratory Analysis:** When the user's tasks are not known in advance, showing the raw data (e.g., in a line chart or scatter plot) is more flexible than pre-computing a specific statistic that may not be relevant.
- **Losing Context:** Explicitly encoding a statistic can sometimes obscure the underlying raw data and its distribution. A composite chart (e.g., line chart + bars for average) is a good compromise, but a simple box plot hides the raw data entirely.

## Trade-offs

- **Flexibility vs. Specificity:** A chart designed for one specific task (e.g., comparing averages) may be less effective for other tasks (e.g., finding the absolute maximum). Explicitly encoding statistics makes a chart less of a general-purpose tool.
- **Visual Clutter:** Adding explicit encodings for statistics (e.g., layering a moving average and range bars on a line chart) can increase visual clutter if not designed carefully.

## Signs of Trouble

- **High Cognitive Load:** Users report that it's "a lot of work" or "hard to tell" what the average or spread is for a given period.
- **Inconsistent Judgments:** Different users looking at the same raw data make wildly different estimations of a summary property.
- **Task Failure:** A chart shows raw data, but users are frequently asked to perform summary comparisons that the chart doesn't directly support, leading to errors.

## How to Improve

- **For Comparing Averages:** Switch from a simple line chart to a **composite graph** that overlays bars representing the average for each period.
- **For Comparing Spread/Distribution:** Switch from a line chart to a **box plot**, which is specifically designed to show spread (IQR), median, and outliers.
- **For Comparing Ranges/Extrema:** Use a **modified stock chart** with explicit range bars or a **box plot** to make the minimum and maximum values for each period perceptually salient.
- **For Finding Outliers:** Use an **event striping** visualization that uses a distinct visual mark to explicitly highlight outlier data points.