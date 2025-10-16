---
id: use-delta-charts-for-proportions
title: "Use delta charts to accurately judge proportions of relationships"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:bar
  - chart:dot-plot
  - task:compare
  - task:distribution
  - task:summary
  - data:quantitative
  - visual:length
  - visual:position
  - access:cognitive-load-risk
sources:
  - type: research
    ref: Nothelfer & Franconeri, 2020
    url: https://doi.org/10.1109/TVCG.2019.2934801
    note: "Experiment 2 showed that using delta charts improved accuracy by over 30% when users had to judge which relationship type (e.g., increase or decrease) was more prevalent."
examples:
  - type: bad
    description: "In a chart showing 'before' and 'after' test scores for 30 students, it is very difficult to accurately judge whether more students improved or declined, especially if the changes are small."
  - type: good
    description: "A delta chart of the same data makes this judgment easy. It is simple to see that more bars are above the zero-line (improved) than below it (declined), allowing for an accurate summary of the distribution of changes."
---

## Guidance

To help users accurately judge the prevalence or proportion of different relationship types (e.g., are there more increases or decreases across all categories?), represent the data in a delta chart.

## Why

Judging the relationship for each individual pair in a standard chart requires significant cognitive effort, leading to high error rates, especially when the differences are small or the proportions are close to 50/50. A delta chart simplifies this task by encoding each relationship as a single positive or negative value around a common baseline. This makes it much easier to visually group, count, and compare the number of different relationship types, significantly improving the accuracy of summary judgments.

## When it applies

- When the task is to get a "gist" or summary of the relationships in aggregate, such as "Did most categories improve?" or "Is the trend generally positive or negative?"
- When judging the distribution of changes across a set of items is the primary goal.

## Exceptions

- If the proportions are extremely lopsided (e.g., 99% increases vs. 1% decrease), the benefit is smaller because the pattern might be obvious even in a standard chart showing individual values.

## Trade-offs

- This method prioritizes the accuracy of judging aggregate proportions over showing the absolute values that produced those proportions.

## Signs of Trouble

- **Guesswork:** Users feel like they are guessing when asked whether increases or decreases are more common in the data.
- **Inaccurate Summaries:** Different people looking at the same chart come to different conclusions about the overall trend.
- **"It's too close to call":** The chart design makes it perceptually difficult to distinguish between, for example, a 55/45 split and a 45/55 split.

## How to Improve

- **Quick Fix: Use Color to Encode Direction.** In the original chart (e.g., grouped bar chart), color-code the marks based on the direction of change (e.g., green for an increase, red for a decrease). This aids in visual grouping and counting without changing the chart structure.

- **Comprehensive Approach: Create a Delta Chart.** A delta chart, where increases are represented as positive values and decreases as negative values, makes the proportion of each immediately clear by comparing the number of marks above versus below the zero baseline.
