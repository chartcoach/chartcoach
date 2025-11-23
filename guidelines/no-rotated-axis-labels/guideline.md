---
id: no-rotated-axis-labels
title: Never Rotate Axis Labels
bibliography: references.bib
description: Avoid rotating text labels; instead, rephrase, transpose, or change the
  chart type.
labels:
- visual:orientation
- impact:accessibility
- chart:bar
- chart:column
---

## The Rule <!-- role: advice -->
Don't make your readers turn their heads. Never rotate axis labels. Find another place inside the chart, concise the text, or change the chart type.

## The Logic <!-- role: reason -->
Rotated text is significantly harder to read and requires physical effort (neck craning) or mental rotation. It breaks the natural left-to-right reading flow. If labels don't fit horizontally, it indicates a layout problem, not a need for rotation [@muth_text_in_data_visualizations_2022].

## Where to Apply <!-- role: context -->
*   **User Goal:** Reading categorical labels on an axis.
*   **Data Type:** Column charts with long category names or many columns.
*   **Audience:** All users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** There are virtually no exceptions for 90-degree rotation in standard web viewing. 45-degree rotation is a "lesser evil" but still discouraged.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may need to change the chart type entirely (e.g., from vertical columns to horizontal bars).
*   **The Risk:** Horizontal bars might take up more vertical screen space than a compact column chart.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Rotating labels 45 or 90 degrees to cram them in at the bottom of a column chart.
*   **Why it fails:** It compromises readability for the sake of maintaining a specific chart type.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the text angled?
*   **The Test:** Can you read the text without tilting your head?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use concise abbreviations or rephrasing to shorten labels so they fit horizontally.
*   **Best Fix:** Swap the chart type from a Column Chart to a Bar Chart. This provides ample horizontal space for long labels.
