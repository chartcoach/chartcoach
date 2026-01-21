---
id: use-small-multiple-maps-for-faster-distribution-characterization-in-geopropagation
title: Use Small-Multiple Maps When Speed Matters for Distribution Characterization
bibliography: references.bib
description: For distribution-characterization tasks, small-multiple maps were faster
  than a proportional-symbol map in the collated study outcomes.
labels:
- chart:small-multiples
- task:characterize-distribution
- visual:color-saturation
- visual:position
- impact:speed
- data:geospatial
- data:temporal
- audience:expert
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use small-multiple maps rather than a proportional-symbol map when the primary goal is faster completion on characterize-distribution tasks.

## The Logic <!-- role: reason -->

Small multiples can support quick scanning across time steps for distribution-related judgments, reducing time even if accuracy is not improved.

- **The Principle:** Speed via rapid visual scanning across juxtaposed frames.
- **The Evidence:** The collated results rank small-multiple maps (E-1) faster than proportional-symbol map (E-2) for characterize-distribution time, with a recorded significant pair E-1 > E-2 in [@pena-arayaComparisonGeographicalPropagation2020], as captured by [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly characterizing distribution patterns (time-sensitive analytic work).
- **Data Type:** Geo-temporal propagation shown over multiple time steps.
- **Audience:** Analysts working under time constraints.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When accuracy in distribution characterization is the priority.
- **Reason:** The collated record ranks proportional-symbol map (E-2) above small multiples (E-1) for characterize-distribution accuracy (no reported significant pair).

## The Price <!-- role: costs -->

- **The Sacrifice:** Possible reduction in accuracy for distribution characterization.
- **The Risk:** Users may answer faster but less correctly depending on the distribution prompt.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using small multiples as the default for all distribution work.
- **Why it fails:** The speed advantage does not imply an accuracy advantage; the collated rankings differ by metric.

## How to Check <!-- role: check -->

- **Visual Sign:** Users answer quickly but with more mistakes on distribution questions.
- **The Test:** Track both completion time and error rate; if errors rise, prefer the accuracy-oriented alternative.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Keep small multiples but add an optional single-map alternative for careful checking.
- **Best Fix:** Use task-adaptive defaults: small multiples for speed-first distribution scanning; proportional-symbol map when correctness is paramount.
