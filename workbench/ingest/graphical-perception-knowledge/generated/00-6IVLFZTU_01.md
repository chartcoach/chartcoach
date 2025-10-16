---
id: prefer-bars-over-pies-for-comparison
title: "Prefer bar charts over pie charts for making accurate comparisons"
tags:
  - impact:perceptual
  - impact:performance
  - chart:bar
  - chart:pie
  - chart:donut
  - task:compare
  - task:rank
  - data:quantitative
  - visual:position
  - visual:length
  - visual:angle
audience:
  - audience:general
medium:
  - medium:static
  - medium:interactive
evidence:
  strength: high
  summary: "Experiments by Cleveland & McGill (1984) and replicated by Heer & Bostock (2010) show that people judge length and position (bar charts) with significantly higher accuracy than angle (pie charts) for comparison tasks. Zeng & Battle's (2023) review confirms this is a foundational and widely accepted finding in graphical perception."
sources:
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: https://doi.org/10.2307/2288400
    note: "The original study demonstrated that comparisons based on position along a common scale (as in bar charts) are perceptually superior to those based on angle (as in pie charts)."
    role: primary
  - type: research
    ref: Heer & Bostock, 2010
    url: https://doi.org/10.1145/1753326.1753357
    note: "A large-scale replication confirmed that bar charts lead to lower error rates than pie charts for comparison tasks."
    role: supporting
  - type: research
    ref: Skau & Kosara, 2016
    url: https://doi.org/10.1109/TVCG.2016.2598532
    note: "Investigated the perceptual cues in pie charts, finding that people may use a combination of angle, area, and arc length, but that position-based charts remain superior for comparison."
    role: related
---
## Guidance
For tasks that require viewers to compare or rank the magnitude of different categories, use a bar chart or dot plot instead of a pie chart or donut chart.

## Why
Humans are much more accurate at judging and comparing lengths from a common baseline (as in a bar chart) than they are at judging and comparing angles or areas (as in a pie chart). Using a pie chart for comparison tasks increases cognitive load and leads to higher error rates, as small differences between slices are difficult to discern.

### Core Principle
Match the visualization type to the primary task. For comparison tasks, choose a chart that leverages the most accurate perceptual encoding (position/length).

## When it applies
- The primary goal is for the audience to compare the values of different categories.
- You need to show the ranking of categories.
- Accuracy of interpretation is a priority.
- You have more than 2-3 categories.

## Exceptions
- **Part-to-Whole Judgment:** When the primary goal is to show how a few parts make up a whole (e.g., "Category A is about 25% of the total"), and precise comparison between parts is not critical, a pie chart with 2-3 slices can be acceptable.
- **Value Retrieval:** One study (Redmond, 2019, cited in Zeng & Battle, 2023) found that pie charts can be accurate for simple `retrieve value` tasks, though this is not their typical use case.

## Trade-offs
- **Familiarity:** Some audiences are very accustomed to pie charts, and switching to a bar chart might feel less familiar, even if it's more effective.
- **Composition Focus:** Bar charts make it harder to see the part-to-whole relationship compared to a pie chart. A 100% stacked bar chart can be an alternative, but it removes the common baseline for most segments.

## Signs of Trouble
- **Many Slices:** The pie chart has more than 4-5 slices, making it cluttered and comparisons impossible.
- **Similar Slices:** The pie chart contains slices of very similar size, forcing the viewer to guess which is larger.
- **3D or Exploded Slices:** The use of 3D effects or exploding slices distorts the angles and areas, making accurate perception impossible.
- **Comparison Task:** The chart's caption or the presenter's narrative is focused on comparing categories (e.g., "Category A is larger than Category B").

## How to Improve
- **Quick Fix: Add Labels and Sort.** If you must use a pie chart, add direct percentage and value labels to each slice and sort the slices by size from largest to smallest. This allows users to read the values directly, bypassing the inaccurate angle comparison.
- **Moderate Redesign: Switch to a Bar Chart.** The most effective improvement is to convert the pie chart into a bar chart. This aligns all categories to a common baseline, making comparisons effortless and accurate.
- **Comprehensive Redesign: Choose the Best Chart for the Task.** Consider if a simple sorted table, a dot plot, or a lollipop chart might be even more effective, depending on the space constraints and the number of categories.