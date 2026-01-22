---
id: prefer-contiguous-cartograms-for-best-sort-accuracy-in-tested-condition
title: Prefer contiguous cartograms for highest sorting accuracy in a tested sorting
  condition (vs non-contiguous, Dorling, and rectangular)
bibliography: references.bib
description: Contiguous cartograms ranked highest in accuracy for a sorting condition,
  outperforming other cartogram types.
labels:
- chart:cartogram
- task:sort
- visual:area
- visual:position
- impact:accuracy
- data:geospatial
- audience:general
- variant:contiguous
---

## Prefer contiguous cartograms for sorting accuracy in the condition they win <!-- role: advice -->

Prefer a contiguous cartogram for sorting when your sorting question format matches a condition where contiguous cartograms are the most accurate among cartogram types. Treat this as sorting-condition-specific rather than universal for all ranking prompts.

## Why contiguous cartograms can improve sorting accuracy in some setups <!-- role: reason -->

Sorting across many regions depends on consistent visual comparison and region identification; preserving map structure can reduce misidentification and ordering mistakes.

**Mechanism:** More stable geographic structure can reduce comparison errors when ordering regions by value.

**Evidence:** In one sorting condition, contiguous cartograms ranked highest in accuracy over non-contiguous, Dorling, and rectangular cartograms, with significant pairwise differences reported that included contiguous outperforming each other type [@nusratEvaluatingCartogramEffectiveness2018; @zengReviewCollationGraphical2023].

**Notes:** Another sorting condition grouped contiguous with other non-rectangular cartograms rather than placing it alone at the top.

## When this sorting-condition rule applies <!-- role: context -->

- **User Goal:** Correctly rank regions by a quantitative variable.
- **Task:** Sort.
- **Data:** Regions whose values are encoded by area within the cartogram.
- **Chart Setting:** Static cartogram display with a fixed sorting prompt format.
- **Audience:** Users who need correct ordering more than aesthetic novelty.
- **Success Criterion:** Higher sorting accuracy for the specific sorting prompt type.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your sorting prompt matches a condition where contiguous is not uniquely best (or where another type ties/leads). **Why:** Sorting accuracy rankings vary across sorting conditions.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose advantages other cartogram types provide for other tasks in your workflow. **Risk:** If your sorting prompt differs from the tested condition, performance gains may not materialize. **Mitigation:** Validate on your sorting prompt set before committing.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Assuming one cartogram type is always best for sorting regardless of prompt design. **Why it fails:** The evidence includes multiple sorting conditions with different ranking structures.

## Quick tests <!-- role: check -->

**Failure Sign:** Users’ sorted answers disagree with the true order more than expected. **Quick Check:** Compare accuracy on your sorting prompts using contiguous vs Dorling (or non-contiguous) cartograms. **Stronger Test:** Run a within-subject experiment that mirrors your prompt format and measure sorting error rates.

## What to do instead <!-- role: fix -->

- Use a non-contiguous or Dorling cartogram if your sorting condition shows comparable accuracy to contiguous in your tests.
- Offer multiple cartogram types and let users switch when sorting is difficult.
- Supplement the cartogram with a separate sortable table or ranked list for ordering tasks.
- Narrow the sorting task (e.g., top few vs full ordering) and re-evaluate which cartogram type yields the best accuracy.
