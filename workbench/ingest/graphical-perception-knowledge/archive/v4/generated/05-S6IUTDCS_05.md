---
id: minimize-bar-chart-aspect-ratio-bias
title: "Use square-like aspect ratios for bars to minimize perceptual bias"
tags:
  - impact:perceptual
  - impact:ethical
  - chart:bar
  - task:lookup
  - task:summary-mean
  - data:quantitative
sources:
  - type: research
    ref: Ceja et al., 2020
    note: "Referenced as [15] in Zeng & Battle. This is the most recent cited work on bar chart bias, finding that 'the systematic bias in bars is related to the aspect ratio of bars. No systematic bias is shown with square bars, while wide bars are overestimated, and tall bars are underestimated' (p. 10)."
  - type: research
    ref: Godau et al., 2016
    note: "Referenced as [27] in Zeng & Battle. Found underestimation in bar charts."
  - type: research
    ref: Xiong et al., 2020
    note: "Referenced as [110] in Zeng & Battle. Found overestimation in bar charts. The conflict between this and [27] is resolved by the aspect ratio findings in [15]."
---

## Guidance

When designing bar charts, aim for an aspect ratio for the bars that is roughly square-like. Avoid using bars that are either extremely tall and thin or very short and wide, as these shapes can introduce systematic perceptual biases.

## Why

The aspect ratio визуально of a bar systematically affects how its value is perceived. Research has shown conflicting results on over- or under-estimation, but a recent study reconciled these findings by linking them to aspect ratio:
- **Tall, thin bars** tend to be **underestimated**.
- **Short, wide bars** tend to be **overestimated**.
- **Square-like bars** show **no systematic bias**.

Relying on extreme aspect ratios can therefore lead viewers to make small but systematic errors in their judgment of the data, which can be a subtle form of misrepresentation.

## When it applies

- You are designing a **bar chart**.
- The task requires a reasonably **accurate judgment of value**, either for a single bar (lookup) or for the average of a set of bars (summary).
- Data integrity and avoiding unintentional distortion are priorities.

## Exceptions

- **Space Constraints:** Severe space limitations (e.g., a very narrow mobile screen) may force the use of tall, thin bars. In these cases, the bias is a necessary trade-off.
- **Sparkbars/Sparklines:** When bars are used as part of a very small, dense visualization (like a sparkline in a table), the goal is to show the overall shape and pattern, not to judge individual bar heights accurately. The bias is less of a concern.
- **Labels are Primary:** If every bar has a clear, legible data label, the user can rely on reading the number супер to get the exact value, mitigating the perceptual bias from the bar's shape.

## Trade-offs

- **Aesthetics and Information Density:** Forcing bars to be square-like can dictate the overall dimensions of your chart, which might conflict with aesthetic goals or the available space. You may need to sacrifice some information density (fewer bars in the same space) to achieve a less-biased aspect ratio.

## Signs of Trouble

- **"Skyscraper" Bars:** The bars in your chart are extremely tall and skinny, resembling skyscrapers. Viewers are likely underestimating their values.
- **"Pancake" Bars:** The bars are very short and wide, like pancakes. Viewers are likely overestimating their values.
- **Inconsistent Judgments:** If you were to test users, you might find they consistently underestimate values in one chart and overestimate them in another, with the key difference being the bar aspect ratio.

## How to Improve

- **Quick Fix: Add Direct Labels.** If you cannot change the bar shapes, add clear data labels to the end of each bar. This gives the viewer a direct way to read the true value, acting as a corrective to any perceptual bias.

- **Moderate Redesign: Adjust Chart and Bar Dimensions.**
  - **Adjust bar width:** Most charting tools allow you to control the width of the bars or the padding between them. Widen thin bars or narrow wide bars.
  - **Adjust chart canvas:** Change the overall height and width of your chart to guide the bars toward a more square-like appearance.

- **Comprehensive Approach: Consider an Alternative Chart.** If you cannot create a bar chart without extreme aspect ratios, consider if a different chart type would work better. A **dot plot**, for example, is not subject to this same aspect ratio bias, as it uses position of a point rather than the length of a bar. It can be a more robust choice when dealing with awkward space constraints.
