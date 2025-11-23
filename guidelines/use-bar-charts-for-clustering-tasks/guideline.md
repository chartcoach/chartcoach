---
id: use-bar-charts-for-clustering-tasks
title: Use Bar Charts to Identify Clusters
bibliography: references.bib
description: Bar charts provide the best balance of accuracy and user preference for
  clustering tasks compared to scatterplots or tables.
labels:
- chart:bar-chart
- task:cluster
- visual:length
- impact:effectiveness
- data:categorical
- data:quantitative
---

## The Rule <!-- role: advice -->
When the user's task involves finding clusters (grouping similar data attribute values), use a **Bar Chart**. Avoid using tables or line charts for this specific task.

## The Logic <!-- role: reason -->
Experimental evidence collated by Zeng and Battle [@zeng_review_2023] and conducted by Saket et al. [@saket_task-based_2019] indicates that Bar Charts facilitate high accuracy for clustering tasks.
*   **The Principle:** Visual aggregation. The length encoding in bar charts allows users to visually group similar values more effectively than reading text (tables) or interpreting positions (scatterplots).
*   **The Evidence:** In the experimental rankings, Bar Charts (E-4, E-5, E-6) consistently ranked in the top tier for accuracy and were the most preferred visualization by users for clustering tasks [@saket_task-based_2019]. While Pie Charts were faster, users significantly preferred Bar Charts.

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying groups of similar values or counting how many distinct groups exist within a dataset.
*   **Data Type:** A combination of nominal/ordinal categories and quantitative values (small scale, e.g., 5-34 data points).
*   **Audience:** General users who prioritize readability and familiarity.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Speed is the absolute only priority, and user preference is irrelevant.
*   **Reason:** The data shows that **Pie Charts** (E-10, E-11, E-12) were actually faster than Bar Charts for clustering tasks in the specific experiments performed [@saket_task-based_2019], though less preferred by users.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may lose some vertical space compared to a compact table.
*   **The Risk:** If the dataset is extremely large (hundreds of bars), the "clustering" effect may correspond to screen resolution rather than data distribution, unlike a Scatterplot which handles density better.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a Table (E-13, E-14, E-15).
*   **Why it fails:** The experimental data shows Tables are significantly slower and less accurate for detecting clusters because users must cognitively process individual numbers rather than perceiving visual patterns [@saket_task-based_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the user forced to read row-by-row to find groups of similar numbers?
*   **The Test:** Ask, "Can I see which items group together in under 2 seconds without reading a single number?"

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add conditional formatting (color bars) to the table to simulate bar length.
*   **Best Fix:** Convert the visualization to a standard Bar Chart.
