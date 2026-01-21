---
id: use-pie-charts-only-for-simple-part-to-whole-shares
title: Use Pie Charts Only for Simple Part-to-Whole Shares
bibliography: references.bib
description: Use pie charts only to show how a single 100% total divides into a few
  easily distinguishable shares.
labels:
- chart:pie
- task:part-to-whole
- visual:angle
- impact:clarity
- data:categorical
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use a pie chart only when you’re showing one 100% total split into a few (max five) shares that are easy to distinguish—especially shares near 25%, 50%, or 75%—and avoid pie charts for precise comparisons or multiple totals. [@muth_pie_charts_2018]

## The Logic <!-- role: reason -->

Pie charts are easiest to read when the slice sizes align with familiar quarter/half/three-quarter proportions, but they are poor for comparing similar-sized shares and cannot show more than one total effectively. [@muth_pie_charts_2018]

- **The Principle:** Match chart type to the perceptual task (spotting approximate proportions vs. comparing many/close values).
- **The Evidence:** [@muth_pie_charts_2018]

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Understand how a whole (100%) divides into a few shares; quickly spot a roughly quarter/half/three-quarter split. [@muth_pie_charts_2018]
- **Data Type:** One categorical part-to-whole breakdown with a small number of categories (≤5). [@muth_pie_charts_2018]
- **Audience:** General readers who benefit from quick, approximate proportion recognition. [@muth_pie_charts_2018]

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You need readers to compare shares precisely or the differences are small.\
  **Reason:** Pie slices are not the best choice for comparing sizes of shares; use bars/columns instead. [@muth_pie_charts_2018]
- **Scenario:** You have more than five shares.\
  **Reason:** Labeling becomes messy; a stacked bar/column is tidier. [@muth_pie_charts_2018]
- **Scenario:** You only have two values.\
  **Reason:** It’s effectively one number plus “the rest to 100%,” so a single stated value may be clearer than a chart. [@muth_pie_charts_2018]
- **Scenario:** You need to compare two (or more) totals (e.g., two polls).\
  **Reason:** One pie chart can only show one total; use a stacked bar chart to compare. [@muth_pie_charts_2018]

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** You give up the “always use a pie” familiarity and may need to switch to bars/stacked bars for comparability. [@muth_pie_charts_2018]
- **The Risk:** If you force a pie into a comparison task or overload it with categories, readers may misread or ignore differences. [@muth_pie_charts_2018]

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Using a pie chart to compare many similar shares.\
  **Why it fails:** Pie charts are not the best option for comparing slice sizes when differences are small. [@muth_pie_charts_2018]
- **The Wrong Fix:** Packing more than five categories into a pie.\
  **Why it fails:** The labeling gets untidy and harder to read. [@muth_pie_charts_2018]
- **The Wrong Fix:** Using two-slice pies for a single percentage point.\
  **Why it fails:** A chart is unnecessary when one number (and its complement to 100%) is the message. [@muth_pie_charts_2018]
- **The Wrong Fix:** Using separate pies to compare totals.\
  **Why it fails:** A single pie shows only one total; comparisons across pies are not the recommended approach here. [@muth_pie_charts_2018]

## How to Check <!-- role: check -->

- **Visual Sign:** Many thin slices, cramped labels, or a chart where the main takeaway is “which share is bigger?” but slices look similar. [@muth_pie_charts_2018]
- **The Test:** Count the categories (if >5, it fails) and ask: “Am I asking readers to compare slice sizes precisely or compare multiple totals?” If yes, don’t use a pie. [@muth_pie_charts_2018]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce categories by grouping small slices into “others,” or remove the chart and state the single key percentage when it’s just two values. [@muth_pie_charts_2018]
- **Best Fix:** Switch to a bar/column chart for comparing shares, or a stacked bar/stacked column chart when you have many shares or need to compare multiple totals. [@muth_pie_charts_2018]
