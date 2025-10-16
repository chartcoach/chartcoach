---
id: avoid-bar-charts-for-mean-aggregation
title: "Use point charts instead of bar charts for judging average values"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:ethical
  - chart:bar
  - chart:scatter
  - task:summary-mean
  - task:aggregate
  - data:quantitative
  - audience:general
  - medium:static
  - medium:screen

evidence:
  strength: medium
  summary: "Godau et al. (2016) found in a series of experiments that viewers systematically underestimate the average of values presented in a bar chart, a bias not present in point charts."

sources:
  - type: research
    ref: Godau, Vogelgesang, & Gaschler, 2016
    url: https://doi.org/10.1016/j.chb.2016.01.036
    note: "Primary experimental evidence demonstrating systematic underestimation of the mean in bar charts compared to point charts."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Review paper that discusses systematic bias in bar charts (Table 8) and synthesizes findings from papers like Godau et al."
    role: supporting

examples:
  - type: bad
    description: "A bar chart used to show the distribution of values, from which a viewer might try to infer the average. The filled area of the bars encourages a biased, lower perception of the mean."
  - type: good
    description: "A dot plot (or a 1D scatterplot) showing the same data. By using points instead of bars, the visualization avoids the perceptual bias and allows for a more accurate estimation of the average."
---

## Guidance

To help viewers accurately judge the average (mean) of a set of values, use a point chart (dot plot) or scatterplot rather than a bar chart.

## Why

Viewers systematically underestimate the average value of a set of bars. This perceptual bias is robust and occurs because people's attention is drawn to the center of mass of the bars, not their top edges which actually encode the values. This leads to a perceived average that is consistently lower than the true average. Point-based charts do not suffer from this bias.

### Core Principle

Make the most important visual judgments easy and accurate. If the task is to judge an average, the chart type should not introduce a systematic perceptual error into that judgment.

## When it applies

- When the primary task for the viewer is to estimate, judge, or compare the overall average of a group of values.
- When presenting distributions of quantitative data where the central tendency is a key takeaway.

## Exceptions

- If the primary task is to look up individual values or compare specific pairs of values (not the overall average), a bar chart is often effective. The underestimation bias is specific to the aggregation task of judging the mean.
- When bar charts are a strong convention for a specific audience, and the cost of violating that convention is high. In this case, mitigate the issue by adding an explicit reference line for the average.

## Trade-offs

- **Familiarity:** Bar charts are extremely common and familiar to a general audience. A dot plot may be slightly less familiar, potentially requiring a brief moment of orientation for some viewers.
- **Visual Weight:** Bars have a greater visual weight than points, which can sometimes be used to emphasize magnitude. This is lost when switching to a dot plot.

## Signs of Trouble

- **Exclusive use of bar charts:** The visualization relies solely on bar charts for showing distributions where the mean is a key feature.
- **Misleading comparisons:** A design decision (e.g., choosing a bar chart over a dot plot) leads to inaccurate conclusions about the data's central tendency, even if the data is plotted correctly.

## How to Improve

- **Quick Fix: Add a Reference Line.** If you must use a bar chart, add a clearly labeled horizontal line that explicitly marks the average value. This gives viewers a direct and unbiased visual anchor, overriding their biased perceptual judgment.

- **Comprehensive Redesign: Switch to a Point-Based Chart.** Replace the bar chart with a dot plot or a 1D scatterplot. This directly addresses the root cause of the bias by removing the filled areas of the bars. This is the most effective way to ensure viewers can accurately perceive the average.
