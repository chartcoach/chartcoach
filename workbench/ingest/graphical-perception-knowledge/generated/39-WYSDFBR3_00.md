---
id: avoid-rainbow-colormap-for-ordered-data
title: "Avoid rainbow colormaps for encoding ordered quantitative data"

tags:
  # Impact dimensions (select all that apply)
  - impact:perceptual
  - impact:cognitive
  - impact:accessibility
  - impact:ethical
  - impact:aesthetic

  # Chart types (use hierarchy with dots for specificity)
  - chart:map
  - chart:map.choropleth
  - chart:map.isarithmic
  - chart:heatmap

  # Tasks (what the user is trying to accomplish)
  - task:rank
  - task:compare
  - task:trend
  - task:distribution

  # Data characteristics
  - data:quantitative
  - data:ordinal
  - data:spatial

  # Visual channels
  - visual:color
  - visual:color.hue

  # Audience characteristics
  - audience:general
  - audience:expert

  # Medium/format
  - medium:static
  - medium:interactive
  - medium:screen
  - medium:print

  # Accessibility risks
  - access:color-vision-risk
  - access:cognitive-load-risk

evidence:
  strength: high # Options: high | medium | low
  summary: "Gołębiowska & Çöltekin (2020, n=534) found that rainbow colormaps lack an intuitive perceptual order. When asked to order rainbow hues, participants produced 101 unique sequences with no consensus. In contrast, a sequential scheme yielded near-universal agreement (81.7% consistency), demonstrating a strong 'dark is more' bias. This confirms that spectral order does not map to perceptual magnitude."

sources:
  - type: research
    ref: Gołębiowska & Çöltekin, 2020
    url: https://doi.org/10.1109/TVCG.2020.3035823
    note: "Primary study (n=534) demonstrating lack of intuitive order in rainbow colormaps. In an ordering task, accuracy with rainbow was 38% vs. 81.7% with sequential (p<0.001)."
    role: primary # Options: primary | supporting | related
  - type: research
    ref: Borland & Taylor, 2007
    url: https://doi.org/10.1109/MCG.2007.323435
    note: "Seminal paper titled 'Rainbow Color Map (Still) Considered Harmful,' which synthesizes the perceptual problems of rainbow schemes."
    role: supporting
  - type: research
    ref: Brewer, 1997
    url: https://doi.org/10.1559/152304097782439312
    note: "Classic cartographic paper critiquing the use of spectral schemes for representing magnitude."
    role: supporting

tools:
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/
    description: "Provides pre-built, perceptually-tested sequential and diverging color schemes."
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: "Tool to test color palettes and simulate how they appear to users with color vision deficiencies."
---

## Guidance

Avoid using rainbow (spectral) colormaps for encoding continuous or ordered data. Instead, use a sequential or diverging color scheme that has a clear, monotonic progression in lightness.

## Why

The order of hues in a rainbow (red, orange, yellow, green, blue) does not create a natural sense of "more" or "less" for the human visual system. This makes it difficult for viewers to accurately judge the magnitude of the data, compare values, or perceive overall patterns. Rainbow colormaps can create false boundaries where none exist in the data and hide details in areas with low perceptual contrast (e.g., the yellow-green region).

### Core Principle

Visual encodings should match the structure of the data. Ordered data requires a perceptually ordered visual encoding, which rainbow schemes fail to provide. A monotonic change in lightness (from light to dark, or dark to light) is a much stronger and more intuitive visual cue for magnitude than a change in hue.

## When it applies

- When visualizing continuous quantitative data, such as temperature, elevation, density, or any other scalar field.
- When using chart types like heatmaps, choropleth maps, or isarithmic maps.
- When the user's task involves comparing values, ranking regions, or understanding the overall distribution of the data.

## Exceptions

- **Categorical Data:** If the colors represent distinct, unordered categories (e.g., land use types like 'forest', 'water', 'urban'), a palette of distinct hues is appropriate. However, this is a categorical palette, not a rainbow colormap applied to ordered data.
- **Specialized Conventions:** In some scientific fields, rainbow colormaps are a strong, albeit problematic, convention. Even in these cases, using them carries significant perceptual risks.
- **Specific Value Lookup:** For the narrow task of looking up a specific value by matching a color to a legend, rainbow schemes can be faster, but this comes at the cost of inhibiting all other tasks.

## Trade-offs

- **Aesthetics vs. Clarity:** Some people find rainbow colormaps visually appealing or vibrant. Choosing a sequential scheme prioritizes perceptual accuracy and clarity over this subjective aesthetic preference.
- **Familiarity vs. Effectiveness:** In fields where rainbow schemes are common, switching to a sequential palette may seem unfamiliar to an expert audience, but it will almost certainly improve their ability to interpret the data correctly.

## Signs of Trouble

- **The "Stripe" Effect:** The chart appears to have distinct bands of color, creating artificial boundaries that may not exist in the data.
- **Inability to Rank:** It's difficult to tell at a glance whether green represents a higher or lower value than yellow.
- **Muddled Center:** The central range of the colormap (often yellow/green) is difficult to distinguish, obscuring details in that range.
- **Accessibility Fail:** A colorblindness simulator reveals that major portions of the color scale (e.g., red and green) become indistinguishable.

## How to Improve

- **Quick Fix: Switch to Grayscale.** A simple grayscale ramp (black to white) is a perceptually ordered sequential scheme and is almost always better than a rainbow colormap for showing magnitude.

- **Moderate Approach: Use a Single-Hue Sequential Scheme.** Choose a single color and vary its lightness and saturation from light to dark (e.g., light blue to dark blue). Tools like ColorBrewer make this easy. This provides a strong perceptual ordering.

- **Comprehensive Approach: Use a Perceptually Uniform Multi-Hue Sequential Scheme.** For a more visually rich palette, use a scheme like Viridis, Magma, or Plasma. These palettes are carefully designed to have a monotonic increase in lightness while also moving through different hues, but they avoid the perceptual problems of a full rainbow. They are both visually appealing and perceptually effective.
