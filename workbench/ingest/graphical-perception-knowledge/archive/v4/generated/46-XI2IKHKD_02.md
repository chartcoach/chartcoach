---
id: avoid-tables-pie-charts-for-correlation
title: "Avoid using tables or pie charts for correlation tasks"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:table
  - chart:pie
  - task:correlation
  - data:quantitative
  - audience:general
  - medium:static
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Saket et al., 2019
    url: https://doi.org/10.1109/TVCG.2018.2829750
    note: "Experiments showed that tables and pie charts were 'significantly less accurate, slower, and less preferred by users' for correlation tasks (Guideline G5)."

examples:
  - type: bad
    description: A table lists movie budgets and ratings. To find a correlation, a user must mentally scan and compare many pairs of numbers, which is slow and error-prone.
  - type: bad
    description: A pie chart shows budget per rating. It is perceptually impossible to judge the correlation between the two variables from the angles or areas of the slices.
---

## Guidance

Do not use tables or pie charts when the user's primary goal is to identify a correlation between two variables.

## Why

Correlation is a judgment of a relationship across many data points. Tables and pie charts are not visually structured for this task.
- **Tables** require users to read individual numbers and perform a series of slow, cognitively demanding mental comparisons to form a judgment about the overall trend. This is highly inefficient and error-prone.
- **Pie charts** encode data using angles and area, visual channels that are very poor for judging relationships between variables. It is perceptually impossible to see a trend across slices.

Empirical research confirms that both chart types lead to significantly lower accuracy, slower performance, and strong user disapproval for correlation tasks.

## When it applies

- The main task is to determine if a relationship exists between two variables (e.g., "Do sales increase with ad spend?").
- The data involves at least two quantitative or ordinal variables.

## Exceptions

- **When used for annotation:** A table might be presented *alongside* a scatterplot to provide exact values for lookup, but it should not be the primary tool for judging the correlation itself.

## Trade-offs

- There are no benefits to using tables or pie charts for correlation that would outweigh their severe perceptual and cognitive drawbacks. Following this guideline does not involve meaningful trade-offs; it is a fundamental best practice.

## Signs of Trouble

- **The "Mental Scan":** You observe users scanning back and forth between rows and columns in a table, trying to piece together a trend in their head.
- **Guesswork:** Users looking at a pie chart express confusion or simply guess when asked about a correlation.
- **Poor performance:** Task completion times for correlation questions are very high, and error rates are significant.
- **User frustration:** Users complain that the task is difficult or impossible with the provided visualization.

## How to Improve

- **Comprehensive approach:** Replace the table or pie chart with a visualization designed for correlation.
  - **For ordered data (like time series):** Use a **line chart**.
  - **For non-ordered quantitative data:** Use a **scatterplot**.

  Both of these chart types visually encode the data in a way that makes patterns of correlation perceptually obvious, dramatically improving accuracy, speed, and user satisfaction.
