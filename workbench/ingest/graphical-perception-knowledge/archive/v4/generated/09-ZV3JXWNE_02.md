---
id: use-bar-chart-for-common-tasks
title: "Use bar charts for sorting, filtering, and understanding distributions"
tags:
  - impact:perceptual
  - chart:bar
  - task:sort
  - task:filter
  - task:distribution
  - task:cluster
  - task:aggregate
  - task:find-extremum
  - data:quantitative
  - data:categorical
sources:
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Meta-analysis (Table 9) shows bar charts are recommended for 6 out of 10 common analytical tasks based on a review of empirical studies [17, 34, 78]."
---

## Guidance

Bar charts are a highly effective and versatile choice for a majority of common analytical tasks, including sorting values, filtering data, characterizing distributions, clustering, and aggregation.

## Why

Bar charts encode quantitative values using the position of the bar's end along a common scale. This visual encoding is the most accurate for human perception of magnitude, making bar charts a robust and reliable default for many analytical goals. Their simplicity reduces cognitive load and allows for quick, accurate comparisons.

## When it applies

- The user needs to compare the magnitude of values across different categories.
- The task involves finding the largest or smallest value (`Find Extremum`), ordering categories by value (`Sort`), or seeing the shape of the data (`Characterize Distribution`).

## Exceptions

- **Correlation:** For visualizing the correlation between two quantitative variables, a scatterplot is superior.
- **Trends over Time:** For visualizing trends over a continuous variable like time, a line chart is generally preferred.
- **Part-to-Whole:** To emphasize a part-to-whole relationship, a pie chart or stacked bar chart may be used, but with a loss of accuracy for comparing the parts to each other.

## Trade-offs

- While effective, bar charts can become cluttered if there are too many categories. In such cases, it may be better to highlight the top N categories and group the rest into an "Other" category.
- Some research notes that the aspect ratio of bars can introduce systematic bias in perception, though this effect is often smaller than the inaccuracies of other chart types.

## Signs of Trouble

- A less effective chart type, like a pie chart or a word cloud, is being used for ranking or comparing magnitudes.
- Viewers have difficulty accurately determining the order or relative size of categories.

## How to Improve

- **Moderate Redesign: Switch to a Bar Chart.** If a pie chart, donut chart, or a series of numbers in a table is being used to show magnitudes for comparison, replace it with a bar chart.
- **Quick Fix: Sort the Bars.** For improved readability, sort the bars in ascending or descending order unless there is a natural, meaningful order to the categories (e.g., age groups, time periods).