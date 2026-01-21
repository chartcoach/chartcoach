---
id: use-discrete-per-period-aggregation-for-average-comparisons
title: Use Discrete Per-Period Aggregation When Comparing Averages
bibliography: references.bib
description: For tasks comparing average values across time periods, use discretely
  aggregated per-period summaries rather than a raw line alone.
labels:
- chart:composite
- chart:box-plot
- chart:color-stock
- task:aggregate
- visual:position
- visual:color
- impact:accuracy
- data:temporal
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When users must compare averages across time periods, show discrete per-period aggregates (e.g., per-month mean) rather than only the raw time-series line.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Task-aligned, discrete aggregation reduces the need for mental averaging and supports more accurate summary comparison.
- **The Evidence:** In the aggregate task ranking, the composite graph that encoded the per-period mean (E-4) ranked highest, and per-period summary designs (e.g., E-6 and E-3) ranked above the plain line (E-1), with significant pairwise differences reported (e.g., E-4 better than multiple others; E-6 better than multiple others) [@albersTaskdrivenEvaluationAggregation2014]. This is captured via the collation approach in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Decide which period has the highest average (mean) value.
- **Data Type:** Quantitative time series with comparisons over discrete periods (e.g., months).
- **Audience:** General viewers where correctness matters more than preserving every raw point.

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** The user’s main task is to find specific point extrema rather than compare averages.
- **Reason:** Extrema tasks showed different top-performing designs than the average/aggregate task, indicating task dependence within the same study [@albersTaskdrivenEvaluationAggregation2014], as highlighted in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Reduced visibility of within-period fluctuations compared to showing only raw data.
- **The Risk:** Users may over-trust the aggregated display and miss important within-period structure that is not summarized by the mean (the study’s designs trade raw detail for summaries in some conditions) [@albersTaskdrivenEvaluationAggregation2014], as documented in [@zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Showing only a raw line and expecting viewers to “eyeball” monthly averages.
- **Why it fails:** The raw line (E-1) ranked last for the aggregate task in the reported ranking [@albersTaskdrivenEvaluationAggregation2014], as collated in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers repeatedly scan across many points in a period and still look uncertain about which period’s average is higher.
- **The Test:** Ask a user to choose the highest-average period quickly; if they must mentally integrate many samples (rather than read an explicit per-period mean), you are likely violating the rule (consistent with E-1’s low rank) [@albersTaskdrivenEvaluationAggregation2014], as collated in [@zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a per-period mean overlay (e.g., bars or other summary marks) while keeping the raw series visible.
- **Best Fix:** Use a design that explicitly encodes per-period means and ranked highly for aggregate (e.g., the composite design E-4) per [@albersTaskdrivenEvaluationAggregation2014], as recorded in [@zengReviewCollationGraphical2023].
