---
id: avoid-stereotypical-skin-colors
title: Avoid Stereotypical Skin Tone Colors
bibliography: references.bib
description: Do not use colors that mimic literal skin tones or racial stereotypes
  (e.g., yellow for Asia, black for Black people).
labels:
- visual:color
- data:categorical
- impact:inclusivity
- audience:general-public
---

## The Rule <!-- role: advice -->
Do not represent racial categories using stereotypical skin colors. Specifically, avoid using black for data about Black people, white for white people, or yellow for Asian people.

## The Logic <!-- role: reason -->
Race is a social construct, not a biological definition strictly defined by skin color. Literal skin colors are rarely accurate differentiators, and using colors like yellow or red relies on offensive historical stereotypes and colonial worldview mapping [@muth_race_ethnicity_colors_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** Visualizing demographic data involving race, ethnicity, or world regions.
*   **Audience:** A general or diverse audience where respectful representation is critical.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Highlighting a minority group against a majority baseline.
*   **Reason:** It is acceptable to use a neutral warm light gray for a "White" category if it functions as a backdrop to emphasize the "People of Color" categories in saturated colors. In this context, gray represents "baseline/background" rather than skin tone [@muth_race_ethnicity_colors_2024].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "immediate" cognitive association some readers might have with stereotypical colors.
*   **The Risk:** Readers may need to reference the color key more frequently if the colors are abstract.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using "realistic" shades (e.g., dark brown vs. beige).
*   **Why it fails:** Even "realistic" attempts reinforce the idea that skin color defines race, and creates palettes that may be aesthetically unappealing or hard to distinguish.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the color palette look like a "flesh tone" gradient or a historical colonial map?
*   **The Test:** Ask: "Is this color chosen because it looks like the person, or because it is a good categorical color?"

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Randomize the color palette so hues do not align with skin stereotypes.
*   **Best Fix:** Select a high-quality categorical color palette (e.g., blues, purples, greens) that has no biological association with the groups being visualized.
