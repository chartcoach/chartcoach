---
id: apply-truncation-caution-to-bar-and-line-charts
title: "Apply the Same Caution for Y-Axis Truncation to Both Bar and Line Charts"
tags:
  - impact:perceptual
  - impact:ethical
  - chart:bar
  - chart:line
  - task:compare
  - task:trend
  - data:quantitative
  - audience:general
  - medium:static
evidence:
  strength: medium
  summary: "Challenging common wisdom, Correll et al. (2020) found no significant difference in the exaggeration of perceived effect size between bar charts and line charts when the y-axis was truncated (n=40, F(1,38) = 0.5, p = 0.50). Both chart types produced similar increases in perceived severity."
sources:
  - type: research
    ref: Correll, Bertini, & Franconeri, 2020
    url: https://doi.org/10.1145/3313831.3376222
    note: "Experiment 1 (n=40) directly compared bar charts and line charts at different truncation levels and found that 'increased y-axis truncation results in increased perceived severity' for both, with no significant interaction with chart type."
    role: primary
examples:
  - type: bad
    description: "A style guide strictly forbids truncating bar chart axes but provides no guidance for line charts, assuming they are exempt from perceptual exaggeration effects. This leads to inconsistent and potentially misleading charts."
  - type: good
    description: "A designer evaluates a truncated line chart showing climate change, recognizing that the steep slope, while accurately plotting the data points, will perceptually exaggerate the rate of change for viewers. They add an annotation to provide context."
---
## Guidance

Do not assume that line charts are immune to the perceptual exaggeration caused by y-axis truncation. The common advice to always start bar charts at zero while allowing truncated line charts is not supported by perceptual evidence regarding exaggeration effects. Apply the same critical judgment to both.

## Why

Experiments show that the subjective impact of y-axis truncation is persistent across both visualization designs. While they use different primary visual encodings (length for bars, position/slope for lines), truncating the axis magnifies the visual change in both cases, leading to a similar increase in the viewer's perception of the effect's severity.

### Core Principle

Perceptual exaggeration from axis truncation is a function of scaling the data range within the visual container, an effect that is not unique to a single type of encoding like length.

## When it applies

- When deciding on the y-axis range for a line chart or a bar chart.
- When creating or reviewing visualization style guides.

## Exceptions

- This guideline applies to the *perceptual effect of truncation*, not to the fundamental choice of which chart type to use. A line chart is still better for showing trends in continuous data, while a bar chart is better for comparing discrete categories. The choice of chart type should be based on the data structure first.

## Trade-offs

- Following this guideline may lead you to be more conservative with truncating line charts than is common practice.
- Conversely, it may also justify truncating a bar chart in situations where showing a small but important trend is critical—the same justification often used for line charts.

## Signs of Trouble

- **Inconsistent Standards:** Your style guide or practice strictly forbids truncated bar charts but is silent on or permissive of truncating line charts.
- **Unintended Exaggeration:** You have truncated a line chart to show a trend and assume there is no risk of the audience perceiving that trend as more dramatic than it is.

## How to Improve

- **Quick approach:** Review all charts with truncated axes, regardless of type. For line charts, add a clear note in the title or caption acknowledging the truncation and its purpose, just as you would for a bar chart.
- **Moderate approach:** Create a unified y-axis policy in your style guide that applies to both bar and line charts. This policy should focus on the *communicative goal* and the *scale of meaningful change*, rather than on the chart type.
- **Comprehensive approach:** For any chart where you truncate the axis (bar or line) to show detail, consider providing an alternative view or interactive control that allows the user to see the zero-baselined version to understand the full magnitude and context.
