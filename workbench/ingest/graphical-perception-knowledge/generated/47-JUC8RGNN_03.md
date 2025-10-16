---
id: use-aggregated-views-for-average-comparison
title: "Use aggregated views for comparing averages across time periods"
tags:
  - impact:perceptual
  - impact:performance
  - impact:cognitive
  - task:summary-mean
  - task:compare
  - chart:line
  - chart:bar
  - chart:heatmap
  - data:temporal
  - audience:general
  - medium:screen
evidence:
  strength: medium
  summary: "Albers et al. (2014, n=64) found that for comparing monthly averages, designs that explicitly aggregated data by month were most effective. A composite graph (line+bar) achieved 86% accuracy and a woven colorfield achieved 78% accuracy, both significantly outperforming a standard line graph (48%) which showed continuous, un-aggregated data (p < .0001)."
sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "The study showed that both explicitly encoding the average (composite graph) and visually grouping data to encourage perceptual averaging (woven colorfield) were superior to showing raw, continuous data for average comparison tasks (p < .0001)."
    role: primary
---
## Guidance

When users need to compare the average value of a time series across discrete periods (e.g., month-to-month), use a visualization that either explicitly calculates and displays the average for each period or visually groups the data within those periods.

## Why

Mentally calculating the average of a fluctuating line over a specific range is a cognitively demanding and inaccurate task. Designs that offload this work by either pre-calculating the average (e.g., showing a bar for the monthly mean) or using visual techniques to facilitate perceptual averaging (e.g., grouping colors into a block) lead to much better user performance.

### Core Principle

Align the computational structure of the visualization with the structure of the user's task. If the task is to compare monthly aggregates, the visualization should be structured around monthly aggregates.

## When it applies

- The task is to compare summary statistics like the mean or average across different time periods (e.g., "Which month had the highest average sales?").
- You are visualizing a continuous time series but the comparisons of interest happen at a coarser, discrete level of granularity (e.g., daily data, monthly comparisons).

## Exceptions

- When the task requires seeing fine-grained, continuous trends or specific point values, and not summary statistics. A standard line graph is better for seeing the exact shape of the data over time.

## Trade-offs

- Aggregating the data loses detail about the intra-period trends. A composite graph (showing both the raw line and the aggregate bars) mitigates this but at the cost of higher visual complexity.
- A chart designed for monthly averages may be misleading if the user then tries to perform a weekly comparison.

## Signs of Trouble

- **Inaccurate Summaries:** When using a standard line chart, users are unable to correctly identify which month has the highest average value.
- **Focus on Peaks:** Users mistake the month with the highest single peak for the month with the highest average.
- **Cognitive Overload:** Users express frustration or report that comparing averages is "too hard" or requires too much mental effort.

## How to Improve

- **Quick Fix: Switch to a Bar Chart.** If only the average matters, discard the raw data and show a simple bar chart with one bar for each period's average. This is highly accurate for the specific task but loses all underlying detail.
- **Moderate Redesign: Use a Woven Colorfield.** If using a heatmap-style colorfield, "weave" the pixels within each period (i.e., randomly permute them). This breaks up local trends and creates a more uniform block of color, which the visual system can average more effectively.
- **Comprehensive Approach: Use a Composite Graph.** Overlay a bar chart of the periodic averages on top of the raw line chart. This provides the best of both worlds: the line shows the detailed trend, and the bars provide an accurate, explicit encoding for comparing averages.
