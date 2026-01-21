---
id: avoid-single-bar-with-overlays-when-measuring-differences-precisely
title: Avoid single-bar charts with difference overlays for precise difference measurement
bibliography: references.bib
description: For per-category difference measurement, single-bar-with-overlays is
  less accurate than a difference chart and is more error-prone than grouped overlays
  in the reported ranking.
labels:
- chart:bar
- task:aggregate
- visual:overlay
- impact:accuracy
- data:categorical
- audience:general
- comparison:multi-series
- derived:difference
---

## The Rule <!-- role: advice -->

For **precise per-category difference measurement**, do not rely on a **single bar chart with difference overlays (SB+D)**; use a **difference chart** instead.

## The Logic <!-- role: reason -->

Even when differences are present as overlays, SB+D can lead to misreads because users must separate the meaning of the bar (target value) from the overlay (difference), which is less direct than a difference-only encoding for a measurement task.

- **The Principle:** Prefer the most direct encoding of the value users must report.
- **The Evidence:** For difference measurement accuracy, the ranking places **E-2 (difference chart)** above **E-4 (SB+D)** (and above other designs), indicating the difference chart is most accurate among the tested variants [@srinivasanWhatsDifferenceEvaluating2018]; this is recorded as structured guidance in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Enter or report the exact absolute change for a given category.
- **Data Type:** Two-series category comparisons where deltas are explicitly requested.
- **Audience:** Mixed-literacy dashboard users (including those likely to confuse what the overlay represents).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your primary goal is not numeric difference measurement but keeping the target series as the dominant view.
- **Reason:** The evidence cited here is specifically for the difference-measurement task ranking [@srinivasanWhatsDifferenceEvaluating2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** A difference chart may not display raw target values as bars simultaneously.
- **The Risk:** Users may need an additional view for raw values.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping SB+D and adding more text instructions to “read the overlay value.”
- **Why it fails:** The underlying issue is competing marks/semantics in one view; the measured ranking still places the difference chart higher for accuracy [@srinivasanWhatsDifferenceEvaluating2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users report the target bar’s value instead of the difference value during a “difference for this category” task.
- **The Test:** Run a quick internal test: ask 5 people to state the difference for a named category; if several state the bar value, switch chart type.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide a separate difference-only view for measurement questions.
- **Best Fix:** Use a difference chart as the primary display for difference measurement tasks (and optionally pair it with a bar chart for raw values) [@srinivasanWhatsDifferenceEvaluating2018; @zengReviewCollationGraphical2023].
