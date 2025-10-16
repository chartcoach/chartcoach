---
id: use-pie-charts-for-part-to-whole-estimation
title: "Use pie charts over simple bar charts for part-to-whole estimation"
tags:
  - impact:perceptual
  - chart:pie
  - chart:bar
  - chart:bar.stacked
  - task:composition
  - task:compare
  - data:quantitative
  - data:categorical
  - visual:angle
  - visual:length
  - audience:general
  - medium:static
sources:
  - type: research
    ref: Redmond, 2019
    url: https://doi.org/10.1109/VISUAL.2019.8933718
    note: Found that simple pie charts resulted in lower mean absolute error than simple horizontal stacked bar charts for part-to-whole estimation tasks.
---

## Guidance

For tasks requiring users to estimate the size of a segment as part of a whole, a simple pie chart can lead to more accurate estimations than a simple stacked bar chart that lacks a quantitative scale.

## Why

Experiments show that the mean absolute error is lower for pie charts than for baseline horizontal bar charts in part-to-whole judgment tasks. This may be due to the natural perceptual anchors (at 0°, 90°, 180°, and 270°) that pie charts provide, which viewers use as reference points for estimation.

## When it applies

- When the primary task is for a user to estimate the percentage or proportion of a single category relative to the total.
- When visualizing a small number of categories (typically 2-5).
- When comparing a simple (e.g., two-segment) pie chart against a simple stacked bar chart that does not have a quantitative scale.

## Exceptions

- This guidance does not apply when comparing multiple segments *against each other*, as bar charts with a common baseline are superior for that task.
- If a quantitative scale is added to the bar chart, the bar chart becomes significantly more accurate and likely outperforms the pie chart.
- For a large number of categories, a pie chart becomes cluttered and unreadable, making a sorted bar chart a better choice.

## Trade-offs

- While potentially more accurate for single-segment estimation, pie charts are notoriously poor for comparing non-adjacent slices or for comparing values across multiple different pie charts.
- Choosing a pie chart may go against the strong opinions of some stakeholders or established style guides that forbid their use, requiring you to justify the choice with evidence.

## Signs of Trouble

- **Frequent Misinterpretation:** Users consistently over or underestimate the proportions shown in a stacked bar chart without a scale.
- **Comparison Difficulty:** When looking at a stacked bar, users struggle to judge the size of any segment not on the baseline.

## How to Improve

- **Quick Fix: Add Labels.** If you must use a stacked bar chart, add direct percentage labels to each segment to remove ambiguity and the need for estimation.

- **Moderate Approach: Switch to a Pie Chart.** For a simple part-to-whole task, switch from a basic stacked bar chart to a pie chart, as evidence suggests it can improve estimation accuracy.

- **Comprehensive Approach: Use a Scaled Bar Chart.** The most accurate way to show part-to-whole proportions is often a 100% stacked bar chart with a clear quantitative scale from 0% to 100%. This provides the benefits of the bar format with the necessary reference points for accuracy.
