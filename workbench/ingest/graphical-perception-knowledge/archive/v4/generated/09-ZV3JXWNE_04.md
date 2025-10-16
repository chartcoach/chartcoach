---
id: use-color-hue-for-nominal
title: "Use distinct color hues for categorical data, not for ordered data"
tags:
  - impact:perceptual
  - impact:ethical
  - visual:color
  - data:categorical
  - data:quantitative
  - data:ordinal
  - access:color-vision-risk
sources:
  - type: research
    ref: Mackinlay, 1986
    url: https://doi.org/10.1145/22949.22950
    note: "Established that color hue is effective for nominal data but not for ordered data."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Meta-analysis (Table 3) reinforces that hue (CH) is for nominal data (N) and not fully recommended for ordinal (O) or quantitative (Q) data."
---

## Guidance

Use different color hues (e.g., red, blue, green) to distinguish between nominal categories that have no inherent order. Avoid using a multi-hue sequence (like a rainbow) to represent ordered data (ordinal or quantitative).

## Why

Hues are excellent for showing "what" or "which" (category), but not "how much" (magnitude). A standard rainbow colormap is not perceptually uniform or ordered; viewers cannot reliably map the sequence of colors to a sequence of values. This leads to misinterpretation of the data, with some ranges appearing more important and others being obscured. For ordered data, a sequential palette (based on saturation or luminance) is required.

## When it applies

- When choosing a color scheme for any visualization.

## Exceptions

- **Diverging Palettes:** For bipolar data that pivots around a meaningful central value (like zero), a diverging palette that uses two different hues (e.g., blue to white to red) is an effective technique.
- **Cyclical Data:** For cyclical data (e.g., seasons of the year, compass direction), a cyclical color palette can be appropriate, but should be chosen carefully.

## Signs of Trouble

- **Rainbow Scale:** A continuous quantitative variable (e.g., temperature, elevation) is encoded with a rainbow color scheme.
- **Unordered Hues for Order:** An ordinal scale (e.g., "Bad," "Neutral," "Good") is encoded with unrelated hues (e.g., "blue," "green," "red") instead of a sequential or diverging palette.

## How to Improve

- **Moderate Redesign: Switch the Palette Type.**
  - For **quantitative data**, replace the multi-hue rainbow palette with a **sequential palette** (e.g., light blue to dark blue).
  - For **diverging data**, use a **diverging palette** (e.g., purple to gray to green).
  - For **categorical data**, ensure the chosen hues are maximally discriminable and accessible. Use a tool like Viz Palette or ColorBrewer to select a colorblind-safe palette.