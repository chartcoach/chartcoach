---
id: prioritize-totals-in-area-charts
title: Use Area Charts When Totals Matter
bibliography: references.bib
description: Use area charts only when the cumulative total is as significant as individual
  shares.
labels:
- chart:area
- chart:line
- task:compare
- visual:magnitude
- impact:clarity
---

## The Rule <!-- role: advice -->
Use area charts only if the total size of the stacked categories (the height of the stack) is as important to the reader as the individual shares. If the total is irrelevant, use a line chart instead.

## The Logic <!-- role: reason -->
Area charts emphasize the volume of data and how the cumulative sum evolves over time.
*   **The Principle:** Visual Weight. The filled area draws attention to the magnitude of the whole pile, not just individual trends.
*   **The Evidence:** According to [@muth_area_charts_2018], many readers find line charts easier to understand than area charts. Therefore, the area chart is justified only when the "total" conveys essential meaning (e.g., total market size alongside market share).

## Where to Apply <!-- role: context -->
*   **User Goal:** Showing how a cumulative metric (like total revenue) and its components (revenue sources) develop simultaneously.
*   **Data Type:** Stacked quantitative data over time.
*   **Audience:** General audiences needing to see the "big picture" volume.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Comparing specific changes between categories.
*   **Reason:** If the goal is to see if one share overtook another or to compare precise trends, a line chart is superior because it does not rely on stacking [@muth_area_charts_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Readability of individual trends.
*   **The Risk:** Readers may struggle to interpret the inner layers of the chart because they lack a common straight baseline.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using an area chart for a single metric over time.
*   **Why it fails:** If there is only one value, a line chart is clearer, and a column chart is better for few dates. Area charts force the y-axis to zero, which may obscure trends in single-series data [@muth_area_charts_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** A filled chart where the top edge (the total) is flat or meaningless.
*   **The Test:** Ask, "Does the reader need to know the sum of these parts?" If no, change the chart type.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Convert the chart to a line chart.
*   **Best Fix:** Use a line chart to emphasize trends or a stacked bar chart if comparing categorical splits is more important than the time series.
