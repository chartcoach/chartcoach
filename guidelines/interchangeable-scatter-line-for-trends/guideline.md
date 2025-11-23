---
id: interchangeable-scatter-line-for-trends
title: Treat Scatterplots and Line Charts as Equivalent for Trend Accuracy
bibliography: references.bib
description: Scatterplots and line charts provide comparable accuracy for correlation
  tasks.
labels:
- chart:scatterplot
- chart:line-chart
- task:correlate
- task:trend-estimation
- impact:flexibility
---

## The Rule <!-- role: advice -->
Choose freely between scatterplots and line charts when designing for trend estimation, as they offer equivalent performance accuracy.

## The Logic <!-- role: reason -->
Empirical rankings indicate no statistically significant performance difference between scatterplots and line charts for correlation tasks. Both encodings allow users to perform "regression by eye" with similar levels of accuracy, unlike area charts which degrade performance.
*   **The Principle:** Equivalent Encoding Efficiency
*   **The Evidence:** Structured rankings place both Line Charts (E-2) and Scatterplots (E-1) in the top tier for correlation tasks, distinguishing them from lower-performing designs like area charts [@zeng_review_2023] [@correll_regression_2017].

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying correlations or trends in bivariate data.
*   **Data Type:** Quantitative data on the Y-axis; Ordinal or Quantitative data on the X-axis.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High data density (Overplotting).
*   **Reason:** If data points are extremely dense, a line chart (aggregating or connecting points) may be clearer than a scatterplot cloud.
*   **Scenario:** Discrete, non-ordered categories.
*   **Reason:** A line chart implies continuity. If the X-axis is nominal (unordered categories), a line chart is misleading, and a scatterplot or strip plot must be used.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Relying solely on accuracy metrics ignores secondary design factors like implied continuity (Line) vs. discrete observation (Scatter).
*   **The Risk:** Choosing a line chart for discrete data may imply a temporal relationship that does not exist, even if the trend accuracy is theoretically equivalent.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Avoiding line charts for trend tasks because they are "less statistical" than scatterplots.
*   **Why it fails:** Evidence suggests users can extract correlation trends from lines just as well as from points.

## How to Check <!-- role: check -->
*   **The Test:** Check if the X-axis implies a sequence. If yes, both charts are valid options.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Select the chart type based on whether you wish to emphasize the *sequence* of values (Line) or the *distribution* of individual observations (Scatter), knowing that accuracy remains constant.
