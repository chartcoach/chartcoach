---
id: balance-luminance-for-numerosity
title: Normalize Luminance When Mapping Numerosity
bibliography: references.bib
description: Darker collections of objects appear more numerous than lighter ones,
  biasing density estimates.
labels:
- visual:luminance
- visual:color
- task:estimate
- task:compare
- impact:bias
- chart:scatter
---

## The Rule <!-- role: advice -->
Avoid using luminance (lightness/darkness) to differentiate groups if the user needs to compare their quantities.

## The Logic <!-- role: reason -->
Ensemble coding is susceptible to interference between visual dimensions. Specifically, darker collections of items perceptually appear more numerous than lighter collections of the same quantity [@szafir_four_2016].
*   **The Principle:** Dimensional Interference
*   **The Evidence:** Studies show that when luminance varies, it biases the perceived number of items (numerosity), whereas differences in hue or orientation are generally robust [@szafir_four_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the size or density of two different groups (e.g., "Are there more Democrats or Republicans?").
*   **Data Type:** Categorical data mapped to color in scatterplots or dot maps.
*   **Audience:** General audiences interpreting density or frequency.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The background is dark.
*   **Reason:** The effect is driven by contrast; on a black background, lighter items might appear more distinct/numerous (though the paper specifically cites "darker collections" in standard contexts).

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "value" channel of color, restricting you to hue and saturation.
*   **The Risk:** Reducing contrast differences might make individual point identification harder for colorblind users if not managed carefully with hue.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a sequential color scale (light blue to dark blue) for categories.
*   **Why it fails:** The dark blue category will appear more frequent than the light blue category, even if counts are equal.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is one category significantly darker (lower value/L*) than the other?
*   **The Test:** Convert the image to grayscale. If one group is much darker gray than the other, you risk biasing the count.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Adjust the colors so they have similar luminance (perceptual brightness).
*   **Best Fix:** Use distinct hues (e.g., Orange vs. Purple) that have been balanced for luminance.
