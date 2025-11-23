---
id: discrete-aggregation-alignment
title: Align Aggregation Bins with Task Intervals
bibliography: references.bib
description: Compute and visualize data in discrete blocks (e.g., months) if the user's
  task is based on those specific time units.
labels:
- chart:bar-chart
- chart:stock-chart
- task:compare
- data:temporal
- process:aggregation
---

## The Rule <!-- role: advice -->
If the user's task involves comparing discrete time intervals (e.g., "Which month was best?"), visualize the data using discrete aggregation blocks (e.g., monthly bars/boxes) rather than continuous smoothing (e.g., moving averages).

## The Logic <!-- role: reason -->
Matching the computational variable (granularity) to the task variable reduces the cognitive load of segmenting the data.
*   **The Principle:** Task-Design Alignment (Computational Variables).
*   **The Evidence:** Designs that discretely aggregated data per month (Composite Graphs, Box Plots) outperformed designs that used continuous moving averages (Modified Stock Charts) for monthly comparison tasks in [@albers_task-driven_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing performance across specific, named time periods (Months, Quarters, Years).
*   **Data Type:** Continuous time series data that has hierarchical calendar structures.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user is looking for trends that do not align with calendar boundaries (e.g., a 40-day cycle).
*   **Reason:** Discrete blocking artificially breaks patterns that cross the boundary lines (aliasing).

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose visibility of trends that happen *between* the bins or across the edges of the bins.
*   **The Risk:** The "Modifiable Areal Unit Problem" (MAUP)—changing the bin size or position might change the perceived result.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Overlaying a continuous 30-day moving average to help compare months.
*   **Why it fails:** The moving average blurs the boundaries between months, making it harder to isolate the value contribution of a specific named month.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the user question refer to "March" vs "April," but the visualization shows a smooth, unbroken line?
*   **The Test:** Can you clearly see where "March" begins and ends without reading the x-axis ticks closely?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add vertical dividers to segment the continuous line.
*   **Best Fix:** Aggregate the data into discrete steps (bars, boxes, or step-lines) that match the period of interest.
