---
id: use-small-multiple-line-charts-to-untangle-overlapping-lines
title: Use Small Multiple Line Charts to Untangle Overlapping Lines
bibliography: references.bib
description: Split a crowded multi-line time series into separate panels so each trend
  is easy to parse.
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

Use small multiple line charts instead of a single multi-line chart when lines overlap heavily and become hard to follow.

## The Logic <!-- role: reason -->

Separating each series into its own panel reduces visual clutter and makes it easier to trace each trend without confusing crossings and overlaps, improving readers’ ability to parse the chart [@muth_small_multiple_line_charts_2024].

- **The Principle:** Reduce overplotting by separating signals
- **The Evidence:** [@muth_small_multiple_line_charts_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand the trend/shape of each category over time without distraction
- **Data Type:** Multiple time series with frequent overlap or crossings
- **Audience:** General readers who need low-effort readability

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary question is which line is higher/lower at a specific point in time (precise cross-series comparison at dates).
- **Reason:** Small multiples make point-in-time comparisons across panels difficult; a normal line chart supports that comparison better [@muth_small_multiple_line_charts_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Uses more space and can require scrolling, especially on mobile.
- **The Risk:** Readers may lose the ability to compare series directly at specific dates [@muth_small_multiple_line_charts_2024].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping everything in one chart and relying on many colors to distinguish overlapping lines.
- **Why it fails:** Color doesn’t solve overlap; the lines remain hard to trace and the chart overwhelms readers [@muth_small_multiple_line_charts_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** You can’t reliably trace a single series from start to end without losing it in crossings.
- **The Test:** Try following one category’s line with your finger/eye from left to right; if you regularly lose it, the chart is too tangled and should be faceted [@muth_small_multiple_line_charts_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of series shown (keep only those supporting the intended takeaway).
- **Best Fix:** Switch to small multiple line charts so each series gets its own panel [@muth_small_multiple_line_charts_2024].
