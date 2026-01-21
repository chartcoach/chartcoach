---
id: use-multiplexed-uniwidth-fonts-to-bold-numbers-without-breaking-table-alignment
title: Use Multiplexed Fonts for Bolded Table Numbers
bibliography: references.bib
description: "If you need to bold values in tables, use multiplexed (uniwidth) fonts\
  \ so bold text doesn\u2019t shift alignment."
labels:
- chart:table
- task:highlight
- visual:typography
- impact:clarity
- data:numeric
- audience:general
- complexity:advanced
- source:datawrapper
---

## The Rule <!-- role: advice -->

When highlighting table values in bold, use a multiplexed (duplexed/uniwidth) font so bold and regular characters keep the same width.

## The Logic <!-- role: reason -->

In many fonts, bold text becomes wider than regular, which can disrupt visual alignment in tables; multiplexed fonts keep character widths consistent across weights, letting you emphasize values without shifting columns [@muth_fonts_2022].

- **The Principle:** Stable alignment across font weights
- **The Evidence:** [@muth_fonts_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing values in tables while noticing emphasized cells
- **Data Type:** Dense numeric tables where some values are bolded
- **Audience:** Readers who scan tables quickly (news, dashboards, reports)

## When to Break It <!-- role: exceptions -->

- **Scenario:** You don’t need mixed weights inside aligned columns (no bolding within numeric columns).
- **Reason:** If nothing changes weight, there’s no alignment shift to prevent [@muth_fonts_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer font choices (multiplexed fonts are a narrower subset).
- **The Risk:** If the multiplexed font’s overall look doesn’t match brand typography, it may reduce visual consistency [@muth_fonts_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Bolding key table numbers using a normal (non-multiplexed) font and assuming alignment remains unchanged.
- **Why it fails:** Many fonts widen in bold, subtly disturbing column rhythm and making the table look uneven [@muth_fonts_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Columns appear to “wobble” or spacing changes when some cells are bolded.
- **The Test:** Toggle bold on/off for the same value and see whether its width changes and pushes neighboring spacing or alters column edges [@muth_fonts_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce reliance on bold within aligned numeric columns (use it more selectively) [@muth_fonts_2022].
- **Best Fix:** Switch the table to a multiplexed font designed for uniwidth behavior across weights (e.g., try a multiplexed font like Recursive) and then apply bold for emphasis [@muth_fonts_2022].
