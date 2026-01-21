---
id: prefer-contiguous-cartograms-for-filter-accuracy
title: Prefer Contiguous Cartograms for Filtering Accurately
bibliography: references.bib
description: For filter-style judgments on cartograms, contiguous cartograms yield
  higher accuracy than non-contiguous, Dorling, and rectangular variants.
labels:
- chart:cartogram
- task:filter
- visual:area
- visual:position
- impact:accuracy
- data:geospatial
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a **contiguous cartogram** when the user must **filter** regions correctly (i.e., pick regions matching a condition) based on cartogram content.

## The Logic <!-- role: reason -->

Filtering requires correctly identifying which regions satisfy a criterion; the study’s measured accuracy ranks contiguous cartograms highest for a filtering condition.

- **The Principle:** Choose the cartogram type that empirically minimizes filtering errors for region-level selection.
- **The Evidence:** In the collated results, filtering accuracy is ranked **E-1 (contiguous) > E-3 (non-contiguous) > E-4 (Dorling) > E-2 (rectangular)** with significant pairwise differences reported across all adjacent pairs in that ordering [@nusratEvaluatingCartogramEffectiveness2018]. This guideline is derived via the structured collation approach described in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly select regions that meet a condition (filtering).
- **Data Type:** Geo-referenced regions with a **quantitative** value encoded by **area**, laid out by map position (positionX/positionY).
- **Audience:** General audiences performing map-based lookups or selections.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary goal is **aggregate** judgment rather than selection/filtering.
- **Reason:** Aggregate accuracy is ranked differently (Dorling highest in the provided results), so optimizing for filtering may harm aggregation performance [@nusratEvaluatingCartogramEffectiveness2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may give up performance for other tasks whose best-performing cartogram differs.
- **The Risk:** Over-optimizing for filtering can lead to suboptimal outcomes for correlation/aggregation tasks in the same view [@nusratEvaluatingCartogramEffectiveness2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using **rectangular cartograms** by default because they look “cleaner.”
- **Why it fails:** Rectangular cartograms are last in the reported filtering-accuracy ranking for the relevant condition [@nusratEvaluatingCartogramEffectiveness2018], as collated in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users frequently select the wrong regions when applying the filter condition.
- **The Test:** Run a quick task check: ask users to identify which regions satisfy a stated condition and compare error rates between contiguous vs. rectangular/Dorling alternatives.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from **rectangular** or **Dorling** to a **contiguous** cartogram.
- **Best Fix:** Offer contiguous as the default for filtering tasks and allow alternate cartogram types only when the user’s task changes (task-aware switching), consistent with the knowledge-collation intent in [@zengReviewCollationGraphical2023].
