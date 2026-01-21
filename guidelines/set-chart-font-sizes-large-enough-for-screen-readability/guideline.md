---
id: set-chart-font-sizes-large-enough-for-screen-readability
title: Set Chart Text Large Enough to Read
bibliography: references.bib
description: Use font sizes that remain readable on-screen; treat anything below ~12px
  as likely too small depending on the typeface.
labels:
- chart:general
- task:read
- visual:typography
- impact:accessibility
- data:general
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Set chart and table text to a readable size; avoid going below ~12px unless you have validated legibility for your specific font.

## The Logic <!-- role: reason -->

Readability depends on more than size (font family, capitalization, letter spacing, and color all matter), and very small text becomes hard to read on screens; the post notes that, depending on the typeface, sizes below 12px will likely be too small [@muth_fonts_2022].

- **The Principle:** Legibility is multi-factor (size + typeface + styling)
- **The Evidence:** [@muth_fonts_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Reading axis ticks, labels, notes, and table text without zooming
- **Data Type:** Any visualization with supporting text (annotations/notes) or dense labels
- **Audience:** General public on typical screens/laptops/phones

## When to Break It <!-- role: exceptions -->

- **Scenario:** Very limited space where a small secondary label is acceptable and you can confirm it remains readable.
- **Reason:** The post emphasizes there’s no one universal minimum; font family and other styling can change what’s readable [@muth_fonts_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Larger text consumes more space, potentially reducing room for the data marks.
- **The Risk:** If you enlarge text without adjusting layout, labels may overlap or truncate [@muth_fonts_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Shrinking labels below ~12px to prevent overlaps instead of redesigning the layout.
- **Why it fails:** It solves collisions by sacrificing readability, making the visualization harder to use [@muth_fonts_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Readers need to zoom; labels look cramped or “hairline”; axis ticks are hard to decipher.
- **The Test:** Ask a coworker/friend to read key labels at normal viewing distance; if they hesitate or lean in, increase size or adjust typography/layout [@muth_fonts_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase font size to a comfortable baseline (and treat \<12px as a red flag) [@muth_fonts_2022].
- **Best Fix:** Increase size and then resolve collisions by shortening text, adjusting margins, or reducing label density—rather than shrinking below legible sizes [@muth_fonts_2022].
