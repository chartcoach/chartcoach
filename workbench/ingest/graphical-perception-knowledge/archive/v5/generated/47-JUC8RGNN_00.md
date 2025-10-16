---
id: use-position-for-extremes
title: "Use position-based charts to find extreme values in time series"
tags:
  - impact:perceptual
  - impact:performance
  - chart:line
  - chart:bar
  - chart:scatter
  - task:find-extremum
  - data:quantitative
  - data:temporal
  - visual:position
  - visual:color
  - medium:static
  - medium:screen
evidence:
  strength: medium
  summary: "An experiment with 8 chart types and over 300 participants found that position-based charts (e.g., line, composite, stock) achieved 87-96% accuracy for finding min/max values in time series, while color-based charts (e.g., colorfields) only achieved 43-69% accuracy."
sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "Primary experiment comparing 8 time series visualization techniques across 6 aggregate comparison tasks."
    role: primary
---

## Guidance

For tasks that require identifying the maximum or minimum value in a time series, prefer chart types that encode values using position (e.g., line charts, composite charts) over those that use color (e.g., colorfields/heatmaps).

## Why

Position along a common scale is a more perceptually accurate visual channel for extracting precise quantitative values compared to color saturation or hue. This allows viewers to make more reliable judgments about which single point is the absolute highest or lowest in the dataset.

### Core Principle

Humans judge quantities more accurately by comparing positions along a common scale than by comparing less precise visual channels like color or area.

## When it applies

- When the primary task for the viewer is to locate the single highest or lowest data point within a dataset, especially in a dense time series.
- When accuracy in identifying the absolute extremum is critical.

## Exceptions

- If the task is to get a rough "gist" of high or low regions rather than finding the single most extreme point, color can be an effective and space-efficient encoding.
- If the primary goal is to spot outliers, a specialized design like event striping may be more effective.

## Trade-offs

- **Space:** Position-based charts like line graphs typically require more vertical space than a compact colorfield/heatmap.
- **Task Suitability:** While better for finding extreme values, simple line charts can be less effective for summary tasks like judging the average or spread of data over a period.

## Signs of Trouble

- **Inaccurate Judgments:** Viewers struggle to correctly identify the single highest or lowest value when using a color-based chart.
- **Regional Confusion:** Viewers misinterpret a dark region on a heatmap as containing the absolute maximum, when it may just be a cluster of high-but-not-maximal values.
- **Slow Performance:** Viewers have to slowly scan the entire chart and hover over many points to find the extremum.

## How to Improve

- **Quick Fix:** If you must use a color-based chart, add interactive tooltips that show the exact value on hover, providing an escape hatch for accurate lookups.
- **Moderate Approach:** Convert the visualization from a colorfield/heatmap into a standard line chart. This immediately leverages the perceptual accuracy of position.
- **Comprehensive Approach:** Use a modified stock chart or composite chart that not only uses position but also adds explicit visual markers (e.g., dedicated points, whiskers) to make the local and global extrema visually salient.
