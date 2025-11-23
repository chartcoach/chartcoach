---
id: avoid-stacking-negative-values
title: Avoid Stacked Graphs for Non-Summable Data
bibliography: references.bib
description: Do not use stacked area charts for negative numbers or data that cannot
  be meaningfully summed.
labels:
- chart:area
- chart:stacked
- data:numerical
- impact:validity
- visual:shape
---

## The Rule <!-- role: advice -->
Do not use stacked graphs (stream graphs) if your data includes negative numbers or represents values that should not be summed, such as temperatures.

## The Logic <!-- role: reason -->
Stacked graphs visually sum the data series. If the sum is meaningless, the visualization is misleading.
*   **The Principle:** Semantic Validity of Aggregation
*   **The Evidence:** Stacked graphs represent a visual summation. They do not support negative numbers effectively, and the resulting "top" silhouette is meaningless if the data types (like temperature) cannot be logically added together [@heer_tour_2010].

## Where to Apply <!-- role: context -->
*   **User Goal:** Visualizing aggregate patterns over time.
*   **Data Type:** Time-series data.
*   **Audience:** General analysis.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Analyzing market share or total workforce composition.
*   **Reason:** In these cases, the "sum" (Total Market, Total Unemployed) is a meaningful metric that the user wants to see [@heer_tour_2010].

## The Price <!-- role: costs -->
*   **The Sacrifice:** By avoiding stacking, you lose the "whole vs. part" visualization that clearly shows the total volume.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Stacking temperature readings from different sensors.
*   **Why it fails:** The total height of the graph (e.g., 300 degrees) implies a physical reality that doesn't exist.

## How to Check <!-- role: check -->
*   **The Test:** Ask, "Does the sum of Series A and Series B equal a real, meaningful thing?" If the answer is no (e.g., summing pH levels), do not stack.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Use "Small Multiples" to plot each series in its own chart within the same axes, or plot them as overlapping lines if legibility permits [@heer_tour_2010].
