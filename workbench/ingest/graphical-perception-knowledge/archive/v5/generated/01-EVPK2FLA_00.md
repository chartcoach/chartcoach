---
id: use-linear-for-daily-patterns
title: "Use linear bar charts over radial charts for visualizing daily time patterns"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:bar
  - chart:pie
  - data:temporal
  - data:periodicity.24h
  - task:compare
  - task:lookup
  - task:find-extremum
  - task:rank
  - audience:general
  - medium:static
  - medium:screen
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "A 2020 crowd-sourced study with 92 users found that a 24-hour linear bar chart was significantly more accurate, faster, and subjectively preferred for visualizing daily patterns compared to radial (rose) charts."
sources:
  - type: research
    ref: "Waldner et al., 2020"
    url: https://doi.org/10.1109/TVCG.2019.2934784
    note: "Found that linear charts consistently outperform radial (rose) charts in accuracy, efficiency, and user preference for tasks involving daily cyclical data. The 24-hour linear bar chart was the top performer across all low-level tasks."
    role: primary
examples:
  - type: good
    caption: 24-Hour Linear Bar Chart
    description: "A continuous 24-hour linear bar chart. This format was found to be the most accurate, efficient, and preferred by users for all low-level analytical tasks."
    url: https://i.imgur.com/G5iC7R5.png
  - type: bad
    caption: 12-Hour and 24-Hour Radial (Rose) Charts
    description: "Radial charts were found to be significantly slower, less accurate, and less preferred. Users found them confusing and difficult to interpret, despite the apparent 'clock' metaphor."
    url: https://i.imgur.com/Wp7bXg4.png
---
## Guidance

For visualizing cyclical data like daily patterns, prefer a standard linear bar chart over a radial (or "rose") chart.

## Why

Linear charts are faster to read, more accurate for common tasks, and preferred by general audiences. They leverage our ability to accurately compare lengths from a common baseline. In a 2020 study, users performed all analytical tasks (locating time, reading values, finding the maximum, and comparing values) significantly faster and more accurately with linear charts. Radial layouts, by contrast, were often described as confusing and led to significant interpretation errors.

### Core Principle
Humans judge quantities more accurately by comparing positions or lengths along a common, straight scale than by comparing lengths or angles on a radial axis.

## When it applies
- When displaying time-series data with a daily (24-hour) cyclical pattern.
- When the audience is a general one, without specialized training in reading radial charts.
- When the primary goals include accuracy and speed for tasks like comparing values, looking up specific times, or identifying peaks.

## Exceptions
- **Aesthetic focus:** Radial layouts might be considered for non-analytical purposes where aesthetic appeal or engagement is the primary goal and data accuracy is secondary (e.g., in data art).
- **Domain convention:** They may be appropriate for specialized domains where they are a conventional form, such as visualizing wind direction (a wind rose).

## Trade-offs
- A linear bar chart may be perceived as less novel or visually engaging than a radial chart.
- A long linear chart may require more horizontal space, whereas a radial chart is more compact.

## Signs of Trouble
- **Audience Confusion:** Users report the chart is "confusing," "hard to read," or "unusual."
- **Task Errors:** When asked to find the highest value or compare two times of day, users make frequent errors. For example, the 12-hour radial chart had an error rate of 41% for reading a specific value.
- **Slow Performance:** It takes users significantly longer to complete simple tasks. For example, reading a value took over twice as long with a 12-hour radial chart compared to a 24-hour linear chart.

## How to Improve
- **Quick Fix: Add Direct Labels.** If a radial chart must be used, add direct data labels to each segment. This provides a "perceptual escape hatch," allowing users to read values directly instead of relying on flawed angle and length judgments.
- **Comprehensive Redesign: Switch to a Linear Bar Chart.** The most effective improvement is to change the chart type to a standard linear bar chart, preferably a continuous 24-hour one. This directly addresses the root perceptual and cognitive issues, resulting in higher accuracy, faster performance, and better user satisfaction.