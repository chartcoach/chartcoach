---
id: use-short-monotonic-hue-paths
title: "Use short, monotonic paths through hue for ordered data"
tags:
  - impact:perceptual
  - chart:heatmap
  - chart:map.choropleth
  - task:rank
  - task:trend
  - data:quantitative
  - data:ordinal
  - visual:color
  - visual:color.hue
evidence:
  strength: high
  summary: "Theoretical proof demonstrates that while a full hue circle lacks global intrinsic order, a path covering less than half the hue circle can be intrinsically ordered in a Euclidean color space."
sources:
  - type: research
    ref: "Bujack et al., 2018"
    url: "https://doi.org/10.1109/SciVis.2018.8823772"
    note: "Theorem 5 proves that a hue map can satisfy global intrinsic order if it does not span more than half the circle of hues, providing the formal basis for this guideline."
    role: primary
tools:
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org
    description: "The sequential and diverging schemes in ColorBrewer are built on this principle, using short, monotonic hue paths combined with monotonic luminance."
  - type: learn
    name: "Chroma.js Color Palette Helper"
    url: https://gka.github.io/chroma.js/#color-palette-helper
    description: "Tool for generating color palettes that often follow short, monotonic hue paths."
examples:
  - type: bad
    description: "A colormap that goes from red to yellow to green and back to yellow. The reversal in hue direction breaks the perceptual order."
  - type: good
    description: "A 'Yellow-Green-Blue' sequential colormap. It follows a short, monotonic path through hue (from yellow towards blue) while also increasing in luminance, making the order clear."
---
## Guidance
When using hue to encode ordered data, ensure the path through the hue spectrum is short (covers less than 180 degrees) and monotonic (unidirectional).

## Why
While the full hue circle is periodic and thus not globally orderable without a legend, human perception can reliably order short, adjacent segments of hue (e.g., a progression from orange to yellow to green). The research paper proves that a hue path not exceeding half the circle can satisfy the mathematical conditions for intrinsic order, meaning it can be perceived as ordered without a legend.

### Core Principle
Local perceptual order can be established even when global order is impossible. By constraining the visual range of an encoding, we can create a locally reliable and intuitive representation.

## When it applies
- When designing multi-hue sequential colormaps (e.g., progressing from yellow to blue).
- When designing diverging colormaps (e.g., progressing from blue to a neutral midpoint, and from the midpoint to red). Each arm of the diverging scheme should be a short, monotonic hue path.
- When you need more discriminative power than a single hue or grayscale can provide, but still require clear perceptual order.

## Exceptions
- This guideline is the *exception* that allows for the effective use of multiple hues for ordered data; it explains why well-designed schemes work and rainbow schemes fail. It does not have exceptions itself, but rather defines the conditions for success.

## Trade-offs
- **Discriminative Power vs. Range:** Limiting the hue path reduces the total number of unique colors available compared to using the full spectrum. However, it makes the colors that are used interpretable and meaningfully ordered.

## Signs of Trouble
- **Hue Reversal:** The colormap's hue path changes direction. For example, it moves from red towards green, but then bends back towards yellow.
- **Full Spectrum Traversal:** The colormap contains the full R-O-Y-G-B-I-V spectrum, which by definition violates the "short path" rule.
- **Jumping Hues:** The colormap jumps between distant hues (e.g., from blue directly to orange) instead of progressing smoothly.

## How to Improve
- **Moderate Approach: Use a Pre-built Multi-Hue Scheme.** Select a two- or three-hue sequential scheme from a trusted source like ColorBrewer (e.g., "YlGnBu" for Yellow-Green-Blue). These are designed to follow short, monotonic paths through hue while also increasing in luminance.
- **Comprehensive Approach: Design with Perceptual Models.** When creating a custom palette, use a tool that visualizes the path through a perceptual color space (like CIELAB). Ensure the path is smooth and travels in a consistent direction through the hue dimension, and does not cover more than half of the hue circle.