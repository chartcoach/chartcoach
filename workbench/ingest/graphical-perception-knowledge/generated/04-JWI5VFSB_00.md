---
id: donut-charts-as-accurate-as-pies
title: "Use donut charts with confidence; they are as accurate as pie charts"
tags:
  - impact:perceptual
  - impact:aesthetic
  - chart:pie
  - chart:donut
  - task:composition
  - task:lookup
  - data:quantitative
  - visual:angle
  - visual:size
  - visual:length
  - medium:static
  - audience:general
evidence:
  strength: medium
  summary: "Skau & Kosara (2016, n=92 for study 1, n=93 for study 2) found no significant difference in log absolute error between standard pie charts and various donut charts (p > 0.05), indicating the central angle is not a critical perceptual cue. Donut charts were just as accurate as pie charts."
sources:
  - type: research
    ref: Skau & Kosara, 2016
    url: https://doi.org/10.1111/cgf.12888
    note: "Two experiments (n=92, n=93) compared pie charts to donut charts with varying inner radii for a value retrieval task. Results showed donut charts were as accurate as pie charts (log error for pie: 1.032, standard donut: 1.000; difference not statistically significant). This suggests the central angle is not essential for accurate perception."
    role: primary
examples:
  - type: good
    description: A standard donut chart is a valid alternative to a pie chart and frees up central space for labels or summary information.
    url: https://i.imgur.com/k2j402l.png
  - type: bad
    description: Believing that pie charts are inherently superior to donut charts due to the presence of a central angle is a misconception. Both are perceptually equivalent for value lookup tasks.
---

## Guidance

For part-to-whole visualizations, feel free to use a donut chart instead of a pie chart. You can use the center space for additional information, such as the total value or a summary title, without harming the chart's readability.

## Why

Contrary to the belief that the central angle is the most important part of a pie chart, research shows that removing the center to create a donut chart does not decrease accuracy. Viewers effectively use other cues like arc length and segment area to make accurate judgments. This makes donut charts just as perceptually effective as pie charts for estimating proportions.

### Core Principle

Human perception is flexible; when a primary visual cue (like a central angle) is removed, viewers can effectively switch to other available cues (like arc length or area) to complete the same task without a loss in accuracy.

## When it applies

- When creating a chart to show part-to-whole relationships (composition).
- When you need to visualize proportions and could benefit from using the empty center space for labels or summary figures.

## Exceptions

If the donut becomes extremely thin (e.g., the inner radius is >90% of the outer radius), accuracy may slightly decrease. In this case, the area cue becomes unusable, and viewers must rely solely on arc length. For most standard donut chart designs, this is not a concern.

## Trade-offs

Using the center of a donut chart for text can be useful, but it can also be distracting. Ensure the central content is directly relevant (e.g., a total value, a summary title) and does not visually compete with the data-encoded ring.

## Signs of Trouble

- **Distracting Center:** The text or icon in the center is purely decorative or unrelated, creating chart junk and distracting from the data.
- **Too-Thin Ring:** The donut ring is so thin it looks like a plain circle with varied line thickness. This makes it difficult for viewers to judge the area of the segments, removing a helpful perceptual cue.

## How to Improve

- **Quick Fix:** If you have a pie chart, simply convert it to a donut chart. Most visualization tools allow this with a single click or by adjusting the "inner radius" property.
- **Moderate Improvement:** Place a key summary statistic (like the total value or the value of the largest slice) in the center of the donut chart. This provides valuable context directly on the chart, improving its information density.
- **Comprehensive Redesign:** While donut charts are as good as pies, consider if a bar chart or treemap would be even better for your specific task. Bar charts are superior for comparing values, and treemaps are better for hierarchical part-to-whole data.
