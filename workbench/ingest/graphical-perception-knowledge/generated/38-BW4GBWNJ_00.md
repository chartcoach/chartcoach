---
id: avoid-bar-charts-for-mean-estimation
title: "Avoid bar charts when the primary task is judging an average"

tags:
  - impact:perceptual
  - impact:ethical
  - impact:cognitive
  - chart:bar
  - task:summary-mean
  - data:quantitative
  - visual:length
  - audience:general
  - medium:static
  - access:cognitive-load-risk

evidence:
  strength: medium
  summary: "Godau et al. (2016) found in a series of experiments (n=53, plus replications with n=38, n=80) that viewers systematically and significantly underestimate the average value of data presented in bar charts (p<0.001). This bias was robust across different testing methods and persisted even with outliers."

sources:
  - type: research
    ref: Godau et al., 2016
    url: https://doi.org/10.1016/j.chb.2016.01.036
    note: "Primary study demonstrating a systematic underestimation bias for the mean in bar charts across three experiments. The effect was significant (p < .001) and did not occur with point plots."
    role: primary

examples:
  - type: bad
    description: "A bar chart is used to show the average pollution level for several cities. If the author's goal is to communicate the high overall average, viewers will likely perceive it as lower than it actually is, undermining the message."
  - type: good
    description: "The same pollution data is shown using a dot plot. Viewers can now form a more accurate, unbiased perception of the overall average pollution level across the cities."
---

## Guidance

When the primary goal is for your audience to perceive the overall average of a set of values, avoid using a bar chart.

## Why

Humans have a systematic perceptual bias to underestimate the average of values shown in a bar chart. This occurs because our attention may be drawn to the center of the bars' area rather than the top edge that actually encodes the value. This leads to a consistent and significant underestimation of the true average, which can mislead the audience about the overall level of the data.

### Core Principle

The visual "weight" or shape of a mark can bias perception away from the specific element that encodes the data. For bars, the large filled area distracts from the top edge, biasing the perceived average downwards.

## When it applies

- When showing a series of quantitative values (e.g., performance across several categories, survey results across different groups).
- When a key takeaway message for the audience is understanding the "overall" level, central tendency, or average of those values.

## Exceptions

- If the primary task is to compare the values of individual bars to each other, or to look up the value of a specific bar, a bar chart can still be effective. This guidance is specific to the task of judging the *aggregate average* of the group of bars.

## Trade-offs

- Bar charts are very familiar to a general audience. Avoiding them for this task in favor of a more perceptually accurate chart (like a dot plot) may require a moment more for the audience to orient themselves.

## Signs of Trouble

- **Chart Choice:** You are using a bar chart and your main narrative point is about the "overall average" of the values, but you have not taken steps to counteract the underestimation bias.
- **Audience Feedback:** Viewers' qualitative takeaways seem to consistently understate the central tendency of the data you've presented (e.g., "The numbers seem pretty low overall" when the average is actually moderate or high).

## How to Improve

- **Quick approach:** Add a prominent reference line explicitly marking the average value on the chart. Label it clearly (e.g., "Average: 54.3"). This provides a strong visual anchor that helps counteract the perceptual bias, though it doesn't eliminate the initial biased impression.

- **Comprehensive approach:** Change the chart type to a dot plot (also known as a strip plot). Dot plots encode values using position (a single point) rather than length (a bar), and research shows they do not suffer from the same underestimation bias for judging averages. This is the most effective way to ensure an accurate perceptual takeaway.
