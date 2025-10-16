---
id: encode-deltas-for-comparison
title: "Directly encode differences (deltas) for comparison tasks"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:bar
  - chart:dot-plot
  - chart:line
  - task:compare
  - task:rank
  - task:filter
  - task:aggregate
  - task:direction
  - data:quantitative
  - visual:position
  - visual:length
  - medium:static
  - medium:screen
  - access:cognitive-load-risk

evidence:
  strength: medium
  summary: "Nothelfer & Franconeri (2020, n=39) found in three experiments that directly encoding the difference (delta) between two data points significantly improved performance over showing individual values. Benefits ranged from a 25% reduction in error to a 95% improvement in task speed, depending on the task."

sources:
  - type: research
    ref: Nothelfer & Franconeri, 2020
    url: https://doi.org/10.1109/TVCG.2019.2934801
    note: "Across three experiments (n=39), directly encoding deltas was significantly better than showing individual values for visual search (49-95% faster, p<0.001), proportion judgment (30% more accurate, p<0.001), and averaging (25% less error, p<0.001)."
    role: primary

---
## Guidance

Directly encode the difference (delta) between pairs of data values instead of showing the two individual values, especially when the primary task is to understand the relationship between them.

## Why

The human visual system is inefficient at perceiving relations between separate objects. It requires a slow, serial process of identifying each object, computing the relation, and then moving to the next. Explicitly encoding the delta transforms this difficult relational task into a simple perceptual task of reading a single value (e.g., the length of one bar), which is much faster and more accurate.

### Core Principle

Make the most important comparisons the easiest to see. Convert a complex cognitive calculation into a simple perceptual judgment.

## When it applies

- When the user's primary goal is to compare pairs of values (e.g., before vs. after, target vs. actual).
- When showing the magnitude or direction of change is more important than the absolute values.
- In charts like bar charts, dot plots, or slope graphs where pairs of values are being compared.

## Exceptions

- When the absolute values are critical context and cannot be removed (e.g., needing to know if a score changed from 90 to 95 vs. 10 to 15). In these cases, a difference overlay may be a better compromise than a separate delta chart.
- When the user needs to perform tasks on the individual values, not just the relationship between them.

## Trade-offs

- **Loss of Context:** Displaying only deltas removes the context of the original absolute values. You lose the baseline information.
- **Increased Space:** A separate delta chart can take up more dashboard real estate.

## Signs of Trouble

- **Back-and-Forth:** Viewers have to repeatedly look back and forth between two bars or points to judge the difference.
- **Mental Math:** Viewers are mentally subtracting values to understand the change.
- **Slow Task Performance:** It takes a long time for users to find a specific change or summarize the overall trend.

## How to Improve

- **Quick Fix: Add a Delta Annotation.** If you must keep a chart of individual values, add explicit text labels showing the difference (e.g., "+5%" or "-$20"). This provides a cognitive shortcut even if the perceptual task is hard.

- **Moderate Approach: Use a Difference Overlay.** On a grouped bar chart, overlay a mark (like a line or arrow) that explicitly shows the delta between the two bars. This preserves the absolute values while adding a direct encoding of the difference.

- **Comprehensive Approach: Create a Dedicated Delta Chart.** Replace or supplement the chart of individual values with a chart that directly plots the differences. For example, use a bar chart showing the net change for each category, centered on a zero baseline.
