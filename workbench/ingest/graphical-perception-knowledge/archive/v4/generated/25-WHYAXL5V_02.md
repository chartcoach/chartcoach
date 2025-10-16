---
id: use-size-for-finding-extremes
title: "Use size to help viewers find extreme values"

tags:
  - impact:perceptual
  - chart:bubble
  - chart:scatter
  - chart:map.glyphs
  - task:find-extremum
  - data:quantitative
  - visual:size
  - visual:area
  - audience:general
  - medium:static
  - medium:interactive

sources:
  - type: research
    ref: Chung et al., 2016
    url: https://doi.org/10.1111/cgf.12889
    note: "Found that in a min/max judgment task, 'size' was the most accurate non-numeric visual channel, outperforming value/saturation, texture, hue, and orientation."

tools:
  - type: learn
    name: "A Look at Bubble Charts"
    url: https://datavizcatalogue.com/methods/bubble_chart.html
    description: "An overview of bubble charts, which rely on size to encode a third dimension of data."

examples:
  - type: good
    description: "A scatterplot of countries showing life expectancy (y-axis) and GDP per capita (x-axis), where the size of each bubble represents the country's population. It is very easy to spot the most and least populous countries."
  - type: bad
    description: "In the same scatterplot, if population were encoded using color saturation (from light to dark), it would be much harder to definitively identify the country with the absolute highest or lowest population, especially among countries with similar color shades."
---

## Guidance

When the primary task is to identify minimum or maximum values and position is already used for other variables, encode the quantitative value of interest using the size of the visual marks (e.g., bubble charts, proportional symbol maps).

## Why

The human visual system is very effective at making relative size judgments. Empirical studies show that viewers are highly accurate at identifying the smallest or largest items in a sequence when they are encoded by size. For the specific task of finding extremes, size can be even more accurate than other effective channels like color value/saturation.

## When it applies

- In scatterplots or bubble charts, where you want to encode a third quantitative variable.
- In proportional symbol maps, where the size of a glyph on a map represents a value for that location.
- In any visualization where the primary goal for a particular variable is to make the highest and lowest values "pop."

## Exceptions

- **Large Value Range:** If the ratio between the maximum and minimum value is very large, the largest bubbles may occlude other data points, while the smallest bubbles may become too tiny to be visible or comparable.
- **Accurate Comparisons:** While great for finding extremes, size (specifically, area) is less accurate than position or length for making precise comparisons between non-extreme values. If the primary task is to judge the magnitude of difference (e.g., "is A 2x bigger than B?"), a bar chart is better.

## Trade-offs

- **Accuracy vs. Salience:** Using size makes extremes stand out, but it offers lower precision for comparing intermediate values compared to using position (as in a bar chart).
- **Occlusion:** Large marks can hide smaller marks, especially in dense plots. This can be mitigated with transparency or by putting smaller marks on top, but it remains a risk.

## Signs of Trouble

- **Dense Blob:** The chart is so crowded that large circles are hiding many other data points.
- **Invisible Minima:** The smallest marks on the chart are so small that they are difficult to see or are mistaken for noise.
- **Misleading Scales:** The area of the circle is not scaled correctly to the data value (radius should be scaled to the square root of the value), leading to perceptual distortion.

## How to Improve

- **Quick Fix: Adjust Opacity.** If large bubbles are hiding others, make them semi-transparent so that marks underneath can be seen.
- **Moderate Approach: Set a Sensible Size Range.** Adjust the mapping between data values and mark size. Ensure that the smallest marks are clearly visible and the largest marks do not excessively dominate the chart. You can cap the maximum size or set a minimum size.
- **Comprehensive Redesign: Re-evaluate the Task.** If precise comparisons across all values are more important than just finding extremes, consider changing the chart type. For example, instead of a bubble chart, you could use a standard scatterplot and represent the third variable in a different way (e.g., small multiples, or a separate bar chart).