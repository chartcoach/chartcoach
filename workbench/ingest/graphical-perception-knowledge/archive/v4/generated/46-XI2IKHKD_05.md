---
id: use-saturation-over-hue-for-ordered-data
title: "Use color saturation or lightness, not hue, for ordered data"

tags:
  - impact:perceptual
  - impact:accessibility
  - visual:color
  - data:quantitative
  - data:ordinal
  - access:color-vision-risk

sources:
  - type: research
    ref: Zeng & Battle, 2023
    note: "Review concludes that for ordinal data, Color Saturation (CS) is recommended while Color Hue (CH) is not, based on expressiveness principles from Mackinlay [61] and empirical work [29] (p. 8)."
  - type: research
    ref: Mackinlay, 1986
    url: https://doi.org/10.1145/22949.22950
    note: "Formalized the principle that color hue is not perceptually ordered, while saturation and value are, making them suitable for encoding ordinal or quantitative data."
  - type: practitioner
    ref: ColorBrewer
    url: https://colorbrewer2.org/
    note: Provides vetted sequential and diverging color schemes that vary in lightness/saturation for ordered data.

examples:
  - type: good
    description: A map uses a sequential color scheme from light blue to dark blue to show population density. The perceptual progression from light to dark naturally maps to the data progression from low to high.
  - type: bad
    description: A map uses a rainbow color scheme (blue, green, yellow, red) to show population density. It is not intuitive whether green is 'more' or 'less' than yellow, making the map difficult to interpret and perceptually unordered.
---

## Guidance

When encoding ordered data (quantitative or ordinal) with color, use a sequential palette that varies in saturation and/or lightness (e.g., from light blue to dark blue). Avoid using a qualitative palette that varies primarily in hue (e.g., blue, green, red, yellow).

## Why

Humans do not perceive color hue as having a natural order. There is no intuitive sense that "green" is greater than "blue." In contrast, changes in lightness and saturation are intrinsically perceived as ordered; we naturally see a progression from light to dark. Using a hue-based (rainbow) palette for ordered data creates a perceptual mismatch that forces the viewer to constantly refer to the legend, increasing cognitive load and the risk of misinterpretation. Sequential palettes align with our natural perception, making them intuitive to read.

## When it applies

- You are using color to represent quantitative data (e.g., temperature, sales, population).
- You are using color to represent ordinal data (e.g., rankings like "low," "medium," "high," or survey responses from "strongly disagree" to "strongly agree").
- This applies to any chart type that uses color to encode value, such as choropleth maps, heatmaps, or colored scatterplots.

## Exceptions

- **For categorical data:** If the data has no inherent order (e.g., company names, types of fruit), a qualitative palette that uses different hues is the correct choice to maximize discriminability between categories.
- **For diverging data:** If the data has a meaningful midpoint (like zero), a diverging palette (e.g., blue-white-red) that uses two different hues diverging from a light central color is appropriate. This is still a form of ordered palette.

## Trade-offs

- **Aesthetics:** Rainbow palettes are often perceived as vibrant and visually engaging, which is why they are frequently (mis)used. A single-hue sequential palette may appear more muted, which can be a trade-off between aesthetic appeal and perceptual accuracy.

## Signs of Trouble

- **The Rainbow Problem:** A rainbow (or spectral) color scheme is used to encode sequential or diverging data.
- **Constant Legend-Checking:** You observe viewers repeatedly looking back and forth between the chart and the legend to understand what the colors mean.
- **Order Confusion:** It's not immediately obvious which colors represent higher or lower values. Questions like "Wait, is yellow more or less than green?" are a red flag.
- **False Boundaries:** Abrupt hue changes in a rainbow palette can create the illusion of sharp boundaries in the data where none exist.

## How to Improve

- **Quick approach:** Use a grayscale palette. This is a simple sequential palette that varies only in lightness and is guaranteed to be perceptually ordered and colorblind-safe.
- **Moderate approach:** Choose a pre-vetted sequential color palette from a tool like [ColorBrewer](https://colorbrewer2.org/) or [Viz Palette](https://projects.susielu.com/viz-palette). These are designed by experts to be perceptually uniform and accessible.
- **Comprehensive approach:** Design a custom sequential palette using a perceptually uniform color space like HCL or L*C*h. This gives you full control over hue, chroma, and luminance to create a branded, effective, and accessible palette that progresses smoothly from light to dark.
