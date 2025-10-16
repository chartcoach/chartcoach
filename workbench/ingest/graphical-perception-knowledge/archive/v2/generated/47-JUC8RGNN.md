---
id: position-for-points-color-for-summary
title: "Use Position for Point Comparisons and Color for Summary Judgments"

impact:
  - perceptual
  - performance
  - cognitive
tags:
  - time-series
  - aggregation
  - comparison
  - find-extremum
  - average
  - position
  - color
  - line-chart
  - heatmap

sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "Provides empirical evidence comparing 8 time series visualizations across 6 aggregation tasks, demonstrating the trade-off between position for point tasks and color for summary tasks."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Collates and reviews graphical perception literature, including the Albers et al. study, to create actionable guidelines for visualization recommendation systems."

examples:
  - type: good
    description: "A line chart is highly effective for finding the single highest or lowest value in a time series, as it uses the position channel which is perceived with high accuracy."
  - type: bad
    description: "Using a standard colorfield (heatmap) to find the single highest value in a time series is ineffective. It is difficult to precisely compare two non-adjacent color values."
  - type: good
    description: "A woven colorfield, which groups colors into discrete blocks for each month, is effective for comparing the average value or spread across months. It leverages the visual system's ability to summarize color and texture over an area."
  - type: bad
    description: "A standard line chart is less effective for comparing the average value of different noisy periods, as it forces the viewer to mentally compute the average for each period."
---

## Guidance

For tasks requiring precise extraction of individual values (e.g., finding the maximum or minimum), prioritize visual encodings based on **position**, such as line charts or bar charts.

For tasks requiring summary judgments about a collection of values (e.g., estimating an average or spread), consider visual encodings based on **color**, such as heatmaps (colorfields).

## Why

The human visual system perceives position with high accuracy, making it ideal for reading and comparing exact values. In contrast, color is processed pre-attentively over an area, allowing the brain to quickly form a "gist" or summary impression (like the average color or texture of a region) without needing to inspect each individual point. This makes color a more efficient channel for holistic, summary-level judgments, but a poor one for precise comparisons.

## When it applies

- When visualizing time series data where users need to make comparisons within or between time periods.
- For **point comparison tasks**, such as finding the day with the highest sales, the lowest temperature, or the largest range of values in a month.
- For **summary comparison tasks**, such as identifying the month with the highest average sales, the most variance in stock price, or the most outliers.

## Exceptions

- **Explicit Encoding:** If you explicitly calculate and display a summary statistic, a position-based chart can become very effective for that specific summary task. For example, adding bars that show the monthly average underneath a line chart (a "composite graph") makes it one of the best choices for comparing averages.
- **Task-Specific Designs:** For highly specialized tasks like counting outliers, a custom design that explicitly highlights those features (like "event striping") will outperform general-purpose charts, regardless of whether it's primarily position- or color-based.

## Trade-offs

- Choosing a position-based chart for its accuracy in point comparisons may make summary judgments less efficient and more mentally taxing.
- Choosing a color-based chart for efficient summary judgments sacrifices the ability to accurately read or compare individual data points.
- Augmenting a chart with explicit summary statistics (e.g., an average line) can add visual clutter and typically only supports one specific summary task at the expense of others.

## Evaluate

- [ ] The chart uses color (e.g., a heatmap) but the primary task is to find the single highest or lowest value.
- [ ] The chart uses position (e.g., a line chart) but the primary task is to compare the average value of different noisy periods, and no summary statistic is explicitly shown.

## Repair

1.  **For Point Tasks:** If using a color-based chart (like a heatmap) to find a maximum value, switch to a line chart. This makes the peaks and troughs instantly and accurately identifiable.
2.  **For Summary Tasks:** If using a simple line chart to compare averages, either switch to a chart better suited for summary (like a woven colorfield) or augment the line chart by explicitly adding the average as a second visual element (e.g., bars or a thicker line).
3.  **For Mixed Tasks:** If users need to perform both point and summary tasks, consider providing two separate, coordinated charts or an interactive control that allows users to switch between different chart types.