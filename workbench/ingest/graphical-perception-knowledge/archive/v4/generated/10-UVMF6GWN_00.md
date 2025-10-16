---
id: anticipate-underestimation-of-line-chart-averages
title: "Anticipate that viewers will underestimate the average value of a line chart"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:ethical
  - chart:line
  - task:summary-mean
  - data:quantitative
  - visual:position
  - access:cognitive-load-risk
  - audience:general
  - medium:static
  - medium:screen
sources:
  - type: research
    ref: Xiong et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934400
    note: "Experiments 1, 2, and 3 consistently showed that the average position of a single line in a line chart is systematically underestimated by viewers."
---
## Guidance

Be aware that viewers tend to systematically perceive the average value of a line in a line chart as lower than it actually is.

## Why

Research shows a consistent perceptual bias where the estimated average position of a line is underestimated. This occurs even for simple, single-series line charts and can lead to inaccurate takeaways about the data's central tendency. This bias appears to be a low-level perceptual phenomenon, not a result of a conscious strategy.

## When it applies

- When a key goal is for the user to accurately estimate the average value or overall level of a data series represented by a line chart.
- This applies to both noisy (variable) and uniform (straight) lines.

## Exceptions

- If the primary task is not to estimate the average (e.g., identifying peaks/troughs, comparing specific points, or judging the overall trend direction or volatility), this bias may be less critical.

## Trade-offs

- While line charts are excellent for showing trends over time, this inherent bias can compromise the accuracy of average value perception. Acknowledging this means you might need to add other visual cues to compensate, which could add clutter.

## Signs of Trouble

- **User Misinterpretation:** Users verbally describe or make decisions based on a lower-than-actual average value for the series.
- **Comparative Errors:** When comparing the average of the line chart to a specific benchmark or another chart, users consistently judge the line chart's average as being lower than it is.

## How to Improve

- **Quick approach:** Explicitly state the average value in an annotation, title, or caption. This provides a cognitive correction, even if the perceptual bias remains.

- **Moderate approach:** Add a visual reference line to the chart that marks the true average value. This gives viewers a direct, unbiased anchor for comparison, helping to override the perceptual illusion.

- **Comprehensive approach:** If accurate average perception is the most critical task, consider if another chart type might be less prone to this specific bias. However, be aware that other chart types have their own biases (e.g., bar charts are often overestimated). The best choice depends on which type of error is more acceptable for your use case.
