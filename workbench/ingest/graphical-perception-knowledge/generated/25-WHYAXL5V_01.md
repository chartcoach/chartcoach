---
id: avoid-hue-orientation-for-order
title: "Avoid Using Color Hue or Orientation to Represent Ordered Data"
tags:
  - impact:perceptual
  - impact:cognitive
  - task:rank
  - task:trend
  - task:find-extremum
  - data:quantitative
  - data:ordinal
  - visual:color
  - visual:orientation
  - access:cognitive-load-risk
  - medium:screen
  - medium:static
evidence:
  strength: medium
  summary: "Chung et al. (2016) found in two experiments that color hue and orientation were perceived as the least ordered channels (Exp 1, n=110) and resulted in the highest error rates for finding minimum/maximum values (Exp 2, n=87)."
sources:
  - type: research
    ref: Chung et al., 2016
    url: https://doi.org/10.1111/cgf.12889
    note: "The study directly compared hue and orientation against other channels like value, size, and texture. Hue and orientation consistently performed worst for both perceived orderliness and accuracy in a quantitative judgment task, confirming they are poor choices for ordered data."
    role: primary
  - type: research
    ref: Borland & Taylor, 2007
    url: https://doi.org/10.1109/MCG.2007.323435
    note: "Supporting research arguing that rainbow color maps (which vary hue) are perceptually non-ordered and misleading for quantitative data."
    role: supporting
examples:
  - type: bad
    description: "Using a rainbow color scheme (which primarily varies hue) to encode ordered or quantitative data makes it difficult to perceive the correct order. It is unclear if green is 'more' or 'less' than yellow."
    url: https://i.imgur.com/gI2Qy64.png
  - type: good
    description: "Using a single-hue sequential palette (which varies value/lightness) makes the order clear and intuitive. Darker colors clearly represent larger values."
    url: https://i.imgur.com/kS9X7Hh.png
---

## Guidance

Do not use **color hue** (e.g., a rainbow color scale) or **orientation** (the angle of a line or mark) to encode sequential or quantitative data.

## Why

These visual channels are not perceived by our brains as being naturally ordered. A rainbow is a collection of different categories, not a scale from "low" to "high." Similarly, a 45° angle is not inherently "more" or "less" than a 90° angle. Using these channels for ordered data forces the viewer to memorize an arbitrary mapping, which increases cognitive load and leads to significant errors in interpretation, especially when trying to rank values or find extremes.

### Core Principle

Visual encodings should align with the structure of the data. Unordered channels like hue and orientation are suitable for categorical data, not ordered data.

## When it applies

This guideline applies whenever you are encoding ordinal (e.g., "small, medium, large") or quantitative (numeric) data where the viewer needs to understand the sequence, rank, or relative magnitude of the values.

## Exceptions

- **Cyclical Data:** `Orientation` can be effective for showing cyclical data like wind direction or time on a clock face. `Hue` can also be used for cyclical data (e.g., angles on a color wheel), but this is an advanced use case and should be handled with care.
- **Categorical Data:** `Hue` and `shape` (which often involves `orientation`) are excellent choices for distinguishing between discrete, unordered categories.

## Trade-offs

A rainbow color scale might appear more vibrant and engaging to some viewers. However, this aesthetic appeal comes at the significant cost of perceptual accuracy and clarity. The trade-off is choosing between an engaging but misleading chart and an accurate but potentially less colorful one.

## Signs of Trouble

- **The Rainbow Palette:** A chart uses a spectral color scheme (red, orange, yellow, green, blue, etc.) to represent continuous or ordered data.
- **Memorization Required:** A viewer has to constantly refer to the legend to understand the order of the encoded values.
- **Interpretation Errors:** Users misinterpret the order of values, for example, believing yellow represents a higher value than green, or vice-versa.
- **Inaccurate Comparisons:** Users cannot reliably tell which of two marks represents a larger value without consulting the legend.

## How to Improve

- **Quick Fix:** If you are using a rainbow palette for ordered data, replace it immediately with a single-hue sequential palette (e.g., light blue to dark blue) or a suitable diverging palette if there is a meaningful midpoint.
- **Moderate Redesign:** If using `orientation`, reconsider the task. If it's truly about magnitude, switch the encoding to a more effective channel like `size` or `value`.
- **Comprehensive Redesign:** Fundamentally re-evaluate the visual encoding. Map the ordered data attribute to a channel with a strong perceptual order: `position` (best), `length`, `size`, or `value` (lightness). Reserve `hue` and `shape`/`orientation` for their primary strength: encoding categorical data.