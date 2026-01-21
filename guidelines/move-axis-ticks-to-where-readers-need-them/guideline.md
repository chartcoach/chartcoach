---
id: move-axis-ticks-to-where-readers-need-them
title: Move Axis Ticks Toward the Data-Dense Side
bibliography: references.bib
description: Place axis tick labels on the side where readers are estimating values
  most often.
labels:
- chart:general
- task:estimate
- visual:text
- impact:clarity
- data:quantitative
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Place axis tick labels on the side of the chart where readers most need to estimate values (e.g., move y-axis labels from left to right if the important marks are on the right).

## The Logic <!-- role: reason -->

Reducing the distance between ticks and the marks they help interpret makes rough value estimation faster: readers can compare heights/positions with less scanning across empty space.

- **The Principle:** Reduce interpretation distance between scale and marks
- **The Evidence:** [@muth_text_in_data_visualizations_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly approximate values by comparing marks to ticks
- **Data Type:** Charts with axes (bars, lines, etc.) where key marks cluster on one side
- **Audience:** Any, especially readers scanning for “about how much” rather than exact values [@muth_text_in_data_visualizations_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart is used in a setting with strong conventions you must follow (e.g., a publication style that standardizes axis placement), and moving ticks would confuse more than help.
  - **Reason:** Convention violations can slow readers who rely on habitual scanning patterns [@muth_text_in_data_visualizations_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less standard layout; may require additional design adjustment.
- **The Risk:** Readers might momentarily search for the axis if they expect it on the usual side [@muth_text_in_data_visualizations_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Leaving ticks on the default side even when all salient marks are far away.
  - **Why it fails:** It forces unnecessary eye travel during value estimation [@muth_text_in_data_visualizations_2022].
- **The Wrong Fix:** Moving ticks but not checking collisions with labels/annotations.
  - **Why it fails:** Improves proximity but harms legibility [@muth_text_in_data_visualizations_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Readers must repeatedly look across the plot area to relate marks to tick labels.
- **The Test:** Identify the region with the most/most important marks; if ticks are farthest from that region, try swapping sides and compare reading speed [@muth_text_in_data_visualizations_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move the axis labels to the opposite side (left→right or bottom→top) when that side contains the key marks.
- **Best Fix:** Combine tick relocation with direct labeling/annotations so readers can estimate and identify without scanning back and forth [@muth_text_in_data_visualizations_2022].
