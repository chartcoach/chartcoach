---
id: generate-palettes-via-lch-gradients
title: Generate Hues via LCH Gradients
bibliography: references.bib
description: Create cohesive palettes by interpolating between a bright and a dark
  color using LCH or OKLCH color spaces.
labels:
- visual:color
- task:create
- data:categorical
- data:sequential
---

## The Rule <!-- role: advice -->
When generating a palette from a gradient, use the OKLCH or LCH color modes and set distinct start and end points: a bright start color paired with a dark, saturated end color (or vice versa).

## The Logic <!-- role: reason -->
Standard RGB interpolation can result in muddy or grayish transitions. Using perceptually uniform color spaces like OKLCH or LCH results in nicer-looking gradients. Furthermore, ensuring a contrast in brightness and saturation between the start and end points (e.g., bright yellow start vs. dark blue end) ensures the resulting intermediate colors are distinguishable and accessible [@muth_good_color_palettes_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** Creating a custom palette quickly for large areas (like bar charts) or extending a palette to more categories.
*   **Data Type:** Categorical or Sequential data.
*   **Audience:** General purpose.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Generating a specific diverging palette.
*   **Reason:** Diverging palettes require a neutral center and two distinct hues at the extremes, rather than a single gradient sweep.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You must leave the standard RGB color picker and use specific tools that support LCH/OKLCH (like Gradient Generator or Chroma.js).
*   **The Risk:** If the start and end colors are too similar in lightness, the middle steps may not have enough contrast.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using RGB mode to blend colors.
*   **Why it fails:** This often creates desaturated, "muddy" colors in the middle of the gradient.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the middle colors look gray or dull? Are the colors hard to tell apart?
*   **The Test:** Check the contrast ratio of the brightest color in the gradient against your background to ensure accessibility.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the interpolation mode in your tool from "RGB" to "LCH" or "OKLCH".
*   **Best Fix:** Ensure one endpoint is highly distinct in lightness from the other (e.g., Start: Bright/Pastel, End: Dark/Deep).
