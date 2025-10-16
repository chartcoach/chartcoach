---
id: use-position-for-extrema-tasks
title: "Use position-based charts for finding maximum or minimum values"
tags:
  - impact:perceptual
  - impact:performance
  - chart:line
  - chart:bar
  - task:find-extremum
  - task:rank
  - data:temporal
  - visual:position
  - visual:color
  - audience:general
  - medium:screen
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "Albers et al. (2014, n=64 per task) found that position-based charts like composite graphs (93% accuracy), modified stock charts (89%), and line graphs (88%) were significantly more accurate for finding maximum values in a time series than color-based charts like colorfields (59%) (p < .0001)."
sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "Experimentally compared 8 time-series visualizations across 6 aggregate tasks. Found position encodings consistently outperformed color for point comparison tasks like finding maxima/minima (p < .0001)."
    role: primary
---
## Guidance

For tasks requiring users to find the maximum or minimum value in a time series, prefer visualizations that encode data using position (e.g., line charts, composite bar-and-line charts) over those that use color (e.g., heatmaps, colorfields).

## Why

Position along a common scale is a more perceptually precise visual channel than color saturation or hue. Humans can more accurately judge and compare the specific values of points when they are encoded by their vertical or horizontal position, which is critical for reliably identifying the single highest or lowest value in a dataset.

### Core Principle

Match the visual channel to the task's required precision. High-precision tasks, like identifying a single extreme value, demand high-precision encodings like position.

## When it applies

- When a primary user task is to identify the highest or lowest data point in a series or within specific periods of a series.
- When comparing the performance of different charts for quantitative comparison tasks.

## Exceptions

- If the goal is simply to get a rough "gist" of the data and precision is not important, a color-based chart might be sufficient, though it will be less accurate.

## Trade-offs

- Position-based charts like line graphs can become cluttered with multiple series, whereas color-based charts can sometimes scale to show more data, albeit with lower precision.
- Simple line charts are less effective for summary tasks (like judging averages) compared to some color-based designs.

## Signs of Trouble

- **Inaccurate Readings:** Users consistently fail to identify the true maximum or minimum value when viewing a color-encoded chart like a heatmap.
- **Confounding Brightness with Value:** Users mistake the most saturated or brightest color for the highest value, even if the legend indicates otherwise.
- **Slow Performance:** Users take a long time to scan the entire chart, mentally converting colors back to values, to find the extremum.

## How to Improve

- **Quick Fix: Add Explicit Labels.** If you must use a color-based chart, add labels for the maximum and minimum values to provide a direct lookup. This is a workaround that doesn't fix the perceptual issue but mitigates the inaccuracy.
- **Moderate Redesign: Switch to a Line Chart.** Replace the colorfield or heatmap with a standard line chart. This immediately leverages position for encoding, which is more accurate for this task.
- **Comprehensive Approach: Use a Composite or Stock Chart.** Augment a line chart by overlaying bars for period averages (Composite Graph) or adding explicit marks for period-based extrema (Modified Stock Chart). This not only uses position but also adds visual cues that make finding extrema within specific periods even easier.
