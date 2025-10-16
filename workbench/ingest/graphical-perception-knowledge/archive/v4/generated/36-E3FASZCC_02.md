---
id: use-partial-hue-for-order
title: "Use partial hue progressions to improve discriminability in sequential colormaps"

tags:
  - impact:perceptual
  - visual:color
  - data:quantitative
  - data:ordinal
  - task:rank
  - task:trend
  - medium:static
  - medium:interactive

sources:
  - type: research
    ref: "Bujack et al., 2018"
    url: https://doi.org/10.1109/SciVis.2018.8823772
    note: "Theorem 5 proves that in a Euclidean color space, a hue map satisfies global intrinsic order if it does not span more than half the circle of hues. This provides the theoretical basis for using partial hue progressions in sequential and diverging palettes."

tools:
  - type: implement
    name: "d3-scale-chromatic"
    url: https://github.com/d3/d3-scale-chromatic
    description: "A D3.js module that provides a variety of perceptually-backed color schemes, including multi-hue sequential palettes like Viridis and Turbo."
  - type: learn
    name: "How to Choose Colors for Your Data Visualizations"
    url: https://www.data-to-viz.com/caveat/color.html
    description: "A guide that explains the different types of color palettes, including multi-hue sequential palettes, and when to use them."

examples:
  - type: good
    description: "The 'Viridis' colormap. It progresses from blue to green to yellow. This is a partial hue progression combined with a strong monotonic increase in lightness, creating a highly discriminable and perceptually ordered scale."
  - type: bad
    description: "A colormap that attempts to show order by progressing from yellow to purple to green. This path jumps across the color wheel, creating a non-monotonic hue progression that is not perceptually ordered."
---

## Guidance

To increase the number of discernible steps in a sequential colormap, use a palette that combines a monotonic change in lightness with a smooth, partial progression in hue.

## Why

While a full hue cycle is not ordered, a segment of the hue circle (spanning less than 180 degrees) is perceptually ordered. Incorporating a limited, monotonic hue shift (e.g., from blue to green to yellow) into a sequential colormap increases the total perceptual distance between colors. This makes it easier for viewers to distinguish between nearby values compared to a colormap that only varies in lightness.

## When it applies

- When visualizing continuous data with high resolution, where you need to see subtle variations.
- When a single-hue sequential palette does not provide enough visual distinction across the range.
- For creating effective sequential and diverging colormaps.

## Exceptions

- **Grayscale is sufficient:** If the data has low resolution or if simplicity is the highest priority, a simple grayscale or single-hue palette may be perfectly adequate and less distracting.
- **Brand constraints:** If you are constrained to a specific brand palette that does not include a multi-hue progression, this may not be an option.

## Trade-offs

- **Increased Complexity:** A multi-hue sequential palette is more complex than a single-hue one and, if poorly designed, can introduce artifacts. It's crucial to use well-vetted palettes.
- **Potential Distraction:** The change in hue can be more visually stimulating than a simple lightness ramp, which might be distracting in some contexts.

## Signs of Trouble

- **Low Discriminability:** In a single-hue or grayscale map, large ranges of data are mapped to colors that are visually indistinguishable.
- **Hue Jumping:** The colormap's hue progression is not smooth or monotonic. For example, it goes from blue to red to green, jumping across the color wheel instead of moving smoothly along it.
- **Full Rainbow:** The hue progression spans the entire color wheel, violating the "partial progression" rule and destroying the perceptual order.

## How to Improve

- **Quick Fix: Choose a Vetted Multi-Hue Palette.** Switch from a single-hue palette (e.g., "Blues" from ColorBrewer) to a multi-hue sequential palette (e.g., "YlGnBu" from ColorBrewer or "Viridis" from Matplotlib/D3). These are designed to have the desired properties.

- **Moderate Approach: Design a Diverging Palette.** For data with a critical midpoint (like zero), use a diverging palette. These are effectively two different partial hue progressions moving away from a neutral, light color in the center (e.g., blue-to-gray-to-red).

- **Comprehensive Approach: Create a Custom HCL-Based Palette.** Use a tool or library that supports the HCL (Hue-Chroma-Luminance) color space. Design a colormap by defining a start and end point and creating a linear interpolation between them in HCL space. This allows you to create a smooth, partial hue progression while ensuring lightness remains monotonic.
