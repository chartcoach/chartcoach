---
id: design-palettes-that-work-for-color-vision-deficiency
title: Design Colors to Remain Distinguishable for Colorblind Readers
bibliography: references.bib
description: Use lightness differences and verify with colorblind checks so color-deficient
  readers can still distinguish your encodings.
labels:
- chart:all
- task:distinguish
- visual:color
- impact:accessibility
- data:mixed
- audience:all
- accessibility:color-vision-deficiency
---

## The Rule <!-- role: advice -->

Use lightness differences in gradients and palettes, and test your chart with a colorblind check to ensure the encoded colors remain distinguishable.

## The Logic <!-- role: reason -->

Muth explains there are many types of color vision deficiency, and that palettes with different lightness levels are more likely to remain distinguishable. She recommends using online tools or Datawrapper’s colorblind check to validate distinguishability [@muth_colors_2018].

- **The Principle:** Lightness variation provides redundancy when hue perception varies.
- **The Evidence:** [@muth_colors_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly differentiate categories or value ranges regardless of color vision.
- **Data Type:** Any color-encoded chart (categorical or gradient).
- **Audience:** Public-facing audiences that include colorblind readers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** None stated; the post frames colorblind consideration as necessary due to varied types.
- **Reason:** Without checking, you can’t assume distinguishability for all readers [@muth_colors_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some palettes may need to be less subtle or less brand-faithful to remain distinguishable.
- **The Risk:** If you rely on hue alone, categories/ranges may collapse into indistinguishable colors for some readers [@muth_colors_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Differentiating categories only by hue at similar lightness.
- **Why it fails:** For some color vision deficiencies, hues converge and become hard to tell apart [@muth_colors_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Under colorblind simulation, multiple categories/ranges look the same.
- **The Test:** Run a colorblind check (tool or built-in check) and confirm every encoded color can still be distinguished [@muth_colors_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase lightness differences between confusing colors.
- **Best Fix:** Redesign the palette so categories/ranges differ in lightness (and not only hue), then re-test until all colors remain distinguishable [@muth_colors_2018].
