---
id: line-chart-average-underestimation
title: "Be aware that viewers underestimate the average value of a line chart"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:ethical
  - chart:line
  - task:summary-mean
  - task:aggregate
  - data:quantitative
  - visual:position
  - audience:general
  - medium:static
  - medium:screen
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "Xiong et al. (2020), in a series of three controlled experiments (n=37 total), found that viewers systematically and significantly underestimate the average position of a line in a line chart (p<0.001). This bias persisted for both simple and complex charts."
sources:
  - type: research
    ref: Xiong et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934400
    note: "Primary study demonstrating a consistent underestimation bias for the average of line charts across three experiments. For example, in Experiment 1 the mean deviation was -4.49 pixels (p<0.001)."
    role: primary
role: primary
---

## Guidance

When creating a line chart where viewers need to estimate the average value of the series, be aware that they will likely perceive the average as being lower than it actually is.

## Why

Viewers are subject to a perceptual bias that causes a systematic underestimation of the average vertical position of a line. This means their "gut feeling" or visual summary of the line's central tendency is skewed downwards, which can lead to misinterpretation and flawed conclusions if not accounted for.

### Core Principle

Perception is not a perfect mirror of reality. Even for seemingly precise visual encodings like position, the human visual system can introduce systematic, predictable biases.

## When it applies

- When a key task for the viewer is to judge, estimate, or compare the overall average or central tendency of a data series presented as a line.
- This applies to both simple line charts with a single series and complex charts with multiple series.

## Exceptions

- When the primary task is to interpret the shape, trend, or volatility of the line, and the absolute average value is not important for the user's goal.
- When the line's exact average value is explicitly annotated on the chart, mitigating the need for perceptual estimation.

## Trade-offs

- Line charts are excellent for showing trends and changes over time. However, this strength comes with the trade-off of being potentially misleading when the user's task is to estimate the average value of the series. Prioritizing trend-over-time might come at the cost of aggregate accuracy.

## Signs of Trouble

- **Flawed Takeaways:** Viewers or stakeholders consistently make decisions or draw conclusions that imply a lower overall value than the data supports.
- **Misleading Comparisons:** When comparing the average of a line chart to a specific benchmark, viewers may incorrectly perceive the line's average as being below the benchmark when it is actually at or above it.

## How to Improve

- **Quick approach: Add a Reference Line.** Add a labeled horizontal line to the chart that explicitly marks the true average of the data series. This gives viewers a clear, unbiased visual anchor.

- **Moderate approach: Use Annotations.** Place a clear text annotation directly on the chart that states the average value (e.g., "Series Average: 75.3"). This removes ambiguity and reliance on perceptual estimation.

- **Comprehensive approach: Change Chart Type.** If accurately judging the average is the *most critical* task, a line chart may be the wrong choice. Consider replacing or supplementing it with a chart designed for summary statistics, such as a box plot, a strip plot with a mean indicator, or a simple dot plot showing only the average value.
