---
id: avoid-hue-for-ordered-data
title: "Avoid using color hue to represent ordered or quantitative data"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:accessibility
  - chart:any
  - task:rank
  - task:find-extremum
  - task:trend
  - data:quantitative
  - data:ordinal
  - visual:color
  - access:color-vision-risk
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Chung et al., 2016
    url: https://doi.org/10.1111/cgf.12889
    note: "Found that hue performed poorly for both judging order (correlation task) and finding extreme values. Participants were less accurate and slower compared to channels like size or value/saturation."
  - type: research
    ref: Borland & Taylor, 2007
    url: https://doi.org/10.1109/MCG.2007.323435
    note: "Famously argued that the rainbow color map is harmful because it lacks a natural perceptual ordering, leading to misinterpretation of data."

tools:
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/
    description: "Provides pre-built sequential and diverging color palettes that are perceptually uniform and tested for accessibility."
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: "Allows you to test color palettes and see how they are perceived by people with various forms of color vision deficiency."

examples:
  - type: good
    description: "A choropleth map of population density uses a single hue (blue) with varying saturation, from light blue (low density) to dark blue (high density). The order is immediately intuitive."
  - type: bad
    description: "A weather map uses a rainbow colormap (blue, green, yellow, orange, red) to show temperature. It's not immediately clear if green is hotter or colder than yellow, and the abrupt changes between hues can create false boundaries where none exist."
---

## Guidance

To represent ordered data (quantitative or ordinal), use a sequential color palette that varies in lightness/saturation, such as from light blue to dark blue. Do not use a palette that varies in hue (e.g., a rainbow palette) for ordered data.

## Why

Color hue (e.g., red, green, blue) does not have a strong, universally perceived order. People are less accurate and slower at judging the order of data and finding extreme values when the data is encoded with hue. In contrast, color lightness or saturation (e.g., light to dark) is intuitively perceived as representing a low-to-high scale, making it much more effective for ordered data. Using hue can lead to misinterpretations and mask important patterns.

## When it applies

- When encoding any quantitative or ordinal data with color.
- When creating heatmaps, choropleth maps, or coloring marks in a scatterplot based on a numeric value.
- When the task involves identifying trends, ranking values, or spotting minimums and maximums.

## Exceptions

- **Categorical Data:** Hue is an excellent channel for encoding nominal (categorical) data where there is no inherent order (e.g., using blue for 'Democrats' and red for 'Republicans').
- **Cyclical Data:** For data that is cyclical (e.g., seasons of the year, direction on a compass), a carefully designed cyclical hue-based palette might be appropriate, but this is an advanced use case.

## Trade-offs

- A sequential palette has a more limited number of distinguishable steps compared to the variety offered by multiple hues. However, the clarity and accuracy gained by using a perceptually ordered palette far outweigh the loss of color variety for quantitative data.

## Signs of Trouble

- **"Rainbow" Effect:** The chart uses a full spectrum of colors like red, orange, yellow, green, and blue to show a continuous variable.
- **Ambiguous Order:** You can't immediately tell which end of the color scale represents "more" or "less" without constantly referring to the legend.
- **False Boundaries:** Abrupt changes between hues (e.g., from yellow to green) create strong visual boundaries in the data that are just artifacts of the color choice, not features of the data itself.
- **Poor Performance:** Viewers are slow and inaccurate when asked to find the highest or lowest value in the chart.

## How to Improve

- **Quick Fix: Switch to Grayscale.** A simple grayscale palette (from white to black) is a universally understood sequential scheme and is a safe and effective replacement for a rainbow palette.

- **Moderate Approach: Use a Single-Hue Sequential Palette.** Choose a single hue (like blue) and vary its saturation and/or lightness to create the scale. For example, light blue for low values, medium blue for mid-range values, and dark blue for high values. Tools like ColorBrewer make this easy.

- **Comprehensive Approach: Use a Perceptually Uniform Multi-Hue Palette.** For more complex data, use a multi-hue sequential palette that is designed to be perceptually uniform, like Viridis or Magma. These palettes use multiple hues but control the lightness systematically, so the perceptual order is clear and consistent.