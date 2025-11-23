---
id: color-intensity-in-tables
title: Use Pastel for Backgrounds, Bright for Text
bibliography: references.bib
description: Proper color contrast and saturation rules for highlighting data in tables.
labels:
- chart:table
- visual:color
- impact:accessibility
- impact:aesthetics
---

## The Rule <!-- role: advice -->
When highlighting table elements: use bright, saturated colors for **text**. Use pastel, desaturated colors for **backgrounds** (whole cells, rows, or columns).

## The Logic <!-- role: reason -->
Color is a powerful tool to lead the eye. However, large areas of saturated color (backgrounds) can be overwhelming and make text hard to read. Text strokes are thin, so they require brighter, more distinct colors to be legible. Conversely, backgrounds occupy more space, so they must be subtle (pastel) to ensure the black text remains readable and the table doesn't look cluttered [@muth_tables_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Highlighting interesting information (e.g., highest/lowest values, specific categories).
*   **Visual Element:** Conditional formatting or categorical color coding.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Heatmaps.
*   **Reason:** Heatmaps rely on varying saturation to show magnitude. Darker backgrounds are acceptable there, provided the text color switches to white for contrast [@muth_tables_2019].

## The Price <!-- role: costs -->
*   **The Risk:** Using too many different colors for categories can make the table look like "fruit salad" and confuse navigation.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using the same bright color for a cell background as you would for a bar chart.
*   **Why it fails:** It reduces contrast with the text and overwhelms the reader.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the black text difficult to read against the background color?
*   **The Test:** If the background is a large block of color, is it pastel? If the color is on the font itself, is it bright/bold?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reduce the opacity/saturation of background colors.
*   **Best Fix:** Use distinct color palettes for text highlighting vs. background highlighting.
