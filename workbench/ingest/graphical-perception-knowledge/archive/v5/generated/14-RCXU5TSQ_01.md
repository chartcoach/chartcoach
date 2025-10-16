---
id: select-chart-for-summary-vs-detail
title: "Select chart types based on whether the task is summary or detail-oriented"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:line
  - chart:heatmap
  - chart:colorfield
  - task:summary-mean
  - task:lookup
  - task:trend
  - data:temporal
  - data:quantitative
  - visual:color
  - visual:position
  - audience:general
  - medium:screen

evidence:
  strength: medium
  summary: "Research shows a trade-off between chart types for different analytical tasks. Line charts (using position) are superior for detail-oriented tasks like finding trends or peaks, while color-based charts are more effective for summary tasks like comparing regional averages."

sources:
  - type: research
    ref: Correll et al., 2012
    url: https://dl.acm.org/doi/10.1145/2207676.2208556
    note: "Demonstrates that colorfields (summary task) and line charts (detail task) have different strengths."
    role: primary
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: https://doi.org/10.2307/2288400
    note: "Foundational work establishing that position (used in line charts) is a highly accurate encoding for quantitative judgments, supporting its use for detail-oriented tasks."
    role: related

examples:
  - type: good
    description: "Using a line chart to show stock price trends over a year. The primary task is to see the overall direction, volatility, and specific high/low points."
  - type: good
    description: "Using a calendar heatmap (a type of colorfield) to show the average user activity for each day of the week over a year. The primary task is to compare which days are busiest on average."
  - type: bad
    description: "Using a line chart of minute-by-minute website traffic and asking a user to determine which hour of the day had the highest average traffic. This forces a difficult mental calculation."
---

## Guidance

When visualizing time-series data, explicitly choose the chart type based on the primary analytical task. Use line charts for detail-oriented tasks like identifying trends and finding peaks. Use color-based charts like heatmaps for summary-oriented tasks like comparing averages across segments.

## Why

Different visual encodings are optimized for different perceptual tasks. Position along a common scale (the foundation of a line chart) is excellent for making precise comparisons and judging slope or trend. Color (the foundation of a heatmap) is processed pre-attentively by the brain for summary statistics like 'average color,' making it more efficient for aggregation tasks.

### Core Principle

No single visualization is best for all tasks. The most effective design is one that aligns its visual encoding with the specific question the user is trying to answer.

## When it applies

- When deciding between a line chart and a heatmap/colorfield for visualizing time-series data.
- When designing a dashboard where an audience needs to perform both summary and detail-oriented tasks on the same dataset.
- During the initial design phase, to clarify the primary goal of the visualization.

## Exceptions

- When space is extremely limited, a single, well-designed line chart may be a necessary compromise to show both trend and allow for rough average estimation, even if it's not optimal for the latter.
- For very sparse time-series data, a line chart may be sufficient for both tasks as the mental calculation of averages is trivial.

## Trade-offs

- **Prioritizing summary over detail:** Choosing a heatmap makes it easy to compare averages but obscures the fine-grained shape, trend, and volatility within each segment.
- **Prioritizing detail over summary:** Choosing a line chart makes it easy to see trends and peaks but makes comparing segment averages less accurate and more cognitively demanding.

## Signs of Trouble

- **Task-Chart Mismatch:** Users are employing a line chart to perform slow, inaccurate mental calculations of segment averages.
- **Inefficient Analysis:** Users are looking at a heatmap and trying to discern the exact trend or shape of the data, which is not what it's designed for.
- **User Frustration:** Viewers express difficulty or lack of confidence when asked to perform a summary task with a detail-oriented chart (or vice versa).

## How to Improve

- **Quick approach:** Add annotations to compensate for the chart's weakness. On a line chart, add explicit labels showing the average for each segment. On a heatmap, consider adding small, simplified sparklines to give a hint of the trend.

- **Moderate approach:** Provide both views interactively. Use a button or toggle that allows the user to switch between a line chart view (for trends) and a heatmap view (for averages), empowering them to choose the right tool for their question.

- **Comprehensive approach:** Design a multi-view dashboard. Present both a line chart and a heatmap side-by-side, explicitly labeling each for its intended purpose (e.g., "Trend Over Time" vs. "Average by Month"). This guides the user to the correct view for their task.
