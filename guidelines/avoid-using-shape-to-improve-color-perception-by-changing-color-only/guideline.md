---
id: avoid-using-shape-to-improve-color-perception-by-changing-color-only
title: Do Not Expect Color to Fix Shape Discriminability
bibliography: references.bib
description: Changing mark colors does little to improve shape discrimination in scatterplots
  except at extreme lightness values.
labels:
- chart:scatter
- task:sort
- visual:shape
- visual:color
- impact:clarity
- data:categorical
- audience:general
- complexity:advanced
---

## The Rule <!-- role: advice -->

Do not rely on changing colors to make different mark shapes easier to tell apart in a scatterplot.

## The Logic <!-- role: reason -->

- **The Principle:** Asymmetric interference (color weakly affects shape perception)
- **The Evidence:** The paper reports little to no interference from color on shape perceptions, except for extremely light colors (high lightness) where shapes become harder to distinguish from the background [@smartMeasuringSeparabilityShape2019]. This asymmetry is part of the collated perception knowledge intended to inform recommendation rules [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Sorting or distinguishing categories encoded with different shapes in a scatterplot
- **Data Type:** Categorical classes encoded by shape (often alongside position and possibly color)
- **Audience:** General audiences

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your palette includes extremely light colors that approach the background (e.g., very high lightness on white).
- **Reason:** In that extreme case, color/lightness can reduce shape discriminability by reducing contrast with the background [@smartMeasuringSeparabilityShape2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to change shapes (or their rendering) rather than “just tweak the palette.”
- **The Risk:** If you keep iterating on color to solve shape confusion, you may waste time and still not fix shape discrimination.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Cycling through many palettes hoping a “better” palette will make shapes pop.
- **Why it fails:** The evidence indicates color has only a small effect on shape perception for typical (non-extreme) colors [@smartMeasuringSeparabilityShape2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers still confuse shape categories even after major color palette changes.
- **The Test:** Convert all marks to a single, mid-contrast color; if shape confusions remain, color was never the main lever [@smartMeasuringSeparabilityShape2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase shape distinctiveness by changing the shape set (swap confusing shapes for more distinct ones) rather than changing the palette.
- **Best Fix:** Treat shape and color as asymmetric: optimize shape choices directly for shape-based categorization, and separately choose color knowing that shape will influence color discriminability more than the reverse [@smartMeasuringSeparabilityShape2019; @zengReviewCollationGraphical2023].
