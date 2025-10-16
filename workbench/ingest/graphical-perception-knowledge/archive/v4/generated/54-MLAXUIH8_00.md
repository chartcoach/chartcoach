---
id: start-axis-at-zero-for-magnitude
title: "Start quantitative axes at zero for bar and line charts to avoid exaggerating change"
tags:
  - impact:perceptual
  - impact:ethical
  - impact:logos
  - chart:bar
  - chart:line
  - task:compare
  - task:trend
  - data:quantitative
  - medium:static
  - medium:screen
sources:
  - type: research
    ref: "Correll et al., 2020"
    url: "https://doi.org/10.1145/3313831.3376222"
    note: "Experiments 1, 2, and 3 consistently showed that y-axis truncation significantly increased the perceived severity of effect sizes in both bar and line charts."
examples:
  - type: bad
    url: https://i.imgur.com/n1f1WJ7.png
    caption: Truncated Y-Axis
    description: "This infamous Fox News chart truncates the y-axis to make a 4.6% increase in the tax rate look like a 6-fold increase. The non-zero baseline dramatically exaggerates the difference."
  - type: good
    url: https://i.imgur.com/8YlE145.png
    caption: Zero-based Y-Axis
    description: "The same data with a y-axis that starts at zero. The change is now correctly represented as a small increase, accurately reflecting the data's magnitude."
---
## Guidance
For bar charts and line charts where the primary goal is to communicate the magnitude of values or the size of a change, the quantitative axis (usually the y-axis) must start at zero.

## Why
Starting the axis at a non-zero value truncates the bars or lines, which perceptually exaggerates the differences between data points. This leads viewers to believe that changes or differences are more significant than they actually are. Research shows this is a powerful perceptual bias that occurs in both bar and line charts and is not simply a matter of misreading labels.

## When it applies
- When creating a bar or line chart to show and compare absolute magnitudes.
- When the audience may not be an expert in the data and could be misled by the magnified visual effect.
- When encoding values using length or height as the primary visual channel.

## Exceptions
- When showing small but critical fluctuations that would be invisible on a zero-based scale (e.g., stock price changes, body temperature). In these cases, the truncation should be explicit and the context must justify the focus on small changes.
- For chart types where the goal is to show deviation from a meaningful non-zero baseline, such as index charts (showing percent change from a start date) or statistical process control charts (showing deviation from a mean).
- When the data has no meaningful zero point (e.g., temperature in Celsius or Fahrenheit).

## Trade-offs
- **Clarity vs. Detail:** Starting the axis at zero provides an honest representation of magnitude but can sometimes make small, important variations in the data difficult to see. Truncating the axis highlights these variations but at the cost of distorting their overall significance.

## Signs of Trouble
- **Dramatic Slopes for Small Changes:** A line chart shows a very steep incline or decline, but the axis labels reveal the total change is only a few percentage points.
- **Disproportionate Bars:** In a bar chart, one bar appears twice as tall as another, but its data value is not twice as large.
- **Non-Zero Baseline:** The y-axis of a bar chart showing raw totals or amounts begins at any value other than 0.

## How to Improve
- **Quick Fix: Reset the Axis.** The most direct fix is to change the axis minimum to 0.

- **Moderate Approach: Add Context.** If a truncated axis is necessary to show detail, add explicit annotations to provide numerical context that can temper the misleading visual. For example, add a clear title ("A Small but Critical 1.5% Drop in Q3 Engagement") or label the percentage change directly on the chart.

- **Comprehensive Approach: Change the Chart.** If the goal is to highlight a small change, consider creating a chart that visualizes the *change itself*. A separate bar chart showing the *delta* (the difference between values) can be properly zero-based and honestly represent the magnitude of the change.