---
id: prefer-saturation-for-ordinal-data
title: "Prefer color saturation or luminance over hue for ordered data"
tags:
  - impact:perceptual
  - impact:accessibility
  - data:ordinal
  - data:quantitative
  - visual:color
  - access:color-vision-risk
  - chart:map.choropleth
  - chart:heatmap
  - audience:general

evidence:
  strength: high
  summary: "Mackinlay's (1986) foundational work on encoding expressiveness identifies saturation/luminance as perceptually ordered, while hue is not. Zeng & Battle's (2023) review of 59 papers confirms this, showing that for ordinal data, color saturation (CS) is recommended over color hue (CH). Empirical work by Golebiowska & Coltekin (2022) further validates that saturation ramps are more intuitive and effective than hue-based ramps for summary tasks."

sources:
  - type: research
    ref: Mackinlay, 1986
    url: https://doi.org/10.1145/22949.22950
    note: "The APT framework identifies saturation as an ordered channel suitable for ordinal/quantitative data, while hue is identified as an unordered channel suitable for nominal data."
    role: primary
  - type: research
    ref: Golebiowska & Coltekin, 2022
    url: https://doi.org/10.1109/TVCG.2020.3035823
    note: "Empirical study confirming that color schemes based on saturation/luminance variation are more intuitive and perform better for summary tasks with ordinal data compared to hue-varying schemes."
    role: supporting
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "Review summarizing that for ordinal data effectiveness, theory ranks color saturation (CS) higher than color hue (CH) (Table 3, p. 7)."
    role: related

tools:
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/
    description: "Provides pre-built, well-vetted sequential and diverging color palettes that correctly use saturation and luminance ramps."
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: "Lets you analyze your color palette's luminance and chroma profile to check if it's perceptually ordered."
---
## Guidance
For ordinal (e.g., "low, medium, high") or sequential quantitative data, use a color ramp that primarily varies in saturation and/or luminance. These are known as **sequential** color schemes (e.g., light blue to dark blue). Avoid schemes that primarily change hue (e.g., from red to green to blue).

## Why
Humans naturally perceive a "more vs. less" or "low to high" relationship in saturation and luminance, making it an intuitive way to represent order. In contrast, hue (the color itself) does not have a universal perceptual ordering. A rainbow scale, for example, is not naturally interpreted as a monotonic progression, which can lead to misinterpretation of the underlying data's order.

### Core Principle
The perceptual structure of the visual encoding must match the logical structure of the data. Ordered data requires an ordered visual encoding.

## When it applies
- When assigning a color gradient to a continuous quantitative variable (e.g., temperature, sales, density).
- When color-coding ordinal categories (e.g., survey responses from "Strongly Disagree" to "Strongly Agree").
- When creating heatmaps, choropleth maps, or any surface plot representing a single continuous variable.

## Exceptions
- **Nominal Data:** If the data is purely categorical with no inherent order (e.g., "apples," "oranges," "bananas"), then using distinct hues is the correct approach.
- **Diverging Data:** If the data has a meaningful midpoint (like zero), a **diverging** palette is appropriate. This type of palette uses two different sequential hue-and-saturation ramps that meet at a neutral central color (e.g., blue to white to red).

## Trade-offs
- A single-hue sequential scheme may have less "pop" or visual appeal than a vibrant multi-hue one.
- It can be difficult to discriminate a large number of steps (e.g., more than 9) within a single-hue ramp. In such cases, a carefully designed multi-hue sequential ramp may be necessary.

## Signs of Trouble
- **No clear direction:** It's not immediately obvious which end of the color scale represents "high" vs. "low" without checking the legend.
- **Rainbow colors:** The color scale uses a sequence of many different hues, like a rainbow.
- **Grayscale failure:** When the visualization is converted to grayscale, the ordering is lost, and it becomes a muddle of similar gray tones.

## How to Improve
- **Quick Fix: Use a Pre-built Palette.** Instead of creating a custom gradient, select a "sequential" palette from a trusted tool like ColorBrewer or a built-in library like D3's `d3-scale-chromatic`.
- **Moderate Redesign: Analyze and Adjust.** Use a tool like Viz Palette to examine your current colormap. If the lightness profile is not monotonic (i.e., it goes up and down), it is not perceptually ordered. Replace it with one that has a smooth, monotonic lightness gradient.
- **Comprehensive Approach: Design in a Perceptual Color Space.** If you need a custom palette, design it using a color space like HCL, L\*a\*b\*, or Oklab, which are designed to make it easier to control perceptual attributes. Hold hue constant while varying chroma and luminance to create a robust sequential scale.