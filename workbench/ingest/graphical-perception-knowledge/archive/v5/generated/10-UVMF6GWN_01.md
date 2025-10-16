---
id: recognize-bar-chart-overestimation
title: "Recognize that viewers may systematically overestimate the average value of a bar chart"

tags:
  # Impact dimensions (select all that apply)
  - impact:perceptual
  - impact:cognitive
  - impact:ethical

  # Chart types (use hierarchy with dots for specificity)
  - chart:bar

  # Tasks (what the user is trying to accomplish)
  - task:summary-mean

  # Data characteristics
  - data:quantitative
  - data:categorical

  # Visual channels
  - visual:position
  - visual:size

  # Audience characteristics
  - audience:general

  # Medium/format
  - medium:static
  - medium:screen

  # Accessibility risks
  - access:cognitive-load-risk

evidence:
  strength: medium # Options: high | medium | low
  summary: "A 2020 empirical study found that viewers systematically perceive the average position of a set of bars to be higher than its true value, a consistent perceptual bias."

sources:
  - type: research
    ref: Xiong et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934400
    note: "Primary study that identified and measured the overestimation bias for average position in bar charts."
    role: primary # Options: primary | supporting | related
  - type: research
    ref: Ceja et al., 2020
    url: https://doi.org/10.1109/TVCG.2020.3031024
    note: "This paper, referenced in the literature review, suggests aspect ratio influences bias in bar charts, providing context for exceptions."
    role: related

tools: []

examples: []
---

## Guidance

Be aware that viewers tend to overestimate the average value of a group of bars in a bar chart. This can lead to interpretations that are more optimistic or inflated than the data supports.

## Why

This perceptual bias may occur because bars are "grounded" to an axis, drawing attention to their endpoints (peaks) and their filled area. Unlike a "floating" line, the solid form of bars seems to produce a consistent error where the visual average is perceived as higher than the true statistical average. This can lead to significant misjudgments, especially when assessing overall performance or comparing against a target.

### Core Principle

The visual form of a data representation (e.g., solid bars grounded on an axis) can introduce systematic biases into perceptual judgments, even for a precise encoding like position.

## When it applies

- When viewers need to estimate the average value or central tendency of a series of bars.
- The study showed this bias occurs for bars extending upwards from a bottom axis and for bars hanging downwards from a top axis.

## Exceptions

- The bias may be less of a concern if the task is to compare individual bars or find a specific value, rather than judging the series average.
- Other research suggests the bias may be affected by the aspect ratio of the bars (e.g., very wide or very tall bars may be biased differently), though this is an area of ongoing study.

## Trade-offs

- Choosing an alternative chart type (like a line chart) to avoid this bias would introduce an underestimation bias instead.
- Adding an explicit average line to mitigate the bias can add visual clutter.

## Signs of Trouble

- **Inflated Conclusions:** Stakeholders consistently draw conclusions that are more positive or higher than the true average of the data suggests (e.g., "Performance looks great overall" when the average is merely mediocre).
- **Misleading Comparisons:** When comparing the perceived average of the bars to a target line, the bars may appear to be performing better than they actually are.

## How to Improve

- **Quick approach:** If the average value is a key message, state it explicitly in the chart's title, subtitle, or an annotation. This gives viewers a cognitive anchor to correct their perceptual judgment.

- **Moderate approach:** Add a labeled reference line to the chart that marks the true average. This provides an accurate visual benchmark, directly counteracting the overestimation bias.

- **Comprehensive approach:** If judging the average is critical, consider using a dot plot instead of a bar chart. Using points instead of filled bars may reduce the bias associated with the bars' area and grounding, though this requires further testing. For comparing averages across categories, a dedicated bar chart of just the average values is most direct.
