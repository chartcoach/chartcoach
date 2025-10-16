---
id: mark-range-for-range-tasks
title: "Explicitly encode min/max to facilitate range comparison"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:box-plot
  - chart:stock
  - chart:custom
  - task:determine-range
  - data:quantitative
  - data:temporal
  - visual:position
  - visual:length
  - medium:static
  - medium:screen
evidence:
  strength: medium
  summary: "An experiment found that charts explicitly encoding local extrema (modified stock charts, box plots) achieved 88-92% accuracy for comparing ranges across time periods. This significantly outperformed designs that do not explicitly encode range, like line charts (74%) and colorfields (38-65%)."
sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "Primary experiment demonstrating that explicitly encoding a task-relevant statistic (range) improves performance."
    role: primary
---

## Guidance

When viewers need to compare the range (i.e., the difference between the minimum and maximum) across different periods in a time series, use chart types that explicitly encode the local extrema for each period.

## Why

This design offloads the cognitive work from the viewer to the chart itself. Instead of requiring the viewer to perform two search tasks (find min, find max) per period followed by a mental subtraction and comparison, the chart directly presents the information needed. This makes the comparison task faster, easier, and more accurate.

### Core Principle

Reduce the user's cognitive load by pre-calculating and directly encoding the specific information required for their primary task.

## When it applies

- When the main analytical goal is to identify which time segment (e.g., month, week) has the largest or smallest spread between its highest and lowest values.
- When comparing volatility or value range across different categories or periods.

## Exceptions

- If the raw data contains important patterns (e.g., specific shapes, trends) that would be obscured by the aggregation of a box plot, a line chart with range annotations might be a better compromise.
- If the audience is unfamiliar with statistical charts like box plots, the abstraction might cause confusion.

## Trade-offs

- **Loss of Detail:** Explicitly encoding only the range (as in a box plot) hides the raw data distribution within that range. It makes the range comparison task easier at the expense of other potential insights about the data's shape.
- **Clutter:** Adding range indicators to a chart like a line graph can increase visual clutter if not designed carefully.

## Signs of Trouble

- **Slow Performance:** Viewers take a long time to answer questions about which period has the largest range.
- **Incorrect Heuristics:** Viewers confuse the period with the highest maximum value for the period with the largest actual range.

## How to Improve

- **Quick Fix:** On a standard line chart, add simple annotations like vertical lines or shaded regions to highlight the range in each period.
- **Moderate Approach:** Use a modified stock chart that overlays min/max markers or dedicated range bars onto a line chart, which shows both the raw data and the explicit range.
- **Comprehensive Approach:** If the range comparison is the primary task and the raw data is secondary, use a box plot for each period. This design is optimized for comparing ranges via the box-and-whisker length.
