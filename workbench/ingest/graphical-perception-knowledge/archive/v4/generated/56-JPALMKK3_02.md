---
id: avoid-extra-ticks-on-pie-charts
title: "Avoid adding redundant tick marks to pie charts"
tags:
  - impact:perceptual
  - impact:aesthetic
  - chart:pie
  - task:composition
  - task:compare
  - data:quantitative
  - visual:angle
  - audience:general
  - medium:static
sources:
  - type: research
    ref: Redmond, 2019
    url: https://doi.org/10.1109/VISUAL.2019.8933718
    note: "Found no significant difference in accuracy between a baseline pie chart and a pie chart with added quartile cues (0%, 25%, 50%, 75%), suggesting the ticks are redundant."
---

## Guidance

Adding visual cues like tick marks at the quartiles (0%, 25%, 50%, 75%) to a pie chart does not significantly improve the accuracy of part-to-whole estimations and should be avoided to reduce clutter.

## Why

Research suggests that pie charts inherently possess "natural visual anchors" at the 0°, 90°, 180°, and 270° positions, which viewers instinctively use for estimation. Adding explicit ticks at these same locations is redundant, adds visual clutter, and provides no additional perceptual benefit.

## When it applies

- When designing pie charts for part-to-whole estimation tasks.
- When considering adding non-data visual aids like background guides or tick marks to a pie chart.

## Exceptions

- If the goal is to highlight a specific, non-standard threshold (e.g., a company target of 33%), a single, targeted marker or line might be useful. This guideline applies specifically to redundant, standard-interval ticks like quartiles.

## Trade-offs

- By omitting unnecessary ticks, you achieve a cleaner, more minimalist aesthetic. The trade-off is negligible, as research shows no loss in estimation accuracy.

## Signs of Trouble

- **Chart Clutter:** The pie chart is adorned with ticks, grid lines, or other decorative elements that do not encode data and may distract the viewer.
- **Redundant Information:** Visual elements are present that simply reinforce the inherent structure of the chart, such as a line at the 90° mark on a pie chart.

## How to Improve

- **Quick Fix: Remove the Ticks.** Simply remove the unnecessary quartile tick marks or other non-data guides from the pie chart design to reduce clutter.

- **Moderate Approach: Use Direct Labels.** Instead of relying on any form of estimation, add direct data labels (e.g., "42%") to each slice. This is the most effective way to ensure precise communication of values in a pie chart and removes the need for any estimation aids.

- **Comprehensive Approach: Re-evaluate the Task.** If viewers need such precise values that tick marks are being considered, it signals that the primary task may be 'lookup' rather than 'estimation'. In this case, a table or a bar chart with a scale is a more appropriate and accurate tool than a pie chart.
