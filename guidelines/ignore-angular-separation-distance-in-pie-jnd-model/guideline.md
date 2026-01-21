---
id: ignore-angular-separation-distance-in-pie-jnd-model
title: Ignore Angular Separation as a Driver of JND in Pie Charts
bibliography: references.bib
description: Do not treat angular separation between slices as a primary predictor
  of JND; it showed no significant main effect.
labels:
- chart:pie
- task:sort
- visual:angle
- impact:clarity
- data:quantitative
- audience:general
- perception:jnd
- complexity:advanced
---

## The Rule <!-- role: advice -->

Do not use angular separation between the two compared slices as the primary predictor in a pie-chart JND model.

## The Logic <!-- role: reason -->

In the reported pie-chart results, separation distance (angular distance between slices) did not have a significant main effect on JND, while intensity (slice angle) did.

- **The Principle:** Not all spatial separations drive discriminability; in this context, angular distance is not the dominant factor for JND.
- **The Evidence:** Lu et al.’s pie-chart findings, as captured in the Zeng & Battle collation, indicate no significant main effect of separation distance on JND in pie charts [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## Where to Apply <!-- role: context -->

- **User Goal:** Sorting/ranking by comparing slice magnitudes.
- **Data Type:** Quantitative values encoded via angles; categories differentiated by color hue.
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your pie-chart design differs materially from the studied one (e.g., different numbers of slices or different interaction/annotation behavior).
- **Reason:** This guideline is strictly derived from the reported experiment context and should not be generalized beyond it without validation [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may miss secondary effects not modeled here.
- **The Risk:** If angular separation matters in your specific layout/context, excluding it could reduce accuracy of your JND predictions.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reordering slices primarily to change adjacency, assuming it will improve discriminability of close values.
- **Why it fails:** The evidence (in this experiment context) does not support angular separation as a main driver of JND [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Moving two slices farther apart around the circle does not noticeably improve the ability to tell their sizes apart.
- **The Test:** Hold slice angles constant and vary their angular separation; if discriminability is stable, angular separation is not the primary JND driver [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Focus your discriminability checks on slice angles rather than their separation.
- **Best Fix:** Build pie-chart JND logic around intensity (slice angle) and validate whether adding separation improves prediction in your specific setting [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].
