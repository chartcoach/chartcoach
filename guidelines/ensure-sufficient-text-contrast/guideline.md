---
id: ensure-sufficient-text-contrast
title: Ensure Sufficient Text-Background Contrast
bibliography: references.bib
description: Verify that text placed on top of colored areas is readable.
labels:
- visual:color
- visual:typography
- impact:legibility
---

## The Rule <!-- role: advice -->
Verify contrast ratios before placing text on top of colored backgrounds.

## The Logic <!-- role: reason -->
Not all colors support legible text overlays. Poor contrast strains the eye and makes labels unreadable.
*   **The Principle:** Luminance Contrast.
*   **The Evidence:** [@muth_colorguide_2018] warns that colors like Red and Blue often "don't pass the test" for readability.

## Where to Apply <!-- role: context -->
*   **User Goal:** Annotating maps or labeling data points directly on color.
*   **Task:** Placing white or black text over data marks.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Large decorative text (though still risky).
*   **Reason:** Contrast requirements are stricter for body text and functional labels.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may need to adjust the background color's lightness or darkness, potentially altering the data encoding, to support the text.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using white text on a medium-red or medium-blue background without checking.
*   **Why it fails:** These combinations frequently fail accessibility standards [@muth_colorguide_2018].

## How to Check <!-- role: check -->
*   **The Test:** Use a tool like *Color Review* to check readability for specific text sizes [@muth_colorguide_2018].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use a text outline/halo or move the label off the colored area.
*   **Best Fix:** Adjust the background color lightness to ensure it passes contrast tests.
