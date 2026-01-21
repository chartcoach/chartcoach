---
id: avoid-overly-condensed-or-overly-wide-fonts-in-visualizations
title: Avoid Overly Narrow or Overly Wide Fonts
bibliography: references.bib
description: Prefer normal-width fonts for chart text; condensed fonts hurt readability
  and wide fonts waste space.
labels:
- chart:general
- task:read
- visual:typography
- impact:clarity
- data:general
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use normal-width fonts for chart and table text; avoid overly narrow (condensed) and overly wide typefaces.

## The Logic <!-- role: reason -->

Condensed fonts give each character less space, making text harder to decipher; very wide fonts are readable but consume too much space—both outcomes hurt efficient chart layout and scanning [@muth_fonts_2022].

- **The Principle:** Character spacing supports legibility and layout efficiency
- **The Evidence:** [@muth_fonts_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Reading labels quickly without crowding the chart
- **Data Type:** Charts with many labels, axis ticks, tooltips, table headers
- **Audience:** General readers, especially in newsroom-style graphics

## When to Break It <!-- role: exceptions -->

- **Scenario:** A deliberate design concept where very large text is used and the condensed style is integral to the visual identity.
- **Reason:** The post shows condensed fonts can work when used at very large sizes and as a strong design choice, not as a cramped compromise [@muth_fonts_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to shorten labels or adjust layout instead of “solving” space issues with condensed fonts.
- **The Risk:** If you refuse condensed fonts entirely, you may have to redesign crowded charts (which takes time) [@muth_fonts_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to a condensed font to keep the same font size when the layout is too tight.
- **Why it fails:** It often reads as a cramped compromise and can be less readable than simply reducing font size in a normal-width face [@muth_fonts_2022].
- **The Wrong Fix:** Using a very wide font for many labels.
- **Why it fails:** It wastes space and forces other elements to shrink or collide [@muth_fonts_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Condensed labels look cramped and harder to parse; wide labels push other chart elements out of place.
- **The Test:** Compare two versions: (1) normal-width font at a slightly smaller size vs (2) condensed font at a larger size. If the condensed version isn’t clearer, don’t use it [@muth_fonts_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch back to a normal-width font and reduce size slightly or shorten labels [@muth_fonts_2022].
- **Best Fix:** Redesign spacing (margins, label strategy, or text content) so the visualization works with a normal-width, readable typeface [@muth_fonts_2022].
