---
id: use-log-scale-for-percent-change
title: "Use a logarithmic scale for faster percentage change comparisons in time series"

tags:
  - impact:perceptual
  - impact:performance
  - chart:line
  - task:compare
  - task:trend
  - data:temporal
  - data:quantitative
  - medium:screen
  - medium:interactive

evidence:
  strength: medium
  summary: "Aigner et al. (2011, n=24) found that using a log scale for superimposed line charts was significantly faster for percentage change comparison tasks than using juxtaposed linear scale charts (p<0.001), with no significant change in accuracy."

sources:
  - type: research
    ref: Aigner et al., 2011
    url: https://doi.org/10.1111/j.1467-8659.2010.01845.x
    note: "In a study with 24 participants, superimposed logarithmic charts (Lo+S) led to significantly faster completion times for percent estimation tasks compared to juxtaposed linear charts (Li+J), with `t(23) = 5.16, p < 0.001`. There was no significant difference in error rates (`p > 0.05`)."
    role: primary

examples:
  - type: good
    description: "This chart uses a logarithmic scale to show stock price changes. Equal vertical distances represent equal percentage changes, making it easy to compare the growth rates of Microsoft and Apple, even though their absolute prices are different."
    url: "https://raw.githubusercontent.com/zeng-projects/database-of-graphical-perception/main/assets/images/Aigner2011-figure1c.png"
  - type: bad
    description: "This chart uses a linear scale. It's difficult to compare the percentage growth of the two stocks. The visual change in the lower-valued stock (blue line) is compressed, making its volatility and growth rate hard to assess relative to the higher-valued stock."
    url: "https://raw.githubusercontent.com/zeng-projects/database-of-graphical-perception/main/assets/images/Aigner2011-figure1a.png"
---

## Guidance

Use a logarithmic y-axis when the primary task is to compare the *rate of change* (i.e., percentage change) between two or more time series on a single chart.

## Why

A logarithmic scale transforms constant percentage changes into constant slopes. This makes it perceptually easier and faster for viewers to compare growth rates across different series, especially when the series have different absolute magnitudes. Linear scales, in contrast, represent the same percentage change with different slopes depending on the value, making visual comparison of rates difficult and error-prone.

### Core Principle

Visual encodings should match the structure of the task. For multiplicative comparisons (like percentage change), use a logarithmic scale which is inherently multiplicative.

## When it applies

- When comparing the rate of change or relative growth of multiple time series.
- When time series with very different absolute values are superimposed on the same plot, and you want to give each series a fair visual representation of its own volatility and trend.

## Exceptions

- When the primary task is to compare absolute differences between series. A log scale obscures absolute magnitudes.
- When the data includes zero or negative values, which cannot be plotted on a logarithmic scale.
- If the target audience is known to be unfamiliar or uncomfortable with logarithmic scales, as it may lead to misinterpretation. In these cases, consider indexing instead.

## Trade-offs

- **Clarity of absolute values is lost.** It becomes difficult to judge the actual gap in values between two series.
- **Increased cognitive load for novices.** Users not trained to read log scales may misinterpret the y-axis, assuming it is linear.

## Signs of Trouble

- **The "Flat Line" Problem:** On a linear scale chart with multiple series, the one with the smallest absolute values appears as a nearly flat line at the bottom, even if it has high percentage volatility.
- **Misleading Slopes:** Viewers incorrectly interpret the visual slope on a linear scale as the rate of change, leading to flawed comparisons between high-value and low-value series.

## How to Improve

- **Quick approach:** In your charting tool, change the y-axis scale from "Linear" to "Logarithmic". Ensure the axis is clearly labeled as "Log Scale" to prevent misinterpretation.

- **Moderate approach:** In addition to using a log scale, provide annotations for key percentage changes (e.g., "+50%") to help guide the viewer and reinforce how the scale works.

- **Comprehensive approach:** If accuracy is more important than speed, or if you need to compare heterogeneous data, use indexing instead. Research shows indexing leads to even lower error rates than a log scale.