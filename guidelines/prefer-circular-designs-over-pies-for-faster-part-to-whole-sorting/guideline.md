---
id: prefer-circular-designs-over-pies-for-faster-part-to-whole-sorting
title: Prefer Circular Slice or Straight-Line Circular Charts for Faster Part-to-Whole
  Sorting
bibliography: references.bib
description: Circular slice and straight-line circular charts were faster than pie,
  stacked bar, and treemap designs for part-to-whole sorting in an empirical comparison.
labels:
- chart:radial
- chart:pie
- chart:stacked-bar
- chart:treemap
- task:sort
- visual:area
- impact:speed
- data:categorical
- data:quantitative
- audience:general
---

## The Rule <!-- role: advice -->

When speed matters for part-to-whole **sort** judgments, prefer **circular slice** or **straight-line circular** charts over **pie charts**, **stacked bars**, and **treemaps**.

## The Logic <!-- role: reason -->

- **The Principle:** Some encodings enable quicker comparative judgments for part-to-whole tasks.
- **The Evidence:** In the measured time outcomes, the **circular slice** and **straight-line circular** designs were the fastest group, and were significantly faster than the pie/stacked-bar/treemap group in multiple pairwise comparisons (reported with ANOVA-based testing at p < 0.01) [@kosaraImpactDistributionChart2019]. This is preserved as time-based ranking evidence in the collation review dataset [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly sort/compare which part is larger in a part-to-whole breakdown.
- **Data Type:** Nominal categories with quantitative shares.
- **Audience:** General audiences doing rapid reading (dashboards, operational monitoring).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your primary goal is not speed but convention/familiarity, or you require standard chart forms for stakeholder acceptance.
- **Reason:** The evidence here addresses response time differences for a specific task, not stakeholder preference or comprehension in other tasks [@kosaraImpactDistributionChart2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may choose a less standard chart type.
- **The Risk:** Misinterpretation risk may increase if the audience is unfamiliar with the circular variants (not evaluated here).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Optimizing speed by switching to a treemap because it “packs space better.”
- **Why it fails:** In this experiment, treemaps were in the slower group relative to the circular slice and straight-line circular charts [@kosaraImpactDistributionChart2019; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate longer to type/choose estimates when using pie/stacked bar/treemap displays.
- **The Test:** Time a small set of users doing the same sort questions across chart alternatives; prefer the design that reduces completion time while meeting accuracy needs.

## How to Fix <!-- role: fix -->

- **Quick Fix:** If you currently use pie/stacked bar/treemap for rapid part-to-whole sorting, pilot a circular-slice or straight-line circular alternative.
- **Best Fix:** Select chart type based on the target metric (time vs accuracy) using the empirically observed ranking captured in the review’s collated knowledge [@zengReviewCollationGraphical2023; @kosaraImpactDistributionChart2019].
