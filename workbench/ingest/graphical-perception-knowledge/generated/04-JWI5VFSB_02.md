---
id: avoid-variable-radius-pie-charts
title: "Avoid varying segment radii in pie charts"
tags:
  - impact:perceptual
  - impact:ethical
  - chart:pie
  - chart:donut
  - chart:radial
  - task:compare
  - task:composition
  - data:quantitative
  - visual:size
  - visual:length
evidence:
  strength: medium
  summary: "Inferred from Skau & Kosara (2016), who found arc length and area are key perceptual cues. Varying radii distorts both cues, forcing reliance on the less accurate angle cue. The authors explicitly state this 'should be avoided'."
sources:
  - type: research
    ref: Skau & Kosara, 2016
    url: https://doi.org/10.1111/cgf.12888
    note: "The paper's recommendation, based on their experimental findings: 'Arc length is important. It appears that changing the radius...interferes with people's ability to read the chart. This should be avoided.'"
    role: primary
examples:
  - type: bad
    description: A pie chart where each slice has a different length, creating a spiky, starburst effect. This makes it impossible to accurately compare the proportions using arc length or area.
    url: https://i.imgur.com/gT3L0pC.png
---

## Guidance

Do not use pie chart variations where the radius of each slice is different (sometimes called a "variable radius pie chart" or "rose chart"). Maintain a constant radius for all segments in a standard pie or donut chart.

## Why

Varying the radius of pie chart segments breaks two of the three main visual cues: arc length and area. Since experiments show these are more effective cues than angle for judging proportions, distorting them severely hinders the viewer's ability to accurately interpret the data. This flawed design forces them to rely on the much less accurate angle cue.

## When it applies

- When creating a chart to show part-to-whole relationships where each slice represents a proportion of a single total.

## Exceptions

If the radius itself is encoding a second, separate data variable (creating a polar area chart, a.k.a. Nightingale rose diagram), this is a different chart type with a different purpose. However, in this case, it is no longer a simple part-to-whole chart, and viewers will be comparing areas, which is known to be less accurate than comparing lengths on a common scale (as in a bar chart).

## Signs of Trouble

- **Spiky Slices:** Do the slices of your pie chart have different lengths, creating a starburst or spiky appearance? This is a sign that arc length and area cues are distorted.
- **Inconsistent Outlines:** The outer edge of the chart is not a smooth circle or ring.

## How to Improve

- **Quick Fix:** Immediately change the chart type back to a standard pie or donut chart with a constant radius to restore perceptual integrity.
- **Comprehensive Redesign:** If you have two variables to show (one for proportion, one for radius), use a different chart type that is better suited for multivariate data. For example, a scatter plot, or a bar chart where bar width or color saturation encodes the second variable. This separates the visual encodings and makes them easier to interpret correctly.
