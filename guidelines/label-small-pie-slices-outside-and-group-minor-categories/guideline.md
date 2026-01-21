---
id: label-small-pie-slices-outside-and-group-minor-categories
title: Move Small-Slice Labels Outside and Group Minor Shares
bibliography: references.bib
description: Improve pie chart readability by labeling small slices outside and combining
  minor categories into an 'others' slice.
labels:
- chart:pie
- task:label
- visual:annotation
- impact:clarity
- data:categorical
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

For pie charts, label small slices outside the pie (especially with long labels) and combine tiny categories into an “others” slice to reduce clutter. [@muth_pie_charts_2018]

## The Logic <!-- role: reason -->

Pie charts are hard to label cleanly; external labels and grouping reduce overlap and visual noise, and larger slices are easier to read and require fewer labels. [@muth_pie_charts_2018]

- **The Principle:** Reduce labeling friction and increase legibility by simplifying and externalizing annotations.
- **The Evidence:** [@muth_pie_charts_2018]

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Read category names and understand shares without fighting cramped labels. [@muth_pie_charts_2018]
- **Data Type:** Pie charts with small slices and/or long category names; distributions with a long tail of tiny categories. [@muth_pie_charts_2018]
- **Audience:** General audiences reading quickly, often on constrained layouts. [@muth_pie_charts_2018]

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** Every category must remain separate and explicitly listed (no grouping allowed).\
  **Reason:** An “others” slice would hide required detail; consider a different chart type instead. [@muth_pie_charts_2018]

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Grouping into “others” reduces category-level detail; outside labels can take more surrounding space. [@muth_pie_charts_2018]
- **The Risk:** Over-grouping can obscure meaningful minority categories; external labels can still get crowded if too many slices remain. [@muth_pie_charts_2018]

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Forcing all labels inside the pie, including tiny slices.\
  **Why it fails:** Pie charts are hard to label; small slices don’t leave enough room. [@muth_pie_charts_2018]
- **The Wrong Fix:** Keeping many tiny slices without grouping.\
  **Why it fails:** The overall look gets cluttered; smaller slices are harder to read and increase labeling needs. [@muth_pie_charts_2018]

## How to Check <!-- role: check -->

- **Visual Sign:** Overlapping text, leader lines everywhere, or illegible small labels crammed into thin slices. [@muth_pie_charts_2018]
- **The Test:** If you need to shrink label text to fit, or labels collide, move labels outside and/or group small categories. [@muth_pie_charts_2018]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move the smallest-slice labels outside the chart and shorten labels where possible. [@muth_pie_charts_2018]
- **Best Fix:** Combine minor categories into an “others” slice so the remaining slices are larger and require fewer, clearer labels. [@muth_pie_charts_2018]
