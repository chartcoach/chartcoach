---
id: prefer-square-marks-for-recall-accuracy
title: "Prefer square-like aspect ratios for marks to improve value recall accuracy"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:ethical
  - chart:bar
  - chart:mekko
  - chart:treemap
  - task:lookup
  - task:compare
  - data:quantitative
  - visual:position
  - visual:size
  - medium:static
  - medium:interactive
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "Ceja et al. (2021) demonstrated that the aspect ratio of a bar mark biases its recalled height. Wide bars are overestimated and tall bars are underestimated, while square bars (1:1 aspect ratio) show no systematic bias (p=0.842). This suggests a memory bias towards a 'prototypical square'."
sources:
  - type: research
    ref: Ceja et al., 2021
    url: https://doi.org/10.1109/TVCG.2020.3030422
    note: "Primary study across 3 experiments (n=25, n=15, n=21) identifying and explaining aspect ratio bias in bar charts. The bias was shown to be rooted in memory (Exp. 3)."
    role: primary
---

## Guidance

When designing visualizations with rectangular marks like bar charts, aim for the marks to have an aspect ratio as close to 1:1 (a square) as possible to ensure accurate recall.

## Why

Human memory for a shape is biased towards a more "prototypical" version. For rectangles, this prototype is a square. Consequently, viewers subconsciously "correct" the shape of wide or tall bars in their memory, causing them to recall wide bars as taller (overestimation) and tall bars as shorter (underestimation). Square-like bars are already close to the prototype and are therefore recalled more accurately.

### Core Principle

Incidental visual properties of a mark, like its aspect ratio, can create systematic biases in how the primary encoded value (like position or length) is perceived and recalled.

## When it applies

- When viewers need to compare values that are not shown simultaneously (e.g., in an animated sequence, across different dashboards, or in small multiples).
- When the visualization will be studied and its values recalled from memory later.
- For any chart type that uses rectangular marks where aspect ratio is an incidental property (bar charts, Mekko charts, some treemaps).

## Exceptions

- When the aspect ratio itself is used to encode a data variable (e.g., in certain treemap or Mekko chart designs). In these cases, be aware of the potential for bias and consider adding redundant cues like direct labels.
- When severe space constraints make square-like ratios impossible.

## Trade-offs

- **Inefficient Space:** Optimizing for square-like marks might lead to inefficient use of space, such as leaving a lot of whitespace in a tall, narrow container.
- **Inconsistent Width:** It may conflict with the common practice of maintaining a consistent bar width across all charts in a dashboard.

## Signs of Trouble

- **Extreme Shapes:** Your chart is filled with either very wide "pancake" bars or very tall, skinny "skyscraper" bars.
- **Cross-Chart Confusion:** When comparing two separate bar charts with different mark aspect ratios, the relative sizes seem "off" or counter-intuitive.
- **Memory Errors:** If you look at a chart, look away, and then try to estimate a value, you find yourself consistently over- or underestimating it.

## How to Improve

- **Quick approach: Add Direct Labels.** If you cannot change the aspect ratios, add direct labels with the exact values to each rectangular mark. This provides a "cognitive offload," allowing users to read the value instead of relying on biased perception.

- **Moderate approach: Adjust Chart Dimensions.** Modify the overall width and height of your chart's plot area to make the average mark aspect ratio closer to 1:1. This provides a good balance between accuracy and practicality.

- **Comprehensive approach: Change the Mark Type.** For bar charts with extreme aspect ratios, switch to a dot plot. A dot uses only position to encode the value, which completely eliminates the two-dimensional aspect ratio and its associated bias.
