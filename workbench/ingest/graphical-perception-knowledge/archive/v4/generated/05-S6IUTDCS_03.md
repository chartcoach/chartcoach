---
id: use-saturation-for-ordered-data
title: "Use color saturation or lightness for ordered data, not hue"
tags:
  - impact:perceptual
  - impact:accessibility
  - data:quantitative
  - data:ordinal
  - visual:color
  - visual:color.hue
  - visual:color.saturation
  - access:color-vision-risk
sources:
  - type: research
    ref: Mackinlay, 1986
    note: "Referenced as [61] in Zeng & Battle's Table 3. Mackinlay's expressiveness principles state that color hue (CH) is not intrinsically ordered, making it unsuitable for quantitative (Q) or ordinal (O) data, while color saturation (CS) is."
  - type: research
    ref: Liu & Heer, 2018
    url: https://doi.org/10.1145/3173574.3174172
    note: "Referenced as [58] in Zeng & Battle. This study empirically found that the rainbow colormap performs worst for ordering tasks and should be 'jettisoned'."
examples:
  - type: bad
    description: A rainbow colormap is used to show a quantitative value (e.g., temperature). It is not intuitive whether green represents a higher or lower value than yellow, and the abrupt changes in hue can create false boundaries in the data.
  - type: good
    description: A single-hue, sequential colormap is used for the same data. Values are mapped from light blue (low) to dark blue (high). This variation in saturation and lightness is intuitively perceived as an ordered progression, making it easy to see where values are high or low.
---

## Guidance

When encoding quantitative or ordinal data with color, use a palette that varies in saturation or lightness (e.g., from light blue to dark blue). Avoid using a palette that primarily varies in hue, such as a rainbow colormap.

## Why

The human perceptual system naturally interprets variations in saturation and lightness as an ordered sequence ("less" to "more" or "low" to "high"). In contrast, variations in hue (like red, green, blue) are not inherently ordered. A rainbow colormap is perceptually non-uniform; viewers cannot reliably order the colors, and the sharp, arbitrary transitions between hues can create misleading visual boundaries where none exist in the data. Furthermore, rainbow schemes are notoriously inaccessible to people with color vision deficiencies.

## When it applies

- You are encoding a **quantitative** (continuous) or **ordinal** (ordered categorical) variable.
- You are using `color` as the visual channel.
- This applies to choropleth maps, heatmaps, and any chart where mark color represents an ordered value.

## Exceptions

- **Diverging Data:** If your data has a meaningful midpoint (like zero), a diverging colormap (e.g., blue-white-red) is appropriate. This is still a systematic use of lightness and saturation, just in two directions from a neutral center.
- **Cyclical Data:** For data that is cyclical (e.g., hours of the day, wind direction), a specialized cyclical colormap might be used, but these should be designed криптовалют to loop smoothly.
- **Carefully Designed Multi-Hue Schemes:** Perceptually uniform colormaps like Viridis or Magma vary hue in a controlled way, but they are primarily defined by their smooth, monotonic increase in lightness. These are a valid exception because他们的设计考虑了感知。

## Trade-offs

- **Vibrancy:** A rainbow colormap can appear more vibrant and "colorful" than a single-hue sequential scheme. You are trading this superficial vibrancy for a massive gain in perceptual accuracy, interpretability, and accessibility.

## Signs of Trouble

- **The Rainbow:** The chart uses a full-spectrum rainbow colormap (red, orange, yellow, green, blue, indigo, violet).
- **Order Ambiguity:** A viewer cannot tell if green represents a higher or lower value than yellow without constantly checking the legend.
- **False Boundaries:** The chart appears to have sharp "cliffs" or boundaries that are artifacts of the colormap (e.g., a sudden shift from yellow to green) rather than the underlying data.
- **Accessibility Fail:** When viewed with a colorblindness simulator (e.g., for deuteranopia), large portions of the color scale become indistinguishable.

## How to Improve

- **Quick Fix: Switch to Grayscale.** A simple grayscale palette is perfectly ordered and accessible. It may not be as aesthetically pleasing, but it is perceptually sound.

- **Moderate Redesign: Use a Single-Hue Sequential Palette.** The most common and effective solution. Pick a single hue (like blue) and vary the saturation/lightness from a very light shade to a very dark shade. Most visualization tools have these palettes built-in (e.g., "Blues", "Greens").

- **Comprehensive Approach: Use a Perceptually Uniform Multi-Hue Palette.** For a more vibrant but still perceptually sound option, use a modern, scientifically designed colormap like Viridis, Magma, Plasma, or Cividis. These palettes vary hue in addition to lightness, but they do so in a controlled, perceptually linear way, ensuring they are decodable and robust to color vision deficiencies. Tools like Matplotlib, D3 (d3-scale-chromatic), and ColorBrewer provide excellent, research-backed palettes.