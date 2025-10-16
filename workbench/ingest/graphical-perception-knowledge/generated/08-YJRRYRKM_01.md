---
id: use-indexing-for-relative-comparison
title: "Use indexing to accurately compare relative changes across multiple time series"

tags:
  - impact:perceptual
  - impact:ethical
  - chart:line
  - task:compare
  - task:trend
  - task:correlation
  - data:temporal
  - data:quantitative
  - medium:screen
  - medium:interactive
  - audience:general

evidence:
  strength: medium
  summary: "Aigner et al. (2011, n=24) found that indexing time series data significantly reduced comparison errors (p<0.001) compared to both juxtaposed linear charts and superimposed log-scale charts. It was also strongly preferred by 79% of participants."

sources:
  - type: research
    ref: Aigner et al., 2011
    url: https://doi.org/10.1111/j.1467-8659.2010.01845.x
    note: "The study (n=24) showed indexing resulted in significantly higher task correctness (Friedman test, χ² = 21.59, p < 0.001). Post-hoc tests confirmed indexing was more accurate than both juxtaposed linear charts (p < 0.001) and superimposed log-scale charts (p < 0.01). It was also the most subjectively preferred method."
    role: primary

examples:
  - type: good
    description: "This chart uses indexing, setting a base date to 100. Both stock prices are transformed to show their percentage growth relative to that starting point. This makes it easy and accurate to compare their relative performance directly, even though their original prices were very different."
    url: "https://raw.githubusercontent.com/zeng-projects/database-of-graphical-perception/main/assets/images/Aigner2011-figure1d.png"
  - type: bad
    description: "This superimposed chart with a linear scale makes it nearly impossible to compare the relative performance of the two stocks. The trend of the lower-valued stock (blue line) is visually compressed and its growth appears minimal, which may be misleading."
    url: "https://raw.githubusercontent.com/zeng-projects/database-of-graphical-perception/main/assets/images/Aigner2011-figure1a.png"
---

## Guidance

To compare the relative development (percentage change) of multiple time series from a common point in time, transform the data by indexing. This involves setting a base date to 100 and calculating all other data points as a percentage of that base value.

## Why

Indexing normalizes different series to a common scale (percent change), enabling direct, superimposed comparisons of trends and relative growth with high accuracy. The method was found to significantly reduce user errors because it encodes the desired comparison—relative change—directly as position. It is particularly effective for comparing heterogeneous time series (e.g., stock price vs. an economic index) that have different units or vastly different scales.

### Core Principle

Make the most important comparison the easiest to see. By transforming data to show relative change, you are directly encoding the comparison of interest, reducing the cognitive work required by the viewer.

## When it applies

- When the primary goal is to compare the performance or trend of multiple time series relative to a specific starting point (e.g., "Which stock has grown more since the beginning of the year?").
- When comparing time series that have different units (e.g., dollars vs. index points) or vastly different value ranges, where a shared linear axis would be misleading.

## Exceptions

- When absolute values or absolute differences between the series are the most important information to convey. Indexing completely hides the original magnitudes.
- The choice of the index point (the baseline date) can dramatically alter the narrative. If there is no meaningful or neutral starting point, the method can be misleading. This choice must be made carefully and stated transparently.

## Trade-offs

- **Loss of absolute magnitude.** The chart no longer shows the original values, only the percentage change from the base date. A series with small absolute values can appear to have dramatic growth, which might be misleading without context.
- **Sensitivity to base date.** The entire visual story is anchored to the chosen starting point. A different base date can produce a very different-looking chart and support a different conclusion.

## Signs of Trouble

- **The "Flat Line" Problem:** On a standard multi-line chart, a series with small absolute values appears flat and its trend is impossible to discern, even if it has high percentage volatility.
- **Comparing Apples and Oranges:** You are trying to plot two series with completely different units (like temperature and population) on the same chart, making the shared y-axis meaningless.
- **Misleading Comparisons:** Viewers are looking at a chart with two line series starting at different y-values and incorrectly assuming that the series with the steeper visual slope has a higher growth rate.

## How to Improve

- **Quick approach:** Re-plot the data using an indexed scale. Clearly label the chart and the base date (e.g., "Performance since Jan 1, 2020; Jan 1, 2020 = 100"). Add a horizontal reference line at y=100 to make the baseline obvious.

- **Moderate approach:** Provide an interactive control that allows the user to change the base date for indexing. This allows for more flexible exploration and demonstrates how the narrative can change depending on the starting point.

- **Comprehensive approach:** To provide full context, pair the indexed chart with a secondary chart (e.g., a small multiple) that shows the absolute values of the series over the same period. This allows the viewer to see both the relative trend and the original context of magnitude.