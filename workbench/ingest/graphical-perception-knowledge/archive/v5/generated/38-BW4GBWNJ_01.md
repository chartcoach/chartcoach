---
id: prefer-position-for-quantitative-data
title: "Encode quantitative data with position, not length, angle, or area"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:bar
  - chart:scatter
  - chart:dot-plot
  - chart:pie
  - chart:bubble
  - task:compare
  - task:rank
  - task:lookup
  - data:quantitative
  - visual:position
  - visual:length
  - visual:angle
  - visual:area
  - audience:general

evidence:
  strength: high
  summary: "Cleveland & McGill's foundational 1984 study, replicated many times through 2023, established a clear perceptual hierarchy where position along a common scale is the most accurate visual channel for quantitative comparisons."

sources:
  - type: research
    ref: Cleveland & McGill, 1984
    url: https://doi.org/10.2307/2288400
    note: "Foundational study establishing the perceptual ranking of elementary graphical tasks."
    role: primary
  - type: research
    ref: Heer & Bostock, 2010
    url: https://doi.org/10.1145/1753326.1753357
    note: "Crowdsourced replication study that confirmed the original findings of Cleveland & McGill."
    role: supporting
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Synthesizes the literature, confirming this principle remains a cornerstone of visualization design (Table 3)."
    role: related

examples:
  - type: bad
    description: "A pie chart comparing market share. Viewers must compare angles, which is a perceptually inaccurate task, especially for small differences."
  - type: good
    description: "A bar chart showing the same market share data. Viewers can easily and accurately compare the bar endpoints, which are aligned to a common baseline (the x-axis)."
---

## Guidance

For tasks requiring accurate comparison or judgment of quantitative values, encode the data using position along a common scale (e.g., bar charts, dot plots, scatterplots). Avoid encoding quantitative data with length, angle (e.g., pie charts), or area (e.g., bubble charts), as these are perceived less accurately.

## Why

Humans are significantly more accurate at judging differences in position along a common axis than they are at judging differences in length, angle, or area. This principle, known as perceptual ranking, is a foundational finding in visualization research. Using a more accurate channel like position reduces the risk of misinterpretation and allows viewers to make more precise judgments about the data.

### Core Principle

Humans judge quantities more accurately by comparing positions along a common scale than by comparing angles, areas, or colors.

## When it applies

- When the primary goal is to enable viewers to accurately compare, rank, or look up quantitative values.
- When designing charts like bar charts, line charts, scatterplots, pie charts, or bubble charts.

## Exceptions

- **Showing Part-to-Whole:** When the *only* goal is to show a part-to-whole relationship and the number of slices is very small (2-3), a pie chart can be acceptable, as it strongly affords the "parts-of-a-whole" interpretation. However, a stacked bar chart often works as well or better.
- **Geographic Data:** When using area to encode a value on a map (e.g., a cartogram), the area is tied to a recognizable shape, which can be acceptable if the primary goal is to show a general geographic pattern rather than precise comparisons.

## Trade-offs

- **Space:** Charts that use position effectively (like bar charts) can sometimes take up more space than area-based charts (like treemaps or packed bubble charts).
- **Familiarity/Engagement:** In some non-analytical contexts, charts like pie charts or bubble charts might be perceived as more engaging or familiar, even if they are less perceptually accurate.

## Signs of Trouble

- **Pie or Donut Chart:** A pie or donut chart is used to compare values, especially with more than 3-4 slices.
- **Bubble Chart:** A bubble chart is used for anything other than showing a general impression of magnitude distribution.
- **"Which is bigger?":** Viewers struggle to determine which slice or bubble is larger, especially when the differences are small.
- **Inaccurate Takeaways:** Viewers draw incorrect conclusions about the relative magnitude of different categories.

## How to Improve

- **Quick Fix: Add Direct Labels.** If you must use a pie or bubble chart, add direct data labels (e.g., "42%") to each element. This provides an "escape hatch" for viewers, allowing them to read the exact values instead of relying on their inaccurate perceptual judgment of angle or area.

- **Comprehensive Redesign: Switch to a Position-Based Chart.** The most effective fix is to change the chart type.
  - If you have a **pie chart**, convert it to a **bar chart**.
  - If you have a **bubble chart**, consider a **bar chart** or a **dot plot**.
  This ensures the quantitative values are encoded using the most perceptually accurate channel.
