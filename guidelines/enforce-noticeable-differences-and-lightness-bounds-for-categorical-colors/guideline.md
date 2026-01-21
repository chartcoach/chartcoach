---
id: enforce-noticeable-differences-and-lightness-bounds-for-categorical-colors
title: Enforce Noticeable Differences and Lightness Bounds for Categorical Colors
bibliography: references.bib
description: Prevent near-duplicate colors and avoid extremes that fail on light or
  dark backgrounds.
labels:
- chart:categorical
- task:distinguish
- visual:color
- impact:clarity
- data:categorical
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

Reject candidate categorical colors that are not “noticeably different,” and clamp palette lightness to a mid-range so colors remain visible on typical light and dark backgrounds.

## The Logic <!-- role: reason -->

Colorgorical enforces a minimum discriminability bound by removing colors too close to already chosen colors using a “noticeable difference” interval model tied to mark size, and it constrains lightness (e.g., excluding very light and very dark colors) to maintain visibility against common background extremes [@gramazioColorgoricalCreatingDiscriminable2017a].

- **The Principle:** Just-noticeable differences and background visibility constraints
- **The Evidence:** [@gramazioColorgoricalCreatingDiscriminable2017a]

## Where to Apply <!-- role: context -->

- **User Goal:** Avoid accidental near-duplicates and ensure legibility across background choices
- **Data Type:** Categorical color sets used for marks on charts/maps
- **Audience:** Tool builders and designers creating reusable categorical palettes

## When to Break It <!-- role: exceptions -->

- **Scenario:** You control the background and want a deliberately low-contrast aesthetic (e.g., subtle encoding where color is secondary).
- **Reason:** The lightness clamp is a conservative constraint for visibility across black/white backgrounds; relaxing it trades robustness for style [@gramazioColorgoricalCreatingDiscriminable2017a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced available color space (fewer candidate colors), limiting maximum palette size.
- **The Risk:** You may be unable to generate very large categorical palettes before exhausting acceptable colors [@gramazioColorgoricalCreatingDiscriminable2017a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking colors that are technically distinct in RGB/hex but perceptually too similar at the mark size used.
- **Why it fails:** Discriminability depends on perceptual difference and mark size; near neighbors collapse visually [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Check <!-- role: check -->

- **Visual Sign:** Two categories appear interchangeable on small marks or dense maps.
- **The Test:** Verify each new color clears a minimum difference interval from all existing palette colors; also preview on both light and dark backgrounds [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the most similar color with one farther away in lightness and/or chromatic axes.
- **Best Fix:** Adopt a generation process that removes “indiscriminable neighbors” after each selection and constrains lightness to a safe band [@gramazioColorgoricalCreatingDiscriminable2017a].
