---
id: anticipate-overestimation-of-bar-chart-averages
title: "Anticipate that viewers will overestimate the average value of a bar chart"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:ethical
  - chart:bar
  - task:summary-mean
  - data:quantitative
  - visual:position
  - visual:size
  - access:cognitive-load-risk
  - audience:general
  - medium:static
  - medium:screen
sources:
  - type: research
    ref: Xiong et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934400
    note: "Experiments 1, 2, and 3 consistently showed that the average position of a set of bars is systematically overestimated by viewers."
---
## Guidance

Be aware that viewers tend to systematically perceive the average value (height) of a set of bars in a bar chart as higher than it actually is.

## Why

Research demonstrates a consistent perceptual bias where the estimated average position of bars is overestimated. This happens even for single-series bar charts and can lead to an inflated mental model of the data's central tendency. The paper speculates this may be related to how bars are encoded (using length/area in addition to position) or their aspect ratio.

## When it applies

- When a key goal is for the user to accurately estimate the average value of a series represented by a bar chart.
- This applies whether the bars are of uniform height or are noisy (variable).

## Exceptions

- If the primary task is not to estimate the average (e.g., comparing individual bars, looking up specific values), this bias is less concerning.
- The same research notes that position judgments for bars were more *precise* (less variable) than for lines, despite the bias. Therefore, this overestimation might be an acceptable trade-off for higher precision in judgment.

## Trade-offs

- While bar charts are standard for comparing magnitudes, this overestimation bias can affect the perception of the group's average. Mitigating it with annotations can add visual clutter.

## Signs of Trouble

- **Inflated Estimates:** Users make decisions or draw conclusions based on an average value that is higher than the true mean of the data.
- **Benchmark Errors:** When comparing the average of the bars to a reference line or value, users may incorrectly judge the bars' average as exceeding the benchmark when it does not.

## How to Improve

- **Quick approach:** Explicitly state the average value of the series in an annotation, title, or caption. This provides a direct cognitive correction.

- **Moderate approach:** Add a visual reference line to the chart that marks the true average value. This provides an unbiased anchor that helps viewers correct their biased perception.

- **Comprehensive approach:** The paper suggests the bias might be related to the aspect ratio of the bars. While more research is needed, you could experiment with different bar widths to see if it mitigates the effect. For now, adding a clear reference line is the most reliable strategy.
