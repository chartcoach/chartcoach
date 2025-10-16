---
id: use-value-texture-size-for-order
title: "Use Value, Texture, or Size to Convey Ordered Data"
tags:
  - impact:perceptual
  - impact:cognitive
  - task:rank
  - task:trend
  - task:correlate
  - data:quantitative
  - data:ordinal
  - visual:color
  - visual:texture
  - visual:size
  - chart:glyphs
  - chart:scatter
  - medium:screen
  - medium:static
evidence:
  strength: medium
  summary: "In a crowdsourced experiment (n=110), Chung et al. (2016) found that participants rated sequences encoded with value (lightness) and texture as significantly more ordered than those encoded with hue, shape, or orientation. Size was also found to be highly effective for quantitative judgment tasks."
sources:
  - type: research
    ref: Chung et al., 2016
    url: https://doi.org/10.1111/cgf.12889
    note: "Experiment 1 (n=110) measured the 'perceived orderedness' of different visual channels. Results showed value and texture were perceived as most ordered, while size closely approximated the actual order present in the data. Experiment 2 (n=87) confirmed the effectiveness of size for accuracy in a min/max judgment task."
    role: primary
examples:
  - type: good
    description: "In this example from the study, a sequence encoded with value (top) appears clearly more ordered than the same sequence encoded with a less effective channel, making it easier to perceive the underlying pattern."
    url: https://i.imgur.com/G5gCq6p.png
---

## Guidance

To help viewers perceive order in a sequence of data points, encode the ordered values using **value (lightness)**, **texture**, or **size**.

## Why

These visual channels are perceived as inherently ordered, which makes it easier for viewers to detect patterns of order (or lack thereof). When data is encoded using channels that don't have a strong perceptual order (like color hue), viewers have a harder time ranking elements or identifying trends. Using effective channels reduces cognitive load and improves the speed and accuracy of these tasks.

### Core Principle

Visual encodings should match the structure of the data. Ordered data (quantitative or ordinal) should be represented by visual channels that are themselves perceptually ordered.

## When it applies

This is relevant whenever you need to visually represent rank or order in a sequence of elements. This includes:
- Showing the trend in a series of glyphs or points.
- Helping the user quickly see if a sequence is sorted or chaotic.
- Encoding an ordered attribute on marks in a scatterplot, map, or other chart.

## Exceptions

If the primary task is not about judging order, another channel might be more appropriate. For example, if the goal is to distinguish between discrete, unordered categories, `color hue` or `shape` would be more effective than `value` or `size`.

## Trade-offs

- **Texture** can add visual noise or "chart junk," potentially cluttering the display.
- **Size** can cause occlusion in dense visualizations, where larger marks obscure smaller ones.
- **Value** is highly effective but has a limited number of just-noticeable differences, making it less suitable for high-cardinality data than `size`.

## Signs of Trouble

- **Order Ambiguity:** Viewers are unsure if a sequence of marks is sorted or not, even when the underlying data is.
- **Slow Pattern Detection:** It takes a long time for users to determine the trend or order in the data.
- **Incorrect Ranking:** When asked, users cannot accurately rank two or more marks according to the encoded value.

## How to Improve

- **Quick Fix:** If using a multi-hue color scheme (like a rainbow), switch to a sequential (single-hue) palette that primarily uses `value` (lightness) to show order.
- **Moderate Redesign:** Re-map the ordered data attribute from a less effective channel (like `color hue` or `orientation`) to `size`. If occlusion is an issue, add transparency to the marks.
- **Comprehensive Redesign:** If possible, use `position` on a common scale (e.g., a bar chart or dot plot), which is the most effective channel for showing order and magnitude. If you must use other channels, reserve `value` or `size` for the most important ordered attribute.