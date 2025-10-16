---
id: use-indexed-scale-for-time-series
title: "Use an indexed scale to compare relative performance of time-series"

tags:
  - impact:perceptual
  - impact:performance
  - impact:ethos
  - chart:line
  - task:compare
  - task:trend
  - task:correlation
  - task:rank
  - data:quantitative
  - data:temporal
  - data:heterogeneous
  - visual:position
  - medium:interactive
  - medium:screen

evidence:
  strength: medium
  summary: "A 2011 study found that transforming time-series data to an indexed scale (e.g., starting all series at 100) led to significantly lower error rates for comparison tasks compared to using either logarithmic or linear scales. This method was also strongly preferred by 19 out of 24 users."

sources:
  - type: research
    ref: Aigner et al., 2011
    url: https://doi.org/10.1111/j.1467-8659.2010.01845.x
    note: "Found that indexing led to significantly higher task correctness (p < 0.001) for comparing time-series data versus both log-scale and linear-scale charts. It was also the most subjectively preferred visualization."
    role: primary

examples:
  - type: good
    description: "A line chart comparing several stock prices since the start of the year. The Y-axis is labeled 'Index (Jan 1 = 100)' and all lines start at the 100-mark. It is easy to see which stock has grown the most (the highest line at the end) and which was most volatile (the most jagged line)."
  - type: bad
    description: "A line chart comparing two stocks with very different prices (e.g., one at $500, one at $20) on a single linear Y-axis. It is impossible to tell which one had a higher percentage growth because the variations in the lower-priced stock are visually flattened."
---

## Guidance

When the primary goal is to compare the relative performance of multiple time-series, transform the data to an indexed scale. To do this, set a common starting point in time for all series to a base value (e.g., 100) and plot their subsequent values as a percentage of that base.

## Why

An indexed chart directly encodes the relative change from a common baseline, making it perceptually straightforward to compare performance. Viewers can judge performance simply by seeing which line is higher. This removes the need to mentally calculate percentage changes or interpret non-linear (logarithmic) scales, reducing cognitive load and leading to significantly more accurate judgments. This method is effective for both homogeneous (e.g., stocks) and heterogeneous (e.g., inflation vs. unemployment) data.

### Core Principle

Make the most important comparison the easiest to see. By directly encoding the comparison of interest (relative change), the visualization offloads mental work onto the perceptual system.

## When it applies

- When the primary task is to compare the performance or growth rate of several items from a specific point in time (e.g., "Which investment has grown the most since 2020?").
- When comparing time-series that have different absolute values (e.g., stock prices) or even different units (e.g., stock price vs. a market index).
- When communicating to a general audience, as an indexed scale is often more intuitive than a logarithmic scale.

## Exceptions

- When displaying absolute values is a primary requirement. Indexed charts completely obscure the original magnitudes. A viewer can't tell if a stock price is $10 or $1,000, only how it has changed relative to its starting point.
- When the choice of the index point (the "start date") can be misleadingly "cherry-picked" to support a specific narrative. The story can change dramatically depending on the start date chosen.

## Trade-offs

- **Clarity of Change vs. Loss of Magnitude:** Indexing provides a crystal-clear view of relative performance but completely hides the absolute values of the underlying series.
- **Simplicity vs. Potential for Deception:** While simple to read, the selection of the index point is a powerful editorial choice that can significantly alter the chart's message.

## Signs of Trouble

- **Misinterpreted Magnitudes:** Viewers misinterpret the indexed Y-axis values (e.g., "120") as absolute currency values (e.g., "$120"). This suggests the axis labeling is not clear enough.
- **Flawed Comparisons:** Viewers are trying to compare relative performance on charts with different scales (e.g., a dual-axis chart) or very different magnitudes on a linear scale, leading to incorrect conclusions.
- **Debates over the "Real" Trend:** If the chart's message is highly sensitive to the chosen start date, the index point may be contentious.

## How to Improve

- **Quick Fix: Add Callouts to a Linear Chart.** On a standard line chart, add text boxes or annotations that explicitly state the percentage change for each series from a common start date. This provides the indexed insight without altering the chart.

- **Moderate Redesign: Switch to a Logarithmic Scale.** For an audience comfortable with them, a log-scale chart can also show rates of change. However, comparisons are based on slope, which is less direct and accurate than comparing position on an indexed chart.

- **Comprehensive Approach: Implement an Indexed Chart.** Transform the raw data to create an indexed plot. Clearly label the Y-axis (e.g., "Index, where Jan 1, 2023 = 100") to prevent misinterpretation. In an interactive setting, consider allowing the user to select the index point to enable more flexible and transparent analysis.
