---
id: prefer-lines-over-areas-for-trends
title: "Prefer Line Charts and Scatterplots Over Area Charts for Trend Estimation"

impact:
  - perceptual
  - cognitive
  - logos
  - ethical

tags:
  - line-chart
  - area-chart
  - scatterplot
  - trend
  - correlation
  - perception
  - bias
  - time-series

sources:
  - type: research
    ref: Correll & Heer, 2017
    url: https://doi.org/10.1145/3025453.3025922
    note: "Found that area charts introduce a systematic underestimation of trend intercepts (a 'within-the-area' bias), while line charts and scatterplots do not."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This meta-analysis of 59 perception papers confirms and collates this finding among others, recommending scatterplots or line charts for correlation tasks."

tools:
  - type: implement
    name: Vega-Lite
    url: https://vega.github.io/vega-lite/
    description: A high-level grammar that makes it easy to switch between line, area, and point marks to test different visual encodings.
  - type: learn
    name: The "Why" of Chart Choice
    url: https://www.datawrapper.de/v3/academy/why-you-should-use-a-line-chart
    description: Datawrapper Academy article explaining the appropriate uses for line charts, including showing trends.

examples:
  - type: bad
    description: An area chart used to show stock price fluctuations over time. The filled area can cause viewers to underestimate the trend's true position.
  - type: good
    description: The same stock price data shown as a line chart. This removes the visual asymmetry and allows viewers to more accurately judge the trend's slope and position.

---

## Guidance

When the primary goal is for a viewer to judge or estimate the trend in a dataset, use a line chart or a scatterplot instead of an area chart.

## Why

Research shows that people are less accurate and systematically biased when estimating trends in area charts. The solid color fill of an area chart creates a visual asymmetry known as the "within-the-area" bias. Viewers unconsciously perceive points within the filled area as more likely or important, causing them to consistently underestimate the trend's true value or position.

Line charts and scatterplots are visually symmetric and do not introduce this bias, leading to more accurate "regression by eye."

## When it applies

- The main task for the audience is to perceive the overall trend, slope, or correlation in the data.
- You are visualizing a continuous variable over time (a time series).
- You are showing the relationship between two quantitative variables (bivariate data).

## Exceptions

- When the primary goal is to emphasize the magnitude or volume of a value over time, not the precise trend. For example, a stacked area chart is effective for showing changes in a part-to-whole composition.
- When you are intentionally using the visual weight of the area for aesthetic reasons or to convey a metaphor of substance, but you should be aware of the perceptual trade-off. In such cases, consider adding an explicit trend line to guide the viewer.

## Trade-offs

- **Aesthetic Weight:** Line charts and scatterplots can feel less "substantial" than area charts. You lose the sense of volume or mass that a filled area provides.
- **Overplotting:** For very dense datasets, a scatterplot can become a solid, unreadable blob. A line chart (or an area chart) summarizes the data, avoiding this problem.

## Evaluate

- [ ] Is an area chart being used to show a trend in continuous data (e.g., price over time, temperature over time)?
- [ ] Is the key takeaway you want the audience to have related to the direction, slope, or strength of the relationship in the data?

## Repair

1.  **Change the mark type to a line.** This is the most direct fix, preserving the continuous nature of the x-axis and removing the biasing fill.
2.  **Change the mark type to points (a scatterplot).** This also removes the bias and has the added benefit of showing the individual data points, which can help reveal distribution and density.
3.  **If you must use an area chart, add an explicit trend line.** Superimposing a clearly visible trend line can help anchor the viewer's perception and counteract some of the "within-the-area" bias.