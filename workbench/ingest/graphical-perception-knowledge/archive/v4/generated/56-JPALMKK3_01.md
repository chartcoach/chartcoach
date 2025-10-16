---
id: add-scale-to-part-to-whole-bar-charts
title: "Add a quantitative scale to improve part-to-whole bar chart accuracy"
tags:
  - impact:perceptual
  - chart:bar
  - chart:bar.stacked
  - task:composition
  - task:compare
  - task:lookup
  - data:quantitative
  - visual:position
  - visual:length
  - audience:general
  - medium:static
sources:
  - type: research
    ref: Redmond, 2019
    url: https://doi.org/10.1109/VISUAL.2019.8933718
    note: "Found that a bar chart with a quantitative scale had significantly lower mean absolute error than all other bar chart variants tested, including those with quartile or decile ticks."
---

## Guidance

When using a stacked bar chart for part-to-whole comparisons, adding an external quantitative scale significantly reduces estimation error and improves accuracy.

## Why

A scale provides explicit reference points, allowing viewers to read values more directly rather than relying on the less precise perceptual estimation of length. Experiments show that a bar chart with a scale performs significantly better than one without, and also better than bar charts with only intermediate tick marks (e.g., at every 10%).

## When it applies

- When using a stacked or 100% stacked bar chart where accurate judgment of proportions is important.
- When space permits the inclusion of a clear, legible axis and scale.

## Exceptions

- In some minimalist designs or small multiples, a scale may add unnecessary clutter. In these cases, the goal might be to show overall patterns rather than precise values, and direct labeling of key segments could be a better alternative.

## Trade-offs

- Adding a scale introduces more visual elements to the chart, which can increase visual complexity and occupy space.

## Signs of Trouble

- **High Estimation Error:** When asked to estimate values from the chart, users' answers have a wide variance and are frequently inaccurate.
- **Vague Judgments:** Users can only make general judgments (e.g., "this is about half") rather than more precise ones because there are no reference points.

## How to Improve

- **Quick Fix: Add Tick Marks.** If a full scale is not feasible due to space or aesthetic constraints, add internal visual cues to the bar. Tick marks at deciles (10%, 20%, etc.) are more effective at improving accuracy than tick marks at quartiles (25%, 50%, 75%).

- **Moderate Approach: Add a Full Scale.** Add a clearly labeled quantitative axis (e.g., from 0% to 100%) alongside the bar chart. This is the most effective way to improve estimation accuracy for this chart type.

- **Comprehensive Approach: Re-evaluate the Chart Choice.** If precise judgment is critical, question if a stacked bar is the right choice. A simple bar chart (for comparing absolute values) or a dot plot allows for even easier comparison, although you lose the direct part-to-whole representation in a single bar.
