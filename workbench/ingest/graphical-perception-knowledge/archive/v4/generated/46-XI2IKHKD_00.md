---
id: use-bar-charts-for-cluster-identification
title: "Use bar charts for identifying clusters"

tags:
  - impact:perceptual
  - impact:performance
  - chart:bar
  - task:cluster
  - data:categorical
  - data:quantitative
  - audience:general
  - medium:static

sources:
  - type: research
    ref: Saket et al., 2019
    url: https://doi.org/10.1109/TVCG.2018.2829750
    note: "Experiment found bar charts had high accuracy and speed, and were significantly more preferred by users than pie charts for finding clusters (Guideline G1)."

examples:
  - type: good
    description: A bar chart is used to show the number of movies per genre. It is easy to see the distinct groups (clusters) of genres.
  - type: bad
    description: A line chart is used to show the same data. It is difficult to count the number of distinct groups because the connecting lines create a false sense of continuity.
---

## Guidance

When users need to identify the number of groups or clusters in categorical data, use a bar chart.

## Why

Bar charts encode values using length from a common baseline, which is a highly effective visual channel for human perception. This makes it easy to group items of similar size. An empirical study found that for cluster identification tasks, bar charts offer an excellent combination of high accuracy, high speed, and strong user preference compared to other basic chart types like line charts, scatterplots, or even pie charts.

## When it applies

- The task is to count the number of distinct groups or clusters within a set of categorical data (e.g., "How many different genres are shown in this chart?").
- The dataset has one categorical and one quantitative attribute.
- The number of categories is relatively low (the study used datasets with 5-34 data points, which mapped to fewer categories).

## Exceptions

- **When part-to-whole is critical:** If the primary goal is to see the clusters as a proportion of a total, a pie chart is also a fast and accurate option, though it is generally less preferred by users and performs poorly on other tasks.
- **For multivariate data:** If clustering involves more than two variables, a bar chart is insufficient. A chart type like a parallel coordinates plot or a more advanced clustering visualization would be necessary.

## Trade-offs

- **Space:** Bar charts can take up more space than a pie chart, especially with long category labels.
- **Part-to-whole relationship:** While you can see the relative sizes of clusters in a bar chart, the relationship to the total sum is less immediately apparent than in a pie chart.

## Signs of Trouble

- **User confusion:** Users are taking a long time or making frequent errors when asked to count the number of categories in a visualization.
- **Incorrect chart type:** A line chart is being used for purely categorical data, implying a trend or connection between discrete categories that doesn't exist.
- **Over-plotting:** A scatterplot with overlapping points makes it hard to distinguish or count the underlying groups.

## How to Improve

- **Quick approach:** If using another chart type, ensure the categories are clearly distinct. For a scatterplot, use different colors or shapes for each category. For a pie chart, ensure slices are clearly labeled.
- **Comprehensive approach:** Switch to a bar chart. Sort the bars by value (ascending or descending) to make it even easier to see the groups and their relative sizes. This addresses the task directly by using the most effective visualization type found in the research.
