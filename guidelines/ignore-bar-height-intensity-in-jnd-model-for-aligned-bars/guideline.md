---
id: ignore-bar-height-intensity-in-jnd-model-for-aligned-bars
title: Ignore Bar Height as a Driver of JND in Aligned Bar Comparisons
bibliography: references.bib
description: Do not model bar-chart JND as proportional to bar height (intensity)
  for aligned bars; height showed no significant main effect.
labels:
- chart:bar
- task:sort
- visual:length
- impact:clarity
- data:quantitative
- audience:general
- perception:jnd
- complexity:advanced
---

## The Rule <!-- role: advice -->

Do not use bar height (object intensity) as a primary predictor when modeling JND for comparisons in aligned bar charts.

## The Logic <!-- role: reason -->

In the studied bar-chart setup, bar height did not have a significant main effect on JND, while separation distance did; modeling JND as proportional to intensity would therefore misrepresent discriminability for this chart type.

- **The Principle:** Not all chart encodings follow a simple “Weber-like” intensity rule in context; alignment can shift what drives discriminability.
- **The Evidence:** Lu et al.’s bar-chart results (as collated by Zeng & Battle) report a non-significant main effect for intensity/height on JND in bar charts [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## Where to Apply <!-- role: context -->

- **User Goal:** Sorting/ranking by comparing bar heights.
- **Data Type:** Quantitative values mapped to bar length/height with nominal categories.
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your bar design is not aligned (e.g., the comparison is not anchored to a common baseline) or your comparison target is not height/length.
- **Reason:** This guideline is grounded in the specific aligned bar-chart design represented in the collated design (quantitative→length; nominal→position) and may not transfer to other bar designs [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a simple “scale with value” heuristic.
- **The Risk:** If your bar chart differs materially from the studied configuration, excluding intensity could underfit your JND prediction.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Applying Weber’s-law-style “JND ∝ value/height” to aligned bar charts by default.
- **Why it fails:** The empirical result indicates bar height was not a significant driver of JND in the tested aligned bar setup [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Small differences remain hard/easy to see regardless of whether the bars are short or tall, but change with bar-to-bar separation.
- **The Test:** Hold the separation constant and vary bar heights across cases; if discriminability is similar, intensity is not acting as the main JND driver in your design [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove intensity from your JND heuristic for aligned bars; prioritize separation distance.
- **Best Fix:** Fit/validate a bar-chart JND model that uses separation distance (and excludes height as a main term) for your environment and chart specification [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].
