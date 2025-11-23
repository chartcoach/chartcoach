---
id: prioritize-distinct-color-names
title: Select Colors With Distinct Names
bibliography: references.bib
description: Maximize linguistic difference between colors to improve discrimination
  speed and accuracy.
labels:
- visual:color
- task:identify
- impact:clarity
- data:categorical
- audience:general
---

## The Rule <!-- role: advice -->
Ensure that every color in your categorical palette maps to a distinct linguistic color name (e.g., "Blue," "Red," "Green") rather than relying solely on mathematical perceptual distance.

## The Logic <!-- role: reason -->
While perceptual distance (like CIEDE2000) measures how the eye distinguishes colors, **Name Difference**—the degree to which two colors have distinct color-name association frequency distributions—is often a stronger predictor of user performance. Research by [@gramazio_colorgorical_2017] demonstrates that Name Difference was the most predictive factor for response time in discrimination tasks, outperforming standard perceptual distance metrics. Users identify and separate data categories faster when the colors are linguistically distinct.

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapid identification and discrimination of categories.
*   **Data Type:** Categorical data (nominal classes).
*   **Audience:** General users (relies on common color naming conventions).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Designing for aesthetics over utility.
*   **Reason:** High discriminability (distinct names) often negatively correlates with aesthetic preference. If the goal is purely artistic or atmospheric, strict naming separation may result in a jarring palette [@gramazio_colorgorical_2017].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Aesthetic Preference.
*   **The Risk:** Palettes with high Name Difference (e.g., pairing "Green" with "Red") often result in lower preference ratings compared to palettes with similar hues (e.g., "Blue" and "Cyan") [@gramazio_colorgorical_2017].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying only on CIELAB/CIEDE2000 distance.
*   **Why it fails:** Colors can be mathematically distant in perception space (e.g., a yellow and a chartreuse) but share the same linguistic name in the user's mind ("Yellow"), causing confusion [@gramazio_colorgorical_2017].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there two colors you would describe with the same basic word (e.g., "Light Blue" and "Dark Blue")?
*   **The Test:** Ask a user to name the colors in the legend. If they use the same root word for two distinct categories, the Name Difference is too low.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace one of the confusing colors with a hue from a different color family (e.g., swap a second Blue for an Orange).
*   **Best Fix:** Use a tool that incorporates Name Difference scoring (like Colorgorical) to maximize linguistic distance.
