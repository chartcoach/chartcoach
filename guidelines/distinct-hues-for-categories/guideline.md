---
id: distinct-hues-for-categories
title: Use Distinct Hues for Categories, Not Gradients
bibliography: references.bib
description: Avoid using shades of a single color for categorical data to prevent
  implied ranking.
labels:
- visual:color
- data:categorical
- impact:clarity
- chart:bar
---

## The Rule <!-- role: advice -->
Do not use a gradient color palette (shades of one hue) for categorical data. Conversely, do not use different hues for sequential/quantitative data unless carefully designed. Use distinct hues (e.g., green, yellow, pink) for distinct categories.

## The Logic <!-- role: reason -->
Readers associate dark colors with "more/high" and bright colors with "less/low." If you use shades of blue for categories (e.g., Fruit, Vegetables, Grains), the palette "will imply a ranking of your categories" that may not exist [@muth_colors_2018]. Distinct hues clarify that the data represents separate groups rather than a progression of values.

## Where to Apply <!-- role: context -->
*   **User Goal:** Distinguishing between nominal groups without inherent order.
*   **Data Type:** Nominal categories (e.g., departments, regions, brands).
*   **Audience:** Any reader interpreting the relationship between groups.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The categories actually *do* have an inherent order (Ordinal data).
*   **Reason:** If the categories are "Small, Medium, Large," a gradient is appropriate.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The chart will be more colorful and potentially less "minimalist" than a monochromatic chart.
*   **The Risk:** Using too many distinct hues can look chaotic (see the rule on limiting to seven colors).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "fading" effect on bars just for style.
*   **Why it fails:** It implies the data values are fading or changing, or implies a rank order among the bars.

## How to Check <!-- role: check -->
*   **Visual Sign:** A bar chart where "Apples" are dark blue and "Oranges" are light blue.
*   **The Test:** Ask a user: "Is the dark blue category 'better' or 'larger' than the light blue one?" If they say yes (and it isn't), the color choice is misleading.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Select a "Qualitative" color palette in your software.
*   **Best Fix:** Choose hues with different lightness or saturation to help them stand out, but ensure the hues themselves are distinct (e.g., purple vs. orange), and explain via legend/label.
