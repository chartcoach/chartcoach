---
id: bar-chart-average-overestimation
title: "Recognize that viewers tend to overestimate the average value in bar charts"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:ethical
  - chart:bar
  - task:summary-mean
  - task:aggregate
  - data:quantitative
  - visual:position
  - visual:length
  - audience:general
  - medium:static
  - medium:screen
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "Xiong et al. (2020), in a series of three controlled experiments (n=37 total), found that viewers systematically and significantly overestimate the average value of a set of bars (p<0.001). This bias persisted regardless of whether the bars were uniform or noisy."
sources:
  - type: research
    ref: Xiong et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934400
    note: "Primary study demonstrating a consistent overestimation bias for the average of bar charts across three experiments. For example, in Experiment 1 the mean deviation was +4.19 pixels (p<0.001)."
    role: primary
role: primary
---

## Guidance

When presenting a bar chart where viewers need to estimate the average value of the series, be aware that they will likely perceive the average as being higher than it actually is.

## Why

Viewers are subject to a perceptual bias that causes a systematic overestimation of the average height or length of bars. This means their visual summary of the group's central tendency is skewed upwards. The paper speculates this may be due to the bars' aspect ratio or figure-ground effects, where the ends of the bars ("peaks") draw more attention.

### Core Principle

The way a visual mark is constructed can introduce perceptual biases. The solid, grounded nature of bars appears to be perceived differently from the floating nature of lines when judging averages.

## When it applies

- When a key task for the viewer is to judge, estimate, or compare the overall average value of a group of bars.
- This applies to both single-series and multi-series bar charts.

## Exceptions

- When the primary task is to compare the values of individual bars against each other, and the average of the entire set is not relevant.
- When the average value is explicitly annotated on the chart, removing the need for perceptual estimation.

## Trade-offs

- Bar charts are excellent for accurately comparing the magnitudes of individual categories. This benefit, however, comes with the risk of misrepresenting the group's average value if that is also a task for the viewer.

## Signs of Trouble

- **Inflated Perceptions:** Viewers or stakeholders draw conclusions that assume a higher overall group performance or value than the data actually supports.
- **Misleading Benchmarking:** When comparing the average of a set of bars to a target line, viewers may incorrectly perceive the average as meeting or exceeding the target when it is actually below it.

## How to Improve

- **Quick approach: Add a Reference Line.** Overlay a labeled horizontal line on the chart that explicitly marks the true average value. This provides an unbiased visual anchor for comparison.

- **Moderate approach: Overlay Summary Marks.** Superimpose a box plot or a dot/strip plot over the bars to explicitly show the mean or median. This keeps the individual bar values while adding a clear, accurate summary.

- **Comprehensive approach: Change Chart Type.** If the most critical task is to communicate the average and distribution, a bar chart may be suboptimal. Replace it with a chart designed for summary statistics, such as a box plot or a violin plot, which more accurately convey central tendency and spread.
