---
id: prefer-texture-over-hue-for-correlation-in-1d-sequences
title: Prefer Texture Over Hue for Correlation Judgments
bibliography: references.bib
description: For correlation judgments in 1D ordered sequences, texture encoding yields
  higher accuracy than hue encoding.
labels:
- chart:glyph
- chart:strip
- task:correlate
- visual:texture
- visual:color-hue
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

For correlation judgments in a 1D sequence, use **texture** to encode the quantitative attribute instead of **color hue**.

## The Logic <!-- role: reason -->

Texture provides a more reliably orderable perceptual cue than hue in the tested sequence setting, improving correlation judgment accuracy.

- **The Principle:** More orderable channels better support accurate ordering/correlation judgments.
- **The Evidence:** Texture ranked above hue for correlation accuracy in the extracted ranking [@chungHowOrderedIt2016], as collated into structured guidance for recommendation systems [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Judge correlation/orderedness from a left-to-right sequence of marks.
- **Data Type:** Quantitative values encoded on marks; ordinal index on X.
- **Audience:** General audiences; quick perceptual judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your medium cannot render texture crisply (e.g., very small marks where texture collapses).
- **Reason:** The rule depends on texture being visually discriminable as an ordered cue in the studied stimulus style [@chungHowOrderedIt2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Visual simplicity (texture can add clutter).
- **The Risk:** Moiré/aliasing or busy patterns can distract, especially at small sizes.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using hue gradients to imply order for correlation judgments.
- **Why it fails:** Hue was the lowest-ranked channel for correlation accuracy in this task context [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The sequence’s ordering is hard to perceive even when data is strongly ordered/correlated.
- **The Test:** Replace hue with a stepped texture scale and retest a small sample of users on the correlation judgment task.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap hue encoding for texture encoding while keeping the same positional ordering.
- **Best Fix:** Use a texture encoding scheme with clearly discriminable steps (matching the higher-performing condition for correlation accuracy) [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].
