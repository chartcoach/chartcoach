---
id: use-pie-charts-only-for-a-few-slices-of-a-single-whole
title: Use pie charts only for a few slices of a single whole
bibliography: references.bib
description: Reserve pie charts for showing how one 100% total divides into a small
  number of shares.
labels:
- chart:pie
- task:part-to-whole
- visual:angle
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
---

## Use pie charts only for a few shares of one 100% total <!-- role: advice -->

Use a pie chart only to show how one total (100%) divides into a small set of categories. Keep the number of slices to five or fewer.

## Why pie charts break down as slices multiply <!-- role: reason -->

Pie charts rely on judging angles and areas, and they become harder to read as the display gets more crowded with slices and labels; they also cannot represent more than one total without forcing comparisons across separate pies.

**Mechanism:** As the number of categories increases, slices become thinner and labels compete for space, reducing readability and making comparisons between shares less reliable.

**Evidence:** Pie charts are framed as effective for showing how 100% divides into a few shares, and are recommended up to about five values for cleaner labeling and readability [@muth_pie_charts_2018].

**Notes:** This guideline is about chart scope (one whole, few parts), not about styling choices.

## When you have a single whole split into a small number of categories <!-- role: context -->

- **User Goal:** Understand how one total is divided across categories.
- **Task:** Read approximate shares rather than precisely rank many close values.
- **Data:** One part-to-whole breakdown that sums to 100%, with low category count (≤ five).
- **Chart Setting:** Space-constrained layouts where a compact part-to-whole graphic is helpful.
- **Audience:** General audiences who benefit from simple, low-clutter displays.
- **Success Criterion:** The reader can identify the main shares without struggling with labeling.

## When not to use a pie chart for part-to-whole <!-- role: exceptions -->

- **Break it when:** You need to show more than five categories. **Why:** Slices and labels become messy and harder to read [@muth_pie_charts_2018].
- **Break it when:** You need to compare two (or more) totals side by side (for example, two polls). **Why:** A single pie can only show one total, and multiple pies make comparisons harder [@muth_pie_charts_2018].

## Tradeoffs of restricting pies to few slices <!-- role: costs -->

**Sacrifice:** You may need to aggregate categories or switch chart types to include all groups. **Risk:** Over-aggregating into an “others” category can hide detail readers might care about. **Mitigation:** Make aggregation explicit in the labeling so readers understand what was grouped.

## Common ways pie charts fail at basic scope <!-- role: mistakes -->

- **Mistake:** Using a pie chart with many thin slices. **Why it fails:** Labeling gets untidy and the slices become hard to read [@muth_pie_charts_2018].
- **Mistake:** Using multiple pie charts to compare different totals. **Why it fails:** Each pie represents its own whole, making comparisons between pies difficult [@muth_pie_charts_2018].

## Quick checks for whether a pie chart is in-scope <!-- role: check -->

**Failure Sign:** The chart needs a legend because labels do not fit cleanly, or many slices are too small to name. **Quick Check:** If you have more than five categories, treat that as a fail. **Stronger Test:** Ask a colleague to identify the top two shares without reading a legend; if they struggle, switch formats.

## What to do instead when you exceed the scope <!-- role: fix -->

- Use a stacked bar chart or stacked column chart when you have more than five shares.
- Use a stacked bar chart when you need to compare multiple totals across groups or time.
- Group small categories into a single “others” slice if you must stay with a pie and can justify aggregation.
