---
id: use-row-faceted-split-space-for-faster-aggregate-in-multi-series-time-charts
title: Use Row-Faceted Split-Space Views for Faster Aggregate Judgments Across Multiple
  Time Series
bibliography: references.bib
description: For aggregate tasks over multiple time series, split series into rows
  to reduce completion time compared with shared-space overlays.
labels:
- chart:small-multiples
- chart:line
- task:aggregate
- visual:row
- visual:position
- impact:speed
- data:temporal
- audience:general
- layout:split-space
---

## The Rule <!-- role: advice -->

For aggregate tasks across multiple time series, split series into separate rows (small-multiple style) rather than overlaying all series in one shared chart.

## The Logic <!-- role: reason -->

Separating series reduces within-view interference during whole-series judgments, enabling faster completion.

- **The Principle:** Reduce interference by separating series for whole-series judgments
- **The Evidence:** For the aggregate task, row-faceted split-space designs (E-3 and E-4) are ranked faster than shared-space or non-row split designs (E-1 and E-2), with significant pairwise differences showing E-3 and E-4 faster than E-1 and E-2 [@javedGraphicalPerceptionMultiple2010]. This is included as actionable collated knowledge for recommendation systems [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Compute/compare an aggregate property over time across series (aggregate task).
- **Data Type:** Multiple quantitative time series on an ordinal time axis.
- **Audience:** General analytical users optimizing for speed.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user’s primary constraint is minimizing vertical space or avoiding additional layout complexity.
- **Reason:** Row-faceted designs introduce a multi-row layout (more structure) compared with a single overlaid chart, which may not fit all displays or constraints, even if faster for this task [@javedGraphicalPerceptionMultiple2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose the single shared coordinate space, which can make some pointwise cross-series comparisons less direct.
- **The Risk:** Users may need more cross-row scanning for tasks that require exact alignment at a single time point.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a shared-space overlay for aggregate tasks because it “shows everything together.”
- **Why it fails:** The measured completion time favors row-faceted designs for aggregate tasks, with significant differences versus the shared-space alternatives [@javedGraphicalPerceptionMultiple2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Users pause and re-trace multiple overlapping series to form an aggregate judgment.
- **The Test:** Run a quick timing check on an aggregate question; if an overlaid view is slower than a row-faceted view for the same data/task, adopt the rule.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert the multi-series overlay into a row-faceted layout (one series per row).
- **Best Fix:** In a recommendation system, add a task-conditioned preference that selects row faceting for aggregate tasks on multi-series time data [@zengReviewCollationGraphical2023; @javedGraphicalPerceptionMultiple2010].
