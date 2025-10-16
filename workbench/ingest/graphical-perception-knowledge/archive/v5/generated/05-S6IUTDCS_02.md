---
id: avoid-size-channel-interference
title: "Avoid using size for a secondary variable when a primary variable is read from position"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:scatter
  - chart:bubble-chart
  - task:lookup
  - task:compare
  - data:quantitative
  - visual:size
  - visual:position
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "In a 2018 experiment, Kim & Heer demonstrated that encoding a secondary quantitative variable with size interferes with and slows down the decoding of a primary quantitative variable from its position (x or y-axis) in a scatterplot."
sources:
  - type: research
    ref: Kim & Heer, 2018
    url: https://doi.org/10.1111/cgf.13409
    note: "The study found that charts with Q2:size (e.g., bubble charts) required more time for value tasks compared to charts with Q2:color, suggesting interference from the size channel on positional decoding (Section 4.2.4)."
    role: primary
tools: []
examples: []
---

## Guidance

In charts like scatterplots or bubble charts, avoid encoding a secondary quantitative variable with `size` if the primary task involves accurately reading values for another variable from its `position` on an axis.

## Why

The human visual system experiences "channel interference" when processing some combinations of visual variables. The variation in mark size acts as a distractor, making it more difficult and time-consuming to judge the precise x or y coordinate of the center of each mark. The same study found that using `color` for the secondary variable caused significantly less interference.

### Core Principle

Visual channels are not always independent; encoding one variable can interfere with the perception of another. An effective design minimizes this negative interference for the most critical tasks.

## When it applies

- In bubble charts or other scatter-type plots where x-position, y-position, and size all encode different quantitative variables.
- When the primary analysis task requires precise lookup or comparison of the values on the x or y axes.

## Exceptions

- When the size-encoded variable is the most important one for the analysis, and positional accuracy is secondary.
- When the task is to get a general "gist" of the data or identify broad trends, rather than performing precise lookups.
- In summary tasks (e.g., judging averages), where `size` can be an effective encoding for the primary variable itself.

## Trade-offs

- **You gain:** Faster and more accurate positional lookups.
- **You sacrifice:** The ability to use the powerful `size` channel for an additional quantitative variable. Alternatives like `color saturation` are often less effective for representing continuous quantitative data across a wide range.

## Signs of Trouble

- **Slow Performance:** Users take significantly longer to read values from the axes of a bubble chart compared to a standard scatterplot.
- **Inaccurate Lookups:** Users make more errors when asked to identify the x or y value of a specific bubble, especially when comparing large and small bubbles.
- **User Frustration:** Users express difficulty in pinpointing the exact location of larger or smaller bubbles relative to the axis ticks.

## How to Improve

- **Quick Fix: Add Hover Tooltips.** Implement interactive tooltips that display the precise x, y, and size values when a user hovers over a mark. This provides an "escape hatch" for the perceptual difficulty, allowing for exact value lookup on demand.

- **Moderate Redesign: Switch the Secondary Channel.** Encode the secondary quantitative variable using `color saturation` (e.g., light to dark shade of a single color) instead of `size`. The study found this caused less interference with positional judgments.

- **Comprehensive Redesign: Use Faceting.** If all three variables are important and require accurate reading, consider using small multiples. For example, create a series of standard x-y scatterplots, faceted by bins of the third variable (e.g., separate charts for "small," "medium," and "large" values of the size-encoded variable).
