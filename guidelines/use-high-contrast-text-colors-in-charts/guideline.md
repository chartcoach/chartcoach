---
id: use-high-contrast-text-colors-in-charts
title: Use High-Contrast Colors for Most Chart Text
bibliography: references.bib
description: Keep most chart text in high-contrast colors and verify contrast with
  a checker.
labels:
- chart:general
- task:read
- visual:color
- impact:accessibility
- data:general
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use high-contrast colors for most chart and table text, and verify contrast with a contrast checker.

## The Logic <!-- role: reason -->

Sufficient contrast supports readability; the post points to WCAG contrast guidance and recommends using a contrast checker to ensure compliance for text in visualizations [@muth_fonts_2022].

- **The Principle:** Contrast-based legibility
- **The Evidence:** [@muth_fonts_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Reading labels, annotations, and table text reliably
- **Data Type:** Any visualization with text over backgrounds (white, tinted panels, map fills)
- **Audience:** Broad audiences, including those with low vision or poor display conditions

## When to Break It <!-- role: exceptions -->

- **Scenario:** A small portion of deliberately de-emphasized secondary text (e.g., less important notes) where you still maintain acceptable contrast for legibility.
- **Reason:** The post frames high contrast as the default for “most text,” implying hierarchy can exist—so long as readability is preserved and checked [@muth_fonts_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Subtle, low-contrast aesthetics.
- **The Risk:** Overly dark text everywhere can reduce perceived hierarchy if you don’t also vary size/weight/placement [@muth_fonts_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using light gray text to look “minimal” without checking contrast.
- **Why it fails:** It can violate contrast expectations and become hard to read on many screens [@muth_fonts_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Text looks faint or disappears against the background.
- **The Test:** Run the text and background colors through a contrast checker as recommended in the post [@muth_fonts_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Darken the text color (toward black or near-black) or lighten the background behind text [@muth_fonts_2022].
- **Best Fix:** Establish a small, tested text color palette (primary high-contrast, secondary still-readable) and verify each pairing with a contrast checker [@muth_fonts_2022].
