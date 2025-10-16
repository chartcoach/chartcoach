---
id: avoid-perceptual-pull-multi-series
title: "Separate data series into small multiples to prevent perceptual pull when comparing averages"

tags:
  # Impact dimensions (select all that apply)
  - impact:perceptual
  - impact:cognitive
  - impact:ethical

  # Chart types (use hierarchy with dots for specificity)
  - chart:line
  - chart:bar

  # Tasks (what the user is trying to accomplish)
  - task:summary-mean
  - task:compare

  # Data characteristics
  - data:quantitative

  # Visual channels
  - visual:position

  # Audience characteristics
  - audience:general

  # Medium/format
  - medium:static
  - medium:screen

  # Accessibility risks
  - access:cognitive-load-risk

evidence:
  strength: medium # Options: high | medium | low
  summary: "A 2020 study demonstrated a 'perceptual pull' effect, where plotting two series on the same chart biases the perceived average of each series toward the other, distorting judgment."

sources:
  - type: research
    ref: Xiong et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934400
    note: "Primary study that identified the 'perceptual pull' effect when multiple series (line/line, bar/bar, line/bar) are plotted together."
    role: primary # Options: primary | supporting | related

tools: []

examples: []
---

## Guidance

When viewers need to accurately judge and compare the average values of individual data series, avoid plotting them together on the same set of axes. The presence of one series can "pull" the perceived average of another series toward it, either exaggerating or diminishing the true difference between them.

## Why

This "perceptual pull" effect acts like a cognitive anchoring bias. The second, "irrelevant" data series becomes a powerful visual anchor that distorts a viewer's judgment of the target series. For example, plotting a low-performing series next to a high-performing series can make the high series seem lower and the low series seem higher than they would individually, minimizing their perceived difference. This can lead to seriously flawed comparisons and conclusions.

### Core Principle

Irrelevant information within a single visualization can act as a powerful perceptual anchor, systematically biasing judgments of the relevant information.

## When it applies

- When the primary task is to judge or compare the average level of two or more different data series (e.g., "Is Region A's performance generally higher than Region B's?").
- This effect was observed when plotting two line charts, two bar charts, or a line chart and a bar chart together.

## Exceptions

- If the primary task is to find specific intersections, compare individual point-in-time values, or assess correlation, plotting series together may be necessary and the risk to *average judgment* may be an acceptable trade-off.
- If the series are very far apart, the pull effect might be less pronounced, though it still exists.

## Trade-offs

- **Clarity vs. Space:** Separating series into small multiples is the most effective way to eliminate perceptual pull, but it requires more screen or page space. Plotting them together saves space but introduces a high risk of biased judgment.
- **Comparison Type:** Small multiples excel at comparing overall patterns and averages but can make specific point-in-time comparisons (e.g., "What was the exact difference in May?") more difficult than an overlaid chart.

## Signs of Trouble

- **Distorted Differences:** Viewers perceive a different magnitude of difference between two series' averages than what the data shows. This can manifest as either:
    - **Exaggeration:** A high series next to a low series makes the low one seem even lower.
    - **Minimization:** The series' averages are perceived as more similar than they really are.
- **Biased Judgment against a Target:** When a line chart of 'Target' values is overlaid on a bar chart of 'Actual' values, the perceived average of the 'Actuals' is pulled toward the 'Target' line, distorting the assessment of performance.

## How to Improve

- **Quick approach:** Add explicit annotations stating the average value for each series. This provides a cognitive "escape hatch" for viewers, allowing them to rely on explicit numbers instead of biased perception.

- **Moderate approach:** If the main goal is to compare the averages, create a separate summary chart. For example, a simple bar chart or dot plot where each mark represents the calculated average of a series. This directly encodes the values to be compared.

- **Comprehensive approach:** Use small multiples (also called faceting or trellising). Place each data series in its own small, separate chart, but ensure all charts share the same, aligned y-axis. This design removes the perceptual pull between series while still allowing for accurate comparison across a common scale.
