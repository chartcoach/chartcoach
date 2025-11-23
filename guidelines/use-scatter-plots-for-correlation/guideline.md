---
id: use-scatter-plots-for-correlation
title: Use Scatter Plots to Depict Correlation Without Causation
bibliography: references.bib
description: Present correlation using scatter plots rather than bar charts to reduce
  unwarranted causal inferences.
labels:
- chart:scatter
- chart:bar
- task:correlation
- impact:accuracy
- audience:general
---

## The Rule <!-- role: advice -->
Visualize correlational data using scatter plots instead of bar charts or line graphs.

## The Logic <!-- role: reason -->
Visualizations that show individual data points (disaggregated data) reduce the tendency for viewers to mistakenly infer causality from simple correlation. Bar charts and line graphs often trigger stronger causal associations—such as the belief that "X causes Y"—whereas scatter plots are perceived as less causal. This is partly because scatter plots display variability and outliers, making the lack of a direct deterministic link more apparent.
*   **The Principle:** Illusion of Causality
*   **The Evidence:** [@xiong_illusion_2020]

## Where to Apply <!-- role: context -->
Use this guideline when presenting observational data where two variables are related but one does not necessarily cause the other.
*   **User Goal:** Communicating a relationship between variables while maintaining scientific accuracy regarding causality.
*   **Data Type:** Bivariate quantitative data (e.g., comparisons of GPA vs. breakfast frequency).
*   **Audience:** General audiences or decision-makers who might be prone to "knee-jerk" causal interpretations.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the data *is* causal.
*   **Reason:** If the data comes from a controlled experiment where X *did* cause Y, a bar chart or line graph may appropriately signal that causal relationship.
*   **Scenario:** When exact summary statistics are required.
*   **Reason:** Scatter plots are poor for reading precise average values compared to bar charts.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Summary readability. Viewers take longer to estimate averages or compare group means in a scatter plot than in a bar chart.
*   **The Risk:** Visual complexity. A dense scatter plot with thousands of points may look like "noise" to a lay audience compared to a clean trend line.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a line graph to show "trends" in correlational data.
*   **Why it fails:** Line graphs are often perceived as highly causal because the connecting lines imply a continuous, driving mechanism between data points [@xiong_illusion_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart use solid shapes (bars) or connecting lines to summarize data that is actually messy and observational?
*   **The Test:** Ask a viewer, "Does X cause Y according to this chart?" If they say "Yes" confidently for correlational data, the design is too aggressive.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Overlay individual data points on top of bars or lines (jittered dots).
*   **Best Fix:** Replace the aggregated chart with a scatter plot to show the raw distribution.
