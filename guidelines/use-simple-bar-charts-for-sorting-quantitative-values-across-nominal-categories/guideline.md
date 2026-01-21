---
id: use-simple-bar-charts-for-sorting-quantitative-values-across-nominal-categories
title: Use Simple Bar Charts for Sorting Quantitative Values Across Nominal Categories
bibliography: references.bib
description: Use a bar chart with length encoding to support sorting a quantitative
  measure across nominal categories.
labels:
- chart:bar
- task:sort
- visual:length
- visual:position
- impact:accuracy
- data:quantitative
- data:categorical
- audience:general
- source:talbot2014
- source:zeng2023
---

## The Rule <!-- role: advice -->

Use a simple bar chart (rectangles) with **bar length (linear)** to encode the **quantitative** value and **x-position** to separate **nominal** categories when the task is **sorting**.

## The Logic <!-- role: reason -->

Sorting requires reliable perception of ordered magnitudes; this guideline follows the extracted study context where bar charts are treated as a length-encoding design to support a sorting task.

- **The Principle:** Quantitative magnitude via length on a linear scale
- **The Evidence:** The structured collation records a bar-chart design using **length (linear)** for quantitative data and **positionX (nominal)** for nominal categories under the **sort** task [@talbotFourExperimentsPerception2014], as collated for visualization recommendation [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Sorting/ranking categories by a numeric measure
- **Data Type:** One quantitative field + one nominal grouping field
- **Audience:** General users (no special training assumed)

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not doing a sorting task.
- **Reason:** The extracted knowledge is scoped to the **sort** task only; no other tasks or outcomes are included in the structured record [@zengReviewCollationGraphical2023; @talbotFourExperimentsPerception2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Uses space proportional to the number of categories (one bar per category).
- **The Risk:** If categories are too many, the chart can become dense, making sorting hard in practice (this is a general risk of the form, not evaluated in the extracted record).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching away from length encoding (e.g., encoding the quantitative value with a different channel) while still expecting easy sorting.
- **Why it fails:** This guideline is specifically grounded in a length-based bar chart design for sorting; the structured record does not provide support for alternative encodings here [@zengReviewCollationGraphical2023; @talbotFourExperimentsPerception2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers struggle to tell which categories should come first/last when ordered by value.
- **The Test:** Ask a user to rank the top 3 categories by value using the chart alone; if they hesitate or disagree, the design may not be supporting sorting well in your context.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Ensure the quantitative value is encoded by **bar length** on a **linear scale** and categories are separated by **x-position**.
- **Best Fix:** Rebuild the visualization to match the extracted design pattern exactly: rectangles with length (linear) for the quantitative field and nominal x-position for the category field [@zengReviewCollationGraphical2023; @talbotFourExperimentsPerception2014].
