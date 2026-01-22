---
id: use-track-and-stack-to-align-subvisualizations-by-a-shared-dimension
title: Use track-and-stack layout to align sub-visualizations by a shared dimension
  (e.g., age) while preserving separation
bibliography: references.bib
description: Arrange multiple facet-specific subviews in concentric tracks and stacked
  alignment to support simultaneous cross-facet comparison.
labels:
- task:compare
- task:explore
- visual:layout
- impact:orientation
- data:multifaceted
- audience:expert
- complexity:advanced
- domain:health
---

## Align multiple facet views using shared tracks around a common reference <!-- role: advice -->

When several sub-visualizations share a key dimension (such as age group), place them in track-like lanes and stack them so the shared dimension aligns across the subviews.

## Why track-and-stack supports cross-facet orientation <!-- role: reason -->

A track layout preserves the identity of each facet-specific subview, while stacking aligned structures makes co-occurrence across subviews perceptually available, reducing the effort of matching categories between facets.

**Mechanism:** Shared alignment creates perceptual correspondences across facets, enabling users to compare and relate values without repeatedly re-mapping categories.

**Evidence:** A demography visualization organized age, causes, risks, and locations into concentric tracks with stacked alignment so common age groups co-occur across sub-visualizations, supporting simultaneous independent and joint exploration; the integrated view initially encoded hundreds of selectable items and revealed latent detail through interaction [@olaSimpleChartsDesign2016].

**Notes:** Track-and-stack can be applied at the level of sub-visualizations, not only individual marks.

## When this applies in health data visualization <!-- role: context -->

- **User Goal:** Compare how different facets behave for the same categories (e.g., how causes and risks vary by age).
- **Task:** Cross-facet comparison, spotting co-occurring patterns.
- **Data:** Multiple facets sharing a common categorical backbone.
- **Chart Setting:** Interactive multi-facet analytic views where users need stable landmarks.
- **Audience:** Analysts and practitioners doing exploratory analysis.
- **Success Criterion:** Users can move between facets without losing alignment of the shared categories.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The facets do not share a stable dimension or the shared categories differ across facets. **Why:** Forced alignment can imply false correspondence and confuse interpretation [@olaSimpleChartsDesign2016].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Space efficiency; aligned tracks can consume substantial area. **Risk:** Dense tracks can reduce readability of small marks. **Mitigation:** Use interaction to focus on selected categories and simplify the default view.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Putting related facet views in separate, unaligned regions of the screen. **Why it fails:** Users must mentally map the shared categories across views, increasing cognitive load [@olaSimpleChartsDesign2016].

## Quick tests <!-- role: check -->

**Failure Sign:** Users frequently mis-associate values between facets for the same category. **Quick Check:** Ask a user to compare two facets for one category; if they must hunt for the category twice, alignment is weak. **Stronger Test:** Time cross-facet comparison tasks and compare performance with an aligned vs unaligned layout.

## What to do instead <!-- role: fix -->

- Choose a shared categorical backbone (e.g., age groups) and reuse it as the organizing scaffold across subviews.
- Place facet-specific encodings into track-like lanes that share the same reference ordering.
- Stack the lanes so categories line up and co-occur perceptually.
- Use a central relational subview (e.g., links among facets) to connect the aligned tracks when relationship exploration is required.
