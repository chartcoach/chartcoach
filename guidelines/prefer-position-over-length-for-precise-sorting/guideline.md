---
id: prefer-position-over-length-for-precise-sorting
title: Prefer Position Over Length for Precise Sorting
bibliography: references.bib
description: For sorting quantitative values, encode magnitude by position on a shared
  scale rather than bar length.
labels:
- chart:bar
- task:sort
- visual:position
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception
---

## The Rule <!-- role: advice -->

When users must sort quantitative values, encode the values by **position on a common scale** (e.g., aligned bars) rather than by **length** (e.g., stacked-bar segments that require length judgments).

## The Logic <!-- role: reason -->

Sorting is more accurate when viewers compare **aligned positions** against a shared axis; judging **length**—especially when segments are not aligned to a common baseline—adds perceptual difficulty and increases error.

- **The Principle:** Position-on-common-scale enables more accurate quantitative comparison than length judgments.
- **The Evidence:** Experimental rankings for sorting place position-based bar judgments above length-based ones in Cleveland & McGill’s experiments [@clevelandGraphicalPerceptionTheory1984], and the collation summarizes this as a key encoding effectiveness takeaway for quantitative data [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Sorting categories by magnitude (e.g., “Which is larger?” / rank order).
- **Data Type:** Quantitative values across nominal categories.
- **Audience:** General audiences doing quick comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The goal is not sorting but communicating “part-to-whole” composition with stacked segments.
- **Reason:** The evidence here is specifically about sorting accuracy, not composition reading [@clevelandGraphicalPerceptionTheory1984; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need more space (e.g., grouped bars or separate panels) to keep a shared baseline.
- **The Risk:** Reformatting to aligned position can reduce compactness compared with stacked layouts.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping stacked segments and assuming viewers can “just compare segment lengths” accurately.
- **Why it fails:** Segment comparisons often become length judgments without a shared baseline, which performs worse for sorting in the reported rankings [@clevelandGraphicalPerceptionTheory1984; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The values being compared do not start from the same baseline (segments float at different heights).
- **The Test:** Ask: “Do the compared marks share the same zero/baseline line?” If no, you’re likely forcing length judgments.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert stacked segments used for sorting into side-by-side (grouped) bars aligned to a common baseline.
- **Best Fix:** Redesign so the compared quantities are encoded as positions on a shared axis (aligned bar tops or dot positions) for the sorting task [@clevelandGraphicalPerceptionTheory1984; @zengReviewCollationGraphical2023].
