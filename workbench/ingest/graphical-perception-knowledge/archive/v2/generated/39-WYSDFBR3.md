---
id: avoid-rainbow-colormaps-for-ordered-data
title: "Avoid rainbow colormaps for showing order or patterns"

impact:
  - perceptual
  - cognitive
  - ethos
  - accessibility
  - aesthetic

tags:
  - color
  - colormap
  - rainbow-colormap
  - sequential-colormap
  - choropleth-map
  - isarithmic-map
  - comparison
  - pattern-detection
  - value-lookup
  - recall

sources:
  - type: research
    ref: Gołębiowska & Çöltekin, 2022
    url: https://doi.org/10.1109/TVCG.2020.3035823
    note: "Empirical study comparing rainbow and sequential schemes for map reading and recall tasks. Finds rainbow schemes are not intuitive for ordering, but can be competitive for specific value lookups and hue recall."
  - type: research
    ref: Borland & Taylor, 2007
    url: https://doi.org/10.1109/MCG.2007.323435
    note: "Classic paper arguing that the rainbow color map is (still) considered harmful because it misrepresents data and obscures features."
  - type: practitioner
    ref: C. Ware, "Color Sequences for Univariate Maps"
    note: "Foundational work explaining the perceptual issues with rainbow schemes and proposing principles for effective colormap design."

tools:
  - type: implement
    name: ColorBrewer 2.0
    url: https://colorbrewer2.org/
    description: Provides pre-built, perceptually-sound sequential, diverging, and qualitative color schemes.
  - type: implement
    name: Chroma.js
    url: https://gka.github.io/chroma.js/
    description: A JavaScript library for creating and manipulating colors and color scales.
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: A tool to check how your chosen colors will appear to people with different forms of color vision deficiency.
  - type: learn
    name: "A E-Z guide to color for data viz"
    url: https://blog.datawrapper.de/colorguide/
    description: A practical guide from Datawrapper on choosing effective color palettes.

examples:
  - type: bad
    description: A weather map using a rainbow colormap to show temperature. It is difficult to tell if green represents a higher or lower temperature than yellow without carefully checking the legend, making it hard to see regional patterns at a glance.
  - type: good
    description: The same weather map using a sequential blue color scheme, where lighter blue represents cooler temperatures and darker blue represents warmer temperatures. The ordering is immediately intuitive, leveraging a "dark-is-more" perceptual bias.
---

## Guidance

Avoid using the rainbow (or spectral) color scheme for encoding continuous quantitative or ordered data. Instead, prefer a **sequential color scheme** where lightness varies consistently from light to dark.

## Why

The human visual system does not perceive the hues of a rainbow in a naturally ordered way. It's not intuitive whether yellow is "more" than green, or orange is "less" than red. This ambiguity forces viewers to constantly reference the legend, slows down comprehension, and leads to errors in judging order and seeing patterns.

Sequential schemes (e.g., light blue to dark blue) leverage our innate perceptual ability to associate darkness with quantity ("dark-is-more"). This makes the visualization intuitive, faster to read, and more accurate for tasks involving comparison and pattern detection. Rainbow schemes can also introduce false boundaries that distort the underlying data, making you see stripes and contours that aren't really there.

## When it applies

- When visualizing continuous quantitative data, such as temperature, elevation, density, or pressure.
- When the primary task for the viewer is to understand order, compare values, or identify overall patterns and trends.
- In chart types like choropleth maps, isarithmic maps, and heatmaps that use color fills to represent magnitude.

## Exceptions

- **Specific Value Lookup:** When the primary task is to read a specific value by matching a color to its legend entry (e.g., "What is the exact value at this point?"). The distinct hues of a rainbow can, in some cases, make this direct matching task slightly faster than distinguishing between subtle shades of a sequential scheme.
- **Hue Recall:** If the goal is for a user to remember the *color* of a specific location (not its value). The unique, nameable colors in a rainbow (red, green, blue) are more memorable than "light blue" vs. "medium blue." This is a niche case and rarely the primary goal of a data visualization.
- **Purely Categorical Data:** While not recommended, a rainbow scheme can be used for purely nominal data with no inherent order. However, a purpose-built qualitative palette with perceptually distinct and balanced colors is a much safer and more effective choice.

## Trade-offs

- By choosing a sequential scheme over a rainbow, you prioritize overall clarity and pattern detection at the potential cost of a slightly slower lookup speed for specific values.
- You may sacrifice some of the "vibrancy" or "engagement" that some audiences associate with colorful rainbow palettes, but you gain significant trust and clarity in your data representation.

## Evaluate

- [ ] The chart uses a sequence of many different hues (e.g., red, orange, yellow, green, blue) to show numerical values.
- [ ] It's hard to tell if one color represents a higher or lower value than another without looking at the legend.
- [ ] The colors create strong visual "bands" or "stripes" that may not correspond to meaningful thresholds in the data.

## Repair

1.  **Replace with a sequential scheme.** The best and simplest fix is to swap the rainbow palette with a single-hue or multi-hue sequential scheme. For example, use a scale from light yellow to dark green. This makes the order immediately intuitive.
2.  **Consider a diverging scheme.** If your data has a meaningful midpoint (like zero, an average, or a critical threshold), use a diverging scheme (e.g., blue-white-red). This effectively highlights values above and below the midpoint.
3.  **If it must be a rainbow, add direct labels.** If you are forced to use a rainbow scheme and the task is specific value lookup, reduce the reliance on color by adding tooltips, annotations, or direct labels so users can read the exact values without decoding the color.