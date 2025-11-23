---
id: avoid-thin-fonts
title: Avoid very thin fonts in data visualization
bibliography: references.bib
description: Thin fonts suffer from low contrast and poor legibility.
labels:
- visual:typography
- impact:accessibility
- impact:legibility
- visual:contrast
---

## The Rule <!-- role: advice -->

Do not use "Thin" or "Light" font weights for standard text sizes.

## The Logic <!-- role: reason -->

Text set in thin weights has such delicate strokes that it appears to be a lighter color (e.g., gray instead of black) even when set to black. This lowers the contrast ratio, making the text difficult to decipher.

*   **The Principle:** Stroke Contrast and Optical Sizing
*   **The Evidence:** [@muth_fonts_2022] demonstrates that thin fonts look "brighter" (fainter) and warns they are "really, really hard to read."

## Where to Apply <!-- role: context -->

*   **User Goal:** Reading labels, values, or notes.
*   **Audience:** All users, especially those with visual impairments or poor monitors.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Large Titles with High Contrast.
*   **Reason:** Thin fonts can be used if the text size is very big (titles only) and the color is high-contrast (black on white) [@muth_fonts_2022].

## The Price <!-- role: costs -->

*   **The Sacrifice:** You lose the "elegant" or "airy" aesthetic often associated with thin fonts.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Using thin fonts to de-emphasize text (make it look less important).
*   **Why it fails:** It creates accessibility issues.
*   **The Wrong Fix:** Making thin text gray.
*   **Why it fails:** This compounds the problem, making the text nearly invisible.

## How to Check <!-- role: check -->

*   **Visual Sign:** Does the text look gray even though the color code is black?
*   **The Test:** View the chart on a mobile screen or in bright light. If the lines of the letters disappear, the font is too thin.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** bump the font weight up to "Regular" (400) or "Medium."
*   **Best Fix:** To de-emphasize text, use a Regular weight but apply a dark gray color rather than using a Thin weight [@muth_fonts_2022].
