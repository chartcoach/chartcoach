---
id: avoid-brown-and-olive-hues
title: Avoid Brown and Olive Hues
bibliography: references.bib
description: Exclude brown and olive shades from racial visualization palettes due
  to negative aesthetic and skin-tone associations.
labels:
- visual:color
- data:categorical
- impact:aesthetics
- impact:inclusivity
---

## The Rule <!-- role: advice -->
Remove brown and olive shades from your color palettes when visualizing data on race or ethnicity.

## The Logic <!-- role: reason -->
These specific hues are problematic for two reasons: first, they are reminiscent of skin tones (which should be avoided to prevent stereotyping); second, general audiences tend to dislike these colors aesthetically more than other hues. People of any race may be unhappy seeing themselves represented by these specific colors [@muth_race_ethnicity_colors_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** Creating a pleasing and respectful categorical palette.
*   **Data Type:** Categorical data where specific groups must be assigned distinct hues.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When using a standardized color palette mandated by an organization that includes these colors (though advocacy for change is recommended).
*   **Reason:** Strict brand compliance (though this specific advice suggests these colors are generally poor choices for this topic).

## The Price <!-- role: costs -->
*   **The Sacrifice:** You reduce the number of distinguishable colors available in your palette, which can be challenging for charts with many categories.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a dark olive to replace green.
*   **Why it fails:** It triggers the negative aesthetic and skin-tone association.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there "muddy" colors in the legend?
*   **The Test:** Isolate the color. If it looks like soil or military drab, remove it.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace brown with purple or dark gray. Replace olive with teal or turquoise.
*   **Best Fix:** Use a tested categorical palette that excludes earth tones entirely.
