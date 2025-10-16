---
id: avoid-dark-colors-on-light-backgrounds
title: "Avoid fine-grained comparisons in dark, low-luminance colors on a light background"

tags:
  - impact:perceptual
  - visual:color
  - medium:screen
  - medium:print
  - data:quantitative

evidence:
  strength: medium
  summary: "Liu & Heer (2018) observed a dramatic increase in error rates for comparison tasks involving colors in low-luminance regions (e.g., near-black shades) when presented on a white background. This occurred even when perceptual models predicted the colors should be distinguishable."

sources:
  - type: research
    ref: Liu & Heer, 2018
    url: https://doi.org/10.1145/3173574.3174172
    note: "Found high error rates for dark color triplets in 'greys', 'magma', and 'plasma' colormaps on a white background, hypothesizing that high contrast with the background impedes the discrimination of similar dark shades."
    role: primary

tools:
  - type: validate
    name: Contrast Checker
    url: https://webaim.org/resources/contrastchecker/
    description: "While designed for text, this tool can be used to check the contrast ratio between adjacent dark colors and a light background, though it doesn't directly measure perceptual discriminability."
---

## Guidance

When creating a visualization on a light or white background, be cautious about relying on viewers to distinguish between very dark, low-luminance colors for fine-grained comparisons.

## Why

The high contrast between a bright background and dark color marks can make it perceptually difficult to discriminate between two similar dark shades. The human visual system seems to struggle with resolving subtle differences in the "dark end" of the spectrum under these high-contrast conditions. This can lead to surprisingly high error rates, even when the colors are technically different enough according to standard color models.

## When it applies

- When using a sequential colormap that ends in very dark or near-black colors (e.g., `magma`, `inferno`, or a dark grayscale ramp).
- When the visualization is presented on a white or very light background.
- When it is important for the audience to make precise comparisons between values in the low end of the data range.

## Exceptions

- When the comparisons required are coarse-grained, and distinguishing between, for example, 95% black and 100% black is not critical to the chart's message.
- If the visualization is presented on a dark background. In this case, the opposite problem may occur: difficulty distinguishing between very light, high-luminance colors.

## Trade-offs

- **Data Range vs. Discriminability:** Using the full range from light to black maximizes the dynamic range of the colormap but sacrifices discriminability at the dark end. Truncating the dark end improves local discrimination but slightly reduces the overall range.
- **Aesthetic vs. Perceptual:** Very dark colors can create a strong visual impact, but this may come at the cost of perceptual accuracy for comparisons within that dark range.

## Signs of Trouble

- **The "Black Hole" Effect:** The darkest parts of your visualization appear as a single, undifferentiated mass of black or near-black, even though the underlying data has some variation.
- **Legend Check:** The darkest two or three swatches in your color legend look almost identical when viewed on the chart itself.
- **Inaccurate Low-End Judgments:** When asked, viewers cannot reliably tell the difference between data points represented by the darkest colors on the scale.

## How to Improve

- **Quick Fix: Lighten the Dark End.** Modify your colormap so that it ends at a dark gray (e.g., 85-90% black) instead of pure black. This reduces the extreme contrast and gives the visual system more "room" to perceive differences.
- **Moderate Approach: Choose a Different Palette.** Select a sequential colormap that does not extend into extremely low-luminance values. Some palettes are intentionally designed to avoid the extremes of pure white and pure black.
- **Comprehensive Approach: Invert the Scheme.** If the context allows, consider using a dark background for the visualization and a colormap that ramps from a dark color to a light one. This avoids the specific issue of dark-on-light, but be aware that it may introduce the opposite problem with light colors.