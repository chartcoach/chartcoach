---
id: prioritize-position-for-quantity
title: "Use position on a common scale to encode quantitative data"

tags:
  - impact:perceptual
  - impact:logos
  - task:compare
  - task:rank
  - data:quantitative
  - visual:position
  - visual:length
  - visual:angle
  - visual:area
  - visual:color
  - chart:bar
  - chart:scatter
  - chart:pie
  - chart:donut

evidence:
  strength: high
  summary: "A foundational principle of graphical perception, established by Cleveland & McGill (1984) and replicated in numerous studies, shows that humans judge quantitative data most accurately when it is encoded as position along a common, aligned scale. Subsequent encodings like length, angle, and area are progressively less accurate."

sources:
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: https://doi.org/10.2307/2288400
    note: "The foundational experimental work (n=55) that established the perceptual ranking of visual encodings, showing position on a common scale is superior to length, angle, and area for comparison tasks (p < 0.001)."
    role: primary
  - type: research
    ref: Mackinlay, 1986
    url: https://doi.org/10.1145/22949.22950
    note: "Formalized the perceptual rankings into an automated system (APT), extending them to nominal and ordinal data and solidifying the principle in visualization system design."
    role: primary
  - type: research
    ref: Heer & Bostock, 2010
    url: https://doi.org/10.1145/1753326.1753357
    note: "A large-scale crowdsourced replication (n=1,935) that confirmed the original Cleveland & McGill findings, demonstrating their robustness."
    role: supporting
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.48550/arXiv.2109.01271
    note: "This meta-analysis synthesizes the extensive literature, confirming the primacy of position encodings as a core, widely supported principle (Table 3)."
    role: supporting

examples:
  - type: good
    description: "A simple bar chart encodes sales figures for different regions. Because all bars start from a common baseline (zero), their lengths correspond directly to their position, making it easy and accurate to compare the sales figures."
  - type: bad
    description: "A pie chart shows the same regional sales figures. It is difficult to accurately compare the slice for 'Region A' (e.g., 23%) to 'Region B' (e.g., 25%) because it requires comparing angles or areas, which humans do poorly. A bar chart would make this small difference immediately obvious."
  - type: bad
    description: "A bubble chart uses the area of circles to represent population size. Comparing the area of two different circles is notoriously inaccurate; viewers are likely to misjudge the relative population sizes."
---

## Guidance

For tasks that require accurate comparison or ranking of quantitative values, encode the data using position along a common, aligned scale. Avoid using less accurate encodings like angle, area, or color saturation for this purpose.

## Why

The human visual system is better at judging some visual properties than others. Decades of research in graphical perception have established a clear hierarchy of effectiveness. We are most accurate when comparing positions along a shared scale (like in a bar chart). We are significantly less accurate when comparing lengths of unaligned objects, and even less accurate when comparing angles (like in a pie chart) or areas (like in a bubble chart). Choosing a more effective encoding reduces error and makes insights more obvious.

### Core Principle

The accuracy of human graphical perception varies by visual encoding channel. To enable precise comparisons, match the data and task to the most effective channel available. This is often summarized as the "Cleveland-McGill Scale."

## When it applies

- When the primary task for the viewer is to compare magnitudes (e.g., "Which category is largest?"), rank items, or judge differences between values.
- When creating bar charts, dot plots, or scatterplots, which are all based on position.
- When choosing between a bar chart and a pie chart for showing part-to-whole relationships where comparison of the parts is important.

## Exceptions

- **Showing Composition Only:** If the goal is purely to show a part-to-whole relationship and accurate comparison between parts is not important, a pie chart may be acceptable (e.g., showing a value like "75% complete"). However, a stacked bar chart often does this better.
- **Geographic Data:** For maps, position is already used to encode location. Therefore, other channels like color (for choropleths) or area (for bubble maps) must be used to encode quantitative data, despite being less perceptually accurate. Be aware of the inherent inaccuracies in these chart types.
- **When Other Tasks Dominate:** If the primary task is not comparison but something else, like identifying clusters or correlations, other chart types (like scatterplots) that also use position are still ideal.

## Signs of Trouble

- **Angle/Area Judgments:** The chart forces viewers to compare the angles of pie slices, the areas of circles, or the saturation of colors to understand quantitative differences.
- **"Is This Bigger?":** Viewers express uncertainty when trying to determine which of two non-positional marks (e.g., two pie slices) represents a larger value.
- **Inaccurate Takeaways:** Different people looking at the chart come to different conclusions about the relative size of the components.

## How to Improve

- **From Pie/Donut Chart → Bar Chart:** If you are using a pie or donut chart to compare categories, convert it to a bar chart. This changes the encoding from the less-accurate angle/area to the highly-accurate position/length, making comparisons trivial.

- **From Bubble Chart → Bar or Dot Plot:** If you are using the area of circles to encode quantity, change to a bar chart or a dot plot. This maps the quantity to position along a common axis, dramatically improving comparison accuracy.

- **From Stacked Bars (unaligned) → Grouped Bars (aligned):** When comparing segments within a stacked bar chart, only the bottom-most segment is on a common baseline. To facilitate comparison of all segments, switch to a grouped bar chart where every bar starts at zero.
