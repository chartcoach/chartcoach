---
id: prefer-bar-charts-for-comparisons
title: "Use bar charts for comparing, ranking, and looking up values across categories"

tags:
  - impact:perceptual
  - impact:logos
  - chart:bar
  - task:compare
  - task:rank
  - task:lookup
  - task:distribution
  - task:find-extremum
  - data:quantitative
  - data:categorical
  - visual:position
  - visual:length

sources:
  - type: research
    ref: Saket et al., 2019
    url: https://doi.org/10.1109/TVCG.2018.2864511
    note: "This study, cited as [78] in the review paper, empirically tested five chart types across ten tasks. Bar charts were found to be a top performer for a majority of tasks, including cluster, filter, sort, and aggregation."
  - type: research
    ref: Cleveland & McGill, 1984
    url: https://doi.org/10.2307/2288400
    note: "The foundational work showing that judging position and length on a common scale (the core task in a bar chart) is highly accurate."

tools:
  - type: learn
    name: "Datawrapper Chart Academy: Bar Charts"
    url: https://academy.datawrapper.de/article/133-what-is-a-bar-chart
    description: "A comprehensive guide on when and how to use bar charts effectively."

examples:
  - type: good
    description: "A horizontal bar chart showing the population of the 10 largest cities. The bars are sorted from largest to smallest, making it trivial to compare populations and rank the cities."
  - type: bad
    description: "A pie chart showing the market share of 10 different companies. It's nearly impossible to accurately compare or rank the companies with similar market shares by looking at the slice angles."
---

## Guidance

For displaying and comparing quantitative values across a set of discrete categories, use a bar chart. Sort the bars by value to facilitate ranking and comparison, unless there is an intrinsic order to the categories (e.g., time periods).

## Why

Bar charts encode quantitative data using the length of bars, which are aligned to a common baseline. This leverages our visual system's ability to make highly accurate judgments of position and length. Empirical studies have confirmed that bar charts are one of the most effective and versatile chart types for a wide range of common analytical tasks, including comparing values, ranking categories, filtering data, and identifying extremes.

## When it applies

- When you have one quantitative variable and one categorical variable.
- When the primary user task is to compare the magnitudes of different categories (e.g., "Which product had the highest sales?").
- When you need to show rankings or distributions across categories.

## Exceptions

- **Trends over Time:** For showing a trend over a continuous interval like time, a line chart is generally more effective as it visually emphasizes continuity and change.
- **Correlation:** To show the relationship between two quantitative variables, a scatterplot is the correct choice.
- **Part-to-Whole Composition:** While a bar chart can show composition, a stacked bar chart or treemap might be preferred if the total is meaningful and the breakdown is the main story. However, for comparing the parts, a simple bar chart is still superior.

## Trade-offs

- **Space:** Bar charts, especially with long category labels, can take up significant space. Using a horizontal bar chart can help accommodate long labels.
- **Number of Categories:** With a very large number of categories, a bar chart can become cluttered. In this case, you might need to highlight the most important bars, or switch to a different visualization like a heatmap.

## Signs of Trouble

- **Truncated Axis:** The y-axis of a bar chart does not start at zero, causing the relative lengths of the bars to be visually deceptive.
- **Hard to Compare:** Viewers struggle to compare the values of different categories. This often happens when a different chart type, like a pie chart, is used instead.
- **Unsorted Bars:** The bars are sorted alphabetically or arbitrarily, forcing the viewer to scan the entire chart to find the highest/lowest values or to determine ranks.

## How to Improve

- **Quick Fix: Sort the Bars.** If your bar chart's categories have no inherent order, sort the bars in ascending or descending order of their value. This simple change dramatically reduces the cognitive load required to rank items and find extremes.

- **Moderate Approach: Switch to a Bar Chart.** If you are using a less effective chart type for comparison (like a pie chart, donut chart, or a set of bubbles), switch to a bar chart. This will immediately improve the accuracy of your audience's perceptual judgments.

- **Comprehensive Redesign: Use Horizontal Bars for Long Labels.** If your category labels are long and getting truncated or angled, switch from a vertical bar chart to a horizontal bar chart. This provides ample space for readable, horizontal labels next to each bar.