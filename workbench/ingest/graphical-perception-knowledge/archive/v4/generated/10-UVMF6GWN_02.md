---
id: separate-series-to-avoid-perceptual-pull
title: "Separate data series into different charts to avoid perceptual pull"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:line
  - chart:bar
  - chart:small-multiples
  - task:summary-mean
  - task:compare
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
    note: "Experiments 2 and 3 demonstrate a 'perceptual pull' effect, where the perceived average of one data series is biased toward the position of another series on the same chart."
---
## Guidance

When displaying multiple data series on the same plot, be aware that their perceived averages will be "pulled" toward each other. To ensure accurate perception of each series' average, separate them into small multiples.

## Why

Similar to a cognitive anchoring effect, the presence of an irrelevant data series on the same axes perceptually biases the estimated average of a target series. This "perceptual pull" can either exaggerate or diminish other inherent biases (like the underestimation of lines or overestimation of bars), leading to significant misinterpretation. The effect occurs regardless of whether the series are of the same type (e.g., two lines) or different types (e.g., a line and a bar chart).

## When it applies

- When showing two or more data series (e.g., multiple lines, multiple groups of bars, or a line and bars) on the same chart with a shared Y-axis.
- When the accurate estimation of the average value for *each individual series* is an important task for the viewer.

## Exceptions

- If the primary task is to compare the series *to each other* at specific points (e.g., "which line is higher in May?") or to judge the overall distance between them, plotting them on the same axes is necessary. In this case, the perceptual pull on their averages may be a secondary, acceptable concern.

## Trade-offs

- **Plotting Together:** Facilitates direct, point-by-point comparison between series but introduces perceptual pull, which compromises the accurate perception of individual averages.
- **Separating (Small Multiples):** Ensures more accurate perception of individual series averages but makes direct, point-by-point comparison across series more difficult, as it requires scanning between plots.

## Signs of Trouble

- **Convergence Error:** Viewers' estimates for the averages of two different series are closer together than they should be. For example, they might underestimate the average of a high-value series and overestimate the average of a low-value series shown on the same plot.
- **Exaggerated Bias:** The underestimation of a line chart's average is even worse when a second, lower-value data series is also present on the chart.
- **Distorted Comparison:** The perceived difference in averages between two series is smaller than the actual difference.

## How to Improve

- **Quick approach:** Add clear, distinct annotations with the true average value for each series. This provides a cognitive correction, though it does not fix the underlying perceptual bias.

- **Moderate approach:** Add distinct reference lines showing the average for each series (e.g., a dashed line for series A's average, a dotted line for series B's average). This can help anchor perception to the correct values but may clutter the chart.

- **Comprehensive approach:** Redesign the chart to use small multiples. Place each data series on its own chart, but keep the Y-axis scale consistent across all charts. This eliminates the perceptual pull by physically separating the series, allowing for more accurate judgment of each one's average.
