---
id: prefer-position-for-quantitative-data
title: "Use position on a common scale for the most accurate quantitative comparisons"

tags:
  - impact:perceptual
  - impact:logos
  - chart:bar
  - chart:line
  - chart:scatter
  - chart:dot-plot
  - task:compare
  - task:rank
  - task:lookup
  - data:quantitative
  - visual:position
  - visual:length
  - visual:angle
  - visual:area
  - visual:color
  - audience:general
  - medium:static
  - medium:interactive
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Cleveland & McGill, 1984
    url: https://doi.org/10.2307/2288400
    note: "Established the foundational hierarchy of perceptual tasks, showing position on a common scale is most accurate."
  - type: research
    ref: Mackinlay, 1986
    url: https://doi.org/10.1145/22949.22950
    note: "Integrated the perceptual ranking into an automated system, formalizing the effectiveness of visual channels."

tools:
  - type: learn
    name: "Crowdsourcing Graphical Perception"
    url: https://doi.org/10.1145/1753326.1753357
    description: "Heer & Bostock's 2010 paper that replicated and extended Cleveland & McGill's findings, confirming the ranking of visual channels."

examples:
  - type: good
    description: "A bar chart uses position along a common y-axis, allowing for highly accurate comparisons of length and position."
  - type: bad
    description: "A pie chart uses angle and area to encode values. Viewers are much less accurate at comparing angles and areas than they are at comparing positions on a common scale, making it difficult to judge the relative sizes of slices."
---

## Guidance

For tasks requiring accurate judgment of quantitative values, encode the data using position along a common, aligned scale. Avoid using less effective channels like angle, area, or color saturation as the primary means of comparison.

## Why

Decades of graphical perception research have established a clear ranking of visual channels by their perceptual accuracy. Position along a common scale is the most accurately perceived by humans, followed by length, then angle, area, and finally color and density. This means people are best at judging differences in value when they are encoded by position (e.g., in bar charts or scatterplots) and worst when using channels like color.

## When it applies

- When the primary task is to make precise comparisons, rankings, or lookups of quantitative data.
- When data integrity and accurate interpretation are more important than aesthetic novelty.
- When designing dashboards or analytical tools for a general audience.

## Exceptions

- When position is already used to encode other information, such as geography on a map. In these cases, you must rely on less effective channels like color or size, but you must be aware of the reduced accuracy and potential for misinterpretation.
- For showing part-to-whole relationships where the approximate composition is more important than precise comparison between parts, a pie chart or treemap may be acceptable, but a bar chart is often still better.

## Trade-offs

- **Space:** Charts that use position effectively (like bar charts) can require more screen or page space than more compact representations that use color (like a heatmap or colored table).
- **Familiarity:** Some audiences may be more familiar with less effective chart types like pie charts. Choosing a more effective chart type like a bar chart may require a slight adjustment from the audience, but it will improve their ability to understand the data.

## Signs of Trouble

- **The "Which is bigger?" problem:** Viewers struggle to determine which of two marks (e.g., pie slices, bubbles) represents a larger value, especially when the difference is small.
- **Inconsistent Judgements:** Different people arrive at different conclusions about the relative magnitude of the data.
- **Reliance on Labels:** The chart is unreadable without direct data labels on every element. The visualization itself is not doing the work of communicating the values.

## How to Improve

- **Quick Fix: Add Direct Labels.** If you must use a chart that relies on a less effective channel (like a pie chart or bubble chart), add direct data labels to each element. This provides an "escape hatch" for the user, allowing them to read the exact value instead of relying on flawed perceptual judgment.

- **Moderate Redesign: Improve the Baseline.** If using a chart with unaligned scales (like a stacked bar chart for comparison of internal segments), switch to a grouped bar chart. This places all bars on the same baseline, making comparisons of length and position much easier and more accurate.

- **Comprehensive Redesign: Switch to a Position-Based Chart.** Replace visualizations that use area, angle, or color (e.g., pie charts, treemaps, bubble charts) with ones that primarily use position. For comparing categorical values, use a bar chart or dot plot. For showing correlation, use a scatterplot.