---
id: use-position-for-point-value-comparisons
title: "Use position-based charts for accurate point-value comparisons in time series"

tags:
  - impact:perceptual
  - impact:performance
  - chart:line
  - chart:bar
  - chart:box-plot
  - chart:stock
  - task:compare
  - task:rank
  - task:find-extremum
  - task:determine-range
  - data:quantitative
  - data:temporal
  - visual:position
  - visual:color
  - audience:general
  - medium:static
  - medium:screen

sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "Experiments on time-series aggregation tasks showed that position-based encodings (line charts, composite graphs) consistently outperformed color-based encodings (colorfields) for tasks requiring specific point comparisons, such as finding the maximum, minimum, or range."

examples:
  - type: good
    description: A line chart uses the vertical position to encode values, allowing for accurate comparison of high and low points over time. In the study, line charts and composite graphs performed well for finding maxima.
  - type: bad
    description: A colorfield (one-dimensional heatmap) uses color to encode values. This makes it difficult to precisely identify and compare the single highest or lowest value, leading to lower accuracy on point-comparison tasks.
---

## Guidance

When users need to accurately compare specific point values in a time series (e.g., finding the highest peak, lowest trough, or largest range), use chart types that encode values with position along a common scale, such as line charts or bar charts, rather than those that use color.

## Why

The human visual system is much better at perceiving and comparing differences in position along an aligned scale than it is at comparing differences in color hue or saturation. Research by Albers, Correll, & Gleicher (2014) confirmed this for time-series aggregation tasks, where position-based charts led to significantly higher accuracy for finding maxima, minima, and ranges compared to color-based charts like colorfields.

## When it applies

- The primary user task is to identify, compare, or rank specific individual data points within a larger dataset.
- The tasks include finding the absolute maximum (`find-extremum`), minimum (`find-extremum`), or the range between them (`determine-range`).
- Accuracy of value comparison is a higher priority than seeing an overall "gist" or summary of the data.

## Exceptions

- When the primary task is to get a high-level summary or "gist" of the data distribution, such as identifying the average value or overall spread, color-based encodings like colorfields can be effective and sometimes outperform simple line charts.
- When space is extremely limited, a colorfield can represent a time series more compactly than a line or bar chart.

## Trade-offs

- **Clarity vs. Gist:** While position-based charts are superior for point-value accuracy, they can be less effective than color-based charts for pre-attentively summarizing regions of data (e.g., judging the average value over a month).
- **Space:** Line charts and bar charts typically require more vertical space than a compact colorfield representation.

## Signs of Trouble

- **Task Mismatch:** A colorfield or heatmap is being used, but the primary user question is "Which day had the highest sales?" or "What was the lowest value in June?"
- **Low Accuracy:** Users consistently make errors when asked to identify the highest or lowest points in a color-encoded chart.
- **Visual ambiguity:** It's difficult to tell whether dark green represents a higher value than a slightly less dark green, leading to uncertainty in comparisons.

## How to Improve

- **Quick Fix: Add Annotations.** If you must use a color-based chart, add explicit labels or markers to highlight the specific maximum and minimum values.
- **Moderate Redesign: Switch to a Line Chart.** Replace the colorfield with a standard line chart. This immediately leverages the perceptual advantages of position for comparing values.
- **Comprehensive Approach: Use a Composite Chart.** If users need to perform both point-comparison and summary tasks, consider a composite chart that overlays explicit summary statistics (e.g., monthly average bars) on a line chart of the raw data. This supports multiple tasks effectively.