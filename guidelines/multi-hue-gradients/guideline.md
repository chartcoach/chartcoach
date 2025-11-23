---
id: multi-hue-gradients
title: Use Multi-Hue Gradients for Better Decipherability
bibliography: references.bib
description: Enhance single-hue gradients by incorporating a second or third hue to
  increase distinctness.
labels:
- visual:color
- visual:perception
- data:quantitative
- impact:accessibility
---

## The Rule <!-- role: advice -->
Consider using two or three carefully selected hues for a gradient, rather than just one. Ensure the colors are also encoded through lightness (bright to dark).

## The Logic <!-- role: reason -->
While a single-hue gradient (light blue to dark blue) is standard, readers can distinguish values better if they are encoded through lightness *and* hue. This makes the map or chart "more decipherable" and allows readers to "distinguish the colors on the gradient better" [@muth_colors_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Distinguishing between mid-range values in a heatmap or map.
*   **Data Type:** Continuous quantitative data.
*   **Audience:** General readers, including those with slight color vision deficiencies (if lightness is also used).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Rainbow scales.
*   **Reason:** While multi-hue is good, too many hues (rainbow) with fluctuating lightness confuse readers. Limit to 2-3 hues.

## The Price <!-- role: costs -->
*   **The Sacrifice:** It requires more design skill to pick two hues that blend well (e.g., Yellow to Green to Blue) than just one.
*   **The Risk:** Creating a muddy brown transition if the colors are complementary (e.g., mixing red and green).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing more than two hues with the *same* lightness in the gradient.
*   **Why it fails:** Without the lightness progression, the gradient fails in black and white and is hard for colorblind users.

## How to Check <!-- role: check -->
*   **Visual Sign:** A gradient that looks like a "rainbow" or has dark bands in the middle.
*   **The Test:** Convert to grayscale. Is it a smooth gradient from light to dark? If it goes light-dark-light-dark, it is flawed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use tools like ColorBrewer or Datawrapper defaults.
*   **Best Fix:** Design from a bright color (e.g., white/light yellow) to a dark color (e.g., dark blue) ensuring a smooth transition in lightness.
