---
id: prefer-shared-space-or-row-faceted-over-area-overlay-for-correlation-in-multi-series-time-charts
title: Prefer Shared-Space or Row-Faceted Views Over Area-Overlay for Correlation
  Judgments Across Multiple Time Series
bibliography: references.bib
description: For correlation tasks across multiple time series, avoid area-overlay
  variants that are slower than shared-space line and row-faceted alternatives.
labels:
- chart:line
- chart:small-multiples
- task:correlate
- visual:position
- visual:row
- visual:color
- impact:speed
- data:temporal
- audience:general
---

## The Rule <!-- role: advice -->

For correlation judgments across multiple time series, avoid area-overlay designs; use either a shared-space line chart or a row-faceted split-space view instead.

## The Logic <!-- role: reason -->

Area-overlay variants increase time for correlation tasks relative to line and row-faceted alternatives.

- **The Principle:** Avoid slower encodings/layouts for correlation judgments
- **The Evidence:** For the correlate task, completion time ranks E-1 and E-3 faster than E-2 and E-4, with significant pairwise differences showing E-1 faster than E-2 and E-4, and E-3 faster than E-2 and E-4 [@javedGraphicalPerceptionMultiple2010]. This is captured as structured, reusable evidence in the collation for visualization recommendation [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Judge correlation/association patterns across time series.
- **Data Type:** Multiple quantitative series over an ordinal time axis; series identity is categorical.
- **Audience:** General analytical users optimizing for speed.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Accuracy is the only metric you care about for correlation in this setup.
- **Reason:** Accuracy rankings for correlate group E-1 with E-2 and group E-3 with E-4 (no superiority indicated by the rank grouping), so this rule is specifically about time, not accuracy [@javedGraphicalPerceptionMultiple2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may give up filled-area styling that some designers prefer aesthetically or for emphasis.
- **The Risk:** If area encoding is required for another constraint, you may not achieve the same time benefit.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching from lines to filled areas (area-overlay) to “make trends easier to see” for correlation tasks.
- **Why it fails:** The reported time results place area-overlay designs among the slower options for correlate, with significant differences versus the faster alternatives [@javedGraphicalPerceptionMultiple2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Correlation judgments feel effortful and slow because users must parse filled areas and disentangle them.
- **The Test:** A/B test correlate questions using your current view versus a line overlay (shared-space) or row-faceted view; if completion time drops, the rule applies.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace area-overlay with a shared-space line chart (keep consistent axes and series mapping).
- **Best Fix:** In a recommender, encode a soft preference for E-1/E-3-like designs over E-2/E-4-like designs when task=correlate and optimization goal=speed [@zengReviewCollationGraphical2023; @javedGraphicalPerceptionMultiple2010].
