---
id: color-code-annotation-text
title: Color-Code Annotation Text
bibliography: references.bib
description: Color annotation text to match the data category it describes to reduce
  visual aggression.
labels:
- chart:map
- visual:color
- visual:text
- impact:hierarchy
- audience:general
---

## The Rule <!-- role: advice -->
Reuse your data colors for the text of your annotations.

## The Logic <!-- role: reason -->
Using high-contrast black text for annotations can make them "jump off" the map in an "attention-grabbing way." By matching the text color to the data category (e.g., blue text for wind power data), the annotations "sit back onto the map." This allows the text to "blend in with the data rather than demanding to be read right away," encouraging the eye to wander organically [@mintzer_map_annotations_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** Creating an "elegant" visualization that doesn't feel cluttered.
*   **Data Type:** Categorical data where colors distinguish groups (e.g., Solar vs. Wind).
*   **Audience:** Users engaging in open-ended exploration of a detailed map.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data colors are too light (e.g., pastel yellow) to be legible as text against a white background.
*   **Reason:** Accessibility and readability take precedence over aesthetic blending.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the stark contrast of black text, which might slightly reduce immediate legibility.
*   **The Risk:** If data colors are similar, annotations might become difficult to distinguish from one another.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using bold black text to ensure everything is seen.
*   **Why it fails:** This creates visual clutter and overshadows the actual data points [@mintzer_map_annotations_2024].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the words dominate the image more than the map itself?
*   **The Test:** Squint at the map. If the text is the most prominent element, it is too aggressive.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the font color of the annotation to match the legend color of the data it describes.
*   **Best Fix:** Use a slightly darker shade of the data color for the text to ensure readability while maintaining the color association.
