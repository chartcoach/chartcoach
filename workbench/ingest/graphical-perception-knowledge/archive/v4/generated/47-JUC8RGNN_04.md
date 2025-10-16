---
id: use-composite-charts-for-average-comparison
title: "To compare averages over time, overlay bars representing the average on a line chart of the raw data"

tags:
  - impact:perceptual
  - impact:performance
  - chart:line
  - chart:bar
  - task:compare
  - task:summary-mean
  - data:quantitative
  - data:temporal
  - visual:position
  - visual:length

sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "A 'composite graph'—a line chart of raw data with a bar chart of monthly averages overlaid—was the most accurate design (85.9% accuracy) for the task of identifying the month with the highest average."

examples:
  - type: good
    description: A composite graph layers monthly average bars under a line chart of daily values. This allows users to easily compare the heights of the bars to judge averages, while still seeing the context of the raw data.
  - type: bad
    description: A standard line chart forces the user to mentally estimate the average value for each month, a task that proved to be highly inaccurate in user studies (47.7% accuracy).
---

## Guidance

When the user's task is to compare the average value of a time series across discrete intervals (e.g., comparing average sales per month), use a composite graph that overlays a bar chart of the averages onto a line chart of the raw data.

## Why

This composite design provides the best of both worlds. It transforms the difficult cognitive task of mentally estimating an average into a simple perceptual task: comparing the heights of the bars. At the same time, it retains the line chart of the raw data, providing important context about the distribution, range, and specific values within each period. Albers et al. (2014) found this combination to be the most effective for comparing averages, significantly outperforming both simple line charts (which don't show the average) and color-based encodings.

## When it applies

- The primary user task is to compare the mean value across different time periods (months, weeks, days).
- It is also valuable for the user to see the context of the raw data (e.g., to understand the variability within each period).
- The data is a quantitative time series.

## Exceptions

- **Visual Clutter:** If the data is extremely volatile, the line chart portion might create too much visual noise, interfering with the perception of the underlying bars. In such cases, a simple bar chart of the averages or a box plot might be clearer.
- **Task Simplicity:** If the user *only* cares about the average and has no need for the raw data context, a simple bar chart of the averages is a cleaner, more focused solution.

## Trade-offs

- **Increased Complexity:** A composite chart is visually more complex than a simple line or bar chart. While it supports multiple tasks, it may require slightly more effort to interpret initially.
- **Potential for Occlusion:** The line may pass behind the bars, or the bars could obscure parts of the line. Careful design (e.g., using transparency for the bars) is needed to mitigate this.

## Signs of Trouble

- **Inaccurate Average Estimation:** When using a plain line chart, users are consistently wrong when asked to identify the month with the highest or lowest average.
- **Loss of Context:** When using a simple bar chart of averages, users ask follow-up questions like "But what was the range of values in that month?" or "Was that average skewed by one high day?"

## How to Improve

- **Start with a Line Chart:** Begin with a standard line chart of the time-series data.
- **Compute Averages:** Calculate the average value for each discrete interval (e.g., each month).
- **Add a Bar Layer:** Add a new layer to the chart, drawing a bar for each interval whose height corresponds to the calculated average.
- **Style for Clarity:** Place the bar layer behind the line layer and use a subtle or transparent fill for the bars to ensure the line chart of raw data remains visible.