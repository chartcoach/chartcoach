---
id: avoid-rainbow-colormaps
title: "Avoid rainbow colormaps for ordered data"

impact:
  - perceptual
  - accessibility
  - ethical
  - logos
  - performance

tags:
  - color
  - colormap
  - quantitative-data
  - ordered-data
  - rainbow-colormap
  - jet
  - heatmap
  - choropleth-map
  - comparison
  - accessibility
  - colorblindness

sources:
  - type: research
    ref: Liu & Heer, 2018
    url: https://doi.org/10.1145/3173574.3174172
    note: "Empirically demonstrated that the 'jet' (rainbow) colormap led to the highest error rates and slowest response times for value comparison tasks compared to single-hue and perceptually uniform multi-hue schemes."
  - type: research
    ref: Borland & Taylor, 2007
    url: https://doi.org/10.1109/MCG.2007.323435
    note: "Classic paper detailing the perceptual problems of rainbow colormaps, arguing they can be 'harmful' to interpretation."

tools:
  - type: implement
    name: viridis colormaps
    url: https://bids.github.io/colormap/
    description: "A family of perceptually uniform colormaps (viridis, plasma, magma, cividis) designed to be effective and colorblind-safe alternatives to rainbow schemes. Available in most plotting libraries."
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/
    description: "A widely used tool for selecting effective and accessible sequential, diverging, and qualitative color schemes for maps and charts."
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: "A tool to create, edit, and check color palettes for colorblind-friendliness and perceptual evenness."

examples:
  - type: bad
    description: "A scientific heatmap uses the default 'jet' (rainbow) colormap. The abrupt shifts between green and yellow create false boundaries in the data, while the non-uniform changes in lightness make it impossible to accurately judge the magnitude of differences between regions."
  - type: good
    description: "The same heatmap is visualized using the 'viridis' colormap. The smooth, monotonic increase in lightness allows viewers to correctly perceive the data's order and more accurately estimate the relative differences between values, without introducing misleading artifacts."
---

## Guidance

Avoid using rainbow colormaps (like 'jet' or 'spectral') to represent continuous or ordered quantitative data. Instead, use a perceptually uniform colormap.

## Why

Rainbow colormaps are perceptually non-uniform. The changes in hue and lightness do not correspond to the changes in the data's values, which can mislead viewers by creating false boundaries and hiding important details. Research shows that compared to perceptually uniform alternatives, rainbow colormaps lead to significantly lower accuracy and slower interpretation. They are also not accessible to users with common forms of color vision deficiency.

## When it applies

- When visualizing a continuous variable, such as temperature, pressure, density, or elevation.
- For chart types like heatmaps, choropleth maps, contour plots, or any surface plot where color represents a third dimension.
- When the goal is to accurately compare values, identify gradients, or see the shape and structure of the data.

## Exceptions

For unordered **categorical** data, a palette with distinct hues can be appropriate, though a full rainbow is rarely the best choice due to its lack of perceptual separation between adjacent colors (like yellow and light green). For **ordered** data, there are no established exceptions where a rainbow colormap is the preferred choice for accurate data representation.

## Trade-offs

- **Aesthetics vs. Clarity:** You may sacrifice the high-contrast vibrancy that some viewers associate with rainbow colormaps. The trade-off is gaining significant improvements in data clarity, accuracy, and accessibility.

## Evaluate

- [ ] Does the colormap cycle through multiple distinct hues like red, orange, yellow, green, blue, and purple?
- [ ] Does the perceived lightness of the colormap fail to increase or decrease smoothly? (e.g., it gets bright in the middle with yellow and dark at both ends).
- [ ] Is the colormap named 'jet', 'rainbow', or 'spectral' in the visualization tool's options?

## Repair

1.  **Replace the colormap.** The best and easiest fix is to substitute the rainbow scheme with a perceptually uniform colormap.
2.  **Use a sequential scheme.** For data that progresses from low to high, use a single-hue sequential colormap (e.g., light blue to dark blue) or a multi-hue sequential colormap like 'viridis' or 'cividis'.
3.  **Use a diverging scheme.** If the data shows deviation from a central midpoint (e.g., positive and negative values), use a balanced, two-color diverging colormap (e.g., one that transitions from blue to a neutral gray/white to red).