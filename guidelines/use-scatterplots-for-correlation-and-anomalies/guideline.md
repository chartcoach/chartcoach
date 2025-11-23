---
id: use-scatterplots-for-correlation-and-anomalies
title: Use Scatterplots for Correlation and Anomaly Detection
bibliography: references.bib
description: Select scatterplots over other chart types when the primary analysis
  tasks are finding anomalies or determining correlation.
labels:
- chart:scatterplot
- task:correlate
- task:find-anomalies
- visual:position
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Choose scatterplots as the primary visualization design when the user's task is to identify correlations between attributes or to find anomalies within the dataset.

## The Logic <!-- role: reason -->
Based on a collation of graphical perception studies, scatterplots consistently outperform other visualization types for specific analytical tasks.
*   **The Principle:** Spatial Position Efficiency. The scatterplot's use of position on two continuous axes allows for the most accurate detection of trends (correlation) and outliers (anomalies) compared to alternative designs like parallel coordinates or table lenses.
*   **The Evidence:** In a systematic review of 59 papers, [@zeng_review_2023] synthesizes results showing that scatterplots are the "top choices" specifically for `correlate` and `find anomalies` tasks. This reinforces the task-based design framework proposed by [@sarikaya_scatterplots_2018], which categorizes these as core tasks supported by standard scatterplot designs.

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to see if Variable A increases as Variable B increases, or needs to spot data points that deviate significantly from the norm.
*   **Data Type:** Two continuous quantitative variables.
*   **Audience:** General analysts and scientific users familiar with cartesian coordinates.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset contains a massive number of points leading to severe overdraw.
*   **Reason:** As noted by [@sarikaya_scatterplots_2018], traditional scatterplots fail to scale when the number of points exceeds available screen pixels, making correlation difficult to assess due to occlusion.
*   **Scenario:** The user needs to compare values precisely across many dimensions.
*   **Reason:** Parallel coordinates may outperform scatterplots for specific multi-dimensional cluster tasks [@zeng_review_2023].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Space efficiency. Scatterplots generally require a square or near-square aspect ratio to avoid biasing correlation perception, consuming more screen real estate than compact lists or bar charts.
*   **The Risk:** Perceptual bias. Users may underestimate correlation in parallel coordinate plots, making scatterplots the safer, albeit larger, choice [@zeng_review_2023].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using Parallel Coordinates for correlation tasks.
*   **Why it fails:** Empirical evidence suggests that the degree of correlation is often underestimated in parallel coordinates compared to scatterplots [@zeng_review_2023].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using a chart other than a scatterplot (e.g., a table or parallel coordinates) to show a relationship between two variables?
*   **The Test:** Ask if the primary goal is to see a trend line or a lone outlier. If yes, and the chart is not a scatterplot, apply the rule.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the visualization type to a standard 2D scatterplot.
*   **Best Fix:** Ensure the scatterplot aspect ratio is appropriate for the data range to maximize correlation perception.
