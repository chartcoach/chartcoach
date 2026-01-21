---
id: avoid-shape-for-speed-in-find-extremum-in-1d-sequences
title: Avoid Shape When You Need Fast Extrema Identification
bibliography: references.bib
description: For fast min/max identification in 1D ordered sequences, shape encoding
  is slow and should be avoided.
labels:
- chart:glyph
- chart:strip
- task:find-extremum
- visual:shape
- impact:speed
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

If speed matters for finding minima/maxima in a 1D sequence, **do not encode magnitude with shape**.

## The Logic <!-- role: reason -->

Shape decoding can be slower for extremum judgments in the tested setup, increasing response time compared to other channels.

- **The Principle:** Higher cognitive decoding cost slows time-critical judgments.
- **The Evidence:** Shape was ranked slowest (worst) for time in the find-extremum task in the extracted results [@chungHowOrderedIt2016], as documented in the collation dataset for recommendation contexts [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly identify the smallest or largest element.
- **Data Type:** Quantitative values in a left-to-right sequence.
- **Audience:** Any audience in time-constrained workflows.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Accuracy is the only goal and timing is irrelevant for your use case.
- **Reason:** This guideline is specifically about response time (speed), not accuracy [@chungHowOrderedIt2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose a potentially usable channel for representing ordered values when other channels are occupied.
- **The Risk:** Replacing shape with another channel (e.g., size) may introduce space/occlusion issues.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using many distinct shapes to encode a quantitative progression and expecting quick min/max pick-out.
- **Why it fails:** The extracted timing results show shape as the slowest condition for this extremum task [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users take noticeably longer to answer “which is smallest/largest?” when shape varies.
- **The Test:** Time a small pilot (even informal) on min/max questions; if shape is the bottleneck, switching encodings should reduce completion time.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace shape encoding with a faster channel from the tested set (e.g., saturation or orientation) depending on your constraints.
- **Best Fix:** Choose an encoding that supports faster min/max judgments (shape was worst by time in this context) [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].
