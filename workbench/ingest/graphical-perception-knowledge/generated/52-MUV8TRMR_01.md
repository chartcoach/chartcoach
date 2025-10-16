---
id: reduce-marks-if-ungrouped
title: "For visual search in ungrouped data, reduce the number of marks"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:scatter
  - task:lookup
  - data:cardinality.high
  - medium:interactive
  - access:cognitive-load-risk
evidence:
  strength: high
  summary: "Gramazio et al. (2014, n=31) demonstrated a strong linear relationship between the number of items and search time for randomly arranged visualizations (p<0.001), while grouped layouts showed almost no effect. This indicates that for ungrouped data, more marks directly translates to slower performance."
sources:
  - type: research
    ref: Gramazio, Schloss, & Laidlaw, 2014
    url: https://doi.org/10.1109/TVCG.2014.2346983
    note: "Primary study (n=15 in Exp. 1, n=16 in Exp. 2) found a robust effect of set size on reaction time in random layouts (p<0.001), where search time increased with the number of marks."
    role: primary
---
## Guidance

If marks cannot be spatially grouped and the user needs to find a target, reduce the number of visible marks to improve search speed.

## Why

Without perceptual grouping, finding a target requires a serial search—examining items one by one. The time this takes is directly proportional to the number of items. Reducing the item count is the most direct way to shorten this search time and decrease the user's cognitive load.

### Core Principle

The performance of a visual task is limited by human cognitive and perceptual capacities. Design choices should aim to minimize the cognitive work required to complete the task.

## When it applies

- When displaying a large number of items in a visualization that lacks strong perceptual grouping, such as a multi-class scatterplot where categories are intermingled.
- When the user's primary task is to quickly locate a specific target, not to analyze the entire distribution or find outliers.

## Exceptions

- When the goal is to see the full data distribution, identify individual outliers, or understand data density. In these cases, every data point is important and should not be removed or aggregated.
- When the visualization is static and cannot be filtered or aggregated.

## Trade-offs

- Reducing the number of marks, either through aggregation or filtering, results in a loss of data fidelity and detail. The user can no longer see the individual data points that were removed or combined.

## Signs of Trouble

- **Slow Search:** Users report that finding anything in the chart feels slow, laborious, or overwhelming.
- **Overwhelming Display:** The chart appears as a dense, undifferentiated 'hairball' or cloud of points, with no clear structure.
- **High Error Rate:** Users frequently fail to find the target or give up the search.

## How to Improve

- **Quick Fix: Apply Filters.** In an interactive context, provide filters that allow users to dynamically reduce the number of visible marks based on data attributes.
- **Moderate Approach: Use Aggregation.** For dense point clouds, aggregate clusters of points into a single, larger mark (e.g., using data binning or clustering algorithms).
- **Comprehensive Approach: Use Small Multiples.** Facet the data into multiple smaller charts, each showing a subset of the data (e.g., one chart per category). This reduces the number of items within any single view, making search manageable.