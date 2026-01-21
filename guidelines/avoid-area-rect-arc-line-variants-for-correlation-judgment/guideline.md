---
id: avoid-area-rect-arc-line-variants-for-correlation-judgment
title: Avoid Stacked/Area/Arc/Line Variants for Correlation Judgments When Precision
  Matters
bibliography: references.bib
description: For correlation tasks requiring precise discrimination, avoid the lowest-performing
  chart groups (stacked/area/arc/line variants) relative to top-ranked alternatives.
labels:
- task:correlate
- visual:area
- visual:angle
- visual:length
- visual:orientation
- impact:accuracy
- data:quantitative
- audience:general
- metric:jnd
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When users need to precisely judge correlation, do not use the lowest-ranked chart group from the extracted results (stacked/area/arc and related line variants) as the primary encoding.

## The Logic <!-- role: reason -->

- **The Principle:** Some visualization forms require larger correlation differences before viewers can reliably detect a difference, leading to worse discrimination (higher JND).
- **The Evidence:** In the collated correlate-task JND ranking, one group of designs (including stacked/area/arc and a line variant) is placed in the lowest-performance tier, and the extracted significance pairs show many top-tier designs performing significantly better than those lowest-tier designs [@kayWebersLawSecond2016]. This rule is expressed as a design guideline via the collation framework [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Discriminating correlation strength (e.g., “Which is more correlated?”) with small-to-moderate differences.
- **Data Type:** Two quantitative variables where correlation is the target signal.
- **Audience:** General audiences (including scenarios where consistency and precision are desired).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Correlation precision is not the priority, and another communication goal dominates (e.g., emphasizing stacking, area fill, or a particular layout metaphor).
- **Reason:** The evidence summarized here is specific to correlation discrimination measured via JND, not to other tasks or goals [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may give up stylistic or space-saving formats that could be preferred for other storytelling or layout constraints.
- **The Risk:** Over-optimizing for correlation precision may reduce compatibility with existing dashboards built around stacked/area/arc conventions.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a stacked/area/arc design but “adding more color” or “making the shapes bolder” to imply correlation.
- **Why it fails:** The extracted evidence distinguishes performance by visualization design groups for the correlate task; the lowest tier remains lower-performing than the top tier in JND-based discrimination [@kayWebersLawSecond2016; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Correlation differences look visually ambiguous unless they are extreme.
- **The Test:** Present two similar correlations and see if viewers can reliably pick the stronger one; persistent uncertainty indicates you may be using a lower-performing design for this task [@kayWebersLawSecond2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the primary view with a top-tier alternative for correlation judgment from the extracted results (e.g., a position–position scatterplot) [@kayWebersLawSecond2016].
- **Best Fix:** Use a top-tier correlation view for the correlate task and reserve stacked/area/arc forms for secondary views or other tasks, aligning recommendation logic to the task-specific knowledge base [@zengReviewCollationGraphical2023; @kayWebersLawSecond2016].
