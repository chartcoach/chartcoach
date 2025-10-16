---
id: prefer-position-for-quantitative
title: "Use position on a common scale over other visual channels for quantitative data"
tags:
  - impact:perceptual
  - task:compare
  - task:rank
  - data:quantitative
  - visual:position
  - visual:length
  - visual:angle
  - visual:area
  - chart:bar
  - chart:dot-plot
  - chart:pie
  - chart:bubble
sources:
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: https://doi.org/10.2307/2288400
    note: "Foundational research that established the perceptual ranking of visual encodings."
  - type: research
    ref: Mackinlay, 1986
    url: https://doi.org/10.1145/22949.22950
    note: "Formalized the effectiveness ranking of visual encodings in the APT framework."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Meta-analysis (Table 3) synthesizes this principle from the literature, ranking position as most effective."
---

## Guidance

When encoding quantitative data for comparison or ranking, prioritize using position along a common, aligned scale (as in bar charts or dot plots). This is perceptually more accurate than using length, angle, or area.

## Why

Humans are most accurate at judging differences in position along a common scale. Performance decreases significantly when judging unaligned lengths, and further still when judging angles (as in pie charts) or areas (as in bubble charts). This hierarchy of perceptual accuracy means that charts using position lead to faster and more accurate insights.

## When it applies

- The primary task is to accurately compare or rank quantitative values.
- When choosing the fundamental encoding for a chart designed to show magnitude.

## Exceptions

- **Part-to-whole:** When showing part-to-whole relationships is the primary goal, angle (pie chart) or length (stacked bar) are often used, though they are less accurate for comparing the individual parts to each other.
- **Space Constraints:** When space is highly constrained and you need to encode a third quantitative variable, area (e.g., bubble size) may be a necessary compromise.
- **Geographic Data:** On maps, area (of geographic regions) is an inherent property, and color is typically used to encode a quantitative value.

## Trade-offs

- Using position (e.g., a bar chart) often requires more space than using area (e.g., a treemap) to display the same data.

## Signs of Trouble

- **Impossible Comparisons:** Viewers are asked to compare the sizes of non-adjacent slices in a pie chart or bubbles in a bubble chart.
- **Misinterpreted Ratios:** Viewers misjudge the ratio between two values because they are encoded with area or angle. For example, they may fail to perceive that one pie slice is twice as large as another.

## How to Improve

- **Quick Fix: Add Data Labels.** If you must keep a chart that uses a less accurate encoding (like a pie or bubble chart), add direct data labels (e.g., "42%") to each mark. This provides an escape hatch for reading exact values, bypassing the perceptual difficulty.
- **Moderate Redesign: Align the Scales.** If using multiple bar charts, ensure they share the same axis and baseline to facilitate comparison. Convert a pie chart to a sorted bar chart to make comparisons easier.
- **Comprehensive Redesign: Switch to Position.** Convert charts based on angle or area (pie charts, bubble charts, treemaps for comparison) into a bar chart or dot plot to leverage the superior accuracy of position on a common scale.