---
id: add-scale-to-bar-charts
title: "Add a quantitative scale to bar charts for accurate estimations"

tags:
  - impact:perceptual
  - impact:logos
  - chart:bar
  - chart:bar.stacked
  - task:composition
  - task:lookup
  - task:compare
  - data:quantitative
  - visual:position
  - audience:general
  - medium:static
  - medium:screen

evidence:
  strength: medium
  summary: "A 2019 study (n=316 participants) found that adding an external quantitative scale to a bar chart for part-to-whole estimations yielded the highest accuracy. It significantly outperformed a baseline bar chart, a bar with internal tick marks, and even a pie chart (p<0.05, based on non-overlapping confidence intervals)."

sources:
  - type: research
    ref: Redmond, 2019
    url: https://doi.org/10.1109/VISUAL.2019.8933718
    note: "Found that a bar chart with a quantitative scale was the most accurate visualization for part-to-whole estimation, with a significantly lower mean absolute error than all other tested variants."
    role: primary

examples:
  - type: good
    description: "A horizontal stacked bar chart with a clearly labeled axis from 0% to 100% and major gridlines at 25%, 50%, and 75%. Viewers can easily look up the value of each segment."
  - type: bad
    description: "A progress bar in a dashboard showing project completion, but with no axis or label. It's impossible to tell if the project is 80% or 85% complete."
---

## Guidance

When using a bar chart for part-to-whole comparisons where accuracy matters, always include an external quantitative scale.

## Why

A scale transforms the viewer's task from a difficult perceptual estimation (judging length) to a much easier and more accurate value lookup (reading a position against a marked axis). This minimizes error and ambiguity, ensuring the data is communicated with precision.

### Core Principle

Explicitly encoding values with a scale enables precise lookups, which are more accurate than relying on perceptual estimation.

## When it applies

- When using a bar chart (especially a stacked bar or a single progress-style bar) to show part-to-whole data.
- When the viewer needs to know the precise value of a segment, not just its general size.
- When data accuracy and clarity are more important than a minimalist aesthetic.

## Exceptions

- **Sparklines:** In very small, word-sized graphics (sparklines), a scale would be illegible and add too much clutter. The goal of a sparkline is to show overall shape or trend, not precise values.
- **Redundant Labels:** If every segment of the bar is already annotated with a direct data label (e.g., "65%"), an axis scale may be redundant and can be removed to reduce clutter.

## Trade-offs

- **Visual Clutter:** A scale and its associated gridlines add visual elements to the chart, which can feel more cluttered than a simple, minimalist bar.
- **Space:** The axis and its labels require additional space, which might be a constraint in dense dashboards.

## Signs of Trouble

- **Guesswork:** Your chart displays a bar representing a quantity, but forces the viewer to guess its exact value. A user might think, "Is that bar 60% or 70%?"
- **Inconsistent Judgments:** Different users arrive at different estimates when reading the same bar chart.

## How to Improve

- **Quick Fix: Add Key Reference Marks.** If a full scale is too cluttered, add a few key gridlines or tick marks to serve as anchors. For a 0-100% scale, marks at 25%, 50%, and 75% are highly effective.

- **Moderate Approach: Add a Labeled Axis.** Add a complete quantitative axis (e.g., 0, 20, 40, 60, 80, 100) along the length of the bar. This is the standard and most effective way to provide a frame of reference.

- **Comprehensive Approach: Combine Scale with Direct Labels.** For maximum clarity, provide a full quantitative axis *and* place direct value labels on or next to the bar segments. This provides both the perceptual frame of the bar and the explicit value, serving both quick estimation and precise lookup tasks.
