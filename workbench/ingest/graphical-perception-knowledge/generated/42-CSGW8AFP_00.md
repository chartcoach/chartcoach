---
id: avoid-area-charts-for-trend-estimation
title: "Avoid using area charts for trend estimation"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:logos
  - chart:area
  - chart:line
  - chart:scatter
  - task:trend
  - task:correlation
  - data:quantitative
  - data:temporal
  - visual:area
  - visual:position
  - medium:static
  - medium:interactive
  - access:cognitive-load-risk

evidence:
  strength: medium
  summary: "Correll & Heer (2017, n=48) found that area charts introduce a systematic 'within-the-area' bias, causing viewers to underestimate trend intercepts. Unsigned errors in intercept estimation were more than twice as large for area charts compared to line charts or scatter plots (p < 0.001)."

sources:
  - type: research
    ref: Correll & Heer, 2017
    url: https://doi.org/10.1145/3025453.3025922
    note: "Experiment 2 (n=48) demonstrated a significant 'within-the-area' bias for area charts (p<0.001), showing they lead to systematic underestimation of trend intercepts compared to unbiased line charts and scatter plots."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This review paper collates the findings from Correll & Heer (2017) and other perception studies, confirming that different chart types are not equally effective for tasks like correlation/trend estimation."
    role: related

examples:
  - type: bad
    description: "An area chart is used to show stock price over time. A viewer trying to estimate the overall trend might be biased by the large colored area, underestimating the trend line's position and potentially misjudging its growth."
  - type: good
    description: "The same stock price data is shown using a line chart. The viewer can now estimate the trend without the biasing effect of a filled area, leading to a more accurate 'regression by eye'."
---

## Guidance

When the primary task is for a viewer to accurately estimate a visual trend, prefer line charts or scatter plots over area charts.

## Why

The filled region of an area chart creates a visual asymmetry that introduces a perceptual bias known as "within-the-area" bias. Viewers are unconsciously drawn to perceive the trend as being lower and closer to the x-axis than it actually is, leading to a systematic underestimation of the trend's intercept (its starting point). Line charts and scatter plots do not have this filled region and are therefore not subject to this specific bias.

### Core Principle

Asymmetrical visual encodings can introduce systematic perceptual biases, skewing judgments away from the true data values. A design should not create visual features that interfere with the primary perceptual task.

## When it applies

- When visualizing bivariate data, such as a value changing over time.
- When you expect the audience to visually judge the trend line, its slope, or its starting/ending points without the aid of an explicit, pre-calculated trend line.
- When the accuracy of trend perception is a critical goal for the visualization.

## Exceptions

- When the primary task is to emphasize the cumulative total or volume under a line, and precise trend estimation is a secondary or non-critical goal. For example, showing total sales volume over a year.
- When the area chart is stacked to show part-to-whole composition over time. However, be aware that trend estimation for any individual series (except the bottom one) becomes extremely difficult and unreliable.

## Trade-offs

- **Clarity vs. Volume Emphasis:** Area charts are effective at conveying the concept of volume or cumulative magnitude. By choosing a line chart for trend accuracy, you lose this intuitive emphasis on volume. You may need a separate chart or annotation if both trend and total volume are important.
- **Aesthetics vs. Accuracy:** Area charts can be visually appealing and less "spidery" than line charts, but this aesthetic preference comes at the cost of perceptual accuracy for trend-related tasks.

## Signs of Trouble

- **The "Pulled Down" Effect:** If you trace where you think the trend line should be, does it consistently fall below where a calculated regression line would be?
- **Underestimated Start:** In a time-series chart, do viewers consistently misjudge the starting value of the trend as being lower than it actually is?
- **Task Mismatch:** The chart is titled "Trend of X over Time," but the visual encoding (an area chart) is known to interfere with that very task.

## How to Improve

- **Quick Fix: Add an Explicit Trend Line.** If you must use an area chart, mitigate the bias by overlaying a bold, explicit, and clearly calculated trend line. This gives the viewer a strong visual anchor to follow, overriding their biased perception.

- **Moderate Approach: Switch to a Line Chart.** For time-series data or any data where points are ordered along the x-axis, changing the mark type from `area` to `line` is a simple and highly effective fix. This removes the filled area that causes the bias.

- **Comprehensive Approach: Choose the Right Chart for the Task.** Step back and confirm the primary goal. If it is trend estimation, use a line chart or scatter plot, as they are demonstrably unbiased for this task. If the goal is to show volume, use the area chart but be clear in the title and annotations that the focus is on total magnitude, not the precise trend line.
