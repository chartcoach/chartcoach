---
id: avoid-wide-bar-marks-for-overestimation
title: "Avoid wide bar marks to prevent overestimation of values"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:ethical
  - chart:bar
  - chart:mekko
  - chart:treemap
  - task:lookup
  - task:compare
  - task:rank
  - data:quantitative
  - visual:position
  - visual:size
  - medium:static
  - medium:screen
  - medium:print
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "Ceja et al. (2021, n=25) found that bar marks with wide aspect ratios (e.g., 11.5:1) are systematically recalled as taller than they are, leading to overestimation of their value (mean bias: +4.75 pixels, p<0.001)."
sources:
  - type: research
    ref: Ceja et al., 2021
    url: https://doi.org/10.1109/TVCG.2020.3030422
    note: "Experiment 1 (n=25) found significant overestimation (p<0.001) for wide bars when recalled from memory. This bias is attributed to a regression towards a 'prototypical square'."
    role: primary
---

## Guidance

Avoid using marks in bar charts, Mekko charts, or treemaps that are very wide relative to their height.

## Why

Viewers' memory for a bar's height is biased. They tend to remember the shape as being closer to a "prototypical square." For a wide bar, this means they recall it as being taller than it actually was, leading to an overestimation of the value it represents. This can mislead viewers, especially when they compare values from memory.

### Core Principle

Incidental visual properties of a mark, like its aspect ratio, can create systematic biases in how the primary encoded value (like position or length) is perceived and recalled.

## When it applies

- When viewers need to recall or compare values from memory, such as across charts presented sequentially, on different dashboards, or in a slide presentation.
- The bias is strongest when the value is not perceived and reported simultaneously.

## Exceptions

- If the exact value is not critical and a general sense of magnitude is sufficient.
- If severe space constraints force a wide, short layout. In this case, use other methods to mitigate the bias.

## Trade-offs

- Following this guideline might require more vertical space, which may not always be available.

## Signs of Trouble

- **Pancake Bars:** Your chart contains rectangular marks that are much wider than they are tall (e.g., a horizontal bar chart squeezed into a short vertical space).
- **Cross-Chart Confusion:** When you compare a value from a chart with wide bars to a value on another chart, the comparison feels "off" or inaccurate.

## How to Improve

- **Quick approach: Add Direct Labels.** Add direct data labels to the bars. This gives viewers the exact value, bypassing the need for biased perceptual recall.

- **Moderate approach: Adjust Chart Dimensions.** Increase the chart's height or decrease its width to make the aspect ratio of the bars closer to 1:1 (more square-like).

- **Comprehensive approach: Reconsider the Chart Type.** If you have many categories that result in wide, short bars, a dot plot may represent the values more accurately by using position alone, which removes the aspect ratio bias.
