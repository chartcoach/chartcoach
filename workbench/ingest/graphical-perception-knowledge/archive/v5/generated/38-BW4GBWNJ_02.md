---
id: use-saturation-for-ordinal-data
title: "Use color saturation or brightness for ordinal data, not hue"

tags:
  - impact:perceptual
  - impact:accessibility
  - visual:color
  - data:ordinal
  - data:quantitative
  - chart:heatmap
  - chart:map.choropleth
  - task:rank
  - task:direction
  - access:color-vision-risk

evidence:
  strength: high
  summary: "Foundational theoretical models of expressiveness (Mackinlay, 1986) and extensive empirical research show that saturation and brightness are perceived as ordered, while hue is not. Using sequential color schemes improves task performance for ordered data."

sources:
  - type: research
    ref: Mackinlay, 1986
    url: https://doi.org/10.1145/22949.22950
    note: "Defines the expressiveness principle, stating that visual encodings should match the perceptual character of the data. Recommends against using hue for ordered data."
    role: primary
  - type: research
    ref: Bujack et al., 2018
    url: https://doi.org/10.1109/TVCG.2018.2816551
    note: "Provides a theoretical framework for assessing colormaps, confirming that hue is not inherently ordered."
    role: supporting
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Review paper that summarizes the consensus: 'CH [Color Hue] is not expressive for representing ordinal data, and CS [Color Saturation] performs better than CH'."
    role: related

tools:
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/
    description: "A widely used tool for selecting perceptually-sound sequential, diverging, and qualitative color palettes."
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: "Allows you to create and test color palettes, including simulating for color vision deficiencies."

examples:
  - type: bad
    description: "A map showing unemployment rate by county using a rainbow color scheme. It's impossible to tell if red is higher or lower than green without constantly checking the legend."
  - type: good
    description: "The same map using a single-hue sequential scheme, from light blue (low unemployment) to dark blue (high unemployment). The order is immediately intuitive."
---

## Guidance

When encoding ordered data (e.g., low, medium, high; 0-100), use a sequential color scheme that primarily varies in saturation or brightness (e.g., light blue to dark blue). Avoid using a palette that varies in hue (e.g., a rainbow scheme), as hue does not have a natural perceptual order.

## Why

Changes in saturation and brightness are naturally perceived by the human visual system as an ordered progression ("less" to "more"), which correctly matches the structure of ordinal or quantitative data. In contrast, changes in hue (e.g., from red to green to blue) are perceived as categorical differences. Using a rainbow palette forces the viewer to memorize an arbitrary order from the legend, increasing cognitive load and the risk of error.

### Core Principle

Visual encodings should match the structure of the data. Ordered data deserves an ordered visual encoding.

## When it applies

- When representing any ordered data, including ordinal categories (e.g., "Bad", "Good", "Excellent") or continuous quantitative values (e.g., temperature, population density).
- When designing heatmaps, choropleth maps, or any other chart that uses a color gradient to represent value.

## Exceptions

- **Diverging Data:** If your data has a meaningful midpoint (like zero) and diverges in two directions (e.g., profit and loss), a diverging palette (which uses two different hues that meet at a neutral color) is appropriate. This is a deliberate exception that still follows the core principle, as it uses two sequential schemes joined together.
- **Cyclical Data:** For cyclical data (like phase or wind direction), a cyclical color scheme that varies in hue and returns to its starting point can be effective.

## Trade-offs

- **Aesthetics:** Rainbow palettes can appear vibrant and are sometimes used to attract attention. A well-designed sequential palette is often more subtle, which might be perceived as less "colorful," but it is far more effective and honest to the data.

## Signs of Trouble

- **The Rainbow Palette:** A rainbow (or spectral) color scheme is used to represent sequential or diverging data.
- **Legend-Reliant:** Viewers cannot tell which of two colors represents a higher value without looking at the legend.
- **False Boundaries:** The abrupt hue changes in a rainbow palette create false visual boundaries in the data where none exist, while masking variations within a single hue band.
- **Accessibility Issues:** Rainbow palettes are notoriously bad for people with color vision deficiencies, as common color pairs (like red/green) can become indistinguishable.

## How to Improve

- **Quick Fix: Grayscale It.** A simple test is to view your visualization in grayscale. If the ordering of values is lost, your color scheme is ineffective. A quick fix can be to use a grayscale palette.

- **Comprehensive Redesign: Use a Perceptually-Based Sequential Palette.** The best solution is to replace the hue-based palette with a proper sequential one.
  - For a single series, use a **single-hue sequential** palette (e.g., light blue to dark blue).
  - For more dynamic range, use a **multi-hue sequential** palette that still has a clear progression in brightness/saturation (e.g., yellow to green to blue).
  - Use tools like **ColorBrewer** to select a pre-vetted, perceptually uniform, and colorblind-safe palette.
