---
id: superimpose-lines-for-comparison
title: "Superimpose time-series lines on a single plot for direct comparison"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:line
  - chart:small-multiples
  - task:compare
  - task:trend
  - data:temporal
  - data:cardinality.low

sources:
  - type: research
    ref: "Aigner et al., 2011"
    url: "https://doi.org/10.1111/j.1467-8659.2010.01845.x"
    note: "The study compared a superimposed method (log scale) with a juxtaposed method (linear scale) and found the superimposed method was faster for comparison tasks, supporting the general principle of superimposition for direct comparison."

examples:
  - type: bad
    description: "Juxtaposing two line charts in small multiples requires the viewer to hold the pattern of the first chart in memory while examining the second, increasing cognitive load."
    url: /images/superimpose-juxtaposed.png
  - type: good
    description: "Superimposing the two lines on a single chart allows for immediate, direct comparison at any point in time. It is easy to see when one line is above the other or when their trends diverge."
    url: /images/superimpose-superimposed.png
---

## Guidance

For comparing a small number of time series (typically 2-5), plot them together on the same set of axes (superimposition) rather than in separate, adjacent charts (juxtaposition or small multiples).

## Why

Superimposition places all data in a shared visual space, allowing for immediate and direct comparison. Viewers can easily see which line is higher at any point, where trends cross, or how the gap between them changes over time. Juxtaposition requires viewers to hold information from one chart in memory while looking at another, which increases cognitive load and reduces the precision of comparisons.

## When it applies

- When the primary task is to directly compare the values or trends between a few time series.
- When the series share the same unit and a comparable scale (or can be made comparable via a log scale or indexing).

## Exceptions

- When there are too many lines (more than ~5), leading to a cluttered and illegible "spaghetti plot." In this case, juxtaposition (small multiples) is a superior approach.
- When the series use different units or have vastly different absolute scales that cannot be resolved with a log scale or indexing. Superimposing them would render the smaller-scale series illegible.

## Trade-offs

- Superimposition is highly efficient for direct comparison but scales poorly to many series.
- Juxtaposition scales to many more series but makes direct, point-in-time comparison less efficient.

## Signs of Trouble

- **"Spaghetti Plot":** The chart is an illegible tangle of overlapping lines, making it impossible to follow any single series or distinguish it from others.
- **Eye-Darting:** To compare two series, a viewer's eyes have to dart back and forth between two separate charts.
- **Unnecessary Separation:** Only two or three time series are being compared, but they are shown in separate small-multiple charts, making the comparison needlessly difficult.

## How to Improve

- **Quick Fix:** If you must use juxtaposition for a few series, ensure the y-axes and x-axes of all charts are perfectly aligned and use the exact same scale to make comparison easier.

- **Moderate Improvement:** If you have a cluttered superimposed plot with many lines, use color and line weight to highlight the 1-2 most important series and de-emphasize the rest by making them light gray.

- **Comprehensive Approach:** Use superimposition for 2-5 series. If you have more, switch to small multiples (juxtaposition). Consider creating an interactive version where the user can select or hover to highlight specific series.
