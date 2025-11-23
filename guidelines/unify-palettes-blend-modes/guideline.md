---
id: unify-palettes-blend-modes
title: Unify Colors with Blend Modes
bibliography: references.bib
description: Use the 'Hue' blend mode to harmonize a disjointed set of colors.
labels:
- visual:color
- task:refine
- complexity:advanced
- tool:design-software
---

## The Rule <!-- role: advice -->
If a set of colors feels disjointed, unify them by overlaying a solid colored rectangle (layer) and setting its blend mode to "Hue."

## The Logic <!-- role: reason -->
This technique shifts the hue of all underlying colors towards the color of the overlay rectangle, while maintaining the original lightness and saturation values. This creates a shared "tint" or atmosphere, making the palette feel more cohesive and designed, rather than a random collection of hex codes [@muth_good_color_palettes_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** Fixing a palette where colors clash or feel like they don't belong together.
*   **Data Type:** Any visualization requiring multiple categorical colors.
*   **Audience:** Design-conscious audiences.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Strict accessibility requirements for color distinction.
*   **Reason:** Blending moves hues closer together. A contrast that was previously strong might become weaker (e.g., a blue and purple becoming harder to distinguish), failing accessibility checks.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Reduced distinctness between categories.
*   **The Risk:** You might accidentally lower the contrast between adjacent colors below WCAG standards.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using the "Normal" or "Multiply" blend mode with high opacity.
*   **Why it fails:** This simply darkens or tints the colors too heavily, potentially ruining contrast with the background.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the colors look too similar or "washed out" into a single color family?
*   **The Test:** After blending, verify the contrast ratio between the modified colors. As noted in the source, a strong contrast might become weaker after applying the blend mode.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reduce the opacity/transparency of the overlay layer (less is often more).
*   **Best Fix:** Try the "Overlay" blend mode instead, or choose a different hue for the blending rectangle that sits between the clashing colors.
