---
id: include-grids-cartesian
title: Include Grids in Cartesian Charts
bibliography: references.bib
description: Add gridlines to static charts with Cartesian coordinates to assist users
  in retrieving specific values.
labels:
- chart:bar
- chart:line
- chart:scatterplot
- visual:grid
- task:retrieve-value
- audience:novice
- complexity:basic
---

## The Rule <!-- role: advice -->
Include visible gridlines in visualizations that use a Cartesian coordinate system (such as bar charts, line charts, and scatterplots), especially when interaction is not available.

## The Logic <!-- role: reason -->
When users view static visualizations without interactive tooltips, they rely on visual reference points to estimate values.
*   **The Principle:** **Value Retrieval Support.** In the development of the VLAT, [@lee_vlat_2017] found that adding grids was necessary to help users accurately read values on axes when interactive techniques (like tooltips) were absent.
*   **The Evidence:** In Section 3.1.3, [@lee_vlat_2017] explicitly states, "We included grids in the visualizations that had a Cartesian coordinate system in order to help the potential test takers read values on axes."

## Where to Apply <!-- role: context -->
This applies to standard 2D charts where accurate data retrieval is a task.
*   **User Goal:** Reading specific numerical values from data points (Retrieve Value task).
*   **Data Type:** Quantitative data mapped to spatial axes (Cartesian coordinates).
*   **Audience:** General users, particularly when viewing static media (print, PDF, static images).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Interactive Dashboards.
*   **Reason:** If a user can hover over a data point to see the exact number (tooltips), heavy gridlines may be visual clutter that is no longer functionally necessary for value retrieval.
*   **Scenario:** High-level Trend Analysis.
*   **Reason:** If the goal is strictly to see a trend (e.g., "is it going up?") rather than reading specific numbers, gridlines might distract from the shape of the data.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual cleanliness. Gridlines add "ink" to the chart that isn't data.
*   **The Risk:** If gridlines are too dark or heavy, they can create visual noise or "chart junk" that interferes with seeing the data patterns.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on axis ticks.
*   **Why it fails:** Without a line extending across the plot area, the eye struggles to trace a data point back to the axis accurately, especially for points far from the axis.
*   **The Wrong Fix:** Using extremely dark/thick gridlines.
*   **Why it fails:** This draws attention away from the data bars or lines.

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you look at a bar on the far right of the chart and instantly estimate its value without using a ruler or your finger to trace back to the Y-axis?
*   **The Test:** Try to guess the value of a data point. If you feel eye strain or uncertainty about which tick mark it aligns with, you need gridlines.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Enable standard gridlines in your charting tool.
*   **Best Fix:** Add light gray, thin gridlines that are visible enough to guide the eye but subtle enough to sit in the background behind the data elements.
