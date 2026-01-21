---
id: encode-ordinal-data-with-position-then-color-saturation
title: Encode Ordinal Data with Position, Then Color Saturation
bibliography: references.bib
description: For ordered categories, prioritize position encodings; if color is needed,
  use saturation ahead of hue, texture, and geometric encodings.
labels:
- task:order
- visual:position
- visual:color
- impact:accuracy
- data:ordinal
- audience:general
- complexity:foundational
---

## The Rule <!-- role: advice -->

For ordinal data, encode order with position (x/y). If you must use color, use color saturation before color hue or texture.

## The Logic <!-- role: reason -->

The theoretical effectiveness ordering for ordinal data ranks position (x/y) highest, with color saturation above color hue and texture. This ranking is provided in [@mackinlayAutomatingDesignGraphical1986a] and collated into structured recommendation knowledge by [@zengReviewCollationGraphical2023].

- **The Principle:** Effectiveness ordering for ordinal perceptual tasks
- **The Evidence:** [@mackinlayAutomatingDesignGraphical1986a], as collated in [@zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Perceiving and comparing ordered categories (higher/lower)
- **Data Type:** Ordinal categories (ranked labels)
- **Audience:** General audiences

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot allocate x/y position to the ordinal variable because x/y is reserved for required quantitative axes.
- **Reason:** The ranking assumes position is available for the ordinal attribute.

## The Price <!-- role: costs -->

- **The Sacrifice:** Saturation-based encodings can limit styling options and may require careful legend design.
- **The Risk:** If saturation steps are too subtle, adjacent ordinal levels may be hard to distinguish.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using color hue ramps to indicate ordinal progression by default.
- **Why it fails:** Hue is ranked below saturation for ordinal effectiveness in the captured ordering.

## How to Check <!-- role: check -->

- **Visual Sign:** Order is communicated primarily via changing hues (e.g., shifting across distinct colors) rather than positional order or saturation steps.
- **The Test:** Ask users to point to “the next higher category” without reading labels; if hue changes are doing the work, you may be violating the ranking.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace hue progression with a saturation progression for the same base color.
- **Best Fix:** Re-encode ordinal order using position on an axis (or along a consistent positional direction).
