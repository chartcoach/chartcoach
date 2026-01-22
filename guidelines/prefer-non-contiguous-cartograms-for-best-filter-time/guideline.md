---
id: prefer-non-contiguous-cartograms-for-best-filter-time
title: Prefer non-contiguous cartograms for fastest filtering time (vs contiguous,
  Dorling, and rectangular)
bibliography: references.bib
description: Non-contiguous cartograms produced the fastest completion time for a
  filtering condition, beating other cartogram types.
labels:
- chart:cartogram
- task:filter
- visual:area
- visual:position
- impact:speed
- data:geospatial
- audience:general
- variant:non-contiguous
---

## Prefer non-contiguous cartograms for filtering speed <!-- role: advice -->

Prefer a non-contiguous cartogram when you need the fastest completion time for a filtering-style judgment among cartogram types. Avoid rectangular cartograms for this filtering-speed scenario.

## Why non-contiguous cartograms can speed filtering here <!-- role: reason -->

A design that reduces visual clutter or interference between neighboring shapes can make it faster to locate and evaluate candidate regions during filtering, even if it changes adjacency relationships.

**Mechanism:** Reduced crowding and separation between regions can lower search time for identifying qualifying items.

**Evidence:** In one filtering condition, non-contiguous cartograms ranked fastest in time, and were significantly faster than rectangular and Dorling cartograms for that condition (with additional significant differences involving rectangular) [@nusratEvaluatingCartogramEffectiveness2018; @zengReviewCollationGraphical2023].

**Notes:** This is a speed guideline; the corresponding accuracy ranking for filtering may differ.

## When filtering speed is the primary constraint <!-- role: context -->

- **User Goal:** Quickly identify regions meeting a condition, even if some accuracy loss is acceptable.
- **Task:** Filter.
- **Data:** Geo-referenced regions with a quantitative variable encoded by area.
- **Chart Setting:** Static cartogram selection among contiguous, non-contiguous, Dorling, and rectangular variants.
- **Audience:** Users doing time-sensitive scanning.
- **Success Criterion:** Lower completion time.

## When not to follow this speed-first rule <!-- role: exceptions -->

**Break it when:** Accuracy is more important than speed for your filtering decisions. **Why:** The fastest design is not necessarily the most accurate in the same filtering context.

## Tradeoffs of choosing non-contiguous cartograms for speed <!-- role: costs -->

**Sacrifice:** You may lose support for tasks that depend on preserved adjacency relationships. **Risk:** Faster responses can come with more mistakes if users rely on adjacency cues. **Mitigation:** Pair the fast view with a secondary view for verification when correctness matters.

## Common mistakes when applying this rule <!-- role: mistakes -->

**Mistake:** Choosing the fastest filtering design and assuming it is also best for filtering accuracy. **Why it fails:** The evidence separates time and accuracy outcomes, and the rankings do not necessarily align.

## Quick tests for a speed win <!-- role: check -->

**Failure Sign:** Users take notably longer to finish filtering tasks without improving correctness. **Quick Check:** Time a small set of representative filtering questions on non-contiguous vs your current cartogram type. **Stronger Test:** Run a within-subject timing study using your real tasks and compare median completion time.

## What to do instead if non-contiguous cartograms are unsuitable <!-- role: fix -->

- Use a contiguous cartogram if accuracy is the governing success criterion for filtering in your scenario.
- Use a Dorling cartogram if your filtering prompt does not rely on adjacency and you can accept its time performance.
- Use a rectangular cartogram only if your filtering condition matches a case where it performs well, and confirm with timing tests.
- Split workflows: use non-contiguous cartograms for initial filtering, then switch to a different cartogram type for confirmation.
