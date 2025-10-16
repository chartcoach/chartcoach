---
id: avoid-tall-bar-marks-for-underestimation
title: "Avoid tall, skinny bar marks to prevent underestimation of values"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:ethical
  - chart:bar
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
  summary: "Ceja et al. (2021, n=25) found that bar marks with tall, skinny aspect ratios (e.g., 1:11.5) are systematically recalled as shorter than they are, leading to an underestimation of their value (mean bias: -13.86 pixels, p<0.001)."
sources:
  - type: research
    ref: Ceja et al., 2021
    url: https://doi.org/10.1109/TVCG.2020.3030422
    note: "Experiment 1 (n=25) found significant underestimation (p<0.001) for tall, thin bars when recalled from memory. The effect is caused by a memory bias toward a 'prototypical square'."
    role: primary
---

## Guidance

Avoid using bar marks that are very tall and thin, as they lead viewers to underestimate the values they represent.

## Why

Due to a memory bias towards a "prototypical square," viewers tend to remember tall, skinny bars as being shorter and wider than they actually are. This causes them to systematically underestimate the value encoded by the bar's height, especially when recalling it from memory.

### Core Principle

Incidental visual properties of a mark, like its aspect ratio, can create systematic biases in how the primary encoded value (like position or length) is perceived and recalled.

## When it applies

- When displaying data with a large range where some bars become very tall and thin compared to others.
- When viewers must compare these values to others from memory (e.g., across slides or different dashboards).

## Exceptions

- When using a logarithmic scale to handle a large range of values. The scale's compression is a more dominant factor, though the aspect ratio bias may still exist to a lesser degree.

## Trade-offs

- To make bars less skinny, you may need to use more horizontal space, which might not be available.

## Signs of Trouble

- **Skyscraper Bars:** Your chart has bars that are extremely tall and narrow, resembling skyscrapers.
- **Diminished Extremes:** The highest values in your chart seem less extreme than they should be, making them appear closer to smaller values.
- **Difficult Judgments:** It's hard to accurately gauge the height of the tallest bars without carefully tracing them to the axis.

## How to Improve

- **Quick approach: Add Direct Labels.** If bars must remain tall and skinny, add direct data labels. This allows viewers to read the exact number instead of relying on biased perceptual judgment.

- **Moderate approach: Switch to a Dot Plot.** A dot plot represents each value with a single point, using position alone. This completely eliminates the two-dimensional aspect ratio and its associated bias.

- **Comprehensive approach: Use Paneling or a Log Scale.** If the data has a very large range causing the extreme shapes, consider breaking the chart into panels (small multiples) with different scales or switching to a logarithmic scale. Acknowledge the change clearly to the viewer.
