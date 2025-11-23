---
id: vary-lightness-for-accessibility
title: Vary Lightness Across Categorical Colors
bibliography: references.bib
description: Ensure distinct lightness levels for each color to support accessibility
  and black-and-white printing.
labels:
- visual:color
- impact:accessibility
- impact:clarity
- data:categorical
- audience:general
---

## The Rule <!-- role: advice -->
Select categorical colors that possess different lightness levels. Ensure the palette remains distinct when converted to grayscale.

## The Logic <!-- role: reason -->
Varying lightness ensures that colors are distinguishable not just by hue, but by value. This is critical for accessibility, particularly for colorblind readers (who may struggle to distinguish red and green if they share the same brightness) and for scenarios where charts are printed in black and white. As noted in [@muth_good_color_palettes_2024], if a visualization works in black and white, it is a strong indicator that the colors are easy to tell apart for any reader.

## Where to Apply <!-- role: context -->
*   **User Goal:** Creating a palette that is robust across different mediums (screens, print).
*   **Data Type:** Categorical data where distinctions between groups are necessary.
*   **Audience:** Broad audiences including those with color vision deficiencies (CVD).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Specific aesthetic requirements or strict brand guidelines.
*   **Reason:** Sometimes brand colors must be used even if they share similar lightness values; in these cases, rely on other cues like direct labeling to distinguish categories.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may lose the ability to use highly similar saturation levels for all colors (e.g., a palette of all pastel neons).
*   **The Risk:** The palette might look less "uniform" or "harmonious" in terms of visual weight if lightness varies drastically.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on hue changes (e.g., Red vs. Green) while keeping brightness identical.
*   **Why it fails:** In grayscale or for certain colorblind users, these colors will appear identical, making the chart unreadable.

## How to Check <!-- role: check -->
*   **Visual Sign:** When the chart is desaturated, the colors merge into a single shade of gray.
*   **The Test:** Convert your visualization to "Black and White" or grayscale. If the categories are indistinguishable, the lightness variation is insufficient.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Adjust the brightness/lightness slider of your existing colors in your design tool.
*   **Best Fix:** Define lightness steps first (e.g., 40%, 56%, 72%) and then assign hues to those specific lightness levels to guarantee separation.
