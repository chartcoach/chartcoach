---
id: prefer-color-over-position-for-time-series-averages
title: "Prefer color-based charts over line charts for comparing segment averages"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:line
  - chart:heatmap
  - task:summary-mean
  - task:compare
  - data:temporal
  - data:quantitative
  - visual:color
  - visual:position
  - audience:general
  - medium:screen
  - access:cognitive-load-risk

evidence:
  strength: medium
  summary: "A 2012 study found that for comparing segment averages in time series, a color-based encoding (colorfield) significantly outperformed a standard line chart in accuracy, by leveraging the brain's ability to perform pre-attentive 'perceptual averaging'."

sources:
  - type: research
    ref: Correll et al., 2012
    url: https://dl.acm.org/doi/10.1145/2207676.2208556
    note: "Primary experimental evidence showing colorfields outperform line charts for the task of comparing segment averages in time-series data."
    role: primary

examples:
  - type: bad
    description: "A standard line chart showing daily sales over a year. When asked to find the month with the highest average sales, a viewer must mentally integrate the fluctuating line for each month, a difficult and error-prone task."
  - type: good
    description: "A calendar-style heatmap showing the same daily sales data. Each day is a colored cell, grouped by month. Viewers can pre-attentively and more accurately judge which month has the 'strongest' average color, corresponding to the highest average sales."
---

## Guidance

For time-series data, when the primary task is to compare the average value of different segments (e.g., finding the month with the highest average sales), use a color-based encoding like a colorfield or heatmap instead of a position-based encoding like a line chart.

## Why

The human visual system can efficiently and pre-attentively calculate the average of a region of color. This "perceptual averaging" reduces the cognitive load required to summarize data. In contrast, mentally averaging the height of a fluctuating line requires more conscious effort and is less accurate for this specific task.

### Core Principle

Match the visual encoding to the perceptual demands of the task. For summary tasks, use encodings that leverage the brain's ability to perform pre-attentive summary statistics.

## When it applies

- When the main goal is to compare the *average* or *summary* value of distinct, contiguous regions within a larger time series.
- When visualizing dense time-series data where the summary of a period is more important than individual data points.
- When the audience needs to make quick, approximate judgments about which segment is highest or lowest on average.

## Exceptions

- If the primary task is to identify trends, see the overall shape, or look up specific high/low points (peak-finding), a line chart is more effective. Position is superior for showing change and specific values.
- When precision is critical for comparing *individual* data points, as position is a more precise visual encoding than color.

## Trade-offs

- **Loss of detail:** By encoding values as color in a heatmap, you sacrifice the ability to precisely judge individual data points and see the fine-grained shape of the trend (e.g., volatility, specific peaks and valleys).
- **Color perception issues:** This approach relies heavily on color, making it essential to choose a perceptually uniform, colorblind-safe palette. Poor color choices can invalidate the benefits.

## Signs of Trouble

- **Peak vs. Average Confusion:** Users looking at a dense line chart mistakenly identify the segment with the highest single *peak* as the one with the highest *average*.
- **High Cognitive Load:** It feels like a lot of mental work for a viewer to "blur their eyes" and guess the average height of a segment in a line chart.
- **Inconsistent Judgments:** Different users arrive at different conclusions about which segment has the highest average when viewing a line chart, indicating the task is highly subjective and difficult.

## How to Improve

- **Quick approach:** If you must use a line chart, add explicit annotations. Calculate the average for each segment and display it as a text label or a horizontal reference line over that segment. This offloads the mental calculation from the user but can add clutter.

- **Moderate approach:** Switch the line chart to a colorfield or heatmap. Represent each time point (e.g., day) as a colored rectangle and group them by the segment of interest (e.g., month). Use a perceptually uniform color scale to map the quantitative value.

- **Comprehensive approach:** Provide both views interactively. Allow the user to toggle between a line chart (for trend analysis) and a heatmap (for average comparison), giving them the best tool for each sub-task.
