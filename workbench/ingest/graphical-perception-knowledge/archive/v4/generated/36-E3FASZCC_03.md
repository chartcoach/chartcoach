---
id: luminance-and-saturation-are-ordered
title: "Use luminance or saturation ramps for ordered data"

tags:
  - impact:perceptual
  - visual:color
  - data:quantitative
  - data:ordinal
  - task:rank
  - task:trend
  - audience:general
  - access:color-vision-risk

sources:
  - type: research
    ref: "Bujack et al., 2018"
    url: https://doi.org/10.1109/SciVis.2018.8823772
    note: "Theorem 3 states that in a path metric space, shortest paths (like a pure luminance ramp or saturation ramp) are intrinsically ordered. This provides a strong theoretical foundation for using grayscale and single-hue saturation scales."
  - type: research
    ref: "Ware, 2012"
    url: https://www.elsevier.com/books/information-visualization/ware/978-0-12-381464-7
    note: "Ware emphasizes that a monotonic change in luminance is important for seeing the overall form of data (a qualitative task)."

tools:
  - type: implement
    name: ColorBrewer 2.0
    url: https://colorbrewer2.org/
    description: "Provides pre-vetted single-hue sequential palettes that primarily rely on luminance and saturation ramps."
  - type: learn
    name: "A Guide to Datawrapper's Sequential Palettes"
    url: https://blog.datawrapper.de/colorguide-sequential-palettes/
    description: "Explains the logic and use of sequential palettes, many of which are based on luminance/saturation ramps."

examples:
  - type: good
    description: "A grayscale heatmap showing website clicks. The progression from light gray (few clicks) to black (many clicks) provides an intuitive, unambiguous, and perceptually ordered representation of the data."
  - type: good
    description: "A choropleth map using a single-hue saturation ramp, from gray to a deep blue, to show vaccination rates. The increasing 'amount of color' is easily interpreted as an increasing rate."
---

## Guidance

For representing ordered data, use colormaps that follow a simple luminance ramp (grayscale) or a saturation ramp (from a neutral gray to a saturated hue). These are fundamentally and intuitively perceived as ordered.

## Why

The human visual system naturally and pre-attentively processes variations in lightness and saturation as indicators of magnitude. "More light" (or "more dark") and "more color" are intuitively mapped to "more value." These simple ramps are mathematically "shortest paths" in perceptual color space, which gives them a strong, intrinsic order that is robust and easy to interpret.

## When it applies

- When clarity and unambiguous order are the top priorities for a visualization.
- When visualizing quantitative or ordinal data for a general audience.
- As a safe, default choice for any sequential data.
- When creating accessible visualizations, as luminance is the primary channel perceived by all viewers, including those with color vision deficiencies.

## Exceptions

- **Low Discriminability:** A pure luminance or saturation ramp may not provide enough visually distinct steps to reveal very subtle variations in high-resolution data. In these cases, a multi-hue sequential palette might be better.
- **Aesthetic Goals:** A simple grayscale or single-hue palette may be perceived as less aesthetically engaging than a more colorful alternative. This may be a valid reason to choose another option if the primary goal is engagement rather than precise analysis.

## Trade-offs

- **Discriminability vs. Order:** These simple ramps provide the clearest sense of order but may offer fewer just-noticeable-differences than a multi-hue sequential palette. You trade some discriminability for maximum clarity of order.

## Signs of Trouble

- **Complex Palette for Simple Data:** You are using a complex rainbow or multi-hue palette to show a simple ordered sequence, introducing unnecessary ambiguity.
- **Accessibility Failures:** A colorblindness simulator reveals that your chosen multi-hue palette loses its apparent order for viewers with deuteranopia or protanopia.
- **Viewer Confusion:** Viewers are unsure about the order of values and must constantly refer to the legend.

## How to Improve

- **Quick Fix: Switch to Grayscale.** The simplest way to ensure perceptual order is to use a grayscale colormap. This removes all hue-related ambiguity and is universally accessible.

- **Moderate Approach: Use a Single-Hue Sequential Palette.** Choose a palette from a tool like ColorBrewer that uses a single hue (e.g., "Reds", "Blues", "Greens"). These palettes primarily work by varying lightness and saturation, providing a clear order with an added layer of hue information.

- **Comprehensive Approach: Combine with a Partial Hue Shift.** If more discriminability is needed, use a perceptually uniform multi-hue sequential palette (like Viridis or YlGnBu). These palettes are built upon a strong, monotonic luminance ramp but add a controlled, partial hue shift to increase the number of distinct steps while preserving the fundamental order.