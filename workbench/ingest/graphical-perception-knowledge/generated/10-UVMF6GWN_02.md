---
id: avoid-perceptual-pull-multi-series
title: "Use caution when plotting multiple series if judging averages is important, due to 'perceptual pull' bias"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:line
  - chart:bar
  - task:summary-mean
  - task:aggregate
  - task:compare
  - data:quantitative
  - visual:position
  - visual:length
  - audience:general
  - medium:static
  - medium:screen
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "Xiong et al. (2020, n=24 in relevant experiments) demonstrated a 'perceptual pull' effect where the perceived average of one data series is biased toward the position of another series in the same chart. This interaction was significant (p<0.001) and occurred between two lines, two bar series, or a line and a bar series."
sources:
  - type: research
    ref: Xiong et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934400
    note: "Demonstrated that an irrelevant second data series 'pulls' the perceived average of the target series toward itself, either exaggerating or diminishing the inherent under/overestimation biases. The effect was independent of the mark type of the distracting series."
    role: primary
---

## Guidance

Avoid plotting multiple data series (e.g., two lines, or a line and a bar chart) on the same axes if the primary task is for viewers to accurately estimate the average value of each series independently. The series will perceptually "pull" on each other, distorting their perceived averages.

## Why

The human visual system does not perfectly isolate the two data series. Instead, it exhibits a "perceptual pull" or anchoring effect, where the position of one series influences the perceived average of the other. The perceived averages of the two series are biased towards each other, making them seem closer together than they really are. This can either reduce or exaggerate the inherent underestimation (for lines) and overestimation (for bars) biases.

### Core Principle

Irrelevant but salient visual information can systematically and involuntarily bias the perception of relevant information. The brain integrates contextual information, even when it is instructed to ignore it.

## When it applies

- When displaying two or more data series in the same plot area using lines or bars.
- When an important user task is to estimate the average value of at least one of those series.
- When comparing the averages of the two series to each other.

## Exceptions

- When the primary task is to judge the *difference* or *gap* between the series at specific points in time, not their overall averages.
- When the series are so far apart that the pull effect is likely negligible (though the threshold for this is not known).
- When the goal is to show a general relationship, and precise average estimations are not required.

## Trade-offs

- Plotting multiple series on one chart is space-efficient and excellent for direct, point-by-point comparison. However, this efficiency comes at the cost of introducing a bias that distorts the perception of each series' overall average.

## Signs of Trouble

- **Converging Averages:** Viewers perceive the averages of two series to be more similar than they actually are. For example, a high series is perceived as lower and a low series as higher.
- **Exaggerated Biases:** The perceptual pull amplifies existing biases. For instance, in a chart with a high line and a low line, the low line (target) is pulled down even further by the high line, making its underestimation worse.
- **Inaccurate Comparisons:** Viewers make flawed judgments about which series has a higher average, or by how much, because the perceived difference is distorted.

## How to Improve

- **Quick approach: Increase Visual Separation.** Use highly distinct colors for each series. Add labeled horizontal lines showing the true average for *each series* to provide clear, unbiased anchors. This mitigates the pull by providing correcting information.

- **Moderate approach: Use Small Multiples.** Separate the series into adjacent, faceted charts that share the same y-axis. This physically removes the "pull" from the other series while still allowing for easy comparison of their levels and trends across the aligned axes.

- **Comprehensive approach: Create a Summary Chart.** If the *only* task is to compare the averages, create a separate, simpler chart that visualizes *only* the average values. A simple dot plot or bar chart showing the two average values directly is far more accurate for this specific task than a chart showing the full series.
