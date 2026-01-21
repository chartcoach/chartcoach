---
id: synchronize-time-axes-across-rows-for-comparability
title: Synchronize Time Axes Across Rows to Enable Comparison
bibliography: references.bib
description: Use a shared time scale for each row of predictions so users can compare
  buses without distortion.
labels:
- chart:small-multiples
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- domain:transit
---

## The Rule <!-- role: advice -->

Use a common, synchronized time axis across rows of predicted buses; do not rescale each row independently.

## The Logic <!-- role: reason -->

Per-row rescaling changes how wide/tall distributions appear, making buses with different variances look artificially similar and hindering comparison; synchronized axes preserve comparability across alternatives [@kayWhenIshMy2016].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare which bus is likely to arrive sooner and how uncertain each is.
- **Data Type:** Multiple predictive distributions shown as a list (one per bus) or grouped by route.
- **Audience:** Users scanning several upcoming arrivals.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The interface shows only one bus at a time (no cross-row comparison).
- **Reason:** Comparability across rows is not a requirement in a single-item view [@kayWhenIshMy2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some distributions may appear very compressed if the shared axis must cover a wide range.
- **The Risk:** Fine structure in a narrow distribution may be hard to see without interaction [@kayWhenIshMy2016].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Auto-fit each distribution tightly to its own min/max window.
- **Why it fails:** Users misread relative uncertainty and timing because width/height no longer correspond across rows [@kayWhenIshMy2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Tick marks or time labels differ from row to row.
- **The Test:** Compare two rows: if the same x-position means different times, the axis is not synchronized.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Set all rows to the same time range (e.g., now to +N minutes).
- **Best Fix:** Use a shared grid and consistent tick marks across all rows in the list [@kayWhenIshMy2016].
