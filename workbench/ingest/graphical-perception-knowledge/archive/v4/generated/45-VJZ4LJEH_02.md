---
id: avoid-dark-colors-on-light-background
title: "Avoid using very dark colormap regions on a light background"
tags:
  - impact:perceptual
  - chart:heatmap
  - chart:map.choropleth
  - task:compare
  - data:quantitative
  - visual:color
  - medium:screen
  - medium:print
sources:
  - type: research
    ref: Liu & Heer, 2018
    url: https://doi.org/10.1145/3173574.3174172
    note: "The study observed a 'dramatic increase of error rates in the black regions' of colormaps like greys, magma, and plasma when they were displayed on a white background, suggesting high contrast impedes discrimination of dark shades."
---

## Guidance

When designing a visualization on a white or very light background, avoid colormaps that include very dark colors (approaching black) at one end of the scale.

## Why

The high contrast between a bright background and very dark color patches makes it difficult for the human eye to discriminate between different dark shades. This perceptual effect, known as simultaneous contrast, can mask variations in the data at the dark end of the scale, leading to significantly higher error rates in interpretation.

## When it applies

- When choosing a sequential colormap for any chart that will be displayed on a white or light-colored background.
- This is particularly relevant for colormaps like `magma`, `plasma`, and `greys`, which start at or near black.

## Exceptions

- **Dark Backgrounds:** This guidance is specific to light backgrounds. If you are using a dark background, the inverse problem may occur: it can be difficult to discriminate between very light, near-white colors.
- **Highlighting Only:** If the dark end of the scale is used solely to indicate a "low" or "zero" state and no fine discrimination within that region is required, the risk is lower.

## Trade-offs

- **Dynamic Range:** Avoiding the darkest colors slightly reduces the total available luminance range of the colormap. However, this is a worthwhile trade-off for the large gain in perceptual accuracy at that end of the scale.

## Signs of Trouble

- **The Black Hole Effect:** The darkest end of your color legend appears as a single block of near-black color, making it impossible to see any variation within that range.
- **Poor Discrimination in Dark Areas:** When looking at the chart, all the darkest regions blend together, even if the underlying data values are different.

## How to Improve

- **Quick Fix: Choose a "Safer" Colormap.** Select a perceptually-uniform colormap that does not start at black. For example, `viridis` starts with a dark purple/blue and is generally safer on a white background than `magma` or `plasma`.

- **Moderate Redesign: Adjust the Colormap Domain.** If you must use a colormap that includes black, you can "trim" the darkest part by mapping your data range to a subset of the colormap's domain (e.g., map your data from 0-100 to the colormap's 10%-100% range).

- **Comprehensive Redesign: Invert the Theme.** If discriminating values at the low end is critical, consider using a dark background for your entire visualization. Then, use a colormap that ramps from a dark color up to a very light color. This moves the discrimination challenge to the light end of the scale.
