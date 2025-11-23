---
id: align-text-left-or-right
title: Avoid Center-Aligned Text
bibliography: references.bib
description: Use left- or right-alignment for text blocks to create clean edges and
  improve reading speed.
labels:
- visual:typography
- impact:legibility
- visual:layout
---

## The Rule <!-- role: advice -->
Do not center-align your text. Use left-alignment or right-alignment for titles, descriptions, and annotations.

## The Logic <!-- role: reason -->
Left- or right-aligned text creates a "tidy" look because all lines start or end at the same x-position, creating a clear edge that can run parallel to chart elements. Center-aligned text leaves messy gaps. Furthermore, center-aligned text is harder to read for anything longer than roughly 10 words because readers need a split second longer to find the beginning of the next line [@muth_text_in_data_visualizations_2022].

## Where to Apply <!-- role: context -->
*   **User Goal:** Reading multi-line titles, descriptions, or long annotations.
*   **Data Type:** Any visualization containing text blocks.
*   **Audience:** All readers.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Very short, single-line labels or numbers (like a widely spaced table header).
*   **Reason:** In isolation, centering might visually balance a single element within a specific column width.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "formal" or "invitation-style" aesthetic sometimes associated with centered text.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Centering the title to make it look "official."
*   **Why it fails:** It disconnects the title from the strong vertical alignment of the y-axis or the edge of the chart.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the edges of your text block look ragged on both sides?
*   **The Test:** Draw a vertical line down the side of your text. If the text doesn't touch the line on at least one side, it is center-aligned.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the paragraph alignment setting to "Left" (or "Right" for annotations on the left side of a chart).
