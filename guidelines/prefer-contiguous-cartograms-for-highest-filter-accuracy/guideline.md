---
id: prefer-contiguous-cartograms-for-highest-filter-accuracy
title: Prefer contiguous cartograms for highest filtering accuracy (vs non-contiguous,
  Dorling, and rectangular)
bibliography: references.bib
description: Contiguous cartograms yielded the highest accuracy for some filtering
  judgments, outperforming other cartogram types in a controlled comparison.
labels:
- chart:cartogram
- task:filter
- visual:area
- visual:position
- impact:accuracy
- data:geospatial
- audience:general
- variant:contiguous
---

## Prefer contiguous cartograms for filtering accuracy <!-- role: advice -->

Prefer a contiguous cartogram when the primary requirement is high accuracy on filtering-style judgments among cartogram types. Use non-contiguous, Dorling, and rectangular cartograms only if you accept lower filtering accuracy for this scenario.

## Why contiguous cartograms can improve filtering accuracy here <!-- role: reason -->

When cartograms differ in how well they preserve recognizable geography and spatial relations, viewers can more reliably apply filtering judgments (finding items that meet conditions) when the depiction supports stable spatial reference and recognizable regions.

**Mechanism:** Better support for recognizing regions and their spatial arrangement reduces search and matching errors during filtering judgments.

**Evidence:** In one filtering condition, contiguous cartograms ranked highest in accuracy over non-contiguous, Dorling, and rectangular cartograms, with statistically significant pairwise differences reported among the ranked designs [@nusratEvaluatingCartogramEffectiveness2018; @zengReviewCollationGraphical2023].

**Notes:** This guideline applies to the specific filtering condition where the contiguous design ranked first; other filtering conditions in the same study showed different winners.

## When filtering-accuracy priority triggers this choice <!-- role: context -->

- **User Goal:** Identify which regions satisfy a stated condition with minimal mistakes.
- **Task:** Filter.
- **Data:** Geo-referenced regions with a quantitative variable encoded by area.
- **Chart Setting:** Static cartogram comparison among contiguous, non-contiguous, Dorling, and rectangular variants.
- **Audience:** General audiences doing quick correctness-focused judgments.
- **Success Criterion:** Higher task accuracy (fewer errors).

## When not to follow this filtering-accuracy rule <!-- role: exceptions -->

- **Break it when:** Your filtering situation matches a different filtering condition where a different cartogram type ranked higher in accuracy. **Why:** The observed accuracy ordering varies across filtering setups in the same evidence.

## Tradeoffs of prioritizing contiguous cartograms for filtering <!-- role: costs -->

**Sacrifice:** You may give up advantages other cartogram types show on other tasks or other filtering conditions. **Risk:** Over-generalizing one filtering result can produce mismatches when the filtering question format differs. **Mitigation:** Validate which filtering scenario your application most resembles before standardizing on this choice.

## Common mistakes when applying this rule <!-- role: mistakes -->

**Mistake:** Treating “filter” as a single uniform task and always defaulting to contiguous cartograms. **Why it fails:** The same study includes multiple filtering conditions with different accuracy rankings across cartogram types.

## Quick tests for filtering-fit <!-- role: check -->

**Failure Sign:** Users frequently pick the wrong qualifying region(s) despite clear conditions. **Quick Check:** Pilot two cartogram variants (contiguous vs your current choice) on representative filtering questions and compare error rates. **Stronger Test:** Run a small controlled A/B test on your actual filtering prompts and quantify accuracy differences.

## What to do instead if you can’t use a contiguous cartogram <!-- role: fix -->

- Use the non-contiguous cartogram if it is the best-performing option for the specific filtering condition you match.
- Use the rectangular cartogram if your filtering condition empirically aligns with its higher accuracy in that condition.
- Change the filtering prompt to better match the cartogram type you must use, then re-test accuracy.
- Provide an alternate view (a different cartogram type) for filtering steps while keeping your preferred cartogram for other tasks.
