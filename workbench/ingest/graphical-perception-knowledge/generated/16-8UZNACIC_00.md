---
id: use-wrapped-charts-for-disproportionate-data
title: "Use wrapped bar charts for categorical data with disproportionate values"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:bar
  - task:compare
  - task:rank
  - task:lookup
  - data:categorical
  - data:quantitative
  - access:cognitive-load-risk
  - medium:static
  - medium:interactive

evidence:
  strength: medium
  summary: "Karduni et al. (2020) found in two crowdsourced experiments (n=98, n=190) that wrapped bar charts significantly improve accuracy for identifying small values and estimating large-to-small ratios in datasets with disproportionate values (e.g., low normalized entropy < 0.75). The technique increased accuracy for identifying the smallest bar by up to 35% (d=0.70)."

sources:
  - type: research
    ref: Karduni et al., 2020
    url: https://doi.org/10.1145/3313831.3376365
    note: "Two crowdsourced experiments (n=98, n=190) and an in-lab study (n=24) showed wrapped bars improve accuracy for identifying small values and estimating ratios in datasets with disproportionate values. The effect was strongest for datasets with low normalized entropy (< 0.75)."
    role: primary

examples:
  - type: bad
    description: "A standard bar chart where one value ('President Trump') is so large that all other values are compressed and nearly impossible to distinguish or compare accurately. This creates a high white-space-to-data ratio."
  - type: good
    description: "The 'Du Bois Wrapped Bar Chart' wraps the largest bar, allowing the y-axis to be rescaled. This makes the smaller bars visible and their relative differences discernible, improving comparison accuracy for those values."
---

## Guidance

Use a "wrapped" bar chart when visualizing categorical data where some values are so disproportionately large that they render smaller values difficult to see, compare, or estimate. This technique involves setting a threshold and wrapping any bar that exceeds it, allowing the y-axis to be scaled to the smaller values.

## Why

Standard bar charts can make small values nearly invisible when one or more values are orders of magnitude larger. This is because the y-axis must accommodate the largest value, compressing all smaller bars into a small fraction of the available space. Wrapping the large bars breaks them into segments, allowing the chart's scale to focus on the range of the smaller values. This makes them visible, legible, and comparable, significantly improving user accuracy in identifying the smallest values and estimating ratios between large and small values.

### Core Principle

Make all data points legible. A chart's design should not obscure a subset of the data due to the scale of other data points. Visual scaling should serve the entire dataset, not just the outliers.

## When it applies

- When visualizing categorical data using a bar chart.
- When the dataset contains one or more disproportionately large values that are orders of magnitude greater than the smallest values (e.g., data with low normalized entropy or high H-spread).
- When key analytical tasks include identifying the smallest values, comparing among small values, or estimating the ratio between the largest and smallest values.

## Exceptions

- When all values in the dataset are of a similar magnitude, making a standard bar chart sufficient.
- When the primary and most critical task for the user is to quickly and pre-attentively identify the single *largest* value. The wrapping technique adds cognitive load and time to this specific task.
- When the audience is completely unfamiliar with the convention and no tutorial or explanation is provided. The unconventional design could cause confusion.

## Trade-offs

- **Increased Cognitive Load:** Wrapped bars are less pre-attentive. Users must perform a mental calculation (counting wraps and adding the remainder) to determine the exact value of a large bar, which increases cognitive load and task completion time for those bars.
- **Reduced Accuracy for Largest Bar:** The added cognitive load can decrease accuracy and speed when identifying the largest bar, especially if multiple bars are wrapped multiple times.

## Signs of Trouble

- **Invisible Bars:** In a standard bar chart, some bars are so small they are barely visible, appear to be zero, or are indistinguishable from one another.
- **Vast Whitespace:** The chart area is dominated by empty space because the y-axis is scaled to accommodate a single, exceptionally large bar.
- **Inaccurate Ratio Judgements:** Viewers are unable to accurately estimate how many times larger the biggest bar is compared to the smallest ones, often resorting to pure guesswork.

## How to Improve

- **Quick Fix: Use a Log Scale.** If implementing a wrapped bar is not feasible, change the y-axis to a logarithmic scale. This can make all values visible but distorts the perceived magnitude of differences and requires a more numerate audience to interpret correctly.
- **Moderate Approach: Implement a Static Wrapped Bar Chart.** Convert the standard bar chart to a wrapped bar chart. To mitigate the cognitive load, add clear annotations, such as a label next to the wrapped bar indicating the number of wraps (e.g., "x5 wraps").
- **Comprehensive Approach: Implement an Interactive Wrapped Bar Chart.** Create a chart that allows users to toggle between a standard linear view and a wrapped view. In the wrapped view, provide tooltips on the wrapped bars that reveal their full value on hover. This gives the user control, combining the pre-attentive-glance value of a standard chart with the small-value detail of a wrapped chart.
