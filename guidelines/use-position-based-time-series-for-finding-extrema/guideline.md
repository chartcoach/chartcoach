---
id: use-position-based-time-series-for-finding-extrema
title: Use Position-Based Time-Series Charts to Find Extremes
bibliography: references.bib
description: For finding the highest/lowest point in a time series by period, prefer
  position-based designs over color-saturation designs.
labels:
- chart:line
- chart:composite
- task:find-extremum
- visual:position
- visual:color
- impact:accuracy
- data:temporal
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use position-based encodings (e.g., line/composite/stock-style overlays) rather than color-saturation-only designs when the task is to find extrema (maxima or minima) in time series aggregated by periods.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Higher-fidelity value reading from spatial position supports point-focused judgments.
- **The Evidence:** In the collated experiment results, position-heavy designs ranked above color-saturation designs for both extrema tasks (find-extremum-1 and find-extremum-2), with many significant pairwise differences reported [@albersTaskdrivenEvaluationAggregation2014]. This guideline is derived from the structured collation pipeline described in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Identify which time period contains the highest or lowest value (a point comparison over time).
- **Data Type:** Quantitative values over ordered time (time series) compared across discrete periods.
- **Audience:** General viewers performing accuracy-critical reading.

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** The display must prioritize anomaly/outlier detection rather than extrema.
- **Reason:** A color-based, explicitly anomaly-focused design (event striping) ranked best for find-anomalies in the same study [@albersTaskdrivenEvaluationAggregation2014], as collated in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** You may lose performance on some summary-style tasks that benefit from different encodings.
- **The Risk:** A position-first design that is excellent for extrema may not be the top option for other tasks (e.g., distribution characterization or anomaly finding) in this study’s task set [@albersTaskdrivenEvaluationAggregation2014], as summarized in [@zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Using a colorfield / color-saturation encoding alone to “make peaks pop.”
- **Why it fails:** In the reported rankings, color-saturation designs were consistently lower-ranked than position-based designs for extrema tasks [@albersTaskdrivenEvaluationAggregation2014] (collated in [@zengReviewCollationGraphical2023]).

## How to Check <!-- role: check -->

- **Visual Sign:** Users need to scan many colors to decide which month/day is highest/lowest instead of reading off an axis.
- **The Test:** Ask a viewer to answer “which period has the maximum/minimum?”; if they hesitate because they must interpret shades rather than positions, you are likely violating the rule (consistent with lower-ranked color designs in [@albersTaskdrivenEvaluationAggregation2014], collated by [@zengReviewCollationGraphical2023]).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the primary quantitative encoding from color-saturation to positionY with an appropriate y-axis.
- **Best Fix:** Use one of the higher-ranked position-based designs for extrema tasks (e.g., composite/stock-style overlays or a standard line with clear axes) as reflected by the study rankings [@albersTaskdrivenEvaluationAggregation2014] and collated in [@zengReviewCollationGraphical2023].
