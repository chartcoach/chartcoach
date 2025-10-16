---
id: prefer-color-for-aggregate-judgments
title: "Prefer Color to Position for Aggregate Judgments"

impact:
  - perceptual
  - cognitive
  - performance
tags:
  - color
  - position
  - time-series
  - line-chart
  - heatmap
  - colorfield
  - aggregation
  - comparison
  - perceptual-averaging

sources:
  - type: research
    ref: Correll et al., 2012
    url: https://doi.org/10.1145/2207676.2208556
    note: "Found that colorfield charts (1D heatmaps) significantly outperform line charts for tasks requiring users to judge the average value of a time period."

examples:
  - type: bad
    description: A standard line chart shows daily values over a year. The task is to find the month with the highest average value. Viewers must mentally trace and average the jagged line for each month, which is difficult and error-prone.
  - type: good
    description: The same daily data is shown as a colorfield (a 1D heatmap), with each day represented by a colored cell. The viewer can perceptually average the "block" of color for each month to quickly and more accurately identify the one with the highest overall value.

---

## Guidance

For tasks that require viewers to judge the average value of a region in a time series, encode values using color (as in a 1D heatmap or colorfield) rather than vertical position (as in a line chart).

## Why

The human visual system can efficiently and pre-attentively "average" a patch of color, making it easier to compare the overall value of different regions. This process, known as perceptual averaging, offloads mental work to the visual system. In contrast, mentally calculating the average height of a jagged line is a more demanding cognitive task that is slower and more prone to error.

## When it applies

- When the primary task is to compare aggregate properties, like the mean or sum, of different segments of a dataset (e.g., "Which month had the highest average sales?").
- When visualizing dense time-series data where a quick, approximate summary is more important than reading precise individual values.
- When you want to encourage viewers to see the "bigger picture" or summary trends rather than focusing on individual data points.

## Exceptions

- When the primary task is to identify specific high or low points (extrema), read the exact value of a data point, or trace the path and volatility of a single series. Line charts excel at showing precise positions and shape.
- When the data has very few points within each region, making mental averaging trivial.

## Trade-offs

- **Precision:** You sacrifice the ability to read exact data values. Color encodings are less precise than position for quantitative lookups. It's difficult to map a specific color back to a number, whereas a point's position on an axis is much clearer.
- **Accessibility:** Heavy reliance on color can be problematic for users with color vision deficiencies. Using a well-chosen, perceptually-uniform color scale that also varies significantly in luminance (lightness) is critical to mitigate this.

## Evaluate

- [ ] A line chart is used, and the primary question for the audience is to compare the average value of different time periods.
- [ ] Users struggle to summarize trends over time, focusing only on individual peaks and troughs in a line chart instead of the overall level.

## Repair

1.  Replace the line chart with a **colorfield** (a 1D heatmap), where time runs along one axis and each time point is a colored block representing its value.
2.  Choose a perceptually-uniform and colorblind-safe color scale that varies in luminance (e.g., from light to dark).
3.  If a line chart must be used for other reasons, consider adding a secondary chart (like a bar chart of the monthly averages) to explicitly show the aggregate values.