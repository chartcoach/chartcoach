---
id: use-parallel-coordinates-for-negative-correlation-judgment-over-positive
title: Prefer Parallel Coordinates for Negative Correlation Judgments
bibliography: references.bib
description: When using parallel coordinates for correlation judgment, expect better
  precision for negative correlations than positive.
labels:
- chart:parallel-coordinates
- task:correlate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- metric:jnd
- correlation:negative
- source:zengReviewCollationGraphical2023
- source:harrisonRankingVisualizationsCorrelation2014
---

## The Rule <!-- role: advice -->

If you use parallel coordinates for correlation judgment, prefer configurations/datasets where the relationship is negative rather than positive (i.e., expect higher precision for negative correlations than positive).

## The Logic <!-- role: reason -->

The study reports an asymmetry: parallel coordinates depicting negatively correlated data significantly outperform parallel coordinates depicting positively correlated data for correlation judgment precision (lower JND for negative than positive), indicating that correlation-direction affects perceptual discriminability in this chart type.

- **The Principle:** Correlation-direction asymmetry in perceptual precision (JND) for the same chart family.
- **The Evidence:** Significant difference between parallel coordinates-negative vs parallel coordinates-positive (Mann-Whitney-Wilcoxon, p < 0.001 in the study’s reported comparisons) summarized in the collation [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Judge correlation strength using parallel coordinates.
- **Data Type:** Two quantitative variables visualized in parallel coordinates where correlation direction can be negative or positive.
- **Audience:** General audiences (as in crowdsourced perception testing context).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your data’s correlations are primarily positive and you cannot re-express the problem as negative correlation without changing the meaning of the task.
- **Reason:** The advantage is direction-dependent; forcing negative correlation can misrepresent the underlying relationship [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to accept reduced precision when displaying positive correlations in parallel coordinates (relative to negative within the same chart type).
- **The Risk:** Users may make less reliable correlation discriminations for positive relationships if parallel coordinates are used anyway [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating positive and negative correlation cases as perceptually equivalent in parallel coordinates.
- **Why it fails:** The evidence shows statistically significant asymmetry in JND between directions for this chart type [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users are noticeably less consistent when judging “more correlated” for positive cases than for negative cases in parallel coordinates.
- **The Test:** Split a quick test set into positive and negative correlations and compare user discrimination consistency; expect better performance for negative if your design aligns with the tested parallel-coordinates setup [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** If the goal is correlation judgment and your relationships are positive, switch away from parallel coordinates to a scatterplot.
- **Best Fix:** Use parallel coordinates selectively (e.g., when negative correlations dominate the analysis), and otherwise default to scatterplots for correlation judgment [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].
