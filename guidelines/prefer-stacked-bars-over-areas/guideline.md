---
id: prefer-stacked-bars-over-areas
title: Choose Stacked Bar Charts Over Stacked Area or Line Charts
bibliography: references.bib
description: Among stacked visualization types, stacked bar charts provide better
  correlation perception than areas or lines.
labels:
- chart:stacked-bar
- chart:stacked-area
- task:correlation
- visual:shape
- impact:clarity
---

## The Rule <!-- role: advice -->
When using stacked visualizations to show correlation, use stacked bar charts rather than stacked area or stacked line charts.

## The Logic <!-- role: reason -->
Despite having similar visual forms, the specific visual features (such as "spikiness" vs. distinct bars) impact perception. Stacked bars yield lower perceptual error rates.
*   **The Principle:** **Visual Feature Discrepancy.** Participants assessing stacked area/line charts were distracted by "spikes" and "valleys," whereas stacked bar charts provided features (amount of white space vs. color) that were easier to process for correlation judgments [@harrison_ranking_2014].
*   **The Evidence:** Statistical analysis showed that stacked bar charts significantly outperformed both stacked area and stacked line charts for identifying correlations, particularly in negative data scenarios [@harrison_ranking_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing trends or relationships between parts of a whole over a domain (e.g., time).
*   **Data Type:** Time-series or categorical data suitable for stacking.
*   **Audience:** General audiences interpreting part-to-whole relationships.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset is extremely dense (hundreds of time points).
*   **Reason:** Individual bars may become too thin to resolve, potentially necessitating a continuous area (though this may still suffer from the "spikiness" perceptual penalty).

## The Price <!-- role: costs -->
*   **The Sacrifice:** The "flow" or continuity implied by area/line charts.
*   **The Risk:** Stacked bars may look cluttered if the X-axis has high cardinality.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Smoothing a stacked line chart to remove spikes.
*   **Why it fails:** This alters the data truthfulness. The better approach is changing the mark type to bars.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using a "filled line" or "area" chart to show how two variables interact?
*   **The Test:** Convert the mark type to "Bar." Does the relationship become clearer?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the chart type from "Stacked Area" to "Stacked Bar" in your visualization tool.
*   **Best Fix:** If correlation is the primary message, switch to a scatterplot. If part-to-whole is required, stick to the stacked bar.
