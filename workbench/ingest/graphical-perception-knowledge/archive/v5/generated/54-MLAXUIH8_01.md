---
id: avoid-line-chart-truncation-to-prevent-exaggeration
title: "Avoid truncating the y-axis of line charts to prevent exaggerating trends"

tags:
  - impact:perceptual
  - impact:pathos
  - impact:logos
  - chart:line
  - task:trend
  - task:direction
  - data:temporal
  - data:quantitative
  - audience:general

evidence:
  strength: medium
  summary: "Contrary to some common advice, truncating the y-axis of a line chart causes the same visual exaggeration of effect size as in bar charts. A 2020 study found no significant difference in the inflated 'perceived severity' between truncated line charts and bar charts (F(1,38) = 0.5, p = 0.50), as the steeper slope is perceived as a more dramatic change."

sources:
  - type: research
    ref: "Correll, Bertini, & Franconeri, 2020"
    url: "https://doi.org/10.1145/3313831.3376222"
    note: "Experiment 1 directly compared truncated line and bar charts and found no significant difference in how they inflate perceived severity. Truncation reliably increased perceived severity for line charts, just as it did for bar charts."
    role: primary
  - type: research
    ref: "Berger, 2005"
    url: "https://doi.org/10.1177/0093650204271169"
    note: "Earlier work, cited by Correll et al., found that line charts with steeper slopes are perceived as more 'threatening,' which helps explain the mechanism by which truncation (which steepens slopes) inflates perceived effect size."
    role: supporting

examples:
  - type: bad
    description: "A chart showing global temperature from 1880-2010 uses a y-axis from 55-60°F. While technically correct, this narrow range compresses a century of data into an almost flat line, obscuring the significant warming trend. This is the opposite of truncation exaggeration but shows the impact of axis choice."
    url: https://i.imgur.com/rNfS6D4.png
    caption: "A line chart with a wide axis range that hides the trend."
  - type: good
    description: "The same climate data, but with the y-axis zoomed to the actual range of the data. The upward trend is now clearly visible and accurately represented. The slope of the line now meaningfully communicates the rate of change."
    url: https://i.imgur.com/WlDofC5.png
    caption: "A line chart with an appropriate axis range that reveals the trend."
---

## Guidance

Avoid truncating the y-axis for line charts. While line charts encode data using position, not length, truncation steepens the line's slope, which viewers perceive as a more rapid or severe trend.

## Why

The primary purpose of a line chart is often to show trends, and the slope of the line is the key visual cue for the rate of change. When you truncate the y-axis, you effectively "zoom in" on the data, making the line segments steeper. Research shows that people perceive steeper slopes as more significant, severe, or "threatening." Thus, a truncated line chart, like a truncated bar chart, visually exaggerates the magnitude of the trend.

## When it applies

-   When visualizing trends over time or another continuous variable using a line chart.
-   When the audience is likely to interpret the steepness of the line as an indicator of the trend's severity.

## Exceptions

-   **Financial or Scientific Data in a Narrow Band:** For data like stock prices or patient vital signs, small fluctuations can be highly significant. A non-truncated axis might render these critical changes invisible. In such expert contexts, truncating the axis is often standard practice to amplify the signal.
-   **Index Charts:** Charts that are indexed to a starting value (e.g., 100) are designed to show relative change from that baseline, not an absolute zero. The baseline is the index value, not 0.

## Trade-offs

-   **Signal Visibility vs. Exaggeration:** Setting the axis to the full data range (or to zero) provides context but may make small trends appear flat. Truncating the axis makes the trend more visible but at the cost of exaggerating its steepness and perceived importance.

## Signs of Trouble

-   **Volcano-Like Slopes:** The line on the chart shows extremely dramatic peaks and valleys, but the y-axis range is very small and far from zero.
-   **Misleading Annotations:** A chart is labeled "dramatic increase" but the actual percentage change is modest; the drama comes entirely from the truncated axis.

## How to Improve

-   **Quick Fix: Widen the Axis.** Expand the y-axis range to be closer to zero or to a meaningful contextual baseline. Observe how this "flattens" the line and gives a more tempered view of the trend.

-   **Moderate Approach: Add Contextual Annotations.** If you must truncate, add explicit annotations about the magnitude of the change. For example, add a title like "Small but steady increase of 0.5% per year" to ground the visual in numerical reality.

-   **Comprehensive Redesign: Use an Indexed Chart.** To focus purely on the trend relative to a starting point, re-calculate the data as a percentage change from the first data point. This creates an "index chart" where the focus is explicitly on relative growth, and a zero baseline is not expected.