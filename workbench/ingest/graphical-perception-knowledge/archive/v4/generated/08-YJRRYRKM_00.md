---
id: use-log-scale-for-relative-change
title: "Use a log scale to compare relative changes in time-series data"

tags:
  - impact:perceptual
  - impact:performance
  - chart:line
  - task:compare
  - task:trend
  - data:temporal
  - data:quantitative
  - medium:screen
  - medium:print
  - access:cognitive-load-risk

sources:
  - type: research
    ref: "Aigner et al., 2011"
    url: "https://doi.org/10.1111/j.1467-8659.2010.01845.x"
    note: "The study found that using a log scale for superimposed time-series plots led to significantly faster completion times for percent estimation and trend comparison tasks compared to juxtaposed plots with a linear scale."

examples:
  - type: bad
    description: "On a linear scale, the same percentage growth (e.g., doubling) looks much smaller for the series with lower absolute values (blue line) than for the one with higher values (orange line). This misrepresents their relative performance."
    url: /images/log-scale-linear.png
  - type: good
    description: "On a log scale, the same percentage growth now has the same vertical distance and slope. It's now clear that the blue line had a higher rate of growth initially, a fact obscured in the linear scale version."
    url: /images/log-scale-log.png
---

## Guidance

When comparing the rate of change (e.g., percentage growth) between multiple time series, plot the quantitative values on a y-axis with a logarithmic scale.

## Why

A logarithmic scale transforms values so that equal vertical distances represent equal *percentage* changes, not absolute ones. This aligns the visual slope of the line with the rate of change, making trend comparisons more perceptually accurate and faster. On a linear scale, a 10% increase from 100 to 110 appears much steeper than a 10% increase from 10 to 11, which can be misleading when comparing relative growth.

## When it applies

- When the primary task is to compare the *rate of change* or relative performance between two or more time series.
- When the time series being compared have widely different absolute value ranges, which would cause the series with smaller values to appear flat and devoid of detail on a linear scale.

## Exceptions

- When the goal is to compare *absolute* differences between series, a linear scale is the correct choice.
- When the data contains zero or negative values, as these cannot be represented on a log scale.
- When the audience is not familiar with log scales, which can lead to misinterpretation of absolute magnitudes if not clearly labeled and explained.

## Trade-offs

- **Clarity for Relativities vs. Absolutes:** Using a log scale improves the accuracy of relative comparisons but makes it much harder to judge absolute differences between the series.
- **Expertise vs. Accessibility:** While more accurate for trend analysis, log scales can be less intuitive and increase cognitive load for non-expert audiences.

## Signs of Trouble

- **Flattened Series:** On a linear-scale chart, a time series with a lower absolute value range appears almost flat, obscuring its volatility and trends.
- **Misleading Slopes:** Two series with the same percentage growth rate have visibly different slopes simply because their absolute values are different.
- **Scale Dominance:** The fluctuations of a high-value series dominate the chart, making it difficult to properly analyze other series plotted on the same axes.

## How to Improve

- **Quick Fix:** In your charting tool, change the y-axis setting from "Linear" to "Logarithmic" or "Log."

- **Moderate Improvement:** After switching to a log scale, clearly label the axis as "Logarithmic Scale" and ensure gridlines correspond to powers of 10 (e.g., 10, 100, 1000) to help orient the viewer.

- **Comprehensive Approach:** For maximum clarity, consider "indexing" the data instead. This involves normalizing all series to a common starting value (e.g., 100) and plotting the percentage change directly. This is often more intuitive for a general audience than a log scale.
