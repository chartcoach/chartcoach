---
id: embed-legend-in-title
title: Embed the Color Key into the Title or Description
bibliography: references.bib
description: Replace standard legends by coloring category names directly within the
  chart's title or introductory text.
labels:
- visual:layout
- visual:text
- impact:efficiency
- visual:color
---

## The Rule <!-- role: advice -->
Turn your visualization's title or description into a color key. Color the words representing categories (e.g., "Europe," "Asia") with their corresponding data colors directly in the header text.

## The Logic <!-- role: reason -->
This creates a "double explanation" that saves space by removing the need for a separate "classic" legend. It integrates the "what" (the data) with the "who" (the category) immediately as the user begins reading [@muth_remind_colors_2023].
*   **The Principle:** Integration of Text and Visuals
*   **The Evidence:** [@muth_remind_colors_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Quick comprehension and space-saving.
*   **Data Type:** Charts with a small number of distinct categories (2-4).
*   **Audience:** General audience.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Many Categories.
*   **Reason:** A title with 10 different colored words becomes a "fruit salad" that is hard to read.
*   **Scenario:** Blue Categories.
*   **Reason:** Blue text in a title is universally perceived as a hyperlink. Using blue for a data category in text can confuse readers trying to click it [@muth_remind_colors_2023].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the standard "list" format of a legend, which some users might scan for.
*   **The Risk:** If the title is far from the bottom of the chart, users might still forget the colors (see guideline `keep-color-keys-visible`).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Coloring the text but *also* keeping a separate legend.
*   **Why it fails:** While redundant coding can be helpful, it often clutters the interface unnecessarily unless the chart is very long.

## How to Check <!-- role: check -->
*   **Visual Sign:** Check if you have a legend box taking up space that repeats information already present in the title.
*   **The Test:** Remove the separate legend. Is the chart still understandable solely based on the title?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Style the title using inline CSS or rich text formatting to match the data colors.
*   **Best Fix:** Use a "span" style for the category words to apply the color, and ensure the rest of the text remains high-contrast black/gray.
