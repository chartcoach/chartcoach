---
id: use-delta-charts-for-search
title: "Use delta charts to help users rapidly find specific relationships"
tags:
  - impact:perceptual
  - impact:performance
  - impact:cognitive
  - chart:bar
  - chart:dot-plot
  - task:filter
  - task:find-extremum
  - task:find-anomalies
  - data:quantitative
  - visual:length
  - visual:position
  - access:cognitive-load-risk
sources:
  - type: research
    ref: Nothelfer & Franconeri, 2020
    url: https://doi.org/10.1109/TVCG.2019.2934801
    note: "Experiment 1 found that using delta charts accelerated search for a specific relationship by 49-95% compared to charts showing individual values."
examples:
  - type: bad
    description: "A grouped bar chart with 20 categories shows 'before' and 'after' data. A user asked to find the one category where the value decreased must perform a slow, serial scan of all 20 pairs, comparing two bars at each step."
  - type: good
    description: "A delta chart shows the same 20 categories. The one category with a decrease is immediately visible as the only bar extending below the zero-baseline, making it a simple visual outlier."
---

## Guidance

When a user needs to search for a specific target relationship among many distractors (e.g., find the one item that went down, or the item with the biggest jump), use a delta chart.

## Why

Searching for a relational target (e.g., "small bar next to a tall bar") is a "staggeringly inefficient" visual task that gets slower with every additional data pair you add. Encoding the deltas directly transforms this difficult relational search into a simple feature search (e.g., "find the longest bar" or "find the only negative bar"), which the human visual system can perform much more rapidly, often as a pre-attentive "pop-out" effect. Research shows this can dramatically speed up performance.

## When it applies

- The task is to find an anomaly, outlier, or a specific target defined by its relationship (e.g., "Find the only region that missed its sales target").
- The visualization contains a moderate to high number of data pairs (e.g., >10) that need to be scanned.
- The speed of finding the target is important.

## Exceptions

- When the search criteria depend on the absolute values, not just the relationship (e.g., "Find the region that missed its target *and* had sales below $1M"). In this case, the delta chart alone is insufficient.
- When there are very few data pairs to scan (e.g., <5), the performance benefit will be less pronounced.

## Trade-offs

- This approach heavily optimizes for search speed at the cost of hiding the original values' context, which might be needed for subsequent analysis of the found target.

## Signs of Trouble

- **Painfully Slow Search:** Users complain that it "takes forever" to find the one item they are looking for.
- **"Where's Waldo?" Effect:** A simple search task feels like a difficult visual puzzle that requires careful, item-by-item inspection.
- **Performance Degrades with Data:** The chart becomes functionally unusable as more data points are added because the time required to find anything increases linearly.

## How to Improve

- **Quick Fix: Highlight the Target.** If you cannot change the chart type and the target is known in advance, use a distinct color, size, or annotation to make the target "pop out" from the distractors.

- **Comprehensive Approach: Switch to a Delta Chart.** Create a chart where each item's value is its calculated difference. This makes the search target a simple visual outlier (e.g., the longest bar, the only red dot), enabling rapid identification through pre-attentive processing.
