---
id: avoid-rainbow-colormaps
title: "Avoid rainbow colormaps for ordered data"
tags:
  - impact:perceptual
  - impact:accessibility
  - impact:ethical
  - chart:heatmap
  - chart:map.choropleth
  - task:compare
  - task:rank
  - task:lookup
  - data:quantitative
  - data:ordinal
  - visual:color
  - access:color-vision-risk
evidence:
  strength: high
  summary: "Liu & Heer (2018) found the 'jet' rainbow colormap was the slowest and most error-prone of nine tested colormaps for relative distance judgments. This confirms decades of research showing rainbow palettes distort data, are not perceptually ordered, and are unfriendly to colorblind viewers."
sources:
  - type: research
    ref: Liu & Heer, 2018
    url: https://doi.org/10.1145/3173574.3174172
    note: "Found the rainbow colormap 'jet' performed the worst overall in terms of both time and error, and should be jettisoned."
    role: primary
  - type: research
    ref: Borland & Taylor, 2007
    url: https://doi.org/10.1109/MCG.2007.32
    note: "A widely cited paper arguing that rainbow colormaps are harmful because they are not perceptually ordered."
    role: supporting
  - type: research
    ref: Rogowitz & Treinish, 1998
    url: https://doi.org/10.1109/2.730556
    note: "Early work identifying the perceptual problems with rainbow colormaps."
    role: supporting
tools:
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/
    description: "Provides pre-built sequential and diverging palettes that are perceptually sound alternatives to rainbow schemes."
  - type: implement
    name: Viridis
    url: https://bids.github.io/colormap/
    description: "A set of perceptually-uniform, colorblind-friendly colormaps (Viridis, Magma, Plasma, Inferno) designed to replace rainbow palettes."
---
## Guidance

Do not use rainbow (or "jet") colormaps to represent continuous quantitative or sequential data. Instead, use a sequential or diverging palette that has a clear, monotonic progression in luminance.

## Why

Rainbow colormaps are not perceptually ordered. They create false boundaries and obscure detail, leading viewers to misinterpret the data. People perceive sharp changes between some colors (like yellow and green) and almost no change between others, which rarely matches the underlying data structure. This leads to slower, less accurate interpretation. Furthermore, they are not accessible to users with common forms of color vision deficiency.

### Core Principle

Visual encodings should match the structure of the data. Ordered data deserves a perceptually ordered encoding. A colormap's perceived rate of change should match the data's rate of change.

## When it applies

- When encoding continuous numerical data (e.g., temperature, elevation, density, pressure) with color.
- In any chart that uses a continuous color scale, such as heatmaps, choropleth maps, or surface plots.

## Exceptions

None for representing ordered data. Their use is almost always discouraged by visualization experts for analytical purposes. While they might be used in artistic contexts, they are considered harmful for data communication.

## Trade-offs

- **Aesthetics vs. Clarity:** Some may find rainbow palettes vibrant, but this comes at a high cost to perceptual accuracy and data integrity. The trade-off is in favor of clarity and truthfulness.

## Signs of Trouble

- **False Boundaries:** Your map appears to have sharp stripes or bands of color that do not correspond to significant changes in the underlying data.
- **Luminance Chaos:** Converting the chart to grayscale produces a chaotic pattern with no clear and consistent light-to-dark progression. The brightest bands often appear in the middle of the scale (yellow).
- **Ambiguous Ordering:** It is difficult to tell if green represents a higher or lower value than orange without constantly referring to the legend.

## How to Improve

- **Quick Fix: Use Grayscale.** The simplest perceptually-ordered colormap is a grayscale ramp (white-to-black or black-to-white). This immediately fixes the perceptual ordering problem.

- **Moderate Redesign: Use a Single-Hue Sequential Palette.** Replace the rainbow scheme with a single-hue palette, such as the `Blues` or `Greens` schemes from ColorBrewer. These palettes vary primarily in luminance, making them easy to order perceptually.

- **Comprehensive Redesign: Use a Perceptually-Uniform Multi-Hue Palette.** Adopt a modern, perceptually-uniform colormap like `Viridis`, `Magma`, or `Plasma`. These palettes are designed to have a monotonic luminance ramp (making them perceptually ordered and grayscale-convertible) while also varying in hue, which can improve resolution for fine details. They are also designed to be robust to common forms of color vision deficiency.