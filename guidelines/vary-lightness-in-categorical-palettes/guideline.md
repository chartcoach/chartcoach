---
id: vary-lightness-in-categorical-palettes
title: Vary Lightness in Categorical Palettes
bibliography: references.bib
description: Ensure categorical hues have distinct lightness values for accessibility
  and grayscale compatibility.
labels:
- visual:color
- data:categorical
- impact:accessibility
- audience:colorblind
---

## The Rule <!-- role: advice -->
Ensure distinct hues in a categorical color scale also differ in lightness (brightness), rather than using colors of equal intensity.

## The Logic <!-- role: reason -->
Varying lightness allows the palette to function even when color cannot be perceived, such as when printed in black and white. Additionally, @muth_which_color_scale_2021 notes that distinct lightness makes categories easier to distinguish for all readers, including those with color vision deficiencies.

## Where to Apply <!-- role: context -->
*   **User Goal:** Distinguishing between distinct groups or entities.
*   **Data Type:** Unordered categorical data (e.g., countries, genders, industries).
*   **Audience:** Diverse audiences including colorblind readers or those printing the chart.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High number of categories (though this is generally discouraged).
*   **Reason:** If you have too many categories, it becomes mathematically difficult to assign a unique lightness to each without them becoming indistinguishable.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to make all categories appear "equal" in visual weight; lighter colors may seem less important than darker/saturated ones.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using fully saturated versions of Red, Green, and Blue.
*   **Why it fails:** These may look distinct in color but can appear identical in grayscale or to certain colorblind users.

## How to Check <!-- role: check -->
*   **The Test:** Convert your visualization to grayscale. Can you still distinguish the different categories?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Adjust the brightness/luminance of specific colors in your palette so no two colors share the same grey value.
*   **Best Fix:** Use a colorblind-friendly palette generator (like ColorBrewer) that accounts for lightness differences automatically.
