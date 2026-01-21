---
id: explicitly-encode-monthly-extrema-for-range-and-minmax
title: Explicitly Encode Period Max and Min When Users Compare Ranges or Extremes
bibliography: references.bib
description: When range or min/max comparisons are required per time period, add explicit
  max/min encodings rather than relying on raw series alone.
labels:
- chart:line
- chart:composite
- task:determine-range
- task:find-extremum
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When the task is to determine range or identify extremes per period, explicitly encode period maxima and minima (as derived statistics) instead of relying only on the raw line.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Reducing viewer computation by explicitly mapping needed statistics improves accuracy for point-derived comparisons.
- **The Evidence:** In the determine-range results, designs that included explicit max/min aggregates (e.g., the “modified stock chart” design E-2 and the box-plot design E-3) ranked above the plain line (E-1), with significant pairwise differences reported between those higher designs and lower ones [@albersTaskdrivenEvaluationAggregation2014]. This extraction and ranking is part of the collation described in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Compare ranges (max–min) across periods or find which period contains the min/max.
- **Data Type:** Time series where comparisons are made at a known grouping (e.g., month-by-month).
- **Audience:** General viewers doing accuracy-focused comparisons.

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** The user needs to inspect raw within-period structure (e.g., day-to-day pattern) as the primary objective.
- **Reason:** Explicit max/min summaries can reduce visibility of raw variation; the study includes designs that trade off raw detail to encode aggregates [@albersTaskdrivenEvaluationAggregation2014], as organized in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** More visual elements (layers/marks) and potentially less emphasis on raw time-series detail.
- **The Risk:** If the period grouping is not aligned to the user’s intended comparison granularity, the explicit aggregates can be the wrong summary to foreground (the study’s tasks are period-based) [@albersTaskdrivenEvaluationAggregation2014], as framed in [@zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Expecting viewers to mentally compute ranges from a raw line for each period.
- **Why it fails:** In the determine-range ranking, the raw line design (E-1) was below designs that explicitly included extrema (E-2, E-3) [@albersTaskdrivenEvaluationAggregation2014], as collated in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users repeatedly trace up/down within each period to guess max/min before comparing periods.
- **The Test:** Ask users to answer “which period has the largest range?”; if they must do visible manual scanning for highs and lows in each period, your design is not explicitly encoding what the task needs (consistent with lower ranking for E-1) [@albersTaskdrivenEvaluationAggregation2014], as collated in [@zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit per-period max and min marks (derived aggregates) on top of the existing time-series display.
- **Best Fix:** Use an encoding that directly supports range comparisons by representing per-period extrema clearly (e.g., a stock-style design or box-plot) as reflected by higher accuracy ranks for determine-range in [@albersTaskdrivenEvaluationAggregation2014] and recorded by [@zengReviewCollationGraphical2023].
