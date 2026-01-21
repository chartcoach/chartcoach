---
id: use-color-saturation-over-hue-for-correlation-in-1d-sequences
title: Use Color Saturation Instead of Hue for Correlation Judgments
bibliography: references.bib
description: For correlation judgments in 1D ordered sequences, encode magnitude with
  color saturation rather than hue to improve accuracy.
labels:
- chart:glyph
- chart:strip
- task:correlate
- visual:color-saturation
- visual:color-hue
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When the task is to judge correlation in a 1D ordered sequence, encode the quantitative values using **color saturation (value/lightness)** rather than **color hue**.

## The Logic <!-- role: reason -->

Using saturation supports perceiving an ordered magnitude scale more reliably than hue, which increases accuracy for judging correlation in sequences.

- **The Principle:** Perceptual orderability supports accurate pattern judgments.
- **The Evidence:** In collated results, color-saturation encoding ranked higher than color-hue for correlation accuracy in 1D sequences [@chungHowOrderedIt2016], as recorded and structured for recommendation use [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Determine correlation (orderedness) from a left-to-right sequence.
- **Data Type:** One quantitative attribute arranged by an ordinal sequence position (e.g., time/order on X).
- **Audience:** General audiences performing quick visual judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need hue to represent **categories** (distinct groups) rather than ordered magnitude.
- **Reason:** This rule is specific to using hue as a quantitative/ordered encoding for correlation judgments in the studied setup [@chungHowOrderedIt2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Lower semantic distinctiveness across many categories (saturation is not primarily categorical).
- **The Risk:** If saturation steps are too subtle, differences may be hard to see, undermining the intended order cue.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a rainbow/multi-hue scale to imply increasing magnitude for correlation.
- **Why it fails:** Hue was the lowest-ranked option for correlation accuracy in the reported ranking, indicating reduced reliability for ordered judgments in this context [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers hesitate or disagree about whether the sequence “looks ordered” or correlated.
- **The Test:** Swap hue for a single-hue saturation ramp; if accuracy/consistency improves in a quick pilot, hue was likely hurting correlation perception in this use case.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the hue scale with a monotonic saturation/value scale for the quantitative attribute.
- **Best Fix:** Keep ordinal position on X, and encode magnitude with saturation (as in the higher-ranked design for correlation accuracy) [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].
