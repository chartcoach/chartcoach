---
id: darken-text-for-legibility
title: Darken Text Color When Matching Data Colors
bibliography: references.bib
description: Increase the darkness of colored text labels to ensure legibility compared
  to solid graphical elements.
labels:
- visual:color
- visual:typography
- impact:accessibility
- impact:legibility
---

## The Rule <!-- role: advice -->
When using text (such as labels or annotations) that matches a category's color, make the text color slightly darker than the graphical element (bar, line, or dot) it represents.

## The Logic <!-- role: reason -->
Bright colors that work well for large areas (like bars) often lack sufficient contrast when applied to thin character strokes. The eye perceives the thin lines of text as lighter than a solid block of the same color [@muth_remind_colors_2023].
*   **The Principle:** Perceived Contrast / Spatial Frequency
*   **The Evidence:** [@muth_remind_colors_2023] cites a "The Economist" chart where the label "Hispanic" is a darker shade than the line representing it.

## Where to Apply <!-- role: context -->
*   **User Goal:** reading labels that serve as a direct legend.
*   **Data Type:** Any chart using bright or pastel colors (e.g., yellow, light green, light blue).
*   **Audience:** All users, especially those with vision impairments.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Dark Backgrounds.
*   **Reason:** On a dark background, you would likely need to *lighten* the text rather than darken it to maintain contrast.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Strict color consistency. The hex code of the text will not technically match the hex code of the data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using the exact same yellow or light orange from a bar chart for the text label.
*   **Why it fails:** The text becomes unreadable against a white background.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the text hard to read? Does it vibrate or disappear?
*   **The Test:** Squint at the screen. If the text disappears before the data element does, the text lacks sufficient contrast.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually select a darker shade of the same hue for the text.
*   **Best Fix:** Alternatively, keep the text black/gray and use a colored background (highlight) behind the text to match the data color [@muth_remind_colors_2023].
