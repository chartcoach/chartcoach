---
id: minimize-marks-in-ungrouped-displays
title: "For ungrouped visualizations, minimize the number of marks to speed up visual search"
tags:
  - impact:perceptual
  - impact:performance
  - impact:cognitive
  - chart:scatter
  - data:cardinality.high
  - task:lookup
  - task:find-anomalies
  - visual:color
  - visual:position
  - audience:general
  - medium:static
  - medium:interactive
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "Gramazio et al. (2014, n=15 & n=15) found that for randomly arranged (ungrouped) marks, visual search time increased linearly with the number of marks (p < .001). In contrast, for spatially grouped marks, search time was largely unaffected by the number of marks."
sources:
  - type: research
    ref: Gramazio et al., 2014
    url: https://doi.org/10.1109/TVCG.2014.2346983
    note: "Demonstrated that search time increases with set size for random layouts but not for grouped layouts."
    role: primary
---

## Guidance

In visualizations where marks cannot be spatially grouped by category (like a standard scatterplot), be aware that every additional mark increases the time and effort required for visual search tasks. If search is a primary goal, consider reducing the number of marks shown.

## Why

Without spatial grouping, the visual system defaults to a serial search, examining items one by one or in small chunks until the target is found. This process is slow and scales poorly. The study demonstrated that for randomly arranged marks, search time robustly increased with the number of "distractor" items.

### Core Principle

The performance of serial visual search degrades linearly with the number of items. If you cannot enable preattentive "pop-out" through grouping, performance will suffer as data density increases.

## When it applies

- When displaying data in a scatterplot or another chart type where mark positions are fixed by data values and categories appear randomly distributed.
- When the number of data points (cardinality) is high.
- When a primary user task is to locate specific items based on their category (e.g., finding a purple dot in a sea of other colored dots).

## Exceptions

- When the primary goal is to show the overall distribution, density, or shape of the entire dataset, for which all points are necessary.
- In interactive systems where users can filter or query to reduce the number of visible marks dynamically.

## Trade-offs

- Reducing the number of marks (e.g., by sampling or aggregation) improves search performance but sacrifices data completeness and may hide important outliers or patterns in the overall distribution.

## Signs of Trouble

- **Scalability issues:** A visualization that is easy to search with 100 points becomes nearly unusable with 1,000 points.
- **User frustration:** Users complain that it "takes forever" to find what they are looking for.
- **Overplotting:** Marks are so numerous and dense that they obscure each other, making individual identification impossible.

## How to Improve

- **Quick Fix: Use Highlighting.** In an interactive context, provide a legend or control that allows users to highlight all marks of a single category, making them "pop out" from the others.
- **Moderate Approach: Implement Filtering.** Provide interactive filters so users can reduce the number of visible marks to only those relevant to their current task.
- **Comprehensive Approach: Use Data Aggregation.** If showing every single point isn't critical, consider aggregating the data. This could mean using larger binned marks (like a 2D histogram) or summarizing dense regions, which reduces the number of distinct items a user needs to scan.
