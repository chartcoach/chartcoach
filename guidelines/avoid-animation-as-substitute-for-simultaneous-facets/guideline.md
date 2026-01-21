---
id: avoid-animation-as-substitute-for-simultaneous-facets
title: Avoid Using Animation as a Substitute for Seeing Multiple Facets at Once
bibliography: references.bib
description: Do not rely on temporal substitution (animation) to show facets; prefer
  simultaneous visibility for analytical tasks.
labels:
- chart:animated
- task:analyze
- visual:time
- impact:accuracy
- data:multifaceted
- audience:expert
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Do not use animation to cycle through facets when users need analytical comparison; keep relevant facets visible simultaneously.

## The Logic <!-- role: reason -->

Animated views are temporal and substitutive: one state replaces another. For analytical work on complex data, users must recall prior states, which can overload short-term memory and lead to inaccurate understanding of trends as data increases. [@olaSimpleChartsDesign2016]

- **The Principle:** Reduce reliance on memory during analysis
- **The Evidence:** [@olaSimpleChartsDesign2016]

## Where to Apply <!-- role: context -->

- **User Goal:** Analytical comparison across facets or time (detect trends, compare groups, validate hypotheses)
- **Data Type:** Multivariate health indicators, large datasets with multiple levels/relationships
- **Audience:** Analysts and professionals performing non-routine investigations

## When to Break It <!-- role: exceptions -->

- **Scenario:** The goal is narrative storytelling or a guided presentation where the user is not asked to compare many states precisely.
- **Reason:** Animation can be acceptable for narrative tasks, but is less effective for analytical tasks requiring recall and precise comparison. [@olaSimpleChartsDesign2016]

## The Price <!-- role: costs -->

- **The Sacrifice:** More screen space or denser visuals when multiple facets are shown together.
- **The Risk:** Without careful organization, simultaneous views can become cluttered. [@olaSimpleChartsDesign2016]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding a “play” control to show different facets one after another and assuming users will integrate them mentally.
- **Why it fails:** Users must remember previous frames; cognitive load rises and trend judgments become unreliable. [@olaSimpleChartsDesign2016]

## How to Check <!-- role: check -->

- **Visual Sign:** Users pause/rewind repeatedly to compare states or ask for “side-by-side.”
- **The Test:** Freeze the animation at any point—if users cannot compare needed facets without replaying, the design violates the rule. [@olaSimpleChartsDesign2016]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide a static “compare” mode that pins multiple states/facets side-by-side.
- **Best Fix:** Encode multiple facets within an integrated structure (e.g., layered/stacked/linked representations) so comparison is perceptual rather than memory-based. [@olaSimpleChartsDesign2016]
