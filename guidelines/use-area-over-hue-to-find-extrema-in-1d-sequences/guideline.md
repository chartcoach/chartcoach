---
id: use-area-over-hue-to-find-extrema-in-1d-sequences
title: Use Area (Size) Instead of Hue to Find Extrema
bibliography: references.bib
description: For finding minima/maxima in 1D ordered sequences, encoding magnitude
  by area is more accurate than by hue.
labels:
- chart:glyph
- chart:strip
- task:find-extremum
- visual:area
- visual:color-hue
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

For min/max (find-extremum) tasks on a 1D sequence, encode the quantitative values using **area/size** rather than **color hue**.

## The Logic <!-- role: reason -->

Area/size provides a more reliable magnitude cue than hue for identifying extremes in a sequence, improving accuracy.

- **The Principle:** More discriminable magnitude cues support extremum identification.
- **The Evidence:** Area (circle size) ranked highest and hue ranked lowest for find-extremum accuracy in the extracted results [@chungHowOrderedIt2016], as collated for visualization recommendation [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Find the smallest or largest element in a sequence.
- **Data Type:** Quantitative values along an ordinal sequence (X position indicates order).
- **Audience:** General audiences; scanning-focused tasks.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must avoid changing mark size due to strict layout constraints (e.g., overlap would obscure marks).
- **Reason:** The rule assumes size changes remain readable for the sequence format used in the study [@chungHowOrderedIt2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Space and potential occlusion (large marks can overlap neighbors).
- **The Risk:** Extremely large/small marks may dominate attention or become hard to compare if crowded.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using hue gradients to indicate magnitude and expecting users to spot minima/maxima reliably.
- **Why it fails:** Hue was the worst-ranked encoding for find-extremum accuracy in this context [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users miss the true min/max when hue is used, or disagree on which item is the smallest/largest.
- **The Test:** Convert the encoding from hue to size and rerun the same min/max questions; improved accuracy indicates hue was the bottleneck.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace hue encoding with circle size (area) while keeping the sequence order on X.
- **Best Fix:** Use area/size as the quantitative encoding for find-extremum in 1D sequences (the top-ranked design for accuracy) [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].
