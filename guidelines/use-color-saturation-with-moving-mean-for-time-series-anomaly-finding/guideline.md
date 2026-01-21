---
id: use-color-saturation-with-moving-mean-for-time-series-anomaly-finding
title: Use Color-Saturation With a Moving-Mean Design to Find Anomalies
bibliography: references.bib
description: For anomaly finding in time series, prefer the color-saturation moving-mean
  design tested as best in the study.
labels:
- chart:colorfield
- task:find-anomalies
- visual:color
- impact:accuracy
- data:temporal
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When the task is to find anomalies in a time series, use a color-saturation design with a moving-mean-style transformation (the top-ranked anomaly design in the study) rather than position-only or other color variants tested.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** A visualization that emphasizes deviation relative to a smoothed baseline supports anomaly identification better than designs not optimized for that deviation signal.
- **The Evidence:** In the find-anomalies ranking, the moving-mean color-saturation design (E-7) ranked highest and was significantly better than E-1, E-2, E-4, and E-5 (all listed as significant pairs with E-7 as better) [@albersTaskdrivenEvaluationAggregation2014]. This task-linked ranking is part of the structured collation process in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Identify which time period contains anomalies/outliers relative to typical behavior.
- **Data Type:** Quantitative time series where anomaly detection is performed across discrete periods.
- **Audience:** General viewers doing anomaly screening where accuracy is important.

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** The primary task is precise extrema or range comparison.
- **Reason:** For extrema and range tasks in the same study, position-based and/or explicitly extrema-encoding designs rank above color-saturation designs [@albersTaskdrivenEvaluationAggregation2014], as synthesized in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Reduced support for precise point reading from axes compared to position encodings.
- **The Risk:** Users may struggle with exact value extraction or point-to-point comparisons, reflecting the lower ranks of color-based designs on point comparison tasks in the same results table [@albersTaskdrivenEvaluationAggregation2014], as collated in [@zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Keeping a standard line chart and expecting anomalies to be “obvious.”
- **Why it fails:** In the find-anomalies ranking, the line design (E-1) is below E-7 and is significantly worse than E-7 [@albersTaskdrivenEvaluationAggregation2014], as recorded in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Anomalies are only detectable by carefully scanning peaks/valleys, not by immediately noticing deviations.
- **The Test:** Show the chart briefly and ask “which period has anomalies?”; if users must re-check multiple segments carefully, prefer the top-performing anomaly design (E-7) identified in [@albersTaskdrivenEvaluationAggregation2014] and collated by [@zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a smoothed baseline representation (moving-mean transformation) and encode deviations using color-saturation.
- **Best Fix:** Switch to the study’s top-ranked anomaly design (E-7) for anomaly tasks, per [@albersTaskdrivenEvaluationAggregation2014] and its structured capture in [@zengReviewCollationGraphical2023].
