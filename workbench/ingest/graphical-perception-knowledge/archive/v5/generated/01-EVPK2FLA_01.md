---
id: use-continuous-view-for-global-extrema
title: "Use a single, continuous chart to find global maximums or minimums"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:bar.small-multiples
  - chart:line.small-multiples
  - task:find-extremum
  - task:rank
  - data:temporal
  - data:periodicity.24h
evidence:
  strength: medium
  summary: "A 2020 study found that when data was split into two separate charts (e.g., for AM and PM), users made significantly more errors when finding the maximum value. They often selected the peak from only one chart, failing to identify the true global maximum."
sources:
  - type: research
    ref: "Waldner et al., 2020"
    url: https://doi.org/10.1109/TVCG.2019.2934784
    note: "Found that a single, continuous 24-hour chart was significantly faster and more accurate for finding the maximum value compared to two juxtaposed 12-hour charts. Separated charts had an error rate of 12-16%, while the continuous chart had a 0% error rate for this task."
    role: primary
examples:
  - type: good
    caption: Continuous 24-Hour Bar Chart
    description: "Displaying the full 24-hour cycle in a single, continuous view makes the global maximum (the tallest bar) easy to identify at a glance."
    url: https://i.imgur.com/G5iC7R5.png
  - type: bad
    caption: Separated 12-Hour Bar Charts
    description: "Splitting the data into two charts for AM and PM requires the user to find the peak in each chart and then compare them. This increases cognitive load and led to errors where users picked the wrong peak."
    url: https://i.imgur.com/39Q5H7F.png
---
## Guidance

When the primary task is to find the highest or lowest value in a dataset, display the data in a single, continuous view rather than breaking it into small multiples.

## Why

Splitting data into separate charts (e.g., juxtaposed charts for "AM" and "PM") increases cognitive load and the risk of error. Viewers may focus on only one chart and identify a *local* maximum, missing the true *global* maximum present in the other chart. A continuous view makes global patterns easier to spot and compare, leading to faster and more accurate performance.

### Core Principle
To facilitate global comparisons and pattern finding, present the entirety of the relevant data within a single, unified visual frame whenever possible.

## When it applies
- When a key task for the viewer is to identify the single highest or lowest point across an entire dataset (e.g., finding the peak hour for traffic over a full day).
- When using small multiples to break up a continuous sequence like a time series.

## Exceptions
- Small multiples are highly effective for tasks involving the comparison of overall shapes and patterns *between* the charts (e.g., "Is the morning rush hour shaped differently than the evening rush hour?").
- When screen space is severely limited and breaking the data is the only way to make it fit without excessive scrolling.

## Trade-offs
- A single continuous chart might become very long and require scrolling if the dataset is large, whereas small multiples can arrange data more compactly.
- Small multiples can make it easier to compare specific corresponding points (e.g., 8 AM vs 8 PM when stacked vertically) but make global comparisons harder.

## Signs of Trouble
- **Misidentified Peaks:** Users incorrectly identify the peak value because they only looked at one of the multiple charts. In the study, this happened in 12-16% of trials with separated charts.
- **Slow Performance:** Users take a long time to find the maximum because they must visually scan each chart individually and then mentally compare the peaks.

## How to Improve
- **Quick Fix: Add a Global Annotation.** If you must use small multiples, add a salient visual mark (e.g., a colored dot, an arrow) and a text annotation to explicitly highlight the global maximum across all charts.
- **Comprehensive Redesign: Combine into a Single Chart.** Re-plot the data as one continuous chart (e.g., a 24-hour bar chart instead of two 12-hour charts). This is the most direct and effective way to support the task of finding global extrema.