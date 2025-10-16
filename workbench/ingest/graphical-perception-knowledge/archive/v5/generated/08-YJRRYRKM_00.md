---
id: superimpose-log-scale-time-series
title: "Superimpose time-series on a logarithmic scale for faster trend comparison"

tags:
  - impact:perceptual
  - impact:performance
  - chart:line
  - task:compare
  - task:trend
  - task:correlation
  - task:aggregate
  - data:quantitative
  - data:temporal
  - visual:position
  - visual:color
  - medium:interactive
  - medium:screen
  - access:cognitive-load-risk

evidence:
  strength: medium
  summary: "A 2011 study with 24 participants found that comparing time-series trends on a superimposed logarithmic scale was significantly faster than on a juxtaposed linear scale, with no loss in accuracy."

sources:
  - type: research
    ref: Aigner et al., 2011
    url: https://doi.org/10.1111/j.1467-8659.2010.01845.x
    note: "Found superimposing time-series on a log scale was significantly faster (p < 0.01) for comparison tasks than juxtaposing them on a linear scale, with no significant difference in error rate."
    role: primary

examples:
  - type: good
    description: "Two time-series with different value ranges are superimposed on a single chart with a logarithmic Y-axis. This allows for direct comparison of their relative growth rates, as equal slopes represent equal percentage changes."
  - type: bad
    description: "Two time-series are placed in separate, juxtaposed charts (small multiples) with linear Y-axes. Comparing trends requires the viewer to visually jump between the two charts and mentally account for the different scales and starting points, a slower and more cognitively demanding process."
---

## Guidance

When comparing the relative change (e.g., growth rate, volatility) between multiple time-series, superimpose them on a single line chart that uses a logarithmic Y-axis.

## Why

A logarithmic scale transforms multiplicative changes (e.g., a 10% increase) into constant visual distances, regardless of the absolute value. This makes it easier to visually compare percentage-based trends, as equal slopes represent equal percentage changes. Superimposing the lines brings them into close proximity, facilitating direct visual comparison and leading to significantly faster task completion.

### Core Principle

Visual encodings should match the structure of the task. For tasks involving multiplicative comparisons (rate of change), a logarithmic scale is more appropriate than a linear one.

## When it applies

- When the primary task is to compare relative changes, percentage growth, correlation, or volatility between two or more time-series.
- When the time-series have vastly different absolute value ranges (e.g., comparing the stock price of a large-cap company with a small-cap one).
- When the audience is focused on trends rather than absolute differences in magnitude.

## Exceptions

- When the primary goal is to compare absolute differences. A linear scale is required to accurately judge additive differences.
- When the audience is unfamiliar with or likely to misinterpret logarithmic scales. In such cases, a more explicit representation like an indexed chart or juxtaposed linear charts may be safer, despite being slower for comparison.
- When there are too many overlapping series, creating an unreadable "spaghetti plot". In this scenario, small multiples (juxtaposition) or highlighting specific series may be clearer.

## Trade-offs

- **Clarity vs. Familiarity:** Log scales are perceptually effective for showing relative change but can be less intuitive for general audiences who expect linear scales. This may increase cognitive load or risk of misinterpretation if not clearly labeled.
- **Speed vs. Potential Clutter:** Superimposition is faster for comparison but can become cluttered and illegible if too many lines are shown.

## Signs of Trouble

- **Misleading Slopes:** On a linear scale chart, you notice that a change from 10 to 20 (a 100% increase) has a much shallower slope than a change from 100 to 110 (a 10% increase). This visually misrepresents the rate of change.
- **"Flat" Line:** When comparing two series with different magnitudes on a linear scale, the series with the smaller value range appears almost flat, obscuring its volatility and trends.
- **Chart Hopping:** With juxtaposed (side-by-side) charts, you observe viewers' eyes constantly darting back and forth to make a single comparison, indicating high cognitive effort.

## How to Improve

- **Quick Fix: Add Annotations.** On a standard linear chart, add text annotations that explicitly state the percentage change for each series over a key period. This provides the relative information without changing the chart type.

- **Moderate Approach: Switch to Log Scale.** Change the Y-axis scale of your superimposed line chart from "linear" to "logarithmic." Ensure the axis is clearly labeled as a "logarithmic scale" to prevent misinterpretation.

- **Comprehensive Approach: Use an Indexed Chart.** Instead of showing absolute values, transform the data to show an indexed value (e.g., setting the start date for all series to 100). This directly plots the relative change and removes the need for audiences to interpret a log scale.