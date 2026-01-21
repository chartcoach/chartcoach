---
id: prefer-contiguous-cartograms-over-dorling-and-rectangular-for-correlation-accuracy
title: Prefer Contiguous Cartograms for Correlation Accuracy
bibliography: references.bib
description: For correlation judgments in cartograms, contiguous cartograms produced
  higher accuracy than Dorling and rectangular cartograms in the reported results.
labels:
- chart:cartogram
- task:correlate
- visual:area
- visual:position
- impact:accuracy
- data:geospatial
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When users must judge **correlation over space/time** (as tested), choose a **contiguous cartogram** rather than Dorling or rectangular cartograms.

## The Logic <!-- role: reason -->

Correlation judgments depend on correctly interpreting spatial patterns and relative region magnitudes; the measured accuracy ranks contiguous highest among the reported set for the correlation task.

- **The Principle:** Choose the cartogram type with empirically higher accuracy for correlation judgments.
- **The Evidence:** For the correlate task, accuracy rank is **E-1 (contiguous) > E-4 (Dorling) > E-2 (rectangular)** with significant differences reported for each pair in that order [@nusratEvaluatingCartogramEffectiveness2018]. This is included as structured evidence in the collation pipeline described in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Determine which spatial side/area is more associated with higher values (a correlation-style judgment as captured in the dataset).
- **Data Type:** Geo regions with quantitative values encoded by area.
- **Audience:** General audiences interpreting geographic patterns.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are selecting among cartogram types not compared in the reported correlate ranking (e.g., non-contiguous not present in the correlate ranking here).
- **Reason:** The evidence provided only ranks E-1, E-4, and E-2 for correlation; it does not support conclusions about other variants in this task entry [@nusratEvaluatingCartogramEffectiveness2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may not get the best performance for aggregation tasks (where Dorling ranks higher in accuracy in the reported results).
- **The Risk:** If your “correlate” task differs from the tested correlate setup, gains may not transfer.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Defaulting to rectangular cartograms for any “analytical” task because they appear structured.
- **Why it fails:** Rectangular is lowest-ranked among the reported set for correlation accuracy (E-2 is worse than E-4 and E-1) [@nusratEvaluatingCartogramEffectiveness2018], consistent with the collation goal of avoiding weak designs [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users disagree widely or answer incorrectly on correlation questions using Dorling/rectangular designs.
- **The Test:** Run the same correlation question set on contiguous vs. Dorling vs. rectangular and compare accuracy.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the correlate view to a **contiguous cartogram**.
- **Best Fix:** Provide task-aware defaults: contiguous for correlation, other types only when the user’s task changes, using collated rankings as in [@zengReviewCollationGraphical2023; @nusratEvaluatingCartogramEffectiveness2018].
