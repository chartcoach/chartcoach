---
id: align-aggregation-granularity-with-task
title: "Align the chart's data aggregation with the discrete intervals relevant to the user's task"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:bar
  - chart:box-plot
  - chart:line
  - task:compare
  - task:summary-mean
  - data:quantitative
  - data:temporal
  - audience:general

sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "For a task comparing monthly averages, visualizations that computed and displayed statistics on a discrete, per-month basis (like composite graphs and box plots) significantly outperformed those using continuous aggregation (like a moving average on a stock chart)."

examples:
  - type: good
    description: A composite graph calculates and displays a distinct average bar for each month. This discrete aggregation aligns perfectly with the task of comparing months.
  - type: bad
    description: A line chart with a 30-day continuous moving average overlaid. While it shows a smoothed trend, the continuous nature makes it difficult to extract a single, representative value for 'June' to compare against 'July'.
---

## Guidance

When users need to compare summary statistics across discrete time intervals (e.g., months, quarters, weeks), ensure the visualization computes and displays those statistics for the same discrete intervals, rather than using a continuous aggregation like a moving average.

## Why

Aligning the computational structure of the visualization with the conceptual structure of the task reduces cognitive load. If a user is asked to "compare June and July," a chart that provides a single, clear visual mark for "June's average" and another for "July's average" directly supports this comparison. A continuous moving average, by contrast, blurs the boundaries between months and does not provide a single, canonical value for the interval, forcing the user to perform extra mental work and estimation. The study by Albers et al. confirms that this alignment matters: discrete aggregation led to higher accuracy for monthly comparison tasks.

## When it applies

- The user's tasks are structured around discrete, non-overlapping time units (e.g., "Which month was best?", "Compare Q1 to Q2").
- The goal is comparison between these specific intervals.

## Exceptions

- **Identifying Trends:** When the goal is to see a smoothed, high-level trend and de-emphasize seasonal or short-term volatility, a continuous moving average is a very effective tool.
- **Shifting Windows:** If the user's task involves analyzing rolling time windows (e.g., "the last 30 days") rather than fixed calendar units, a continuous moving average is more appropriate.

## Trade-offs

- **Trend vs. Interval:** Discrete aggregation is excellent for comparing intervals but can obscure the underlying continuous trend by creating sharp visual breaks at interval boundaries. Continuous aggregation is excellent for trends but poor for interval comparison.
- **Flexibility:** Hard-coding aggregation to a specific interval (e.g., months) makes the chart less useful for tasks at a different granularity (e.g., weeks or quarters). Interactive controls that allow the user to change the aggregation period can mitigate this.

## Signs of Trouble

- **Task Mismatch:** The chart shows a 7-day moving average, but the business meeting is focused on comparing performance quarter-over-quarter.
- **User Confusion:** Users are unsure how to interpret a moving average line to answer a question about a specific calendar month. "Where on the line is the value for just June?"

## How to Improve

- **Quick Fix: Add Markers.** If you must use a moving average, you could add points to the chart that mark the average value on the 15th of each month as a rough proxy, but this is not ideal.
- **Comprehensive Approach: Change Aggregation Method.** If the task is interval comparison, replace the continuous moving average with a discrete aggregation. For example, instead of a 30-day moving average line, calculate the average for each calendar month and display it as a bar chart, a series of box plots, or as points on a line chart.