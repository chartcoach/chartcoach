---
id: use-explicit-extrema-for-range-comparison
title: "Explicitly mark extrema to help users compare ranges"
tags:
  - impact:perceptual
  - impact:performance
  - chart:box-plot
  - chart:line
  - task:determine-range
  - task:compare
  - data:temporal
  - audience:general
  - medium:screen
evidence:
  strength: medium
  summary: "For the task of comparing the value range (max-min) within time periods, Albers et al. (2014, n=64) found that charts explicitly encoding extrema were most effective. Modified stock charts (92% accuracy) and box plots (89% accuracy) significantly outperformed standard line graphs (74%) where the extrema had to be found manually (p < .0001)."
sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "Found that making the minimum and maximum values for each period perceptually salient (via stock chart bars or box plot whiskers) dramatically improved accuracy on a range comparison task compared to a standard line graph (p < .0001)."
    role: primary
---
## Guidance

When users need to compare the range of values (the difference between the maximum and minimum) across different categories or time periods, use a chart that explicitly marks the extrema, such as a modified stock chart or a box plot.

## Why

In a standard line chart, comparing ranges requires a user to perform a multi-step mental process for each period: scan to find the peak, scan to find the trough, mentally subtract the two, hold the result in working memory, and then repeat for all other periods. This is slow and error-prone. Charts that explicitly mark the extrema make the key components of the range (the min and max values) perceptually salient, simplifying the task to comparing the distance between two visible marks.

## When it applies

- The user's task is to identify which category or time period has the largest or smallest difference between its highest and lowest value.
- This is distinct from comparing spread/variance, which considers all points. Range is only concerned with the two extreme points.

## Exceptions

- If the data is very noisy, the range might be determined by outliers and not be a meaningful representation of the data's typical behavior. In this case, comparing spread using a box plot (which shows interquartile range) is more robust.

## Trade-offs

- Modified stock charts and box plots add visual clutter compared to a simple line chart.
- These chart types are optimized for range/distribution tasks and may be less effective for judging the overall shape of the trend compared to a standard line chart.

## Signs of Trouble

- **Slow Task Completion:** Users take a very long time to answer questions about which period had the greatest range.
- **Inaccurate Comparisons:** When viewing a line chart, users frequently choose the wrong period as having the largest range.
- **Conflating Maximum with Range:** Users incorrectly assume the period with the highest peak value also has the largest range.

## How to Improve

- **Quick Fix: Highlight the Min/Max Points.** On a standard line chart, add distinct markers (e.g., dots) for the minimum and maximum point in each period. This helps guide the user's eye but still requires them to estimate the distance.
- **Moderate Redesign: Use a Box Plot.** Replace the line chart with a series of box plots. The distance between the ends of the whiskers directly visualizes the range for each period, making comparison straightforward.
- **Comprehensive Approach: Use a Modified Stock Chart.** Augment the line chart with explicit visual marks (e.g., horizontal bars) for the min and max of each period. This retains the continuous trend information from the line while adding highly effective support for the range comparison task.
