---
id: mind-bar-chart-aspect-ratio
title: "Use near-square aspect ratios for bars to minimize perceptual bias"
tags:
  - impact:perceptual
  - chart:bar
  - task:summary-mean
  - task:lookup
  - data:quantitative
  - visual:length
audience:
  - audience:general
medium:
  - medium:screen
evidence:
  strength: medium
  summary: "A recent experiment by Ceja et al. (2020) resolved conflicting findings on bar chart bias. The study found that bar aspect ratio is a key factor: tall, skinny bars are systematically underestimated, wide, short bars are overestimated, and bars with a near-square aspect ratio show no systematic bias. This provides a clear, actionable way to improve the accuracy of bar charts."
sources:
  - type: research
    ref: Ceja et al., 2020
    url: https://doi.org/10.1109/TVCG.2020.3030337
    note: "This study (ref [15] in Zeng & Battle) found that systematic bias in bar charts is related to their aspect ratio, with square bars showing no bias."
    role: primary
  - type: research
    ref: Godau et al., 2016
    url: https://doi.org/10.1016/j.chb.2016.01.036
    note: "An earlier study (ref [27]) that found a systematic underestimation in bar charts."
    role: related
  - type: research
    ref: Xiong et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934811
    note: "A conflicting study (ref [110]) that found an overestimation in bar charts. The work by Ceja et al. helps explain these contradictory results."
    role: related
---
## Guidance
When designing bar charts, be aware that the aspect ratio of the bars (the ratio of width to height) can introduce systematic perceptual biases. Aim for bars that are not excessively tall and skinny or short and wide.

## Why
Research has shown that viewers do not perceive the length of all bars equally. Very tall, thin bars tend to be perceived as shorter than they actually are (underestimation), while very wide, short bars are perceived as longer (overestimation). This can lead to misinterpretation of the data, especially when judging averages or making subtle comparisons. Bars with a more balanced, squarish aspect ratio are perceived most accurately.

## When it applies
- When creating bar charts of any kind (vertical, horizontal).
- When the precise magnitude of the bars is important for interpretation.
- When viewers might be mentally averaging a group of bars.

## Exceptions
- When space constraints are extreme and force the use of very thin or very short bars. In this case, be aware of the potential for bias and consider adding direct data labels.
- For sparklines or other highly condensed visualizations where the overall shape is more important than the exact value of any single bar.

## Trade-offs
- **Space:** Achieving a near-square aspect ratio may require more horizontal space for vertical bar charts (or vertical space for horizontal bar charts) than is available, especially with many categories.
- **Aesthetics:** Extremely thin bars are sometimes used for stylistic reasons, but this comes at the cost of perceptual accuracy.

## Signs of Trouble
- **"Skyscraper" Bars:** The chart contains bars that are extremely tall and narrow.
- **"Pancake" Bars:** The chart contains bars that are extremely short and wide.
- **Inconsistent Bar Widths:** Bar widths vary within the same chart, making aspect ratios inconsistent and introducing an uncontrolled variable.

## How to Improve
- **Quick Fix: Adjust Bar/Gap Width.** In your charting tool, increase the width of the bars (or decrease the space between them) to make them less skinny. For wide bars, decrease their width.
- **Moderate Redesign: Reconsider the Chart Scale.** If your data has a very large range, forcing some bars to be extremely tall, consider transforming the scale (e.g., a log scale, though this has its own perceptual challenges) or splitting the chart into multiple charts with different scales.
- **Comprehensive Redesign: Switch to a Dot Plot.** If you cannot avoid extreme aspect ratios due to space constraints, consider using a dot plot instead. A dot plot encodes value using only position, which is not subject to the same aspect-ratio-driven biases as length. Zeng & Battle (2023) note that one study found no bias with point marks.