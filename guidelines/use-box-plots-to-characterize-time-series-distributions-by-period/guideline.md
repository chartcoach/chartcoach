---
id: use-box-plots-to-characterize-time-series-distributions-by-period
title: Use Per-Period Box Plots to Characterize Distributions
bibliography: references.bib
description: To characterize the distribution of values within each time period, prefer
  box-plot summaries over other tested time-series designs.
labels:
- chart:box-plot
- task:characterize-distribution
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

For distribution characterization by time period, use box plots (per period) rather than the other tested time-series designs.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Explicitly summarized distributional statistics (as in box plots) support more accurate distribution judgments than designs that require inferring distribution from raw sequences or color fields.
- **The Evidence:** In the characterize-distribution task ranking, the box-plot design (E-3) ranked highest and was significantly better than multiple alternatives (significant pairs include E-3 outperforming E-5, E-4, E-1, E-7, and E-2) [@albersTaskdrivenEvaluationAggregation2014]. This ranking is presented via the collation structure in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Identify or compare distributional properties across periods (e.g., how values are spread within months).
- **Data Type:** Time series grouped into discrete periods for per-period summaries.
- **Audience:** General viewers needing accurate distribution comparisons.

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** The task is anomaly/outlier counting using an encoding that explicitly marks outliers.
- **Reason:** The study’s anomaly task had a different top-ranked design (E-7), and some designs were not evaluated/afforded for certain tasks in the study setup [@albersTaskdrivenEvaluationAggregation2014], as captured in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Loss of detailed temporal shape within each period (box plots summarize instead of showing the full daily sequence).
- **The Risk:** Users may not be able to trace exact dates or local patterns, because the box plot collapses within-period order (a tradeoff inherent in the tested designs) [@albersTaskdrivenEvaluationAggregation2014], as discussed through the design-space lens in [@zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Using a plain line chart to answer “how spread out are values within each month?”
- **Why it fails:** In the characterize-distribution ranking, the line design (E-1) was below the box-plot design (E-3), and E-3 showed significant advantages over E-1 [@albersTaskdrivenEvaluationAggregation2014], as collated in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart forces users to visually integrate many points to guess the within-period spread.
- **The Test:** Ask users to compare distributions across two periods; if they must “mentally summarize” many points rather than compare explicit distribution summaries, switch to a box-plot-style summary (aligned with E-3’s top rank) [@albersTaskdrivenEvaluationAggregation2014], as collated in [@zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace or add a per-period box-plot summary view alongside the existing time-series chart.
- **Best Fix:** Use the per-period box plot as the primary display for distribution characterization tasks, consistent with the top-ranked performance in [@albersTaskdrivenEvaluationAggregation2014] and its collation in [@zengReviewCollationGraphical2023].
