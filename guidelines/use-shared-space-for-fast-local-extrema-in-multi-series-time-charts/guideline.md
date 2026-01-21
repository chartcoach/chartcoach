---
id: use-shared-space-for-fast-local-extrema-in-multi-series-time-charts
title: Use Shared-Space Line Charts for Faster Local Extremum Finding Across Multiple
  Time Series
bibliography: references.bib
description: For finding which series is highest at a specific time point, prefer
  shared-space line techniques over split-space layouts to reduce completion time.
labels:
- chart:line
- chart:small-multiples
- task:find-extremum
- visual:position
- visual:color
- impact:speed
- data:temporal
- audience:general
- layout:shared-space
- layout:split-space
---

## The Rule <!-- role: advice -->

For finding the highest series at a specific time point, use a shared-space line chart (overlay series in one chart) instead of splitting series into separate rows.

## The Logic <!-- role: reason -->

Shared space reduces eye travel between separate subplots when comparing values at a single x-position, enabling faster judgments.

- **The Principle:** Minimize gaze travel for point-in-time comparison
- **The Evidence:** In the collated results, shared-space (E-1) is as fast as the best alternative and faster than split-space row-faceted designs (E-3, E-4) for the find-extremum task in completion time [@javedGraphicalPerceptionMultiple2010]. This guideline is drawn from the structured collation of graphical perception findings for recommendation use [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which time series has the maximum value at a particular time point (extremum-at-time).
- **Data Type:** Multiple quantitative time series over an ordinal time axis; series identity encoded categorically.
- **Audience:** General analytical users optimizing for speed.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your primary objective is accuracy rather than speed for the same extremum task.
- **Reason:** Accuracy rankings place E-2 above the other designs for find-extremum (even though the shared-space design is faster than split-space row designs) [@javedGraphicalPerceptionMultiple2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may increase overlap/clutter relative to splitting series into separate rows.
- **The Risk:** With many series, shared-space overlays can become harder to parse even if they are fast for the task.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Splitting series into rows (faceting) to “declutter” even when the task is a single-time-point maximum.
- **Why it fails:** In the reported time results, row-faceted split-space designs are slower than the shared-space design for find-extremum [@javedGraphicalPerceptionMultiple2010].

## How to Check <!-- role: check -->

- **Visual Sign:** You (or users) must scan up and down multiple rows to decide which series is highest at the same time point.
- **The Test:** Time a few representative users on a “which series is highest at time t?” question; if row-faceted designs are slower, you are likely violating the rule.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Collapse small multiples into a single shared-space overlay for the extremum-at-time view.
- **Best Fix:** Provide a shared-space line chart as the default view when the user selects a find-extremum-at-time task, reserving split-space views for other task contexts [@zengReviewCollationGraphical2023; @javedGraphicalPerceptionMultiple2010].
