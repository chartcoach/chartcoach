---
id: use-multi-hue-for-resolution
title: "Use perceptually-uniform multi-hue colormaps for high-resolution quantitative data"
tags:
  - impact:perceptual
  - chart:heatmap
  - chart:map.choropleth
  - task:compare
  - data:quantitative
  - visual:color
evidence:
  strength: medium
  summary: "Liu & Heer (2018) found that while single-hue colormaps perform well for large differences, they exhibit higher error for small value ranges. Perceptually-uniform multi-hue colormaps (like Viridis) provided better resolution for discriminating fine details."
sources:
  - type: research
    ref: Liu & Heer, 2018
    url: https://doi.org/10.1145/3173574.3174172
    note: "Primary finding that multi-hue colormaps can provide improved discrimination while preserving perception of order, especially for small data value ranges."
    role: primary
  - type: research
    ref: Smith & van der Walt, 2015
    url: https://www.youtube.com/watch?v=xAoljeRJ3lU
    note: "Introduced Viridis as a perceptually-uniform default colormap for Matplotlib, establishing the design principles for such palettes."
    role: related
tools:
  - type: implement
    name: Viridis Colormaps
    url: https://bids.github.io/colormap/
    description: "Provides the Viridis, Magma, Plasma, and Inferno colormaps, which are designed for perceptual uniformity and accessibility."
---
## Guidance

For continuous quantitative data, prefer a perceptually-uniform multi-hue colormap (like Viridis) over a single-hue colormap when discriminating small differences is important.

## Why

Ramping through both hue and luminance (as in `Viridis`) can provide greater perceptual separation between adjacent colors than ramping through luminance alone (as in single-hue palettes). This improved "resolution" makes it easier for viewers to discern subtle variations in the data that might otherwise be invisible in a single-hue gradient.

### Core Principle

The more perceptual distance between colors, the easier they are to tell apart. Judiciously designed multi-hue palettes can create more perceptual distance across the full range of data values than single-hue palettes.

## When it applies

- When visualizing continuous scalar fields (e.g., in heatmaps, scientific visualizations, or detailed choropleth maps) where small, local variations are meaningful.
- When you need to resolve fine details in a dataset with a high dynamic range.
- When a single-hue colormap appears to have "washed out" regions where detail is lost.

## Exceptions

- If the primary goal is to show overall magnitude and only large-scale comparisons are needed, a simple single-hue or grayscale colormap is often sufficient and can be less visually overwhelming.
- For applications involving discrete color scales with a small number of bins (e.g., 5-7 colors), single-hue palettes are generally acceptable and effective.

## Trade-offs

- **Simplicity vs. Precision:** A multi-hue colormap introduces more aesthetic complexity than a simple, elegant single-hue ramp. The choice depends on whether the priority is on analytical precision or visual simplicity.

## Signs of Trouble

- **Washed-Out Gradients:** In a visualization using a single-hue map, subtle but important variations in the data appear as a single, uniform block of color.
- **Low Resolution:** It is difficult for viewers to distinguish between two adjacent regions that have slightly different data values.

## How to Improve

- **Comprehensive Approach: Switch to a Perceptually-Uniform Multi-Hue Palette.** Replace the single-hue sequential palette (e.g., `Blues` from ColorBrewer) with a perceptually-uniform multi-hue palette such as `Viridis`, `Magma`, or `Plasma`. These are specifically designed to have a smooth, ordered luminance progression while leveraging changes in hue to increase discriminability.