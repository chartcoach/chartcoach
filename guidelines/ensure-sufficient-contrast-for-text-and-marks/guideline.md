---
id: ensure-sufficient-contrast-for-text-and-marks
title: Meet Minimum Contrast Ratios
bibliography: references.bib
description: "Use sufficiently high contrast\u2014especially for small text\u2014\
  so charts remain readable in varied viewing conditions."
labels:
- chart:all
- task:read
- visual:color
- impact:accessibility
- data:mixed
- audience:all
- accessibility:contrast
---

## The Rule <!-- role: advice -->

Ensure foreground/background contrast is at least 2.5 for big text and at least 4 for small text, and avoid bright or complementary hues as backgrounds.

## The Logic <!-- role: reason -->

Low contrast reduces legibility across screens and lighting; small text needs higher contrast. Muth also warns that complementary hues and bright backgrounds can hinder readability and comfort [@muth_colors_2018].

- **The Principle:** Legibility depends on luminance contrast, especially at small sizes.
- **The Evidence:** [@muth_colors_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Read labels, annotations, and values reliably.
- **Data Type:** Any chart with text, thin lines, or light colors (including grey).
- **Audience:** Broad audiences, including readers on low-quality screens or low-light environments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** None stated; the post frames contrast as a requirement for readability.
- **Reason:** Readability is foundational to interpretation [@muth_colors_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less freedom to use very light text or subtle styling.
- **The Risk:** Increasing contrast can make the design feel harsher if not balanced with hierarchy and spacing [@muth_colors_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using light grey text on white or bright colored backgrounds for “minimalism.”
- **Why it fails:** Small text becomes unreadable; comprehension suffers [@muth_colors_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Labels fade into the background; readers need to zoom in.
- **The Test:** Measure contrast ratios (big text ≥ 2.5; small text ≥ 4) using a contrast tool as suggested by Muth [@muth_colors_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Darken text/lines or lighten the background until the ratio is met.
- **Best Fix:** Redesign the palette to avoid bright/complementary backgrounds and ensure all text styles meet the recommended contrast thresholds [@muth_colors_2018].
