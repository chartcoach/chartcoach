---
id: use-event-striping-for-outliers
title: "Use event striping to highlight and count outliers in time series"
tags:
  - impact:perceptual
  - impact:performance
  - chart:custom
  - chart:heatmap
  - task:find-anomalies
  - data:quantitative
  - data:temporal
  - visual:color
  - visual:salience
  - medium:static
  - medium:screen
evidence:
  strength: medium
  summary: "In an experiment to find the month with the most outliers, a specialized 'event striping' design achieved 67% accuracy. This dramatically outperformed all other conventional designs, including line charts (37%), colorfields (31%), and composite charts (34%)."
sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "Primary experiment showing that a task-specific design that makes outliers salient is far more effective for outlier detection tasks."
    role: primary
---

## Guidance

When the main task is to identify and count outliers in a time series, use an "event striping" design where outlier data points are rendered with a highly salient visual mark (e.g., a bright, distinct color) on top of a more subdued representation of the rest of the data.

## Why

This design leverages the pre-attentive power of visual salience. By making outliers "pop" visually, it transforms the task from a slow, serial scan of every data point into a fast, parallel process of spotting and counting the distinct marks. It makes the information the user is looking for the most visually prominent element.

### Core Principle

To support a specific search task, make the target of the search the most visually salient element in the display.

## When it applies

- The primary analytical task is outlier detection, anomaly detection, or finding periods of unusual activity.
- You have a clear, pre-defined rule for what constitutes an outlier (e.g., values more than 2 standard deviations from the mean).

## Exceptions

- If every data point is of equal importance and there is no a priori definition of an "outlier," this method would not apply.
- If the goal is to understand the trend of the main body of data, this method can be distracting as it draws attention away from the "normal" values.

## Trade-offs

- **De-emphasis:** This technique necessarily de-emphasizes the non-outlier data, making it harder to perceive subtle trends in the "normal" range.
- **Definition-Dependent:** The effectiveness of the chart is entirely dependent on having a meaningful and appropriate definition of what constitutes an outlier.

## Signs of Trouble

- **Invisible Variation:** On a standard line or bar chart, the y-axis scale is so dominated by a few extreme outliers that the variation in the rest of the data is compressed into a flat line and is invisible.
- **Slow Detection:** Viewers are unable to spot or count outlier events without slowly and manually scanning the entire dataset.

## How to Improve

- **Quick Fix:** On a standard chart (like a scatter or line plot), simply change the color and/or size of data points that meet the outlier criteria to make them stand out.
- **Comprehensive Approach:** Implement a full event striping design. Render the main body of data as a smoothed, low-salience colorfield (heatmap) and overlay the outlier points as high-contrast, distinct marks (e.g., bright vertical lines or large dots).
