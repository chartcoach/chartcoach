---
id: provide-explicit-interaction-instructions
title: Provide Explicit Instructions for Interactive Elements
bibliography: references.bib
description: Always provide visible text explaining how to use interactive features,
  including mouse and keyboard controls, to ensure accessibility.
labels:
- impact:accessibility
- impact:operability
- task:interact
- task:navigate
- compliance:wcag
- audience:novice
---

## The Rule <!-- role: advice -->
If a data visualization possesses any interactive capabilities, you must explicitly explain them to the user. Do not rely on "intuition." You must provide instructions for all input methods, including specific keys required for keyboard navigation.

## The Logic <!-- role: reason -->
Designers often fall into the trap of believing that "if a design is good, no instructions are needed." This is an ableist assumption that relies on a specific, normative model of user behavior and ability. Explicit instructions are critical for operability and cognitive accessibility.

*   **The Principle:** Operability and Predictability. Users with cognitive disabilities or those using assistive technologies (like screen readers or keyboards) cannot rely on visual affordances alone to guess interaction mechanics.
*   **The Evidence:** The Chartability framework identifies the lack of interaction cues as a critical failure [@elavsky_how_2022]. Furthermore, WCAG guidelines emphasize that form fields and interactive controls must include clear instructions to help users understand what is required [@w3c_understanding_labels].

## Where to Apply <!-- role: context -->
This guideline applies to any data interface that is not a static image.

*   **User Goal:** Navigating complex data structures, filtering data, or accessing details-on-demand (tooltips).
*   **Data Type:** Interactive dashboards, drill-down charts, or time-series with zooming/panning.
*   **Audience:** All users, but specifically vital for keyboard-only users, screen reader users, and users with cognitive disabilities.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Completely static visualizations.
*   **Reason:** If there is no interactivity (no tooltips, no filtering, no zooming), no instructions are required regarding operation.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate. You must allocate space for text descriptions or help buttons.
*   **The Risk:** Visual clutter if the instructions are wordy or poorly placed.

## Common Mistakes <!-- role: mistakes -->
*   **The "Intuitive" Fallacy:** Assuming users will know to "brush" a timeline or click a bar without being told.
*   **Mouse-Only Instructions:** Providing text that says "Hover for details" while failing to list the keys (e.g., Arrow keys, Enter, Space) required for keyboard users to access the same data.
*   **Hidden Instructions:** Burying the controls in a documentation page rather than placing them near the interface element.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for text near the chart title or footer. Does it say "Click," "Hover," or "Use arrow keys"?
*   **The Test:** Navigate to the chart using only the `Tab` key. Is it obvious what keys you need to press next to interact with the data points?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a subtitle or caption to the chart: "Hover over bars to see values. Use Tab to focus and Arrow Keys to navigate."
*   **Best Fix:** Implement a dedicated "Accessibility" or "How to Navigate" feature similar to the San Francisco COVID-19 dashboard, which provides specific keyboard commands (e.g., "Ctrl+Enter to enter the dashboard, Arrow keys to navigate") [@sf_covid19_data].
