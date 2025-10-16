---
id: prefer-position-length-for-comparisons
title: "Use position and length over slope for more accurate quantitative comparisons"

tags:
  - impact:perceptual
  - impact:performance
  - task:compare
  - task:rank
  - data:quantitative
  - visual:position
  - visual:length
  - visual:angle
  - chart:bar
  - chart:scatter
  - chart:line

evidence:
  strength: high
  summary: "Multiple studies, including a foundational 1984 paper and a 2020 replication, show that viewers compare values encoded by position (dot plots) and length (bar charts) more accurately and efficiently than values encoded by slope (slope graphs)."

sources:
  - type: research
    ref: Nothelfer & Franconeri, 2020
    url: https://doi.org/10.1109/TVCG.2019.2934801
    note: "Confirmed that position and length encodings are superior to slope for relational tasks, with search rates for slope being significantly slower."
    role: primary
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: https://doi.org/10.1080/01621459.1984.10478084
    note: "Foundational study establishing the perceptual ranking of visual channels, placing position and length above angle/slope for quantitative judgments."
    role: supporting

examples:
  - type: good
    description: "Bar charts use length to encode values, and dot plots use position. Both are highly effective for accurate comparisons, as confirmed by the research."
  - type: bad
    description: "Slope graphs use angle to encode the magnitude of change. While useful for showing direction, they are less precise for comparing the exact magnitude of change between different categories."
---

## Guidance

When encoding quantitative values for comparison tasks, prefer using visual channels like position (as in dot plots or line charts) or length (as in bar charts) over slope (as in slope graphs).

## Why

The human visual system is fundamentally better at precisely judging differences in position along a common axis and differences in length than it is at judging differences in angles or slopes. This perceptual hierarchy means that charts using position and length lead to faster, more accurate interpretation.

### Core Principle

Align your choice of visual encoding with the known strengths and weaknesses of human perception.

## When it applies

- When viewers need to accurately compare or rank quantitative values.
- When choosing between a bar chart, dot plot, or a slope graph to show changes between two points.
- When precision in judging magnitude is more important than showing a general trend.

## Exceptions

When the primary task is specifically to compare **rates of change**. In this case, slope is the most direct and appropriate representation of the data, even if it is less perceptually precise for comparing absolute magnitudes.

## Trade-offs

- **Space Efficiency:** Slope graphs can be very space-efficient for showing changes for many categories between two time points. Opting for a bar or dot plot may require more horizontal or vertical space.
- **Focus:** Slope graphs are excellent at drawing attention to the direction of change (increase/decrease) and rank-ordering, but at the cost of comparing the magnitude of those changes.

## Signs of Trouble

- **Imprecise Judgments:** Viewers struggle to determine which of two similar-looking slopes represents a larger change.
- **High Error Rate:** When tested, viewers have a high error rate in ranking the magnitude of changes represented by slopes.
- **Slow Performance:** It takes viewers significantly longer to perform comparison tasks with slope charts compared to bar charts or dot plots.

## How to Improve

- **Quick Fix: Add Labels.** If you must use a slope graph for its compactness, add direct labels showing the exact value or the amount of change to mitigate the perceptual inaccuracies of judging slopes.

- **Moderate Approach: Switch to a Dumbbell Chart.** A dumbbell chart uses two dots (position) for the start and end values, connected by a line (length). This design leverages two stronger perceptual cues—the position of the dots and the length of the connecting line—to make comparisons easier.

- **Comprehensive Approach: Use a Bar or Delta Chart.** Switch to a grouped bar chart to show the two values using length, or create a separate delta chart that uses length to show the difference. These methods provide the most perceptually accurate way to compare the magnitudes.
