---
id: prefer-position-length-for-comparison
title: "Use position or length over slope to encode values for comparison"
tags:
  - impact:perceptual
  - chart:bar
  - chart:dot-plot
  - chart:slopegraph
  - chart:line
  - task:compare
  - task:rank
  - task:filter
  - data:quantitative
  - visual:position
  - visual:length
  - visual:angle
sources:
  - type: research
    ref: Nothelfer & Franconeri, 2020
    url: https://doi.org/10.1109/TVCG.2019.2934801
    note: "Found that position (dot plots) and length (bar charts) led to faster and more accurate comparisons than slope encodings, for both individual and delta charts."
  - type: research
    ref: Cleveland & McGill, 1984
    url: https://doi.org/10.2307/2288400
    note: "Established the foundational ranking of perceptual tasks, placing position along a common scale and length as more accurate than angle/slope for quantitative judgments."
examples:
  - type: bad
    description: "A set of small, individual slopegraphs, each showing a change for one category. Asking a user to find the category with the steepest increase is difficult because comparing the precise angles of multiple non-aligned slopes is perceptually hard."
  - type: good
    description: "A bar chart or dot plot where the length or position of the mark represents the magnitude of the change. This allows for fast and accurate ranking and comparison because all marks share a common baseline."
---

## Guidance

When asking viewers to compare, rank, or search through quantitative values, encode those values using position along a common scale (as in a dot plot) or length (as in a bar chart) rather than slope or angle.

## Why

Human perception is more precise and efficient at judging differences in position and length than it is at judging differences in angle or slope. This principle, established by Cleveland & McGill, holds true for comparison tasks. Using position or length results in faster task completion and fewer errors, especially when multiple values need to be compared and ranked. The performance difference is particularly stark in search tasks, where finding a target slope is much slower than finding a target length or position.

## When it applies

- Any task that requires comparing the magnitude of two or more quantitative values.
- When creating delta charts to show differences, encode the deltas using position or length for maximum perceptual efficiency.
- This applies whether you are charting absolute values or the differences (deltas) between them.

## Exceptions

- When the primary goal is to show *rank change* between two time points, a connected slopegraph can be highly effective, as the crossing lines make rank changes salient.
- When showing *rate of change* is the explicit goal and the audience is trained to interpret slopes (e.g., in some scientific or financial contexts), the slope metaphor can be powerful despite its lower perceptual precision for magnitude comparison.

## Trade-offs

- Bar charts and dot plots may take up more vertical or horizontal space than a series of compact slope lines.
- Slope is a very direct visual metaphor for "rate of change." Switching to a bar chart to gain perceptual precision loses this direct metaphor.

## Signs of Trouble

- **Imprecise Judgments:** Users can tell which slope is steeper, but have difficulty judging *how much* steeper it is compared to another slope.
- **Slow Performance:** In tasks requiring users to search for or rank multiple items based on slope, performance is slow and error-prone.
- **Inconsistent Grouping:** When slopes are arranged in a row, they can create unintended A- and V-shaped patterns that interfere with judging individual slopes.

## How to Improve

- **Quick Fix: Add Labels.** If you must use slopes, add explicit data labels for the values or the rate of change so users don't have to rely solely on perceptual estimation.
- **Comprehensive Approach: Change the Visual Encoding.** Convert the chart from one using slope to one using length (bar chart) or position (dot plot) to represent the key quantitative values. This will improve perceptual accuracy and speed for comparison tasks.
