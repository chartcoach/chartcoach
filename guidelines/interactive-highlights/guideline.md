---
id: interactive-highlights
title: Implement Interactive Highlights
bibliography: references.bib
description: Use hover effects to connect chart elements with tooltips or legends
  for clarity.
labels:
- visual:interaction
- impact:accessibility
- data:web-based
- source:web
---

## The Rule <!-- role: advice -->
For web-based visualizations, use interactive hover effects. Ensure that hovering over an element highlights it (and fades others) or connects it explicitly to a tooltip/legend.

## The Logic <!-- role: reason -->
Even if two colors look identical to a colorblind user (e.g., red and green appearing as brown), interactivity allows the user to isolate specific data points. The reaction to the mouse movement confirms which element is being viewed [@muth_colorblindness_2020].
*   **The Principle:** Selective Attention / Isolation.
*   **The Evidence:** [@muth_colorblindness_2020] explains that while red and green might look the same, hovering over a donut slice allows the user to understand which specific slice corresponds to the data, regardless of the color confusion.

## Where to Apply <!-- role: context -->
*   **User Goal:** Exploring specific values in a dataset.
*   **Data Type:** Interactive web charts (HTML/SVG/Canvas).
*   **Audience:** Users on desktop or devices with pointer capability.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Static media (PDFs, print, images).
*   **Reason:** Interactivity is impossible.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Development time. It requires coding interaction logic.
*   **The Risk:** Interaction is not accessible to everyone (e.g., keyboard-only users) if not implemented correctly, so it should not be the *only* method of distinction.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying *only* on tooltips to identify data.
*   **Why it fails:** It forces users to hunt for data (scrubbing) rather than seeing patterns at a glance.

## How to Check <!-- role: check -->
*   **Visual Sign:** When you mouse over a line or slice, does it stand out?
*   **The Test:** Hover over a color key item—does the corresponding chart element light up?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add standard browser tooltips (title attributes).
*   **Best Fix:** Implement "linked hovering": hovering the legend highlights the chart, and hovering the chart highlights the legend. Fade out non-selected elements.
