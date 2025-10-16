---
id: group-similar-marks-for-search
title: "Group similar marks to speed up visual search"
tags:
  - impact:perceptual
  - impact:performance
  - impact:cognitive
  - chart:scatter
  - chart:heatmap
  - chart:treemap
  - task:lookup
  - task:find-anomalies
  - data:categorical
  - visual:color
  - visual:position
  - audience:general
  - medium:static
  - medium:interactive
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "Gramazio et al. (2014, n=15 & n=15) found in two experiments (grids and scatterplots) that spatially grouping marks by color significantly sped up visual search times compared to randomly arranged marks (p < .001). The benefit of grouping increased with the number of marks."
sources:
  - type: research
    ref: Gramazio et al., 2014
    url: https://doi.org/10.1109/TVCG.2014.2346983
    note: "Primary study demonstrating that grouping by color reduces search time for finding a target."
    role: primary
---

## Guidance

Group marks that share a categorical attribute (e.g., color) together spatially to accelerate visual search tasks.

## Why

Spatial grouping leverages the visual system's preattentive processing capabilities. When similar items are clustered, they form a single perceptual "object" or texture region. This allows viewers to search across a few large groups instead of many individual items, drastically reducing cognitive load and search time. The study found this "pop-out" effect makes search performance largely independent of the number of marks.

### Core Principle

Reduce the number of distinct items a viewer must scan by creating larger, perceptually grouped units.

## When it applies

- When a key task is to find a specific item or a small group of items (a visual search or lookup task).
- In visualizations where the spatial arrangement of marks is flexible, such as heatmaps, treemaps, or categorical bar charts that can be sorted by category.
- When using color to encode categories, and you want to make it easier for users to find all items of a particular color.

## Exceptions

- When the spatial position of marks is determined by other data variables and cannot be altered (e.g., standard scatterplots where X and Y position are fixed, or geographic maps).
- When the primary goal of the visualization is to show the distribution or randomness of categories.

## Trade-offs

- Grouping may create an unintended sense of order or a continuous gradient if not done carefully, which could be misleading for purely categorical data.
- Forcing a grouped layout might conflict with other organizational principles (e.g., alphabetic or numeric sorting).

## Signs of Trouble

- **"Where's Waldo?" effect:** Users have to hunt laboriously through a sea of differently colored marks to find a target.
- **Slow performance:** Tasks involving finding a single item take a long time, and the time increases significantly as more data is added.
- **High perceived effort:** Users report that the visualization feels "cluttered" or "messy" and is difficult to search through.

## How to Improve

- **Quick Fix: Re-sort the data.** In charts like bar charts or tables, sort the data by the categorical color variable to bring similar items together.
- **Moderate Redesign: Use Small Multiples.** If direct grouping isn't possible (like in a scatterplot), consider breaking the visualization into small multiples, one for each category. This creates strong spatial grouping.
- **Comprehensive Approach: Choose a chart type that supports grouping.** If the data allows, switch from a scatterplot to a heatmap or a sorted bar chart where spatial proximity can be controlled to reflect categorical similarity.
