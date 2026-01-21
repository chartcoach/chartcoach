---
id: do-not-assume-shape-and-size-are-separable-in-multiclass-scatterplots
title: Account for Shape Bias When Using Size in Scatterplots
bibliography: references.bib
description: When size encodes data in scatterplots, treat shape as a biasing factor
  that can make equal-sized marks appear unequal.
labels:
- chart:scatter
- task:sort
- visual:shape
- visual:size
- impact:accuracy
- data:categorical
- audience:general
- complexity:advanced
---

## The Rule <!-- role: advice -->

If you encode data with mark size in a scatterplot, do not vary mark shape across categories unless you are prepared for systematic size perception bias.

## The Logic <!-- role: reason -->

- **The Principle:** Non-separability (shape significantly affects size perception)
- **The Evidence:** The paper reports that shape significantly affects size perception; some shapes are perceived as larger than others even when rendered at comparable sizes, indicating limited separability between shape and size in scatterplot marks [@smartMeasuringSeparabilityShape2019]. This kind of interaction is exactly the sort of graphical perception knowledge collated for recommendation constraints [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing magnitude via point size while also distinguishing categories via shape
- **Data Type:** Quantitative x/y, plus a quantitative attribute mapped to size, and nominal categories mapped to shape
- **Audience:** General audiences (and analysts) who need accurate size-based interpretation

## When to Break It <!-- role: exceptions -->

- **Scenario:** Shape is the primary encoding and size is not intended to be compared (decorative or redundant sizing).
- **Reason:** If size is not used for judgments, bias in perceived size is less likely to matter [@smartMeasuringSeparabilityShape2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced channel capacity (you may avoid using shape when size is important).
- **The Risk:** Without shape, you may need other methods to distinguish categories (e.g., relying more on color).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding category by shape while encoding magnitude by size and assuming viewers will “mentally normalize” differences.
- **Why it fails:** The evidence shows systematic size biases across shapes; equal sizes can be perceived as unequal [@smartMeasuringSeparabilityShape2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Some categories look consistently “bigger” or “smaller” than others even when the underlying size values are similar.
- **The Test:** Render the same size value across all categories but keep the different shapes; if some categories still look larger, your shape set is biasing size [@smartMeasuringSeparabilityShape2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use a single shape for all points when size is an important quantitative encoding.
- **Best Fix:** If you must use multiple shapes, explicitly account for shape-driven size bias by redesigning the encoding so size comparisons aren’t made across different shape categories (e.g., avoid cross-category size comparisons in the same view) [@smartMeasuringSeparabilityShape2019; @zengReviewCollationGraphical2023].
