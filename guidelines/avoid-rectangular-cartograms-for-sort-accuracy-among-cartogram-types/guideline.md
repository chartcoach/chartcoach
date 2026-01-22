---
id: avoid-rectangular-cartograms-for-sort-accuracy-among-cartogram-types
title: Avoid rectangular cartograms for sorting accuracy when contiguous, non-contiguous,
  or Dorling are available
bibliography: references.bib
description: Rectangular cartograms ranked worst for sorting accuracy compared with
  other cartogram types in tested sorting conditions.
labels:
- chart:cartogram
- task:sort
- visual:area
- visual:position
- impact:accuracy
- data:geospatial
- audience:general
- variant:rectangular
---

## Avoid rectangular cartograms for sorting accuracy <!-- role: advice -->

Avoid rectangular cartograms for sorting tasks when you can instead use contiguous, non-contiguous, or Dorling cartograms. If you must use a rectangular cartogram, expect lower sorting accuracy.

## Why rectangular cartograms can hurt sorting accuracy here <!-- role: reason -->

Sorting requires reliable comparative judgments across multiple regions; distortions in shape and layout that make regions harder to recognize or compare can increase ranking errors.

**Mechanism:** Layout and shape distortions increase cognitive load and comparison mistakes when ordering regions by value.

**Evidence:** In one sorting condition, contiguous, non-contiguous, and Dorling cartograms formed a top group while rectangular cartograms ranked worst, with significant pairwise differences showing each of the three outperforming rectangular in accuracy [@nusratEvaluatingCartogramEffectiveness2018; @zengReviewCollationGraphical2023]. In another sorting condition, rectangular cartograms again ranked last behind contiguous, non-contiguous, and Dorling cartograms, with multiple significant pairwise differences reported [@nusratEvaluatingCartogramEffectiveness2018; @zengReviewCollationGraphical2023].

**Notes:** Time rankings for sorting did not show significant differences in the provided results, so this guideline is about accuracy.

## When sorting is the key task <!-- role: context -->

- **User Goal:** Correctly order regions by a quantitative value.
- **Task:** Sort.
- **Data:** Geo-referenced regions with quantitative values encoded by area.
- **Chart Setting:** Choosing between cartogram types for a static display.
- **Audience:** General users performing ranking judgments.
- **Success Criterion:** Higher sorting accuracy.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot use non-rectangular cartograms due to a hard constraint in your system. **Why:** The tested alternatives may be unavailable even if they are more accurate for sorting.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose any benefits a rectangular cartogram provides for other, non-sorting tasks in your workflow. **Risk:** Users may trust an incorrect ordering if the map looks authoritative. **Mitigation:** Add validation steps or alternate views when ordering decisions are consequential.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Using a rectangular cartogram to sort “because it looks clean and grid-like.” **Why it fails:** The tested evidence shows lower sorting accuracy versus other cartogram types.

## Quick tests <!-- role: check -->

**Failure Sign:** Users frequently mis-rank regions or swap close ranks. **Quick Check:** Ask users to identify the top few regions using rectangular vs contiguous (or Dorling/non-contiguous) and compare accuracy. **Stronger Test:** Log ranking agreement with ground truth across cartogram types in an A/B test.

## What to do instead <!-- role: fix -->

- Use a contiguous cartogram for sorting when accuracy is paramount.
- Use a non-contiguous cartogram or Dorling cartogram if contiguous is unavailable, and validate accuracy with a pilot.
- Provide an alternate cartogram type specifically for sorting steps in the workflow.
- Reduce reliance on sorting within the cartogram by offering a separate ranked list view alongside the map.
