---
id: use-color-for-time-series-average
title: "Use color encoding instead of line position for comparing time-series averages"

tags:
  - impact:perceptual
  - impact:performance
  - impact:cognitive
  - chart:line
  - chart:heatmap
  - task:summary-mean
  - task:compare
  - data:temporal
  - data:quantitative
  - visual:color
  - visual:position
  - medium:screen
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Correll et al., 2012
    url: https://doi.org/10.1145/2207676.2208556
    note: "Experimentally showed that a 'colorfield' (1D heatmap) significantly outperformed a standard line graph for the task of identifying the month with the highest average value in a time series."

examples:
  - type: bad
    description: "A standard line graph encodes values by position. While good for seeing trends and peaks, it requires significant mental effort to estimate and compare the average value of different segments (months)."
  - type: good
    description: "A 'colorfield' encodes values using color. This allows viewers to use perceptual averaging, a more efficient preattentive process, to quickly judge the average value of each segment, leading to higher accuracy."
---

## Guidance

To help viewers compare average values across different periods in a dense time series, encode the data values using a color scale (creating a colorfield or 1D heatmap) rather than a line graph.

## Why

This approach leverages **perceptual averaging**. The human visual system can efficiently and preattentively summarize large regions of color with minimal conscious effort. In contrast, mentally averaging the varying heights of a line graph is a more demanding cognitive task. By encoding values as color, you offload the work of aggregation from the viewer's brain to their visual system, resulting in faster and more accurate judgments.

## When it applies

- The primary user task is to **compare aggregate statistics** (specifically the mean) across distinct intervals in a time series. For example, "Which month had the highest average sales?" or "Which week had the lowest average temperature?".
- The time series is dense, making it difficult to visually assess the average from a fluctuating line.
- The exact shape of the trend or the value of individual points is less important than the summary of each period.

## Exceptions

- If the primary task is to identify **precise values** at specific points, track the exact **shape of a trend**, or spot **peak/trough values**, a line graph remains more appropriate. Color encodings are less precise than position for value lookup.
- When you need to compare the rate of change (slope) between different points.

## Trade-offs

- **You gain** speed and accuracy for aggregate comparison tasks.
- **You sacrifice** the ability for viewers to perceive fine-grained details, such as the exact shape of the data, the rate of change (slope), or the precise value of individual data points. This design prioritizes summary-level efficiency over detail-level precision.

## Signs of Trouble

- **Peak-vs-Average Confusion:** In a line chart, viewers incorrectly identify the time period with the highest single *peak* as having the highest *average*.
- **Slow Performance:** Viewers take a long time to make a decision when asked to compare averages between two or more segments of a line chart.
- **Low Confidence:** Users report "guesstimating" or feeling uncertain about their answers when judging averages from a line graph.

## How to Improve

- **Quick approach:** If you must keep a line chart, you can augment it. Add a separate, simpler chart (like a bar chart) below it that explicitly shows the average for each period. This separates the detailed view from the summary view.

- **Comprehensive approach:** Replace the line graph with a **colorfield** (a 1D heatmap).
  1.  Divide the horizontal axis into the relevant time intervals (e.g., months).
  2.  For each interval, display a series of small, colored blocks, where each block represents a data point (e.g., a day).
  3.  Map the data values to a perceptually linear color scale (e.g., a single-hue sequential or diverging scale from ColorBrewer).
  4.  This directly encodes the data in a way that supports efficient perceptual averaging.
