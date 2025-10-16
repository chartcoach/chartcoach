---
id: prefer-bars-over-pies-for-comparisons
title: "Prefer bar charts over pie charts for making comparisons"
tags:
  - impact:perceptual
  - chart:bar
  - chart:pie
  - task:compare
  - task:rank
  - data:quantitative
  - data:composition
evidence:
  strength: high
  summary: "Foundational research by Cleveland & McGill (1984), replicated by Heer & Bostock (2010) and summarized in Zeng & Battle (2023), established a perceptual hierarchy where humans judge position along a common scale (bar charts) more accurately and efficiently than angle or area (pie charts)."
sources:
  - type: research
    ref: Cleveland & McGill, 1984
    url: https://doi.org/10.1080/01973533.1984.10648834
    note: "Original study establishing the perceptual hierarchy of visual encodings, finding position > length > angle."
    role: primary
  - type: research
    ref: Heer & Bostock, 2010
    url: https://doi.org/10.1145/1753326.1753357
    note: "Crowdsourced replication confirming Cleveland & McGill's findings that bar charts lead to more accurate comparisons than pie charts."
    role: supporting
  - type: research
    ref: Zeng & Battle, 2023
    note: "Review paper summarizing this well-established finding (see Section 5.2.3, p. 10)."
    role: supporting
tools: []
examples: []
---

## Guidance

When the primary task is to compare or rank the values of different categories, use a bar chart instead of a pie chart.

## Why

The human visual system is much more accurate at judging and comparing lengths from a common baseline (the core mechanic of a bar chart) than it is at judging angles, arcs, or areas (the core mechanics of a pie chart). This makes comparisons in bar charts easier, faster, and less error-prone.

### Core Principle

Humans judge quantities more accurately by comparing positions along a common scale than by comparing angles or areas. Designs should use visual encodings that are highest on the perceptual hierarchy for the most important tasks.

## When it applies

- When comparing the magnitude of different categories (e.g., "Which region had the most sales?").
- When ranking categories from smallest to largest.
- When the precise difference between categories is important to communicate.

## Exceptions

- When showing a part-to-whole relationship with very few (2-3) and highly distinct slices (e.g., 75% vs 25%), and the goal is to emphasize the simple composition rather than precise comparison. Even then, a stacked bar chart is often a better alternative.
- In some rare cases for retrieve value tasks, pie charts can perform adequately if the goal is to read the value of a single, clearly labeled slice.

## Trade-offs

- **You gain:** Significantly improved accuracy, speed, and confidence in comparing and ranking values.
- **You sacrifice:** A pie chart can more immediately signal that the data represents parts of a whole. A bar chart requires a title or other context to make this compositional relationship clear. However, the gain in comparative accuracy usually outweighs this minor loss.

## Signs of Trouble

- **Many Slices:** A pie chart with more than 4-5 slices becomes almost impossible to read accurately.
- **Similar Values:** It is very difficult to tell which slice is larger when their values are close (e.g., 23% vs. 25%).
- **Ranking Difficulty:** Viewers struggle to rank the slices from largest to smallest without painstakingly reading every data label.
- **3D or Exploded Slices:** Using 3D perspective or exploding slices further distorts the areas and angles, making perception even less reliable.

## How to Improve

- **Quick Fix: Add Direct Labels.** If you must use a pie chart, add direct data labels (values and/or percentages) to each slice. This allows viewers to read the values, providing an escape hatch from relying on flawed perceptual estimation.

- **Moderate Redesign: Sort the Slices.** Order the pie chart slices from largest to smallest (usually starting at the 12 o'clock position and going clockwise). This helps slightly with ranking but doesn't solve the core perceptual issue of comparing similar-sized slices.

- **Comprehensive Redesign: Switch to a Bar Chart.** The most effective solution is to convert the pie chart to a bar chart. To make ranking and comparison effortless, sort the bars in descending or ascending order.
