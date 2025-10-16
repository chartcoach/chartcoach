---
id: prefer-continuous-charts-for-global-tasks
title: "Use a Single, Continuous Chart for Global Tasks like Finding the Maximum"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:bar.small-multiples
  - chart:line.small-multiples
  - chart:small-multiples
  - data:temporal
  - data:periodicity
  - task:rank
  - task:find-extremum
  - audience:general
  - access:cognitive-load-risk

evidence:
  strength: medium
  summary: "Waldner et al. (2020, n=92) found that a single, continuous 24-hour chart enabled users to find the maximum value significantly faster than two separate 12-hour charts (3.8s vs 4.6s, p=0.019). The separated charts were also more error-prone, with users often selecting the maximum from only one of the two charts."

sources:
  - type: research
    ref: Waldner et al., 2020
    doi: 10.1109/TVCG.2019.2934784
    note: "Primary experiment showing a significant main effect for cardinality on time to locate the maximum (F(1,79)=5.721, p=0.019, η²p=0.068). Qualitative error analysis showed users of 12-hour charts mistakenly selected a local maximum from the wrong sub-chart."
    role: primary

examples:
  - type: good
    description: A single, continuous 24-hour bar chart makes it easy to spot the overall highest value across the entire day (around 5 PM).
    url: https://i.imgur.com/8QjU3oE.png
    caption: A single 24-hour linear bar chart.
  - type: bad
    description: Two separate 12-hour bar charts break the data at noon. A viewer might mistakenly think the highest value is the peak in the AM chart (around 8 AM) and miss the true global maximum in the PM chart.
    url: https://i.imgur.com/K3Zp5uC.png
    caption: Two juxtaposed 12-hour linear bar charts.
---

## Guidance

For tasks that require a global understanding of a dataset, such as finding the overall maximum or minimum value, use a single, continuous chart rather than breaking it into multiple smaller, separate charts (small multiples).

## Why

Separating a continuous dataset (like a 24-hour time-series) into multiple charts forces the viewer to perform an extra cognitive step: first, find the maximum in each chart, and second, compare those maxima to find the true global one. This increases cognitive load and is highly error-prone, as viewers often neglect to complete the second step and incorrectly report a local maximum as the global one. A single, continuous chart makes the global maximum perceptually salient and unambiguous.

### Core Principle

Reduce cognitive work by making the most important comparisons the easiest to see. A task that is global in nature (e.g., "find the highest value overall") should be supported by a visualization that is global in scope.

## When it applies

- When visualizing a continuous variable, like time, that has been broken into segments.
- When a key user task is to identify global extrema (highest or lowest values) or to understand the overall range of the data.
- When using small multiples to represent parts of a whole series (e.g., AM/PM, Q1/Q2/Q3/Q4).

## Exceptions

- When the primary task is to compare the segments themselves (e.g., "Compare the overall pattern of AM vs. PM") and finding the global maximum is not a priority.
- When horizontal or vertical space is severely limited, and breaking the chart is the only way to make it fit. Acknowledge that this compromises global tasks.
- When the break point is a natural and meaningful discontinuity in the data, rather than an arbitrary split.

## Trade-offs

- **Space vs. Accuracy:** A single, continuous chart (e.g., a long horizontal bar chart) may have an awkward aspect ratio and take up more space than a more compact grid of smaller charts. This trade-off prioritizes accuracy for global tasks over space efficiency.

## Signs of Trouble

- **Local Maxima Errors:** Users report the highest value, but it's only the maximum for one of the sub-charts, not the overall dataset.
- **Slow Comparisons:** Users take a long time to answer questions about the overall range or trend because they have to scan back and forth between multiple charts.
- **Incomplete Analysis:** User insights focus heavily on patterns within one sub-chart, ignoring the broader context provided by the others.

## How to Improve

- **Comprehensive Redesign: Combine into a Single Chart.** The most effective solution is to merge the separate charts into a single, continuous visualization. For example, combine two 12-hour bar charts into one 24-hour bar chart.

- **Moderate Improvement: Add Visual Guides.** If you must keep the charts separate, add annotations or visual guides that highlight the global maximum. For example, draw a dashed line across all charts indicating the level of the global maximum, and use an arrow to point to it. This adds clutter but mitigates the primary error.

- **Quick Fix: Add a Summary Note.** Include a text annotation that explicitly states the global maximum and when it occurs (e.g., "The daily peak of 45 accidents occurred at 5 PM"). This doesn't fix the visual representation but provides a crucial escape hatch for viewers.