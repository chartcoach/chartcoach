---
id: explicit-statistic-mapping
title: Explicitly Encode the Task-Relevant Statistic
bibliography: references.bib
description: Map the specific variable the user needs (e.g., average, range) directly
  to a visual channel rather than forcing mental calculation.
labels:
- chart:box-plot
- chart:composite
- task:summarize
- visual:mapping
- impact:accuracy
- data:timeseries
---

## The Rule <!-- role: advice -->
If you know the user needs to compare a specific summary statistic (such as the mean, range, or spread), explicitly compute and visualize that statistic rather than showing raw data and expecting the user to derive it visually.

## The Logic <!-- role: reason -->
Visualizations that offload computation from the brain to the display perform better. Explicit mapping variables allow the visualization to do the work.
*   **The Principle:** Cognitive Offloading / Mapping Variables.
*   **The Evidence:** In [@albers_task-driven_2014], "Composite Graphs" (which explicitly plotted monthly averages as bars) and "Box Plots" (which explicitly plotted ranges and means) significantly outperformed designs that required users to visually estimate these values from raw data.

## Where to Apply <!-- role: context -->
*   **User Goal:** Making judgments about aggregate properties (e.g., "Which month had the highest average?" or "Which month had the most variation?").
*   **Data Type:** High-density time series where raw points obscure the trend.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user's task is unknown or highly varied.
*   **Reason:** Explicitly encoding one statistic (e.g., the mean) might clutter the view or mislead the user if their actual goal is to find outliers or specific raw values.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Explicitly encoding statistics often requires aggregating or hiding the raw data (as in a box plot), which removes context about local features or distribution shape.
*   **The Risk:** The user might confuse the derived statistic (e.g., the mean line) for the raw data trace.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding a "benchmark" line (like a global average) when the user needs to compare *local* averages.
*   **Why it fails:** A global benchmark helps, but explicit local encoding (like monthly average bars) provides a direct comparison object for the specific task.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the user have to look at a cloud of points and mentally draw a line through the middle to answer the question?
*   **The Test:** If the question is "Which month has the highest average?", is the "average" visually represented as a distinct object (point, line, bar)?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Overlay a moving average or discrete average bars on top of the raw series.
*   **Best Fix:** Use a composite design (e.g., a Box Plot or Composite Graph) that prioritizes the summary statistic while keeping necessary context.
