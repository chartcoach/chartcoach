---
id: use-discrete-aggregation-for-averages
title: "Use discrete, task-aligned aggregation to compare average values"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:bar
  - chart:box-plot
  - chart:custom
  - task:summary-mean
  - data:quantitative
  - data:temporal
  - medium:static
  - medium:screen
evidence:
  strength: medium
  summary: "An experiment showed that charts using discrete monthly aggregation (e.g., composite bar/line, box plot, woven colorfield) achieved 68-86% accuracy in comparing monthly averages. In contrast, charts without this discrete aggregation (e.g., standard line graph, continuous colorfield) performed poorly, achieving only 48-60% accuracy."
sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "Primary experiment showing that aligning the visual aggregation unit with the task's conceptual unit (e.g., months) improves accuracy for summary tasks."
    role: primary
---

## Guidance

When the task is to compare average values over discrete time periods (e.g., monthly averages), use visualizations that compute and display the data in corresponding discrete visual chunks (e.g., one bar per month).

## Why

Displaying data in discrete units that match the task's units makes the comparison direct and intuitive. It prevents viewers from having to perform difficult and error-prone perceptual tasks, such as mentally segmenting a continuous line or visually averaging a continuous field of color.

### Core Principle

Align the visual structure of the chart with the conceptual structure of the analytical task.

## When it applies

- The primary task is to compare summary statistics like the mean or median across distinct, non-overlapping time periods (e.g., comparing sales by quarter).
- The analysis is focused on period-by-period comparisons, not on continuous trends.

## Exceptions

- If the task involves identifying trends that cross period boundaries, a continuous encoding (like a moving average on a line chart) may be more appropriate.
- If the period of aggregation is not known in advance or needs to be flexible, an interactive tool that allows the user to define the aggregation window is needed.

## Trade-offs

- Discretizing the data can obscure finer-grained trends within each period.
- This design can make it harder to see patterns that do not align neatly with the chosen period boundaries (e.g., a trend that starts mid-month).

## Signs of Trouble

- **Peak-Average Confusion:** When looking at a line chart, viewers confuse the month with the highest peak value for the month with the highest average value.
- **Inaccurate Estimation:** Viewers are unable to reliably determine which of two complex line segments has a higher average value.

## How to Improve

- **Quick Fix:** On an existing line chart, add horizontal lines that explicitly mark the average value for each period.
- **Moderate Approach:** Change the visualization to a bar chart where each bar's height represents the average value for one period.
- **Comprehensive Approach:** Use a composite chart that overlays bars for the discrete averages on top of a line chart of the raw data. This robustly supports the summary comparison task while also providing the context of the underlying data.
