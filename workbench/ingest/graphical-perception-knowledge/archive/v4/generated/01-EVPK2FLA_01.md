---
id: prefer-continuous-charts-for-global-tasks
title: "Prefer a single, continuous chart over separated charts for global tasks"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:bar
  - chart:small-multiples
  - task:rank
  - task:find-extremum
  - data:temporal
  - data:periodicity.24h
  - audience:general
  - medium:screen
  - medium:static
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Waldner et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934784
    note: "The study found that a single, continuous 24-hour bar chart was more efficient for finding the maximum value than two juxtaposed 12-hour charts. Separated charts introduced errors where users selected the maximum from the wrong chart."

examples:
  - type: good
    caption: A single, continuous 24-hour chart
    description: This chart presents all 24 hours of data in a single, continuous view. This makes it easy to scan and identify the global maximum value across the entire day without error.
    url: /images/waldner-2020-fig3.png
  - type: bad
    caption: Two juxtaposed 12-hour charts for a.m. and p.m.
    description: The data is split into two separate charts for morning and afternoon. This requires the viewer to scan both charts and mentally compare their peaks to find the true daily maximum, increasing cognitive load and the risk of error.
    url: /images/waldner-2020-fig2.png
---

## Guidance

When the primary task is to identify global patterns (like the overall maximum value), present the data in a single, continuous chart rather than splitting it into multiple juxtaposed charts (e.g., small multiples).

## Why

Splitting a time series into multiple charts increases cognitive load. To find a global maximum, the viewer must first find the local maximum in each chart and then compare them. This multi-step process is slower and more error-prone. The Waldner et al. (2020) study found that when data was split into a.m. and p.m. charts, users sometimes made errors by selecting the maximum value from the incorrect chart (e.g., choosing the a.m. peak when the true daily peak was in the p.m. chart). A single, continuous chart allows for an immediate and accurate visual scan of all data.

## When it applies

- **Task:** When the main goal is to find global features like the overall maximum, minimum, or range of values across an entire dataset.
- **Chart Type:** Applies to both linear and radial charts, but the effect is particularly clear with linear bar charts.

## Exceptions

- **Task is Comparison:** If the primary task is to explicitly compare the two segments (e.g., "Compare morning rush hour to evening rush hour"), then juxtaposing them can be effective.
- **Space Constraints:** If horizontal space is extremely limited, vertically stacking two shorter charts might be a necessary compromise over one very long chart that requires scrolling.
- **Meaningful Segments:** If the data has distinct, meaningful segments (e.g., weekday vs. weekend) and the focus is on comparing the patterns within those segments, separation is justified.

## Trade-offs

- **Compactness vs. Clarity:** A single continuous chart may require more horizontal or vertical space than several smaller, wrapped charts.
- **Reading Order Bias:** The study noted a top-to-bottom reading bias with juxtaposed charts, where users paid more attention to the top (a.m.) chart. While this can be a drawback, it could also be used intentionally to guide attention to a specific segment.

## Signs of Trouble

- **Incorrect Global Peaks:** Users incorrectly identify the overall maximum or minimum because they only look at one of the separated charts.
- **Slow Comparison:** Users take a long time to answer questions that require comparing values between the different charts.
- **Underestimation:** When comparing values between two separate charts, users may underestimate the difference between them.

## How to Improve

- **Quick Fix: Add Visual Cues.** If charts must be separated, add a clear visual annotation (e.g., a label or arrow) that explicitly points out the global maximum across all charts to prevent misinterpretation.
- **Moderate Redesign: Improve Alignment.** For juxtaposed linear charts, ensure they are perfectly aligned (e.g., vertically stacked as in the study) to make comparison as easy as possible.
- **Comprehensive Redesign: Combine into One Chart.** The best solution for global tasks is to merge the separated charts into a single, continuous visualization. This eliminates ambiguity and reduces the cognitive steps required to find global patterns.