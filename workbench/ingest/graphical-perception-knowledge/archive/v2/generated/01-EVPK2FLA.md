---
id: use-linear-for-daily-patterns
title: "Use linear bar charts, not radial charts, for daily patterns"

impact:
  - perceptual
  - cognitive
  - logos
  - ethos
  - performance
tags:
  - bar-chart
  - radial-chart
  - rose-chart
  - polar-area-chart
  - time-series
  - cyclical-data
  - daily-patterns
  - comparison
  - read-value
  - find-extremum
  - general-public

sources:
  - type: research
    ref: Waldner et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934784
    note: "Found that a simple 24-hour linear bar chart was more accurate, efficient, and preferred than clock-like radial charts for visualizing daily patterns, even though the radial layout seems intuitively appealing."

examples:
  - type: bad
    description: A pair of 12-hour radial rose charts (one for AM, one for PM). This 'clock-like' design was found to be less accurate and slower to read than a simple linear bar chart.
  - type: good
    description: A single 24-hour linear bar chart. This format was found to be the most accurate, efficient, and user-preferred method for showing daily patterns.
---

## Guidance

For visualizing cyclical data over a day (e.g., hourly website traffic, accidents by hour), use a standard linear bar chart instead of a radial (rose or polar area) chart.

## Why

Despite the intuitive appeal of a "clock-like" display, research shows that people interpret linear bar charts more quickly, accurately, and with higher confidence. Radial charts, which use length or area on a polar axis, are harder for our brains to decode precisely and can lead to significant errors in reading values. A simple bar chart leverages our natural ability to easily compare lengths along a common, straight baseline, making it the clearer and more effective choice.

## When it applies

- You are visualizing time-series data that repeats on a daily cycle (a 24-hour period).
- The data is aggregated into discrete time units (e.g., hourly totals).
- Your audience is a general, non-expert group.
- Key tasks include reading specific values, finding the highest/lowest points, or comparing different time periods (e.g., morning vs. afternoon).

## Exceptions

- **When angle is the primary data variable.** For data where direction is inherently meaningful, such as wind direction, a radial layout can be appropriate. In this case, the angle encodes the data, not just the time period.
- **For aesthetic or artistic purposes.** In infographics or data art where visual appeal and engagement are prioritized over precise data interpretation, a radial layout might be chosen for its unique look. Be aware that this choice sacrifices clarity and accuracy.

## Trade-offs

- A linear bar chart may be perceived as less visually novel or "creative" than a circular radial chart.
- A long linear chart (e.g., 24 separate bars) can take up more horizontal space than a compact radial chart.

## Evaluate

- [ ] Data representing daily time-based patterns is displayed in a circular format (like a rose chart or polar area chart).
- [ ] The primary axis for time wraps around a circle instead of running along a straight line.
- [ ] Values are encoded as the length or area of segments radiating from a central point.

## Repair

1.  **Switch to a linear bar chart.** This is the most important fix. Change the chart type from a radial/rose chart to a standard bar chart.
2.  **Use a single, continuous time axis.** For showing overall patterns and helping users find the absolute highest or lowest point in a day, a single 24-hour axis is most effective.
3.  **If horizontal space is limited,** you can stack two 12-hour linear charts vertically (e.g., one for AM, one for PM). This is still preferable to a radial chart, but be aware it can make it slightly harder to spot the single highest point of the entire day.