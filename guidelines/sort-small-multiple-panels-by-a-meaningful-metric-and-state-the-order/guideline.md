---
id: sort-small-multiple-panels-by-a-meaningful-metric-and-state-the-order
title: Sort Panels by a Meaningful Metric and State the Order
bibliography: references.bib
description: Order small-multiple panels by a metric like start value or end value
  to guide what readers see first.
labels:
- chart:line
- task:rank
- visual:layout
- impact:clarity
- data:temporal
- audience:general
- chart:small-multiples
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Sort small-multiple panels by a meaningful rule (e.g., start value, end value, range, % change, or difference), and state the sorting rule in the chart description.

## The Logic <!-- role: reason -->

Panel order controls the reading path and determines what readers notice first; meaningful sorting improves navigation and helps the chart answer specific questions more directly [@muth_small_multiple_line_charts_2024].

- **The Principle:** Layout order shapes interpretation
- **The Evidence:** [@muth_small_multiple_line_charts_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify “highest at end,” “improved most,” or other ranked insights while scanning multiple panels
- **Data Type:** Many categories over time
- **Audience:** General readers who benefit from guided structure

## When to Break It <!-- role: exceptions -->

- **Scenario:** There’s no defensible “meaningful” metric for ordering, or the audience expects lookup by name.
- **Reason:** In that case, alphabetical order is better than no logic and supports finding a specific category [@muth_small_multiple_line_charts_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Readers may need a moment to understand the ordering.
- **The Risk:** If the sort rule isn’t communicated, readers may assume an order (e.g., alphabetical) and misread the structure [@muth_small_multiple_line_charts_2024].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Leaving panels in arbitrary/default order.
- **Why it fails:** Readers can’t tell where to look first or how to interpret the sequence of panels [@muth_small_multiple_line_charts_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Panels feel randomly arranged; readers can’t explain why one panel is next to another.
- **The Test:** Ask someone to infer the ordering in one sentence; if they can’t, either the sort isn’t meaningful or it isn’t communicated [@muth_small_multiple_line_charts_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Apply a simple, interpretable sort (e.g., end value) and add a one-line description of it.
- **Best Fix:** Choose a sort that matches the main question (start, end, change, range) and explicitly document it in the chart description [@muth_small_multiple_line_charts_2024].
