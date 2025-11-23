---
id: avoid-tables-for-correlation
title: Use Scatterplots or Line Charts for Correlation
bibliography: references.bib
description: Tables perform poorly for identifying relationships between variables;
  use position-based encodings instead.
labels:
- chart:scatterplot
- chart:line-chart
- task:correlate
- visual:position
- impact:insight
- data:multivariate
---

## The Rule <!-- role: advice -->
To show the relationship (correlation) between two variables, use **Scatterplots** or **Line Charts**. Avoid Tables and Pie Charts for this task.

## The Logic <!-- role: reason -->
The ability to perceive a trend requires the brain to process the aggregate shape of data points.
*   **The Principle:** Pattern Recognition. Position encodings allow the eye to fit a "mental regression line" through the data.
*   **The Evidence:** Based on the rankings in Zeng and Battle [@zeng_review_2023], Line Charts (E-7..9) and Scatterplots (E-1..3) ranked highest for accuracy and time in correlation tasks. Tables (E-13..15) and Pie Charts (E-10..12) were ranked at the bottom [@saket_task-based_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Determining if $X$ increases as $Y$ increases (positive correlation) or identifying trends.
*   **Data Type:** Two quantitative variables.
*   **Audience:** Analysts looking for causal relationships or predictive trends.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data is not ordered or continuous (for Line Charts).
*   **Reason:** Line charts imply continuity. If the X-axis is nominal (e.g., Fruit types), a line chart implies a relationship between "Apples" and "Bananas" that doesn't exist. Use a Scatterplot instead.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Exact values are hard to read (see the "Retrieve Value" guideline).
*   **The Risk:** Overplotting in scatterplots can obscure the density of the correlation.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a Table and asking users to "compare columns."
*   **Why it fails:** Tables force serial processing (reading one by one), making it cognitively impossible to "see" a correlation coefficient of $r=0.7$ effectively [@saket_task-based_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Two columns of numbers side-by-side.
*   **The Test:** Can you tell if the relationship is positive, negative, or random in under 1 second?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add "Sparklines" or small bars inside the table cells.
*   **Best Fix:** Switch to a Scatterplot or, if time-series data, a Line Chart.
