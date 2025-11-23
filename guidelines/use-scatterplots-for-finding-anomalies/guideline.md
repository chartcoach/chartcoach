---
id: use-scatterplots-for-finding-anomalies
title: Use Scatterplots to Find Anomalies
bibliography: references.bib
description: Scatterplots outperform other charts in accuracy and user preference
  for identifying outliers and anomalies.
labels:
- chart:scatterplot
- task:find-anomalies
- visual:position
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Use **Scatterplots** when the primary task is to identify anomalies or outliers within the data.

## The Logic <!-- role: reason -->
According to the knowledge base curated by Zeng and Battle [@zeng_review_2023], specifically the experiments by Saket et al. [@saket_task-based_2019], Scatterplots are the superior choice for anomaly detection.
*   **The Principle:** The spatial position channel ($x, y$) allows items that do not fit the pattern to "pop out" pre-attentively.
*   **The Evidence:** Scatterplots (E-1, E-2, E-3) ranked #1 in accuracy and user preference for the "Find Anomalies" task. They significantly outperformed Tables and Pie Charts in effectiveness metrics [@saket_task-based_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Spotting values that deviate from the norm or relationship.
*   **Data Type:** Two quantitative variables (or one quantitative and one ordinal/nominal) where spatial positioning is possible.
*   **Audience:** Users analyzing relationships or quality control data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset is purely 1-dimensional and categorical.
*   **Reason:** A Bar Chart (E-4) was found to be faster (though less accurate) for some anomaly tasks in the study [@saket_task-based_2019], likely because scanning a single sorted dimension is cognitively low-load.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Scatterplots can suffer from overplotting if the dataset is massive.
*   **The Risk:** Users may perceive false clusters if the axis scales are manipulated (e.g., truncated axes).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a Pie Chart or Table.
*   **Why it fails:** The study explicitly ranks Pie Charts (E-10..12) and Tables (E-13..15) at the bottom for finding anomalies. In a table, the user must read every value; in a pie chart, comparing arc lengths for slight deviations is perceptually difficult [@saket_task-based_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you looking at a grid of numbers to find a mistake?
*   **The Test:** Blur the chart. Can you still see the lonely dot away from the group?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If using a table, use highlighting/color for values outside standard deviation.
*   **Best Fix:** Plot the two variables on Cartesian coordinates (Scatterplot).
