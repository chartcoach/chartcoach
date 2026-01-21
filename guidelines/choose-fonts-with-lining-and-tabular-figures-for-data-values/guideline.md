---
id: choose-fonts-with-lining-and-tabular-figures-for-data-values
title: Choose Fonts with Lining and Tabular Numbers
bibliography: references.bib
description: Use lining figures for readability and tabular figures for alignment
  in axes, tooltips, and tables.
labels:
- chart:general
- task:compare
- visual:typography
- impact:clarity
- data:numeric
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use fonts that provide **lining** numerals and enable/choose **tabular** numerals for chart and table numbers.

## The Logic <!-- role: reason -->

Lining figures keep all digits the same height, which improves legibility for axis ticks, tooltips, and tables; tabular figures make each digit the same width, improving column alignment and helping readers compare numeric magnitudes and digit counts quickly [@muth_fonts_2022].

- **The Principle:** Numeric legibility (lining) + numeric alignment (tabular)
- **The Evidence:** [@muth_fonts_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Reading exact values and comparing numbers precisely
- **Data Type:** Numeric labels (axes), tooltips, table columns, annotations with numbers
- **Audience:** Any audience—especially screen readers of dense numeric displays

## When to Break It <!-- role: exceptions -->

- **Scenario:** Numbers appear as part of running paragraph text where aesthetics outweigh fast numeric comparison.
- **Reason:** Proportional figures can look nicer in paragraphs because wider digits (like 8) get more space than narrow ones (like 1) [@muth_fonts_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Slightly less “natural” typography in prose-like contexts.
- **The Risk:** If tabular figures are used everywhere (including narrative paragraphs), the text can look less typographically refined than proportional figures [@muth_fonts_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Leaving the default numeral style unchecked (ending up with oldstyle figures in UI-like chart text).
- **Why it fails:** Oldstyle figures can be harder to read quickly in axis ticks, tooltips, and tables because they don’t share a consistent height [@muth_fonts_2022].
- **The Wrong Fix:** Using proportional figures in tables “because they look nicer.”
- **Why it fails:** Proportional digits undermine alignment and make quick comparisons harder [@muth_fonts_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Table columns look ragged even when right-aligned; digit strings don’t visually “stack”; digits have varying heights (some dip below the baseline).
- **The Test:** Compare two numbers with the same digit count (e.g., 124.17 vs 680.90). If their visual widths differ or they don’t align cleanly in a column, you’re not using tabular figures; if digits rise/fall like lowercase letters, you’re not using lining figures [@muth_fonts_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a font family known (in your workflow) to include tabular lining figures and apply that font to chart/table text [@muth_fonts_2022].
- **Best Fix:** In addition to selecting a suitable font, explicitly enable tabular/lining figure settings where your software supports it, and reserve proportional figures for paragraph text only [@muth_fonts_2022].
