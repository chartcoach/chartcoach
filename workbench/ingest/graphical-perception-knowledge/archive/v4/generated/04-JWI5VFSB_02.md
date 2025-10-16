---
id: avoid-varying-pie-radii
title: "Maintain a constant radius for all segments in a pie or donut chart"

tags:
  - impact:perceptual
  - impact:ethical
  - chart:pie
  - chart:donut
  - task:composition
  - task:compare

sources:
  - type: research
    ref: Skau & Kosara, 2016
    url: https://doi.org/10.1111/cgf.12888
    note: "The paper's recommendations state that since arc length and area are important, changing the radius interferes with people's ability to read the chart and should be avoided. This is a direct application of their findings."

examples:
  - type: bad
    description: This "spiky" pie chart, sometimes seen in infographics, varies the radius of each segment. This makes the blue segment appear much larger than the green segment, even if their underlying values are similar, because it has both a larger area and arc length.
---

## Guidance

Do not vary the radius of individual segments within a single pie or donut chart. All segments should extend from a common center to a common outer boundary.

## Why

Varying the radius of a segment simultaneously distorts its **area** and **arc length**, which are the two primary visual cues viewers use to judge value and make comparisons. A segment with a larger radius will be perceptually overestimated and appear more important than it is. This practice is inherently misleading and undermines the chart's integrity.

## When it applies

- When designing pie or donut charts, especially for infographics or presentations where there might be a temptation to use this stylistic effect for emphasis.

## Exceptions

- There are no exceptions where this practice is perceptually sound for representing part-to-whole data. If the goal is purely artistic and not data representation, this rule may not apply, but the result should not be presented as a data chart.

## Trade-offs

- You sacrifice a "dynamic" or "spiky" stylistic effect in favor of data accuracy and ethical representation. This is a trade-off that should always be made.

## Signs of Trouble

- **Spiky Segments:** A pie or donut chart where one or more slices extend further from the center than others.
- **Distorted Proportions:** When looking at the chart, it feels difficult to judge the relative size of the segments, and the emphasized (longer) segments seem to dominate the visual.

## How to Improve

- **Quick Fix:** If you need to emphasize one slice, use a more saturated or contrasting color for that slice. Alternatively, slightly "exploding" the slice (pulling it out from the center while maintaining its shape) is a less distorting way to draw attention, but should still be used with caution.

- **Comprehensive Redesign:** If emphasizing a specific value is the primary goal, a pie or donut chart is often not the best choice. Switch to a **bar chart**, where you can easily use color, an outline, or an annotation to highlight a specific bar without distorting the data representation for all other values.
