---
id: encode-differences-directly
title: "Encode differences directly for faster and more accurate comparisons"

impact:
  - perceptual
  - performance
  - cognitive
  - logos

tags:
  - comparison
  - change
  - difference
  - bar-chart
  - dot-plot
  - delta-chart
  - performance
  - perception

sources:
  - type: research
    ref: Nothelfer & Franconeri, 2020
    url: https://doi.org/10.1109/TVCG.2019.2934801
    note: "Primary study demonstrating that directly encoding differences (deltas) improves comparison task performance by 25-95% across visual search, proportion, and averaging tasks."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "A review paper that collates and synthesizes graphical perception knowledge, including the findings from Nothelfer & Franconeri."

examples:
  - type: bad
    description: "A grouped bar chart shows 'before' and 'after' test scores. To see who improved and by how much, viewers must mentally compare the height of every pair of bars, a slow and error-prone process."
  - type: good
    description: "A bar chart directly plots the change in test scores (the 'delta') for each student. It's immediately obvious who improved (positive bars) or declined (negative bars) and by how much, making the comparison effortless."
---

## Guidance

When the main goal is for viewers to compare pairs of values (e.g., "before" vs. "after"), create a chart that directly visualizes the *difference* (or "delta") between them, rather than showing the two original values side-by-side.

## Why

The human visual system is "staggeringly inefficient" at mentally calculating differences between separate marks like bars or dots. It's a slow, sequential process that requires focusing on one pair at a time.

Directly encoding the difference transforms this difficult mental calculation into a simple perceptual task: reading a single value from one mark. This dramatically improves the speed (by up to 95%) and accuracy of comparisons.

## When it applies

- The primary task is to find, count, or average the **changes** or **relationships** between paired data points.
- You are comparing "before and after" states, two different treatments, or any other paired data where the difference is the key message.
- The exact magnitude of the original values is less important than the size and direction of the difference between them.

## Exceptions

- When the context of the original, absolute values is critical to the story. For example, if viewers need to know that a 10% increase happened on a base of 1,000, not a base of 10. Showing only the delta hides this original magnitude.
- When viewers need to perform tasks on the individual values themselves, such as finding the highest "after" value in a dataset.

## Trade-offs

- **Loss of Context:** Showing only the differences removes the viewer's ability to see the original absolute values, which can be crucial for a full understanding.
- **Increased Space:** A dedicated delta chart often requires additional space on a page or dashboard compared to a single grouped chart showing the original values.

## Evaluate

- [ ] A chart uses grouped bars, paired dots, or dual lines to show paired data (e.g., "Test Scores Before" and "Test Scores After").
- [ ] The chart's title, caption, or the user's most likely goal involves judging the *difference* between the pairs (e.g., "Which student improved the most?").
- [ ] Viewers must mentally subtract one value from another to understand the key message.

## Repair

1.  **Create a delta chart.** This is the most effective fix. Add a new chart that plots the calculated difference for each pair. Use length (a bar chart) or position (a dot plot) to represent the delta values, as these are easiest to perceive accurately.
2.  **Use a difference overlay.** If you must preserve the original values, consider overlaying the delta on the original chart (e.g., using an arrow or line to connect the "before" and "after" bars). This preserves context while still making the difference more explicit.
3.  **Improve grouping.** If you cannot change the chart type, ensure the paired values are placed immediately next to each other with minimal empty space. This reduces the cognitive load of the mental comparison, even if it doesn't eliminate it.