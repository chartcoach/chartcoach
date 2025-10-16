---
id: use-explicit-encoding-for-outliers
title: "Explicitly highlight outliers to improve their detection"
tags:
  - impact:perceptual
  - impact:performance
  - impact:cognitive
  - task:find-anomalies
  - chart:line
  - chart:heatmap
  - data:temporal
  - visual:color
  - visual:shape
  - audience:general
  - medium:screen
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "Albers et al. (2014, n=48) found that an 'Event Striping' chart, which explicitly visualizes outliers as distinct stripes on a colorfield, achieved 67% accuracy for outlier detection. This was more than double the performance of standard line graphs (37%) or colorfields (31%) (p < .0001)."
sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "The study's 'Event Striping' design was created specifically for outlier detection and dramatically outperformed all other general-purpose chart types for that task, demonstrating the power of task-specific encoding (p < .0001)."
    role: primary
---
## Guidance

To help users find outliers in a time series, use a visualization that computationally identifies and explicitly highlights those unusual data points with salient visual marks.

## Why

Standard visualizations require users to perform two difficult mental steps: first, build a mental model of the data's overall distribution and typical values, and second, scan for points that deviate from that model. This is cognitively demanding and error-prone. A chart that pre-calculates and visually separates outliers offloads this work to the computer, making detection faster and more accurate.

### Core Principle

Make the most important information the easiest to see. If finding outliers is the primary task, the design should make them perceptually "pop."

## When it applies

- When the main goal for the user is to identify anomalous data points, "freak events," or values that don't fit the general pattern.
- When designing specialized dashboards for monitoring or anomaly detection.

## Exceptions

- If the definition of an "outlier" is subjective and you want the user to define it themselves through exploration, showing raw data may be preferable.
- If all data points are of equal importance and there is no specific anomaly-detection task.

## Trade-offs

- Designing for a specific task like outlier detection makes the chart less effective for other tasks. The "Event Striping" chart, while excellent for finding outliers, performed poorly for all other tested tasks (e.g., finding average, range, or spread).
- The definition of an "outlier" must be determined beforehand (e.g., >2 standard deviations from the mean), which may not be appropriate for all datasets.

## Signs of Trouble

- **Missed Anomalies:** Users frequently overlook significant, unusual data spikes or troughs in a standard line chart or heatmap.
- **Noise vs. Signal Confusion:** Users cannot distinguish between high-frequency noise and genuine, meaningful outliers.
- **Slow Discovery:** It takes users a long time to manually scan the entire dataset to find just a few unusual points.

## How to Improve

- **Quick Fix: Add Reference Lines.** On a standard line chart, add lines for the mean and +/- 2 standard deviations. This gives users a visual guide to identify points that fall outside the typical range.
- **Moderate Redesign: Use a Different Symbol.** On a scatter or line chart, use a different color or shape to mark points that are algorithmically identified as outliers.
- **Comprehensive Approach: Design a Task-Specific Chart.** Implement a design like "Event Striping," where the background shows a smoothed representation of the data (e.g., a colorfield) and outliers are drawn on top as visually distinct, high-contrast marks.
