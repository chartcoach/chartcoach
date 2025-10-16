---
id: highlight-outliers-explicitly
title: "To help users find outliers, use a visualization that highlights them explicitly"

tags:
  - impact:perceptual
  - impact:performance
  - chart:custom
  - chart:line.annotated
  - chart:scatter.annotated
  - task:find-anomalies
  - data:quantitative
  - data:temporal
  - visual:color
  - visual:shape
  - audience:general

sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "An 'event striping' visualization, which used broad, salient color stripes to mark outlier days over a smoothed colorfield, was by far the most accurate (66.8%) method for the task of counting outliers, outperforming all other tested designs."

examples:
  - type: good
    description: In the 'event striping' chart from the study, outlier days are shown as thick, dark green vertical bands that stand out clearly from the background, making them easy to spot and count.
  - type: bad
    description: A standard line chart requires the user to scan the entire series and decide for themselves which points are 'unusual'. This is subjective and error-prone, and performed poorly (36.7% accuracy) on the outlier task in the study.
---

## Guidance

When the task is to identify and count outliers or anomalies in a time series, use a visualization that explicitly marks these points with a highly salient visual feature (e.g., a distinct color, shape, or size).

## Why

Finding outliers in a dense data series is a difficult visual search task. By pre-calculating which points are outliers and "boosting" them visually, you transform a difficult search-and-judge task into a simple perceptual pop-out task. The "event striping" visualization studied by Albers et al. (2014) did exactly this by representing outliers as thick, high-contrast stripes, making them immediately stand out. This design dramatically outperformed all other chart types that showed only raw data, demonstrating the power of explicitly mapping the target statistic (in this case, "outlier-ness") to a salient visual variable.

## When it applies

- The primary task is to detect, identify, or count anomalies, outliers, or unusual events.
- A clear statistical definition of what constitutes an "outlier" can be established (e.g., more than 2 standard deviations from the mean).
- The audience needs to quickly spot exceptions rather than analyze the entire dataset.

## Exceptions

- **Ambiguous Definition:** If the definition of an "outlier" is subjective and cannot be computationally determined, it's better to show the raw data and let the user apply their own domain knowledge to identify them.
- **Over-emphasis:** If outliers are common, explicitly highlighting all of them could clutter the visualization and obscure other patterns. In this case, it may be better to adjust the outlier threshold or use a chart type like a box plot that can handle them gracefully.

## Trade-offs

- **Context vs. Signal:** Devoting strong visual encoding to outliers may obscure the context of the non-outlier data. The event striping design mitigated this by showing the outliers on top of a smoothed representation of the main signal.
- **Requires Computation:** This approach requires a pre-processing step to identify which points are outliers, which may not be possible in all systems or with streaming data.

## Signs of Trouble

- **Missed Anomalies:** Users fail to notice critical but visually subtle spikes or dips in a standard line chart.
- **Subjective Disagreements:** When looking at a raw data chart, different users disagree on which points should be considered outliers.
- **Slow Detection:** It takes users a long time to scan a chart to find the data points they are looking for.

## How to Improve

- **Quick Fix: Add Markers to a Line Chart.** On an existing line chart, add a distinct symbol (e.g., a red 'X' or a larger circle) to mark data points that meet the outlier criteria.
- **Moderate Approach: Use Box Plots.** If the data is grouped by category or time, a series of box plots can automatically display outliers as individual points beyond the whiskers, making them easy to spot.
- **Comprehensive Approach: Design a Dedicated View.** Implement an "event striping" style visualization where outliers are rendered with a highly salient feature (like a different shape or a bright, high-contrast color) that makes them pop out from the rest of the data.