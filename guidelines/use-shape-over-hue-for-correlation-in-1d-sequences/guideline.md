---
id: use-shape-over-hue-for-correlation-in-1d-sequences
title: Use Shape Instead of Hue for Correlation Judgments
bibliography: references.bib
description: For correlation judgments in 1D ordered sequences, shape encoding performs
  more accurately than hue encoding.
labels:
- chart:glyph
- chart:strip
- task:correlate
- visual:shape
- visual:color-hue
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When asking users to judge correlation in a 1D sequence, encode the quantitative values with **shape** rather than **color hue**.

## The Logic <!-- role: reason -->

In the studied 1D sequence setting, shape supports more accurate correlation judgments than hue, consistent with the idea that more orderable cues improve ordering-related judgments.

- **The Principle:** Orderable encodings improve ordering/correlation task accuracy.
- **The Evidence:** Shape ranked above hue for correlation accuracy in the extracted results [@chungHowOrderedIt2016], captured as structured knowledge for recommendation use [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Assess whether a sequence appears ordered/correlated.
- **Data Type:** Quantitative values mapped to a non-position channel; ordinal sequence on X.
- **Audience:** General audiences doing quick pattern judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Shapes are being used already to encode categories (nominal groups).
- **Reason:** This rule is about using shape as the quantitative/ordered cue; reusing shape may cause ambiguity not evaluated here [@chungHowOrderedIt2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Potential increase in cognitive effort (shape decoding can be slower in some situations).
- **The Risk:** If shape steps are not clearly distinguishable, the ordered mapping may degrade.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using hue to suggest an ordered quantitative progression.
- **Why it fails:** Hue was ranked worst for correlation accuracy in this context [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users frequently misjudge ordering/correlation when hue is used to encode magnitude.
- **The Test:** Replace the hue scale with a stepped shape encoding and compare user accuracy on the same correlation questions.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap hue encoding for a discrete ordered shape progression.
- **Best Fix:** Use the higher-ranked encoding family (shape rather than hue) for correlation judgments in 1D sequences [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].
