---
id: avoid-non-contiguous-cartograms-for-filter-accuracy-in-filter-3-setting
title: Avoid Non-Contiguous Cartograms for Filtering Accuracy When They Rank Last
bibliography: references.bib
description: In one filtering condition, non-contiguous cartograms performed worst
  in accuracy compared to rectangular, contiguous, and Dorling cartograms.
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

If your filtering task matches the study’s condition where non-contiguous performed worst, **do not use a non-contiguous cartogram** for filtering; choose a higher-ranked alternative instead.

## The Logic <!-- role: reason -->

Under some filtering setups, non-contiguous cartograms can reduce accuracy relative to other cartogram types.

- **The Principle:** Use empirically worst-case avoidance: exclude designs that consistently underperform under a given task condition.
- **The Evidence:** For one filtering condition, accuracy rank is **E-2 (rectangular) > E-1 (contiguous) > E-4 (Dorling) > E-3 (non-contiguous)**, with significance pairs indicating E-3 is significantly worse than E-1, E-2, and E-4 [@nusratEvaluatingCartogramEffectiveness2018]. This kind of condition-specific rule extraction follows the collation approach in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly filter/select regions.
- **Data Type:** Quantitative values mapped to region area; geographic layout via positions.
- **Audience:** General audiences making region selections.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The filtering condition matches one where non-contiguous outperforms contiguous (as also reported in the same evidence).
- **Reason:** The paper includes at least one filter case where non-contiguous ranks above contiguous, so this is not universal [@nusratEvaluatingCartogramEffectiveness2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Avoiding non-contiguous may forgo benefits it provides in other contexts.
- **The Risk:** You may need additional logic (task/condition detection) to choose correctly across filtering variants.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking non-contiguous because it preserves shapes/looks familiar in outline.
- **Why it fails:** In the reported filtering condition, it is lowest-ranked for accuracy and significantly worse than several alternatives [@nusratEvaluatingCartogramEffectiveness2018], as captured through [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users repeatedly miss the correct set of regions during filtering.
- **The Test:** Compare error rates for non-contiguous vs. rectangular/contiguous/Dorling using the same filter prompts.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch away from non-contiguous to **rectangular** or **contiguous** for that filtering scenario.
- **Best Fix:** Implement task-condition-aware cartogram selection using collated comparative results as described in [@zengReviewCollationGraphical2023].
