---
id: vary-color-lightness
title: Vary Color Lightness
bibliography: references.bib
description: Ensure colors have distinct brightness levels so they remain readable
  in grayscale.
labels:
- visual:color
- visual:contrast
- impact:accessibility
- impact:readability
---

## The Rule <!-- role: advice -->
Ensure that every color in your visualization varies by lightness (brightness), not just hue. Your chart should be fully readable if printed in black and white.

## The Logic <!-- role: reason -->
Lightness is a visual variable that persists even when hue perception is compromised. If colors possess different brightness levels, colorblind users can distinguish them even if they cannot identify the specific hue [@muth_colorblindness_2020].
*   **The Principle:** Luminance Contrast.
*   **The Evidence:** [@muth_colorblindness_2020] notes that yellow works exceptionally well in colorblind palettes specifically because its high brightness contrasts strongly with other "primary" colors.

## Where to Apply <!-- role: context -->
*   **User Goal:** Ensuring legibility across all vision types and printing mediums.
*   **Data Type:** Any chart relying on color to encode data.
*   **Audience:** Users who may print reports on monochrome printers or have low-contrast vision.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Using gradient scales where the specific hue is the only variable (though this is generally poor practice).
*   **Reason:** If the data requires precise hue identification without value changes (rare in good design).

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may have to abandon "vibrant" pure colors in favor of muddy, pastel, or dark variations to achieve necessary contrast.
*   **The Risk:** Text or thin lines in light colors (like yellow) may become invisible against a white background.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using fully saturated "rainbow" colors.
*   **Why it fails:** Many pure colors (like certain reds and greens) have identical luminance values, making them indistinguishable in grayscale or to colorblind eyes.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do adjacent colors visually vibrate or blend when you squint?
*   **The Test:** "Get it right in black & white." Print the chart on a monochrome printer or apply a grayscale filter. If the sections merge, the lightness is too similar [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Adjust the brightness (B in HSB) of one distinct color to be significantly darker or lighter.
*   **Best Fix:** Utilize a palette designed with varying luminance, such as pairing dark blue with light orange.
