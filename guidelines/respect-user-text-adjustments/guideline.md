---
id: respect-user-text-adjustments
title: Support User-Defined Text Sizing and Spacing
bibliography: references.bib
description: Ensure visualization text responds to browser zoom, custom stylesheets,
  and user system settings regarding font size and spacing.
labels:
- impact:accessibility
- impact:flexibility
- visual:text
- visual:layout
- audience:low-vision
- task:read
---

## The Rule <!-- role: advice -->
Ensure that all text within a visualization responds correctly to user-initiated resizing and spacing adjustments. Do not lock font sizes or spacing with absolute units or rigid containers that prevent browser zoom or custom stylesheets from taking effect.

## The Logic <!-- role: reason -->
This guideline is grounded in the "Flexible" principle of the Chartability framework, which emphasizes robust user agency. Users must be able to adjust the *Perceivable* and *Operable* traits of a data experience to match their needs within the larger technological context they inhabit [@elavsky_how_2022].

*   **The Principle:** **Flexible (POUR + CAF)**. Chartability posits that preferences set in lower-level systems (like browsers or operating systems) must be respected in higher-level environments (visualizations).
*   **The Evidence:** The W3C guidelines regarding "Resize Text" state that content must be resizable up to 200% without loss of content or functionality to assist people with low vision [@w3c_understanding_resize]. Furthermore, guidelines on "Text Spacing" indicate that users may need to override author styles to improve readability [@elavsky_how_2022].

## Where to Apply <!-- role: context -->
This advice applies to all web-based and digital data visualizations, particularly those containing essential textual information.

*   **User Goal:** Reading labels, axes, tooltips, titles, and annotations comfortably.
*   **Data Type:** Any chart utilizing text to convey meaning (e.g., labeled bar charts, scatter plots with tooltips).
*   **Audience:** Users with low vision, users with dyslexia, or users who rely on custom stylesheets for readability.

## When to Break It <!-- role: exceptions -->
There are very few valid reasons to ignore this rule in a digital context, as it is a core accessibility requirement.

*   **Scenario:** Text that is part of a brand logo or logotype.
*   **Reason:** Logos are generally exempt from text spacing requirements in standard accessibility guidelines, though they should still have alternative text.

## The Price <!-- role: costs -->
Designing for text flexibility requires abandoning "pixel-perfect" layouts.

*   **The Sacrifice:** You lose absolute control over the exact positioning of labels. As text grows, it may require the chart layout to shift or reflow.
*   **The Risk:** If the layout is not programmed responsively, enlarged text may overlap with data marks or get cut off by container boundaries, obscuring the data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using `px` (pixels) for font sizes or hard-coding container heights based on a specific font size.
*   **Why it fails:** This ignores browser settings and prevents the text from scaling relative to the user's base font preference.
*   **The Wrong Fix:** Rendering text as part of a raster image (e.g., a PNG of a chart).
*   **Why it fails:** The text pixels scale with the image, often becoming blurry, and the spacing cannot be manipulated by custom stylesheets.

## How to Check <!-- role: check -->
*   **The Test (Zoom):** Use the browser's built-in zoom function to increase the view to 200%.
*   **The Test (Spacing):** Apply a custom stylesheet or bookmarklet that increases line height, letter spacing, and word spacing.
*   **Visual Sign:** Check if the text actually changes size/spacing. Ensure that the text does not overlap other content or vanish outside the chart's bounding box.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch CSS font units from absolute units (like `px` or `pt`) to relative units (like `rem`, `em`, or `%`).
*   **Best Fix:** Implement a responsive layout logic (e.g., collision detection for labels) that adjusts the position of chart elements or increases the container size when the text dimensions change.
