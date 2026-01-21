---
id: use-standard-line-charts-for-point-in-time-cross-series-comparisons
title: Use a Single Line Chart for Point-in-Time Comparisons
bibliography: references.bib
description: Prefer a normal multi-line chart when readers need to compare series
  at the same date.
labels:
- chart:line
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:general
- chart:small-multiples
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Use a normal multi-line chart (not small multiples) when the key task is comparing different series at specific points in time.

## The Logic <!-- role: reason -->

Placing lines in the same coordinate system enables direct vertical comparison at a given x-value (date), which is difficult when lines are separated into different panels [@muth_small_multiple_line_charts_2024].

- **The Principle:** Shared coordinate space supports direct comparisons
- **The Evidence:** [@muth_small_multiple_line_charts_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Answer questions like “Which category was higher in 2022?”
- **Data Type:** Multiple time series where cross-series ranking at specific dates matters
- **Audience:** General readers needing quick comparisons

## When to Break It <!-- role: exceptions -->

- **Scenario:** Lines overlap so much that readers can’t track individual trends.
- **Reason:** If overlap prevents parsing, splitting into small multiples improves readability even if comparisons become harder [@muth_small_multiple_line_charts_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Individual trend shapes can be harder to trace when many lines overlap.
- **The Risk:** Readers may feel overwhelmed by clutter and miss patterns within single categories [@muth_small_multiple_line_charts_2024].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using small multiples even though the main question is cross-series comparison at a date.
- **Why it fails:** Readers can’t easily compare values across separate panels at the same time point [@muth_small_multiple_line_charts_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** You find yourself asking readers to compare categories at a specific year/quarter, but the chart requires scanning multiple panels to do it.
- **The Test:** Ask, “Can a reader answer ‘Which was higher in 2022, A or B?’ in under 5 seconds?” If not, small multiples are the wrong choice [@muth_small_multiple_line_charts_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of categories so a single chart is readable.
- **Best Fix:** Use a normal multi-line chart to keep all series in one shared plot area for point-in-time comparison [@muth_small_multiple_line_charts_2024].
