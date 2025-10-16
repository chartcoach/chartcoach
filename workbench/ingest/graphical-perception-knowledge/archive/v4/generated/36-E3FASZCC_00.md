---
id: avoid-full-spectrum-hue-for-order
title: "Avoid full-spectrum hue progressions for ordered data"

tags:
  - impact:perceptual
  - impact:ethical
  - impact:accessibility
  - visual:color
  - data:quantitative
  - data:ordinal
  - task:rank
  - task:trend
  - task:direction
  - access:color-vision-risk
  - audience:general
  - audience:expert
  - medium:static
  - medium:interactive

sources:
  - type: research
    ref: "Bujack et al., 2018"
    url: https://doi.org/10.1109/SciVis.2018.8823772
    note: "Theorem 4 proves that a full hue map does not satisfy global intrinsic order because it is periodic, meaning viewers cannot reliably determine direction or rank."
  - type: research
    ref: "Borland & Taylor, 2007"
    url: https://doi.org/10.1109/MCG.2007.323435
    note: "Classic paper summarizing the perceptual problems with rainbow colormaps, such as non-uniformity and lack of perceptual ordering."

tools:
  - type: implement
    name: ColorBrewer 2.0
    url: https://colorbrewer2.org/
    description: Provides a set of vetted sequential and diverging color schemes that are perceptually sound.
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: Tool for creating and testing color palettes for perceptual uniformity and color vision deficiency simulation.
  - type: learn
    name: "Cividis: A new perceptually uniform colormap"
    url: https://www.youtube.com/watch?v=xAoljeRJ3lU
    description: A video explaining the design and benefits of perceptually uniform colormaps.

examples:
  - type: bad
    description: "A classic rainbow colormap used to show elevation on a map. Because red appears at both ends of the visible light spectrum, it's ambiguous whether red is high or low without a legend. Furthermore, the transitions between hues (e.g., yellow to green) create false boundaries that may not exist in the data."
  - type: good
    description: "A choropleth map showing unemployment rates by county using a single-hue sequential scheme (e.g., light blue to dark blue). The intuitive progression from light to dark clearly and unambiguously communicates lower to higher rates."
---

## Guidance

Avoid using colormaps that cycle through the full spectrum of hues (like a classic rainbow) to represent ordered (quantitative or ordinal) data. Instead, use a sequential or diverging colormap.

## Why

A full hue cycle is periodic, meaning the colors at the beginning and end of the scale can be perceptually similar (e.g., red and violet in a rainbow). This breaks the perceptual order, making it impossible for a viewer to intuitively know if a value is high or low, or which of two colors represents a larger value, without constantly referencing a legend. These colormaps also introduce false boundaries and are not friendly to viewers with color vision deficiencies.

## When it applies

- When visualizing quantitative or ordinal data where the order of values is meaningful.
- For tasks that rely on perceiving order, such as identifying trends, ranking values, or understanding a continuous progression.
- When creating heatmaps, choropleth maps, or any surface plot representing a continuous variable.

## Exceptions

- **Cyclical Data:** For data that is inherently cyclical (e.g., direction/wind angle from 0-360 degrees, time of day), a cyclical colormap where the start and end colors are the same can be appropriate.
- **Categorical Data:** When data is purely categorical with no inherent order, a qualitative (multi-hue) palette can be used to maximize distinguishability, though care must still be taken with the number of categories.

## Trade-offs

- **Fewer Distinct Steps:** Sequential palettes may feel like they have fewer distinct "steps" than a rainbow palette, which can seem less discriminating for very high-resolution data. However, this is a worthwhile trade-off for ensuring the accurate perception of order.

## Signs of Trouble

- **Rainbow Palette:** The chart uses a colormap with more than two or three unrelated hues in sequence (e.g., red, yellow, green, blue, purple).
- **Order Ambiguity:** It's unclear if blue represents a "higher" or "lower" value than green without constantly checking the legend.
- **Cyclical Confusion:** The colors at the low and high ends of the data range are perceptually similar (e.g., a rainbow map where both ends are reddish).
- **False Contours:** The visualization shows apparent stripes or boundaries that are artifacts of the colormap, not features of the data.

## How to Improve

- **Quick Fix: Switch to Grayscale.** The simplest and safest sequential colormap is grayscale (black to white). It is universally understood and free of hue-related ambiguity.

- **Moderate Redesign: Use a Single-Hue Sequential Palette.** Replace the rainbow colormap with a sequential colormap that varies in lightness and/or saturation within a single hue (e.g., light blue to dark blue). Tools like ColorBrewer provide vetted options.

- **Comprehensive Redesign: Use a Perceptually Uniform Colormap.** Adopt a perceptually uniform colormap like Viridis, Plasma, Inferno, Cividis, or a ColorBrewer multi-hue sequential palette. These are specifically designed so that a change in the data value corresponds to a proportional perceptual change, ensuring accurate and accessible interpretation.
