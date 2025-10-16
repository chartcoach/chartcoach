---
id: watch-for-aspect-ratio-bias
title: "Watch for aspect ratio bias in rectangular marks"

impact:
  - perceptual
  - cognitive
  - ethical
  - logos

tags:
  - bar-chart
  - treemap
  - mekko-chart
  - aspect-ratio
  - position
  - length
  - memory-bias
  - comparison

sources:
  - type: research
    ref: Ceja et al., 2021
    url: https://doi.org/10.1109/TVCG.2020.3030422
    note: "Primary study identifying that the aspect ratio of bars biases their recalled position. Wide bars are overestimated, tall bars are underestimated."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "This survey collated the findings from Ceja et al. to inform automated visualization recommendation systems."

examples:
  - type: bad
    description: "A bar chart with very wide, short bars. A viewer recalling the bar heights from memory is likely to remember them as taller than they actually are."
  - type: bad
    description: "A bar chart with very tall, thin bars. Viewers are likely to underestimate the bar heights when recalling them from memory."
  - type: good
    description: "A bar chart where the bars have a 'squarish' aspect ratio. This shape is less prone to memory bias, leading to more accurate recall of the data values."
---

## Guidance

The aspect ratio of rectangular marks, such as bars in a bar chart, can systematically bias how a viewer remembers their size. Wide bars are recalled as larger than they are, and tall bars are recalled as smaller.

## Why

Humans have a cognitive bias that pulls their memory of a shape towards a "prototypical" square. When a viewer recalls the height of a bar from memory, a wide bar is remembered as being taller (closer to a square), and a tall bar is remembered as being shorter (also closer to a square). This distorts the recalled data value, leading to inaccurate comparisons and judgments.

## When it applies

- When using charts with rectangular marks, including bar charts, stacked bar charts, Mekko charts, or treemaps.
- Especially when users must compare values from memory, such as across different charts on a dashboard, within a small-multiples display, or between sequentially viewed states (e.g., an animation or slideshow).

## Exceptions

- When the primary task does not rely on memory. If a user is only looking up a single value on a chart that is fully and simultaneously visible, this memory bias is less of a concern.
- When chart design constraints (e.g., a very large number of categories, limited screen space) make it impossible to control the aspect ratio. In these cases, be aware of the potential for misinterpretation and consider adding labels.

## Trade-offs

- Forcing rectangular marks to be square-like can lead to inefficient use of space, especially for charts with many categories or a wide range of values.
- Aesthetically, a chart full of "chunky" bars may not be as visually appealing as one with more conventional slender bars.

## Evaluate

- [ ] Chart contains rectangular marks (e.g., bars) with very wide (e.g., > 3:1) or very tall (e.g., > 1:3) aspect ratios.
- [ ] The design requires users to compare values between different charts or views, forcing them to rely on memory of the mark sizes.

## Repair

1.  If possible, adjust the chart's dimensions to make the average aspect ratio of the rectangular marks closer to 1:1 (i.e., more square-like).
2.  If aspect ratios cannot be changed, add direct labels to the marks. This allows users to read the exact numbers instead of judging the bar lengths from memory.
3.  For comparisons across charts, try to combine them into a single chart (e.g., a grouped bar chart) to allow for direct, simultaneous comparison instead of relying on memory.