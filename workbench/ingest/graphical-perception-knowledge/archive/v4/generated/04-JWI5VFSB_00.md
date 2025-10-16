---
id: use-donuts-like-pies
title: "Consider donut charts an effective alternative to pie charts"

tags:
  - impact:perceptual
  - impact:aesthetic
  - chart:pie
  - chart:donut
  - task:composition
  - task:lookup
  - data:quantitative

sources:
  - type: research
    ref: Skau & Kosara, 2016
    url: https://doi.org/10.1111/cgf.12888
    note: "Two studies found that donut charts are as accurate as traditional pie charts for part-to-whole estimations. The removal of the central angle did not hinder perceptual accuracy."

examples:
  - type: good
    description: A donut chart is used to show composition. The central space is effectively used to display the total value, a design advantage over a pie chart, without sacrificing perceptual accuracy.
---

## Guidance

Donut charts are a viable and effective alternative to traditional pie charts for showing part-to-whole relationships.

## Why

Empirical studies show that removing the center of a pie chart to create a donut chart does not decrease viewers' accuracy in estimating proportions. The central angle is the least critical visual cue for this task, and its absence is adequately compensated for by the remaining area and arc length cues.

## When it applies

- When choosing between a pie chart and a donut chart to represent the composition of a whole (e.g., market share, budget allocation).
- When you want to use the central space of a circular chart for a title, a key performance indicator (KPI), or an icon.

## Exceptions

- If the donut becomes extremely thin (e.g., inner radius is more than 80% of the outer radius), accuracy may slightly decrease. In such cases, the area cue becomes less salient, and the chart relies almost entirely on arc length.
- If the specific goal is to have users judge angles, though this is a rare and generally ineffective visualization task.

## Trade-offs

- **Gained:** A donut chart provides a blank central space that can be used for labels, totals, or icons, which is a significant design advantage over a pie chart.
- **Sacrificed:** The explicit central angle cue is removed. However, research shows this is a minimal loss as it's the least important perceptual cue for this chart type.

## Signs of Trouble

- **Unnecessary Hesitation:** A team avoids using donut charts due to an unsubstantiated belief that they are less accurate than pie charts.
- **Wasted Space:** A pie chart is used where the central area could have been productively used for a key takeaway or total value.

## How to Improve

- **Quick approach:** If you have a pie chart, feel confident converting it to a donut chart with a moderate hole size (e.g., 20-60% inner radius). This gains valuable space for labeling or a summary figure without losing perceptual accuracy.

- **Comprehensive approach:** When designing a dashboard or report, treat donut charts and pie charts as functionally equivalent for part-to-whole tasks. Choose between them based on your overall design goals. If you need a prominent spot for a total value or summary, a donut chart is the superior choice.
