---
id: index-time-series-for-relative-change
title: "Index time-series to compare relative change"

impact:
  - perceptual
  - cognitive
  - logos
  - ethical
  - performance
tags:
  - line-chart
  - indexed-chart
  - time-series
  - comparison
  - trend-analysis
  - relative-change
  - different-scales
  - heterogeneous-data

sources:
  - type: research
    ref: Aigner et al., 2011
    url: https://doi.org/10.1111/j.1467-8659.2010.01845.x
    note: "Empirical study showing indexed charts lead to significantly lower error rates and are strongly preferred by users for comparing trends in multivariate time-series data."
  - type: practitioner
    ref: Financial Times Visual Vocabulary
    url: https://ft.com/vocabulary
    note: Lists the 'Index chart' as a standard chart type for comparing relative changes since a particular point in time.

tools:
  - type: learn
    name: "Datawrapper: How to create an index chart"
    url: https://academy.datawrapper.de/article/170-how-to-create-an-index-chart
    description: A practical tutorial on creating and interpreting indexed charts.

examples:
  - type: bad
    description: "Superimposing two stocks with vastly different price ranges (e.g., $20 vs. $200) on a linear scale. The relative changes of the lower-priced stock appear flat and are difficult to interpret, even if it had a higher percentage growth."
  - type: good
    description: "Indexing the same two stocks to a starting value of 100. It becomes immediately clear which stock had a higher percentage growth, as their relative performance is now directly comparable on the same scale."
---

## Guidance

To compare relative change or performance over time between two or more series, normalize them to a common starting point (e.g., 100) and plot them on a single indexed chart.

## Why

Overlaying time-series with different units (e.g., stock price vs. market index) or vastly different value ranges (e.g., a large company's revenue vs. a small one's) on a standard line chart can be misleading. The series with larger absolute values will visually dominate, obscuring the proportional changes in the others. Indexing transforms all series into a common, percentage-based scale, making their relative trends directly comparable. Studies show this leads to significantly more accurate comparisons and is strongly preferred by users.

## When it applies

- When the primary task is to compare the *rate of change* or *percentage growth* (e.g., "Which stock performed better?") rather than their absolute values (e.g., "Which stock has a higher price?").
- When comparing time-series with different units.
- When comparing time-series that share a unit but have drastically different scales.

## Exceptions

- When the primary task is to compare absolute values or the absolute gap between series. Indexing removes this information, making a standard line chart or a panel of charts more appropriate.
- If the chosen index point is an extreme outlier or not representative of a typical state, it can distort the perception of subsequent trends.

## Trade-offs

- **Loss of absolute values:** An indexed chart shows relative change, but you lose the ability to read the original values (e.g., the actual dollar price of a stock) from the y-axis. This can be mitigated with annotations or tooltips.
- **Emphasis on a single reference point:** The entire chart is anchored to the index point. Trends can look very different depending on whether you index from the beginning of the period, a market crash, or a market peak. The choice of this point is critical and should be clearly stated.

## Evaluate

- [ ] Multiple time-series with different units or very different scales are plotted on a single chart with a linear Y-axis.
- [ ] The trend of the series with smaller absolute values is difficult to discern because it appears as a nearly flat line.
- [ ] The user is asked to compare relative growth, but the chart only provides absolute values, forcing them to do mental math.

## Repair

1.  **Choose a meaningful index point.** This is usually the first data point in the time range, but could be another significant event date.
2.  **Rebase each series.** For each series, divide every value by the value at the index point and multiply by 100. This transforms all series to a starting value of 100.
3.  **Plot the new indexed series** on a single line chart. Clearly label the y-axis to indicate it represents an index and state the reference point (e.g., 'Index, Jan 1 2020 = 100').
4.  **(Optional) Add annotations or tooltips** that show the original absolute value on hover to recover some of the lost information.