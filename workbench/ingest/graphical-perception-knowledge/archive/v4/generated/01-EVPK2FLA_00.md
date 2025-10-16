---
id: use-linear-layouts-for-daily-time-series
title: "Use linear layouts over radial layouts for visualizing daily time-series data"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:bar
  - chart:radial
  - chart:rose-chart
  - task:compare
  - task:lookup
  - task:rank
  - task:find-extremum
  - data:temporal
  - data:periodicity.24h
  - visual:position
  - visual:length
  - visual:angle
  - visual:area
  - audience:general
  - medium:screen
  - medium:static
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Waldner et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934784
    note: "A crowd-sourced experiment with 92 non-expert users found that linear bar charts were more accurate, faster, and subjectively preferred over radial rose charts for analyzing daily patterns across four low-level tasks."

examples:
  - type: good
    caption: A 24-hour linear bar chart
    description: This 24-hour linear bar chart was the most accurate, efficient, and preferred visualization in the study. All bars share a common baseline, making length judgments for value lookups and comparisons easy and reliable.
    url: /images/waldner-2020-fig3.png
  - type: bad
    caption: A 12-hour radial rose chart
    description: This radial chart, meant to evoke a clock face, was the worst-performing design. Users found it confusing, difficult to read, and were slower and less accurate. Value comparisons rely on less precise angle and area judgments.
    url: /images/waldner-2020-fig1a.png
---

## Guidance

For visualizing daily time-series data for a general audience, use a linear bar chart instead of a radial (or "rose") chart.

## Why

Humans are significantly faster and more accurate at judging position and length along a common, straight axis (used in linear bar charts) than they are at judging angles and areas (used in radial charts). A study by Waldner et al. (2020) found that even for daily data where a "clock" metaphor might seem intuitive, linear charts performed better across all analytical tasks and were strongly preferred by users. Users reported that radial charts were "confusing" and "hard to decipher," sometimes leading to fundamental misinterpretations of the data.

## When it applies

- **Task:** When viewers need to perform low-level analytical tasks like looking up values, comparing values, or finding the maximum value.
- **Audience:** Especially relevant for a general, non-expert audience who may not be familiar with uncommon chart types.
- **Data:** For periodical time-series data, specifically daily (24-hour) patterns.

## Exceptions

- **Aesthetics over Analytics:** If the primary goal is to create an aesthetically engaging or "fancy" infographic where analytical precision is secondary, a radial chart might be considered. However, this comes at a high risk of misinterpretation.
- **Directional Data:** The authors speculate that for cyclical data that is inherently directional (e.g., wind direction), a radial layout may be beneficial, although this was not tested.

## Trade-offs

- **Clarity vs. Engagement:** You may sacrifice some perceived aesthetic appeal or "fun" that some users associate with novel radial designs. However, you gain significant improvements in clarity, speed, accuracy, and user confidence.

## Signs of Trouble

- **User Confusion:** Users express that the chart is "confusing," "hard to read," or that they don't understand how to interpret the bar lengths.
- **Slow Performance:** It takes users a long time to answer simple questions about the data, such as "Which hour had the most accidents?"
- **High Error Rates:** Users make frequent mistakes when reading values or comparing them. The study found error rates as high as 41% for reading a value from a radial chart, compared to 14% for a linear one.
- **Fundamental Misreading:** Users misinterpret the scale, for instance by assuming a grid line represents a different value than it does, a common issue with radial charts.

## How to Improve

- **Quick Fix: Add Direct Labels.** If you must use a radial chart, add direct data labels to each segment. This provides an escape hatch for users to read the exact value instead of relying on flawed perceptual judgments of angle or area.

- **Comprehensive Redesign: Switch to a Linear Bar Chart.** The most effective solution is to change the chart type. Convert the radial chart into a standard linear bar chart. This aligns all data points to a common baseline, leveraging the most accurate visual channel (position/length) for comparison. The 24-hour continuous linear bar chart was the top performer in the study.