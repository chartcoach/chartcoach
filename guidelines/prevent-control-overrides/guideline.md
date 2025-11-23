---
id: prevent-control-overrides
title: Prevent Custom Controls from Overriding Assistive Technology
bibliography: references.bib
description: Ensure custom keyboard and touch controls do not interfere with screen
  reader settings or native browser navigation.
labels:
- accessibility:operable
- interaction:keyboard
- standard:wcag
- tool:screen-reader
- impact:accessibility
- compliance:critical
---

## The Rule <!-- role: advice -->
Ensure that custom keyboard and touch controls do not override screen reader settings or native browser functionality. Restrict custom key bindings so they apply only when the specific visualization element has focus, and never apply global overrides that affect the entire page or application.

## The Logic <!-- role: reason -->
This guideline falls under the "Operable" principle of the Chartability framework, which mandates that controls must be error-tolerant and discoverable [@elavsky_how_2022]. When visualization controls hijack standard navigation keys (such as the `Tab` key) or standard screen reader shortcuts without proper scoping, they create "keyboard traps" that prevent users from navigating or exiting the interface. According to WCAG standards, character key shortcuts must be remappable, capable of being turned off, or active only when the component has focus to prevent conflicts with assistive technologies [@w3c_character_key].

## Where to Apply <!-- role: context -->
This rule applies to all interactive data visualizations and interfaces that support input beyond standard HTML links and buttons.
*   **User Goal:** Navigating complex data structures or filtering data using a keyboard or touch interface.
*   **Data Type:** Interactive dashboards or charts requiring custom navigation logic (e.g., traversing a scatterplot grid).
*   **Audience:** Users relying on keyboards, screen readers, or other assistive input devices.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Explicit Interaction Modes.
*   **Reason:** While you must not override controls *globally*, you may override standard keys (like arrow keys) *temporarily* if the user has explicitly entered a specific interaction mode (e.g., pressing `Ctrl+Enter` to "enter" a chart area). However, clear instructions and an exit mechanism (like `Esc`) must be provided [@sf_covid19_data_2].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Engineering complexity increases because event listeners must be scoped strictly to specific DOM elements rather than checking global key presses.
*   **The Risk:** Requires careful state management to track when a user has "entered" or "exited" the visualization context.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Attaching keydown event listeners to the `window` or `document` object for chart navigation.
*   **Why it fails:** This captures keystrokes regardless of where the user is on the page, potentially triggering chart actions when the user intends to trigger screen reader commands or browser shortcuts [@w3c_character_key].
*   **The Wrong Fix:** disabling the `Tab` key to force users to navigate internal chart elements.
*   **Why it fails:** This creates a keyboard trap, preventing the user from moving to the next section of the page [@elavsky_how_2022].

## How to Check <!-- role: check -->
*   **Visual Sign:** The focus indicator disappears or gets stuck within a chart, or the screen reader behaves unexpectedly.
*   **The Test:** Perform a manual audit using a keyboard. Press the `Tab` key to navigate through the interface; verify you can enter and exit the visualization. With a screen reader running, ensure that pressing standard reading keys works normally unless you have explicitly focused the chart element [@elavsky_how_2022].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Ensure all custom keyboard event listeners are attached only to the chart container element, not the global window.
*   **Best Fix:** Implement a "two-stage" navigation model. For example, San Francisco's COVID-19 dashboard requires users to press specific keys (e.g., `Ctrl+Enter`) to enter the chart interactions, `Tab` or arrows to navigate internal data, and `Esc` to leave, preventing accidental overrides [@sf_covid19_data_2].
