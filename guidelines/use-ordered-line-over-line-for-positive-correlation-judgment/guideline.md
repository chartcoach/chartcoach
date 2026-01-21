---
id: use-ordered-line-over-line-for-positive-correlation-judgment
title: Use Ordered Line Charts Instead of Unordered Line Charts for Positive Correlation
  Judgment
bibliography: references.bib
description: For correlation judgment on positively correlated data, ordered line
  charts yield better perceptual precision than standard line charts.
labels:
- chart:line
- task:correlate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- metric:jnd
- correlation:positive
- source:zengReviewCollationGraphical2023
- source:harrisonRankingVisualizationsCorrelation2014
---

## The Rule <!-- role: advice -->

For correlation judgment on positively correlated data using line-based displays, use an ordered line chart rather than a standard (unordered) line chart.

## The Logic <!-- role: reason -->

The reported comparisons show ordered line charts (positive) significantly outperform line charts (positive) in correlation judgment precision (lower JND), indicating that ordering the x-axis improves discriminability of correlation strength in this context.

- **The Principle:** Ordering can improve perceptual precision for judging correlation in line-based representations.
- **The Evidence:** The study reports ordered line-positive significantly outperforming line-positive (Mann-Whitney-Wilcoxon, p < 0.001) and this is summarized in the collation [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Judge which of two datasets is more correlated (positive correlation cases).
- **Data Type:** Two quantitative variables presented in a line-based encoding with an explicit order along the x-axis.
- **Audience:** General audiences performing perceptual correlation discrimination.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The x-axis order has semantic meaning (e.g., time or another fixed sequence) and re-ordering would change what the chart means.
- **Reason:** Ordered line charts change the axis order; if order is meaningful, this violates the intended data semantics, and this evidence does not justify that tradeoff [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up the original x-axis order.
- **The Risk:** Users may misinterpret the meaning of the x-axis if they assume a natural order that no longer applies [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a standard line chart for correlation judgment because it “shows a trend.”
- **Why it fails:** For the correlate task with positive correlations, the evidence indicates worse JND (lower precision) than an ordered line chart [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The line looks noisy and users struggle to reliably choose which is more correlated.
- **The Test:** Compare user judgments between the same dataset shown as a standard line vs an ordered line; if ordered line yields more consistent discrimination, you match the reported direction of effect [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Sort the x-axis by the x-variable (or by a monotone ordering consistent with the ordered-line setup used for correlation judgment).
- **Best Fix:** If ordering is not semantically allowed, switch to a scatterplot for correlation judgment instead of using an unordered line chart [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].
