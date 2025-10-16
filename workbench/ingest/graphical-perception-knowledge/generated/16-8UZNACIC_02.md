---
id: avoid-extreme-bar-aspect-ratios
title: "Avoid extreme aspect ratios in bar charts to reduce perceptual bias"

tags:
  - impact:perceptual
  - impact:ethical
  - chart:bar
  - task:compare
  - task:summary-mean
  - data:quantitative

evidence:
  strength: medium
  summary: "Recent research reveals a systematic bias related to bar aspect ratios. A 2020 study by Ceja et al. found that viewers tend to underestimate the values of tall, thin bars and overestimate the values of short, wide bars. Bars with a roughly square aspect ratio showed no systematic bias. This contradicts earlier assumptions that bar chart perception was unbiased."

sources:
  - type: research
    ref: Ceja et al., 2020
    url: https://doi.org/10.1109/TVCG.2020.3031759
    note: "Experimental study that identified and quantified systematic bias in bar charts based on aspect ratio, finding underestimation for tall bars and overestimation for wide bars."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This review synthesizes the findings from Ceja et al. (2020) in Table 8, highlighting the conflict with previous work and establishing aspect ratio as a key factor in perceptual bias for bar charts."
    role: related

examples:
  - type: good
    description: "A bar chart where the bars have a moderate, roughly rectangular aspect ratio (neither extremely tall and skinny nor extremely short and wide). This minimizes the risk of perceptual over- or under-estimation."
  - type: bad
    description: "A bar chart that has been stretched to be very wide, resulting in short, wide bars. Viewers are likely to overestimate the values represented by these bars."
  - type: bad
    description: "A bar chart compressed into a narrow space, resulting in very tall, skinny bars. Viewers are likely to underestimate the values represented by these bars."
---

## Guidance

When creating bar charts, aim for moderate aspect ratios for the bars. Avoid designing charts that result in extremely tall, thin bars or very short, wide bars, as these shapes can introduce systematic perceptual biases.

## Why

While bar charts are generally effective, their accuracy is influenced by the aspect ratio of the bars themselves. Research has shown that viewers systematically underestimate the length of tall, skinny bars and overestimate the length of short, wide bars. This can lead to misinterpretation of the data, where the perceived differences do not match the actual differences in value. Bars with an aspect ratio closer to a square tend to be perceived most accurately, without systematic bias.

### Core Principle

The physical shape of a mark can influence the perception of the quantity it represents. An effective visualization minimizes such perceptual distortions to ensure the visual representation accurately reflects the underlying data.

## When it applies

- When designing any type of bar chart (vertical, horizontal, grouped, stacked).
- When the overall dimensions (height and width) of the chart are being determined, as this directly affects the aspect ratio of the individual bars.
- When accuracy of judgment is a high priority.

## Exceptions

- **Extreme Data Ranges:** If the data has an extremely wide range, it may be impossible to avoid tall bars without using other techniques like a log scale or wrapped bars. In this case, the trade-off may be necessary, but should be acknowledged.
- **Sparklines:** For very small, word-sized charts like spark-bars, the goal is to show overall shape and trend, not precise values. Extreme aspect ratios are inherent and acceptable in this context.

## Trade-offs

- **Layout Constraints:** Adhering to this guideline might require more horizontal or vertical space to maintain moderate aspect ratios, which may conflict with layout constraints (e.g., fitting a chart in a narrow column).
- **Number of Categories:** A chart with many categories will naturally have thinner bars if the total width is fixed. A designer must balance the number of visible categories with the ideal aspect ratio for each bar.

## Signs of Trouble

- **Pencil Bars:** The bars on your chart are extremely tall and thin, resembling pencils. Viewers may be underestimating their values.
- **Pancake Bars:** The bars are very short and wide, like pancakes. Viewers may be overestimating their values.
- **Inconsistent Scaling:** When resizing a chart, the bars become distorted into extreme aspect ratios, potentially changing the audience's perception of the data.

## How to Improve

- **Quick Fix: Adjust Chart Dimensions.** The simplest fix is to adjust the overall height and width of your chart container. Widen a chart with "pencil bars" or heighten a chart with "pancake bars" to bring the bar shapes closer to a moderate rectangle.
- **Moderate Approach: Reduce the Number of Bars.** If you have too many categories forcing bars to be too thin, consider grouping smaller categories into an "Other" category or using filtering to show only the most relevant bars.
- **Comprehensive Approach: Use Small Multiples.** Instead of putting 50 categories on one crowded chart with skinny bars, break the data into logical groups and create a series of smaller, well-proportioned bar charts. This allows each chart to maintain a reasonable aspect ratio while still presenting all the data.
