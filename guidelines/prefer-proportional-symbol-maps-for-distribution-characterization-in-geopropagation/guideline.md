---
id: prefer-proportional-symbol-maps-for-distribution-characterization-in-geopropagation
title: Use Proportional-Symbol Maps to Better Characterize Distributions
bibliography: references.bib
description: For distribution-characterization tasks, a proportional-symbol map ranked
  higher than small-multiple maps in the collated study outcomes.
labels:
- chart:map
- task:characterize-distribution
- visual:color-saturation
- visual:position
- impact:accuracy
- data:geospatial
- data:temporal
- audience:expert
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a proportional-symbol map rather than small-multiple maps when your task is to characterize a distribution.

## The Logic <!-- role: reason -->

A single consolidated view can make it easier to judge overall distributional patterns without integrating across many panels.

- **The Principle:** Reduce integration effort across multiple small panels for distribution judgments.
- **The Evidence:** In the collated experimental results, proportional-symbol map (E-2) ranks above small-multiple maps (E-1) for characterize-distribution accuracy in [@pena-arayaComparisonGeographicalPropagation2020], as structured in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Characterizing distributions in propagation data (overall pattern/spread).
- **Data Type:** Geo-temporal values mapped to regions (sequential color encoding present in both designs).
- **Audience:** Expert or analytic users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When completion time is more important than accuracy for distribution characterization.
- **Reason:** The same collated record ranks small-multiple maps (E-1) faster than proportional-symbol maps (E-2) for characterize-distribution time, with a reported significant pair favoring E-1 over E-2.

## The Price <!-- role: costs -->

- **The Sacrifice:** Potentially slower task completion.
- **The Risk:** Users may take longer to answer distribution questions even if accuracy improves.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing proportional-symbol maps for distribution tasks without checking time cost.
- **Why it fails:** The collated evidence indicates a speed disadvantage for proportional-symbol maps on this task.

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate or repeatedly re-check before answering distribution questions.
- **The Test:** Compare time-to-answer and correctness between both views on a few representative distribution prompts.

## How to Fix <!-- role: fix -->

- **Quick Fix:** If accuracy is needed, switch the default distribution view to proportional symbols.
- **Best Fix:** Offer a toggle: proportional-symbol map for accuracy-first distribution work; small multiples for speed-first scanning.
