---
id: encode-deltas-for-comparison
title: "Directly encode value differences (deltas) to improve comparison tasks"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:bar
  - chart:dot-plot
  - chart:slopegraph
  - task:compare
  - task:direction
  - task:rank
  - data:quantitative
  - visual:length
  - visual:position
  - access:cognitive-load-risk
sources:
  - type: research
    ref: Nothelfer & Franconeri, 2020
    url: https://doi.org/10.1109/TVCG.2019.2934801
    note: "Across three experiments, directly encoding deltas improved performance for comparison tasks by 25-95% over showing individual values."
examples:
  - type: bad
    description: "In this grouped bar chart showing 'before' and 'after' scores, the viewer must mentally compare the height of two bars for each student to determine the change. This is slow and cognitively demanding."
  - type: good
    description: "This 'delta chart' directly encodes the change in score for each student. Increases are positive bars and decreases are negative bars. This makes comparing the magnitude and direction of change much faster and more accurate."
---

## Guidance

When the primary task for the viewer is to understand the relationship—the increase, decrease, or difference—between pairs of data values, create a chart that directly encodes that difference (the "delta") as a single visual mark.

## Why

The human visual system is slow and inefficient at perceiving the relationship between two separate visual marks (e.g., comparing the heights of two bars). This task requires serial attention, forcing the viewer to look back and forth, which increases cognitive load and leads to errors. By pre-calculating the delta and encoding it as a single mark (e.g., one bar representing the difference), you offload this mental work, making comparisons significantly faster, more accurate, and less effortful.

## When it applies

- When comparing pairs of values, such as before/after, treatment/control, projected/actual, or this year/last year.
- When the magnitude or direction of the change is more important for the user's task than the absolute values.
- When the viewer needs to quickly find specific relationships (e.g., find the biggest increase), judge proportions of relationships (e.g., are there more increases than decreases?), or estimate the average difference across all pairs.

## Exceptions

- When the absolute values are critical for context and cannot be omitted. For example, knowing whether a small change occurred on a large or small base value can be crucial, and a delta chart hides this information.
- When the primary task is to look up individual absolute values, not to compare the relationships between them.

## Trade-offs

- **Loss of Context:** Displaying only the deltas removes the context of the original absolute values. A +10% change looks the same whether it's from 10 to 11 or 100 to 110.
- **Screen Real Estate:** Showing a delta chart in addition to the original chart requires more space.

## Signs of Trouble

- **Slow Comparisons:** Viewers take a long time to answer questions like "Which category had the biggest increase?"
- **High Error Rates:** Viewers frequently make mistakes when ranking or judging the magnitude of differences between pairs.
- **Visual Ping-Pong:** You can observe viewers' eyes darting back and forth between the two bars or points they are trying to compare for each category.

## How to Improve

- **Quick Fix: Add Difference Labels.** Keep the original chart (e.g., a grouped bar chart), but add data labels that explicitly state the delta (e.g., `+$50` or `-10%`) for each pair. This provides a numerical escape hatch for the difficult perceptual task.

- **Moderate Approach: Use a Difference Overlay.** On the original chart, add a third mark like a connecting line, arrow, or bracket that visually represents the delta between the two primary marks. This technique is sometimes used in "difference-in-differences" plots.

- **Comprehensive Approach: Create a Delta Chart.** Replace or supplement the original chart with a new chart where the primary visual encoding (e.g., bar length or dot position) directly represents the calculated difference for each category. This is the most perceptually efficient method for comparison-focused tasks.
