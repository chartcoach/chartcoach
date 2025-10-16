---
id: coordinate-color-for-order
title: "Coordinate color attributes for a clear perceptual order"

impact:
  - perceptual
  - cognitive
  - logos
  - ethical
  - aesthetic

tags:
  - color
  - colormap
  - sequential-data
  - quantitative-data
  - ordinal-data
  - perceptual-order
  - luminance
  - saturation
  - hue

sources:
  - type: research
    ref: Bujack et al., 2018
    url: https://doi.org/10.1109/SciVis.2018.8823772
    note: "Demonstrates that monotonicity in a single attribute (like luminance) is not sufficient to guarantee perceptual order. Provides a theoretical framework for evaluating order in colormaps."

tools:
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/
    description: A classic tool for selecting well-tested sequential, diverging, and qualitative colormaps.
  - type: implement
    name: HCL Wizard
    url: https://hclwizard.org/hcl-color-picker/
    description: A tool for creating custom colormaps with explicit control over hue, chroma, and luminance.
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: Allows you to create and check colormaps, showing their path through color space and simulating colorblind vision.
  - type: learn
    name: "A Guide to Understanding Color in Data Viz"
    url: https://www.storytellingwithdata.com/blog/2020/5/14/a-guide-to-understanding-color-in-data-viz
    description: An introductory guide to the roles color plays in data visualization.

examples:
  - type: bad
    description: "A colormap that is monotonic in luminance (brightness) but has a dip in saturation in the middle. This creates a visually distracting 'gray' or 'dull' band that breaks the perception of a smooth, ordered progression."
  - type: bad
    description: "A colormap that is monotonic in hue (e.g., green to blue) but has an uneven luminance path. This creates bright 'hot spots' that unintentionally draw attention and disrupt the sense of order."
  - type: good
    description: "A perceptually uniform colormap like Viridis or Cividis, where luminance increases monotonically while hue and chroma also change smoothly and in coordination, creating a clear and unambiguous sense of order."
---

## Guidance

For ordered data, ensure the colormap progresses smoothly and simultaneously across its luminance (brightness), saturation, and hue, not just one of these attributes in isolation.

## Why

Relying on a single attribute, like a steady increase in brightness, isn't enough to guarantee a perception of order. If other attributes like saturation or hue change erratically (e.g., dipping in the middle), it can create distracting visual bands that break the intended sequence. Our brains interpret color holistically, and a conflict between its properties makes it harder to see the underlying structure in the data.

## When it applies

- When visualizing sequential or diverging data (e.g., temperature, elevation, probability).
- When using any continuous colormap for quantitative or ordinal data.

## Exceptions

- When using color for categorical data, where the goal is for colors to be as distinct as possible, not to imply an order.
- When you intentionally want to highlight a specific range with a contrasting color, which by definition breaks a global perceptual order.

## Trade-offs

Achieving perfect perceptual uniformity may limit the range of available hues, potentially making the colormap seem less vibrant or exciting than a less-ordered one like the 'rainbow' scale. Highly optimized colormaps may not always align with specific brand color palettes.

## Evaluate

- [ ] Does the colormap have any "bands" or "stripes" that seem brighter, duller, or a different color than their neighbors in a non-sequential way?
- [ ] If you squint at the colormap, does it look like a smooth gradient, or do some parts jump out or fade unexpectedly?
- [ ] When viewed in grayscale, does the colormap fail to show a monotonic (steady) increase in brightness?

## Repair

1. **Use a pre-built perceptually uniform colormap.** The easiest and safest fix is to switch to a well-tested option like Viridis, Plasma, Cividis, or the sequential schemes in ColorBrewer.
2.  **Use a specialized tool.** If you need a custom map, use a tool like HCL Wizard or Viz Palette to design a colormap with smooth, coordinated paths for luminance and chroma.
3.  **Check the luminance path.** As a minimum, convert your proposed colormap to grayscale to ensure brightness changes monotonically. If it doesn't, adjust the colors until it does, but remember this check alone is not sufficient.