---
id: avoid-saturation-for-uncertainty
title: Avoid Color Saturation for Uncertainty
bibliography: references.bib
description: Do not use color saturation to represent uncertainty, as users do not
  find it intuitively logical.
labels:
- visual:color
- visual:saturation
- data:uncertainty
- impact:clarity
- task:interpret
---

## The Rule <!-- role: advice -->
Do not use color saturation (vividness/purity) to signify uncertainty levels. Specifically, do not assume that "less saturated" intuitively means "less certain."

## The Logic <!-- role: reason -->
While common design advice often suggests saturation as a variable for uncertainty, empirical evidence contradicts this. In intuitiveness rankings, saturation received a score below 4.0 (the midpoint of the scale), categorizing it as "unacceptable" for visualizing discrete entity uncertainty at the ordinal level. Users did not consistently view changes in saturation as a logical metaphor for changes in certainty [@maceachren_visual_2012].

## Where to Apply <!-- role: context -->
*   **User Goal:** Communicating data quality without forcing the user to constantly consult a legend.
*   **Data Type:** Ordinal or categorical uncertainty attached to point symbols.
*   **Audience:** Any user group, as the lack of intuitiveness suggests a fundamental perceptual disconnect.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When you can combine saturation with Value (lightness).
*   **Reason:** Often "fading" a color involves changing both value and saturation simultaneously. Pure saturation changes (keeping lightness constant) are the primary issue.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose one of the standard dimensions of color, restricting you to Hue (for category) and Value (for uncertainty or magnitude).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using "Grayed out" colors (desaturated but same lightness) to mean "uncertain."
*   **Why it fails:** Users may interpret the grey color as a different category entirely, or simply fail to perceive the order of magnitude.

## How to Check <!-- role: check -->
*   **Visual Sign:** Convert your visualization to grayscale. If the uncertainty encoding disappears (because the values are the same), you are relying on saturation/hue, which is likely unintuitive.
*   **The Test:** Show a vivid red dot and a muted red dot. Ask a user "Which one is more reliable?" If they hesitate or guess randomly, the encoding has failed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Modulate **Value** (lightness) instead of Saturation. Make the uncertain data significantly lighter (whiter) than the certain data.
*   **Best Fix:** Switch to **Fuzziness** (blur) or **Crispness**, which ranked significantly higher (>5.0) for intuitiveness than saturation [@maceachren_visual_2012].
