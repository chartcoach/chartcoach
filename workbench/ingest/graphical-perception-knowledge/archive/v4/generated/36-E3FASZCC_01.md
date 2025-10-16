---
id: monotonicity-is-not-sufficient-for-order
title: "Do not assume a colormap is ordered just because one of its channels is monotonic"

tags:
  - impact:perceptual
  - impact:cognitive
  - visual:color
  - data:quantitative
  - data:ordinal
  - task:rank
  - task:trend
  - audience:expert
  - medium:static
  - medium:interactive

sources:
  - type: research
    ref: "Bujack et al., 2018"
    url: https://doi.org/10.1109/SciVis.2018.8823772
    note: "Theorem 6 demonstrates via counter-example that monotonicity in a single attribute (hue, saturation, or luminance) is not sufficient to guarantee intrinsic perceptual order. The interaction between channels matters."

tools:
  - type: validate
    name: Colormeasures
    url: http://www.colormeasures.org
    description: A tool developed by the paper's authors to analyze and visualize the perceptual properties of colormaps.
  - type: validate
    name: Vischeck
    url: https://www.vischeck.com/
    description: A tool for simulating color vision deficiencies, which can reveal problems in colormaps that rely on hue differences.

examples:
  - type: bad
    description: "A colormap that is monotonic in luminance (continuously gets brighter) but also changes hue from red to yellow and back to red. The non-monotonic change in hue creates a 'flat spot' or perceived reversal in the middle, even though luminance is always increasing. This violates perceptual order."
    url: https://raw.githubusercontent.com/vis-guides/guidelines/main/src/images/bujack-2018-fig1-center.png
  - type: good
    description: "The 'Viridis' colormap, which is monotonic in lightness but also carefully controls its hue and saturation progression to ensure that the perceived change is consistent across the entire range. The result is perceptually uniform."
---

## Guidance

Do not assume a colormap is perceptually ordered simply because it is monotonic in one channel (e.g., strictly increasing in lightness, saturation, or hue). Perceptual order depends on the combined effect of all color channels.

## Why

The human visual system perceives color as a combination of hue, saturation, and lightness. A colormap can be monotonic in one of these attributes (e.g., always getting brighter) while simultaneously changing another attribute non-monotonically (e.g., hue shifts from red to yellow and back to red). This interaction can create perceptual "flat spots," bands, or even reversals, where the perceived order does not match the data order.

## When it applies

- When designing or selecting custom colormaps for ordered data.
- When evaluating a colormap that claims to be "ordered" based on a single attribute.
- In any situation requiring accurate interpretation of continuous data, such as scientific visualization, heatmaps, and surface plots.

## Exceptions

- **Grayscale:** A pure grayscale colormap only varies in luminance. Since other channels are constant (zero saturation), its monotonicity in luminance is sufficient to guarantee perceptual order.
- **Single-Hue Saturation Scale:** A colormap that varies only in saturation (from gray to a single, full-saturated hue) at a constant lightness is also perceptually ordered.

## Trade-offs

- **Simplicity vs. Robustness:** Creating a simple monotonic ramp in one channel is easy but perceptually fragile. Designing a truly perceptually uniform colormap requires more complex tools and knowledge but results in a much more robust and reliable visualization.

## Signs of Trouble

- **False Contours:** The visualization shows apparent boundaries, stripes, or edges that do not exist in the data. This is a classic sign of non-uniformity in the colormap.
- **The "Band" Test:** When looking at a smooth gradient, does the colormap appear to have distinct bands of color (e.g., a "yellow band" in the middle of a green-to-blue ramp)? This indicates a non-linear perceptual shift.
- **The Flat Spot:** A section of the colormap where different data values are mapped to colors that are nearly indistinguishable, causing a loss of detail.
- **The "Squint Test":** If you squint your eyes, does the colormap gradient become splotchy or uneven? A good sequential map should look like a smooth, monotonic gray gradient when you squint.

## How to Improve

- **Quick Fix: Use a Vetted Palette.** The easiest and most reliable solution is to discard the custom colormap and choose a pre-built, perceptually uniform palette from a trusted source like ColorBrewer 2.0 or the standard palettes in libraries like Matplotlib (Viridis, Cividis) or D3.js (d3-scale-chromatic).

- **Moderate Approach: Analyze the Colormap.** Use a tool like Viz Palette or Colormeasures to plot the colormap's path through a perceptual color space (like CIELAB). Look at the plots for lightness (L*), chroma (C*), and hue (h). A good sequential colormap will have a mostly monotonic lightness profile and smooth changes in other channels.

- **Comprehensive Approach: Design in a Perceptual Color Space.** When creating a custom colormap, work in a perceptual color space like CIELAB, CIELUV, or HCL. Instead of defining colors in RGB, define a path through the perceptual space that has the desired properties (e.g., monotonic lightness, controlled hue shift), and then convert the resulting colors back to RGB for display.
