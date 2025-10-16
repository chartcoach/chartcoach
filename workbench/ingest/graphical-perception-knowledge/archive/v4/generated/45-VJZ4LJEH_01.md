---
id: prefer-multihue-for-resolution
title: "Use perceptually-uniform multi-hue colormaps for high-resolution quantitative data"
tags:
  - impact:perceptual
  - impact:performance
  - chart:heatmap
  - chart:map.choropleth
  - task:compare
  - data:quantitative
  - data:cardinality.high
  - visual:color
sources:
  - type: research
    ref: Liu & Heer, 2018
    url: https://doi.org/10.1145/3173574.3174172
    note: "The study found that single-hue colormaps exhibit higher error over small data value ranges, while judiciously designed multi-hue colormaps (like viridis) provide improved resolution and discrimination."
tools:
  - type: implement
    name: D3-scale-chromatic
    url: https://github.com/d3/d3-scale-chromatic
    description: A library providing various perceptually-uniform colormaps, including Viridis, Magma, and Plasma.
---

## Guidance

For visualizing continuous quantitative data, prefer a perceptually-uniform multi-hue colormap (e.g., Viridis) over a single-hue colormap, especially when discriminating small differences is important.

## Why

While single-hue colormaps (e.g., shades of blue) work well for judging large-scale differences, their accuracy drops when viewers need to distinguish between nearby values. The human visual system can more reliably discern small differences when there is a change in both hue (color) and luminance (brightness). Perceptually-uniform multi-hue colormaps are designed to ramp consistently in both, providing better "resolution" for fine-grained comparisons without sacrificing overall perceptual order.

## When it applies

- When visualizing a continuous scalar field, such as in a heatmap or choropleth map.
- When the goal is to accurately perceive both large-scale trends and small, local variations in the data.
- When using a continuous color scale with many steps, where adjacent colors in a single-hue scheme would be nearly indistinguishable.

## Exceptions

- When using a discrete color scale with a small number of bins (e.g., 3-5 categories). In this case, a single-hue scheme is often sufficient and can be aesthetically simpler.
- If the primary and *only* goal is to show the overall shape or a single large trend, and local variations are considered noise, a single-hue scheme can be less distracting.

## Trade-offs

- **Aesthetic simplicity:** Single-hue colormaps can feel more minimalist and less visually complex. Introducing multiple hues adds more color, which might be seen as a trade-off if simplicity is a primary design goal.
- **Cognitive load:** For some very simple tasks, a single-hue ramp might be marginally faster to process, although multi-hue schemes like Viridis were also found to be fast in experiments.

## Signs of Trouble

- **Indistinguishable Neighbors:** In your single-hue color scale, two adjacent values are mapped to colors that are visually indistinguishable from one another.
- **Washed-out Regions:** Parts of your single-hue colormap (often in the middle or light end of the range) appear to have very little variation, masking underlying details in the data.

## How to Improve

- **Moderate Redesign: Switch to a Perceptually-Uniform Multi-Hue Scheme.** Replace the single-hue sequential scheme (e.g., `scaleSequential(d3.interpolateBlues)`) with a perceptually-uniform multi-hue scheme (e.g., `scaleSequential(d3.interpolateViridis)`). This provides a drop-in replacement that improves discriminatory power for small value differences.
