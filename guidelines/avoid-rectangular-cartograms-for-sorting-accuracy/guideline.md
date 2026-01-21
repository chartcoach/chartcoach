---
id: avoid-rectangular-cartograms-for-sorting-accuracy
title: Avoid Rectangular Cartograms for Accurate Sorting
bibliography: references.bib
description: Rectangular cartograms ranked worst for sorting accuracy compared with
  contiguous, non-contiguous, and Dorling cartograms.
labels:
- chart:cartogram
- task:sort
- visual:area
- visual:position
- impact:accuracy
- data:geospatial
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Do not use a **rectangular cartogram** when the user must **sort** regions accurately by the mapped quantitative value; prefer contiguous, non-contiguous, or Dorling cartograms instead.

## The Logic <!-- role: reason -->

Sorting relies on making reliable ordered comparisons across regions; the study’s accuracy results place rectangular cartograms last for sorting.

- **The Principle:** For ordering tasks, avoid designs with empirically higher error rates.
- **The Evidence:** For one sort condition, accuracy rank groups **(E-1 contiguous, E-3 non-contiguous, E-4 Dorling)** ahead of **E-2 rectangular**, with significant differences reported between each of E-1/E-3/E-4 and E-2 [@nusratEvaluatingCartogramEffectiveness2018]. This is recorded and intended for recommendation use per [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Rank regions from largest to smallest (or similar ordering).
- **Data Type:** Quantitative attribute encoded by area in a cartogram.
- **Audience:** General audiences performing comparative ordering on map regions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must use rectangles for reasons outside the measured objective (e.g., rigid format constraints) and can tolerate lower sorting accuracy.
- **Reason:** This guideline optimizes for accuracy on sorting, not for layout constraints; the evidence here only covers accuracy/time outcomes as structured in the collation [@nusratEvaluatingCartogramEffectiveness2018; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose the schematic regularity associated with rectangular layouts.
- **The Risk:** Alternative cartogram types may not match your preferred aesthetic or structural constraints.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to rectangular cartograms to “make comparisons easier.”
- **Why it fails:** Rectangular cartograms are the lowest-ranked option for sorting accuracy in the reported sort condition(s) [@nusratEvaluatingCartogramEffectiveness2018], as collated by [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users mis-order regions or fail to pick the correct next-largest/next-smallest region.
- **The Test:** Give users a quick “which is 2nd largest?” test on your map; compare error rates between rectangular and non-rectangular cartograms.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace rectangular cartograms with **contiguous** (or **Dorling/non-contiguous**) for sorting workflows.
- **Best Fix:** Offer a task toggle: when the user selects “sort/rank,” default to a non-rectangular cartogram type per the collated evidence [@zengReviewCollationGraphical2023; @nusratEvaluatingCartogramEffectiveness2018].
