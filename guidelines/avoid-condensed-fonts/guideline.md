---
id: avoid-condensed-fonts
title: Avoid overly narrow or condensed fonts
bibliography: references.bib
description: Standard width fonts are more legible than condensed options.
labels:
- visual:typography
- impact:legibility
- impact:accessibility
---

## The Rule <!-- role: advice -->

Use normal-width fonts for the majority of your visualization text. Avoid narrow (condensed) fonts unless absolutely necessary for space.

## The Logic <!-- role: reason -->

While narrow fonts save space, the reduced horizontal space per character makes them significantly harder to decipher. They often result in a "cramped compromise" look. Conversely, very wide fonts take up too much valuable chart real estate.

*   **The Principle:** Character Recognition and Spacing
*   **The Evidence:** [@muth_fonts_2022] notes that standard width text in a smaller size is often more readable than bigger text in a narrow typeface.

## Where to Apply <!-- role: context -->

*   **User Goal:** Reading axis labels and tooltips without eye strain.
*   **Data Type:** Categorical labels, chart text.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Very Large Text (Display).
*   **Reason:** Condensed fonts can work aesthetically if the text is set to a very large size, as seen in the 2007 Felton report [@muth_fonts_2022].
*   **Scenario:** Space-constrained axis labels (Fallback).
*   **Reason:** *The Wall Street Journal* falls back to "Retina Narrow" only when needed, preferring normal width otherwise [@muth_fonts_2022].

## The Price <!-- role: costs -->

*   **The Sacrifice:** You have less horizontal space for labels.
*   **The Risk:** You may need to wrap text or reduce font size to fit labels.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Switching to a condensed font to fit long category names on an x-axis.
*   **Why it fails:** It makes the labels hard to read.
*   **The Wrong Fix:** Using wide fonts (like Montserrat) for dense data.
*   **Why it fails:** It eats up chart space.

## How to Check <!-- role: check -->

*   **Visual Sign:** Do the letters feel squished? Does the text look "retro" or cramped?
*   **The Test:** Compare the text against a standard font like Arial or Roboto. If it is significantly narrower, reconsider.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Switch to the normal width version of the font family.
*   **Best Fix:** If space is tight, use a smaller font size in a normal width, rather than a large size in a condensed width [@muth_fonts_2022].
