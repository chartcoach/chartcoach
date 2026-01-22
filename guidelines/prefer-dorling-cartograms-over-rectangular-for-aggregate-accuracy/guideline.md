---
id: prefer-dorling-cartograms-over-rectangular-for-aggregate-accuracy
title: Prefer Dorling cartograms over rectangular cartograms for aggregation accuracy
bibliography: references.bib
description: Dorling cartograms outperformed rectangular cartograms in accuracy for
  an aggregation task.
labels:
- chart:cartogram
- task:aggregate
- visual:area
- visual:position
- impact:accuracy
- data:geospatial
- audience:general
- variant:dorling
---

## Prefer Dorling cartograms over rectangular cartograms for aggregation accuracy <!-- role: advice -->

Prefer a Dorling cartogram over a rectangular cartogram when users must answer aggregation questions accurately from a cartogram. If you must use rectangular cartograms, expect lower aggregation accuracy than at least Dorling and non-contiguous options.

## Why Dorling can outperform rectangular for aggregation here <!-- role: reason -->

Aggregation judgments depend on mentally combining values across multiple regions; a representation that supports rapid extraction of overall magnitudes can reduce errors.

**Mechanism:** A visually consistent mark shape can make it easier to scan and combine perceived magnitudes across regions.

**Evidence:** For an aggregation task, Dorling cartograms ranked highest and rectangular cartograms ranked lowest in accuracy, and both Dorling-over-rectangular and non-contiguous-over-rectangular accuracy differences were reported as significant [@nusratEvaluatingCartogramEffectiveness2018; @zengReviewCollationGraphical2023].

**Notes:** Time rankings for aggregation did not show significant differences in the provided results, so this guideline targets accuracy.

## When aggregation accuracy drives the design choice <!-- role: context -->

- **User Goal:** Correctly compute or compare aggregate amounts across regions.
- **Task:** Aggregate.
- **Data:** Geo-referenced regions with quantitative values encoded by area.
- **Chart Setting:** Static cartogram selection among Dorling, rectangular, and other cartogram variants.
- **Audience:** Users making correctness-sensitive summary judgments.
- **Success Criterion:** Higher aggregation accuracy.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your aggregation questions require preserved adjacency or exact region shapes as part of the judgment. **Why:** Dorling cartograms do not preserve those properties, and the evidence here only covers aggregation accuracy.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose map-like recognition benefits that other cartogram types provide. **Risk:** Users may misinterpret the geography if they expect preserved shapes or adjacencies. **Mitigation:** Pair the cartogram with supporting geographic context when necessary.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Using rectangular cartograms for aggregation because they appear orderly and grid-based. **Why it fails:** The tested aggregation accuracy ranking places rectangular lowest, with significant disadvantages versus Dorling (and non-contiguous).

## Quick tests <!-- role: check -->

**Failure Sign:** Users’ aggregate answers are frequently wrong even when they have enough time. **Quick Check:** Compare aggregate-task accuracy on Dorling vs rectangular cartograms using representative questions. **Stronger Test:** Run a within-subject experiment on your aggregation prompts and compute accuracy differences.

## What to do instead <!-- role: fix -->

- Use a Dorling cartogram when aggregation accuracy is a key requirement.
- Use a non-contiguous cartogram instead of rectangular if Dorling is not suitable and accuracy is still prioritized.
- Provide a separate summary view that computes aggregates and use the cartogram only for context.
- Maintain different cartogram defaults for different tasks, switching to Dorling specifically for aggregation steps.
