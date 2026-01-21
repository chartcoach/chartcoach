---
id: prefer-non-contiguous-cartograms-over-contiguous-for-filter-accuracy-in-specific-filter-setting
title: Use Non-Contiguous Cartograms When They Improve Filtering Accuracy
bibliography: references.bib
description: In one filtering setup, non-contiguous cartograms outperformed contiguous
  cartograms in accuracy.
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

When choosing between the two, use a **non-contiguous cartogram** instead of a contiguous cartogram if you are in a filtering scenario matching the study condition where non-contiguous is more accurate.

## The Logic <!-- role: reason -->

Some filtering scenarios can invert the preferred cartogram type; the empirical rank shows non-contiguous beating contiguous in one filtering condition.

- **The Principle:** Treat cartogram-type choice as task- and condition-dependent rather than universal.
- **The Evidence:** For a reported filtering condition, accuracy is ranked **E-3 (non-contiguous) > E-1 (contiguous)** with a significant difference reported [@nusratEvaluatingCartogramEffectiveness2018]. This conditional extraction is consistent with the collation framing in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Filter/select regions correctly under the same kind of filtering condition tested.
- **Data Type:** Geo regions with quantitative value encoded by area; map-like layout via position.
- **Audience:** General audiences performing region selection.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need a cartogram type supported by broader evidence for filtering across conditions, or you cannot ascertain which filtering condition matches.
- **Reason:** The paper reports multiple filtering outcomes with different rankings; applying this rule without matching the condition risks choosing the wrong type [@nusratEvaluatingCartogramEffectiveness2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Non-contiguous layouts can reduce map “continuity,” potentially affecting other tasks not covered by this specific rule.
- **The Risk:** If your filtering task doesn’t match the tested condition, you may increase errors instead of reducing them [@nusratEvaluatingCartogramEffectiveness2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Generalizing “non-contiguous is best for filtering” to all filter tasks.
- **Why it fails:** Other filtering results in the same evidence base rank contiguous highest, demonstrating inconsistency across conditions [@nusratEvaluatingCartogramEffectiveness2018], as surfaced by [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users are slower or make more wrong selections after switching cartogram types.
- **The Test:** A/B test contiguous vs. non-contiguous with your exact filter questions and measure error rate.

## How to Fix <!-- role: fix -->

- **Quick Fix:** If error rises, revert to **contiguous** cartograms for filtering.
- **Best Fix:** Make cartogram selection conditional on the exact filter-task structure you support, using the “store multiple outcomes per task” approach emphasized in [@zengReviewCollationGraphical2023].
