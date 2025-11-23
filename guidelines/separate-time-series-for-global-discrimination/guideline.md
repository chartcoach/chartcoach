---
id: separate-time-series-for-global-discrimination
title: Juxtapose Time Series for Global Discrimination Tasks
bibliography: references.bib
description: Use small multiples or horizon graphs when users need to scan whole series
  to identify global properties.
labels:
- chart:small-multiples
- chart:horizon-graph
- task:aggregate
- task:filter
- visual:position
- data:temporal
- impact:clarity
---

## The Rule <!-- role: advice -->
Separate multiple time series into juxtaposed views (Small Multiples or Horizon Graphs) when the task involves comparing aggregate properties, discrimination, or identifying anomalies across the entire time range.

## The Logic <!-- role: reason -->
Split-space techniques eliminate occlusion and visual clutter, allowing the user to perceive the "gestalt" or shape of each series independently. This is essential for tasks requiring a dispersed visual span.
*   **The Principle:** Dispersed Visual Span optimization and Clutter Reduction.
*   **The Evidence:** Javed et al. [@javed_graphical_2010] found that split-space techniques (Small Multiples and Horizon Graphs) were significantly faster than shared-space techniques for "Discrimination" tasks (identifying series with the highest value across the whole time range). The review by Zeng et al. [@zeng_review_2023] ranks Designs E-3 (Small Multiples) and E-4 (Horizon Graphs) higher than shared graphs for aggregation and discrimination tasks.

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to scan many series to find ones that meet a criteria (e.g., "Which sensor had the most volatility overall?" or "Which region has the highest overall sales trend?").
*   **Data Type:** Multiple time series, especially when the count is high (N > 4) or the data is noisy.
*   **Audience:** Analysts looking for outliers or general patterns across a dataset.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Limited Vertical Screen Space.
*   **Reason:** Small multiples require dividing the available vertical pixels by the number of series ($S/N$). If $N$ is large, the charts become too flat to read. (Note: Horizon graphs help mitigate this).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision in local comparison.
*   **The Risk:** It becomes difficult to compare the exact Y-value of Series A at time $t$ versus Series B at time $t$ because they are spatially separated.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Plotting 20 lines on one chart to "save space."
*   **Why it fails:** The resulting "spaghetti chart" makes it impossible to distinguish individual series shapes for discrimination tasks.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are lines crossing so frequently that you lose track of a single color?
*   **The Test:** Ask "Which series has the highest peak overall?" If you have to untangle lines to answer, you need split-space.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Facet the data into rows (Small Multiples).
*   **Best Fix:** If vertical space is tight, use **Horizon Graphs** (Design E-4 in [@zeng_review_2023]), which increase data density by slicing and layering bands, maintaining the benefits of split-space without requiring as much height as standard small multiples.
