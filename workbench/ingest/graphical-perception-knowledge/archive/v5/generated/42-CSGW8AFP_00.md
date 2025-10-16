---
id: avoid-area-charts-for-trend-estimation
title: "Avoid area charts for estimating trends"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:ethical
  - chart:area
  - chart:line
  - chart:scatter
  - task:trend
  - task:correlation
  - data:quantitative
  - data:temporal
  - visual:area
  - visual:position
  - audience:general
  - medium:static
  - medium:interactive
  - access:cognitive-load-risk

evidence:
  strength: medium
  summary: "A 2017 crowdsourced study found that the visual asymmetry of area charts leads to a systematic under-estimation of trend intercepts, a bias not present in scatter plots or line charts for the same task."

sources:
  - type: research
    ref: Correll & Heer, 2017
    url: https://doi.org/10.1145/3025453.3025922
    note: "Primary experiment (Experiment 2) identified a 'within-the-area' bias causing under-estimation of trend intercepts in area charts."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "Collated this finding as part of a systematic review of graphical perception literature, confirming its relevance for visualization recommendation systems."
    role: supporting

examples:
  - type: bad
    description: "An area chart is used to show a stock's price over time. Viewers are likely to visually underestimate the overall value trend because their judgment is biased towards the filled-in area below the line."
  - type: good
    description: "The same stock price data is shown as a line chart. Viewers can more accurately judge the trend's slope and intercept without the 'within-the-area' bias distorting their perception."
---

## Guidance

To enable accurate visual trend estimation, use line charts or scatter plots instead of area charts.

## Why

Area charts are visually asymmetrical—the area below the trend line is filled in, but the area above it is not. This asymmetry creates a "within-the-area" perceptual bias, where viewers perceive points inside the filled area as more plausible or likely. This causes them to systematically underestimate the trend's intercept, effectively pulling their mental model of the trend line downwards. Line charts and scatter plots do not have this asymmetry and therefore do not produce this bias.

### Core Principle

Visual asymmetry in a chart can create perceptual biases that systematically distort judgment. Symmetrical encodings promote more accurate, unbiased perception.

## When it applies

- When the primary task for the viewer is to visually estimate, judge, or compare a trend in bivariate data.
- When you are visualizing continuous data over an interval, such as a time series.
- When the accuracy of trend perception is more important than conveying a sense of volume or magnitude.

## Exceptions

- When the primary task is to show part-to-whole composition over time using a stacked area chart, and precise trend estimation of any single series is a secondary goal.
- If the goal is to show cumulative totals and the concept of "volume" is central to the message. Even then, be aware that the trend of the top-level boundary may be misinterpreted.

## Trade-offs

- **Clarity vs. Volume:** Area charts effectively convey a sense of volume or accumulated quantity. Switching to a line chart improves the accuracy of trend perception but loses this visual communication of mass or magnitude.
- **Simplicity vs. Precision:** Relying on a line chart for trend perception is simple but lacks the explicit precision of a statistically calculated trend line.

## Signs of Trouble

- **Chart Choice:** An area chart is used for a single data series where the main task is understanding its trend.
- **User Interpretation:** If you ask viewers to draw the trend they see on an area chart, their lines will likely be systematically lower than those drawn on a line chart of the same data.
- **Misleading Insights:** Decisions based on visual inspection of an area chart may be overly conservative, as the perceived trend is an underestimate of the actual trend.

## How to Improve

- **Quick Fix: Add a Trend Line.** If you must use an area chart, mitigate the bias by adding an explicit, statistically calculated trend line. This gives the viewer a clear, unbiased anchor to override their perceptual judgment.

- **Moderate Redesign: Switch to a Line Chart.** For most trend-analysis tasks, the best fix is to replace the area chart with a line chart. This removes the visual asymmetry and the associated perceptual bias entirely, leading to more accurate visual estimation by the viewer.

- **Comprehensive Approach: Offer Both Views.** In an interactive context, allow the user to toggle between an area chart (to see volume) and a line chart (to judge the trend). This provides the benefits of both chart types without forcing a compromise.
