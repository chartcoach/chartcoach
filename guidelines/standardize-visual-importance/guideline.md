---
id: standardize-visual-importance
title: Avoid UI Palettes for Data Categories
bibliography: references.bib
description: Avoid general design palettes that use accent colors, favoring palettes
  where all colors have equal visual weight.
labels:
- visual:color
- impact:neutrality
- data:categorical
- source:external-palette
---

## The Rule <!-- role: advice -->
Do not use color palettes designed for UI, web design, or interior design for categorical data visualization. Instead, ensure all categorical colors look roughly equally important.

## The Logic <!-- role: reason -->
Palettes from general design sites (like ColorHunt or Adobe Color) or interior design often consist of desaturated background colors paired with highly saturated "accent" colors or "call to action" buttons. In data visualization, unless you intend to highlight specific data points, categorical variables usually carry equal weight. Using a UI palette can inadvertently signal that one category is more important than the others merely because it is more saturated [@muth_good_color_palettes_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing multiple categories objectively without bias.
*   **Data Type:** Categorical data (e.g., industries, regions).
*   **Audience:** Analytical readers looking for patterns across all groups.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Explanatory or "Data Storytelling" charts.
*   **Reason:** If the explicit goal is to highlight one specific category (e.g., "Our Company" vs. "Competitors"), using an accent color against grayed-out colors is appropriate.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose access to thousands of pre-made, trendy palettes found on popular design inspiration sites.
*   **The Risk:** Creating a custom palette takes more time than copying a popular aesthetic from a design blog.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "Trending" palette from a site like ColorHunt without testing it.
*   **Why it fails:** The palette likely contains a mix of pastels and neons, causing the neon categories to dominate the viewer's attention unintentionally.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does one bar or line pop out significantly more than the others?
*   **The Test:** Look at the palette. If it resembles a website theme (mostly grays/whites with one bright blue), it is likely unsuitable for categorical data.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Tweak the saturation of the "accent" colors down and the "background" colors up until they feel balanced.
*   **Best Fix:** Use a generator specifically designed for data visualization, like Colorgorical or the default palettes in tools like Tableau or Datawrapper, which are calibrated for equal importance.
