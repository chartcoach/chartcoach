---
id: recognize-line-chart-underestimation
title: "Recognize that viewers may systematically underestimate the average value of a line chart"

tags:
  # Impact dimensions (select all that apply)
  - impact:perceptual
  - impact:cognitive
  - impact:ethical

  # Chart types (use hierarchy with dots for specificity)
  - chart:line

  # Tasks (what the user is trying to accomplish)
  - task:summary-mean
  - task:trend
  - task:direction

  # Data characteristics
  - data:quantitative
  - data:temporal

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
  summary: "A 2020 empirical study found that viewers systematically perceive the average position of a line to be lower than its true value, a form of perceptual bias."

sources:
  - type: research
    ref: Xiong et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934400
    note: "Primary study that identified and measured the underestimation bias for average position in line charts across three experiments."
    role: primary # Options: primary | supporting | related

tools: []

examples: []
---

## Guidance

Be aware that viewers tend to underestimate the average value when reading a line chart. This perceptual bias can lead them to perceive trends or overall levels as lower than they actually are.

## Why

This is a perceptual bias where the visual encoding of a line "floating" in space leads to a systematic error in judgment. Even for a precise encoding like position, the visual form can distort our perception. The exact cause is still under investigation, but it appears to be a consistent effect. Misinterpreting the average can lead to flawed conclusions, such as underestimating overall performance or the severity of a trend.

### Core Principle

Perceptual judgments, even for precise visual encodings like position, are susceptible to systematic biases introduced by the specific visual form (e.g., a line versus a bar).

## When it applies

- When viewers need to estimate the average value, overall level, or central tendency of a data series represented by a line chart.
- This applies to both noisy and uniform (straight) line charts.

## Exceptions

- The bias may be less of a concern if the primary task does not involve judging the average (e.g., finding the maximum value or identifying a specific point in time).
- The bias can be directly counteracted by adding an explicit reference line showing the true average.

## Trade-offs

- Acknowledging this bias might require adding extra elements (like an average line) that could add visual clutter to the chart.
- Choosing an alternative chart type might mitigate this specific bias but could introduce others or be less effective for showing trends over time.

## Signs of Trouble

- **Understated Conclusions:** Viewers or stakeholders consistently draw conclusions that are more pessimistic or lower than what the data's true average supports (e.g., "Overall sales seem low" when the average is actually on target).
- **Inaccurate Comparisons:** When comparing a line chart's perceived average to an external benchmark or memory, the line chart may seem to underperform.

## How to Improve

- **Quick approach:** If the average value is a key takeaway, state it explicitly in the chart's title, subtitle, or an annotation. This provides a cognitive override to the perceptual bias.

- **Moderate approach:** Add a labeled reference line to the chart that marks the true average value. This gives viewers an accurate visual anchor and corrects for the underestimation bias.

- **Comprehensive approach:** If the primary task is to compare the average of multiple groups (rather than show a trend over time), consider using a chart that more directly encodes the average, such as a dot plot or a bar chart of the average values. Be aware that bar charts have their own overestimation bias.
