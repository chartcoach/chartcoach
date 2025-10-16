---
id: avoid-dark-colors-on-light-bg
title: "Avoid using dark, low-luminance colors for fine distinctions on a light background"
tags:
  - impact:perceptual
  - visual:color
  - medium:screen
  - medium:print
  - data:quantitative
  - task:compare
  - chart:heatmap
  - chart:map.choropleth
evidence:
  strength: medium
  summary: "In an experiment with nine colormaps on a white background, Liu & Heer (2018) found a dramatic increase in error rates in the darkest, low-luminance regions of several colormaps (Greys, Magma, Plasma), suggesting high contrast impedes the discrimination of dark shades."
sources:
  - type: research
    ref: Liu & Heer, 2018
    url: https://doi.org/10.1145/3173574.3174172
    note: "Observed that 'Performance Degrades in Low Luminance Regions' on a white background, with error rates spiking in the dark regions of Greys, Magma, and Plasma colormaps."
    role: primary
---
## Guidance

When designing or choosing a colormap for use on a white or very light background, avoid palettes that rely on fine distinctions between very dark colors.

## Why

The high contrast between a dark color patch and a bright white background can make it perceptually difficult to distinguish between two slightly different dark shades. This effect, a form of simultaneous contrast, reduces the effective resolution of the colormap in its darkest range, leading to higher error rates when viewers try to make comparisons.

### Core Principle

A color's appearance is influenced by its surrounding colors. High-contrast boundaries can interfere with the ability to perceive subtle differences in adjacent colors.

## When it applies

- When using a sequential colormap that progresses to black or a very dark color (e.g., `Greys`, `Magma`).
- When the chart's background is white or light gray, which is common in both print and screen media.
- When the visualization contains small marks or requires viewers to perceive fine details in the darkest parts of the data range.

## Exceptions

- This is less of an issue on a dark chart background, though the opposite problem—difficulty distinguishing very light colors—may occur.
- If the dark end of the scale represents values of little interest or an absence of data, this perceptual limitation may not be problematic.

## Trade-offs

- **Dynamic Range vs. Perceptual Uniformity:** Using the full dynamic range from black to white seems logical, but doing so on a white background sacrifices perceptual uniformity at the dark end of the scale. You may need to sacrifice some of the data range to maintain discriminability.

## Signs of Trouble

- **The Black Hole Effect:** The darkest part of your visualization appears as a single, indistinguishable blob of black or near-black, even though the underlying data has variations in that range.
- **High Error in Dark Regions:** When testing viewer comprehension, you find that users consistently make mistakes when comparing values represented by the darkest colors in your palette.

## How to Improve

- **Quick Fix: Truncate the Colormap.** Modify your colormap to remove the darkest 5-10% of the range. Instead of ending at pure black, end at a dark gray. This avoids the region of poorest discrimination.

- **Moderate Redesign: Choose a Different Palette.** Select a sequential palette that does not end in a very dark, low-luminance color. Some ColorBrewer palettes are designed this way. The `Viridis` colormap also ends in a dark purple/blue rather than pure black, which mitigates this issue.

- **Comprehensive Redesign: Change the Background Color.** If appropriate for your design, switch to a medium or dark gray background. This reduces the overall contrast and can help improve the discriminability of both the darkest and lightest colors in your palette.