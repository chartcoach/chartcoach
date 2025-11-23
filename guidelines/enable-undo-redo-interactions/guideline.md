---
id: enable-undo-redo-interactions
title: Enable Undo and Redo for Interactions
bibliography: references.bib
description: Ensure interactive visualizations allow users to easily reverse or re-apply
  actions to support error tolerance and exploration.
labels:
- impact:accessibility
- impact:usability
- interaction:filtering
- interaction:zooming
- audience:cognitive-disability
- standard:chartability
---

## The Rule <!-- role: advice -->
Provide mechanisms for users to undo and redo their actions within interactive data visualizations. Ensure that when a user performs a task—such as filtering, zooming, or selecting data—they can reverse that specific action or re-apply it without restarting the entire experience.

## The Logic <!-- role: reason -->
Human users inevitably make mistakes, and interfaces must be designed to tolerate them. While standard accessibility guidelines like WCAG often limit "Error Prevention" to data entry fields, data experiences involve complex interactions where errors can occur in navigation and exploration [@elavsky_how_2022].
*   **The Principle:** Forgivable Design (Compromising).
*   **The Evidence:** Research into task analysis emphasizes the importance of designing error-tolerant products that acknowledge human error by providing undo/redo features and recovery methods [@article{baber_task_analysis_1994}].
*   **The Gap:** WCAG criterion 3.3.6 "Error Prevention (All)" technically only applies to data entry and text fields, often leaving the complex interaction errors found in data visualization unaddressed [@elavsky_how_2022].

## Where to Apply <!-- role: context -->
This advice applies to any data visualization that allows the user to change the state of the view.
*   **User Goal:** Exploring data through manipulation (e.g., drilling down, filtering categories, changing time ranges).
*   **Data Type:** Interactive dashboards, explorables, and complex data interfaces.
*   **Audience:** All users, but specifically critical for users with cognitive disabilities or motor impairments where accidental clicks or loss of context are more frequent.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Static Visualizations.
*   **Reason:** If the visualization has no interactive elements or tasks to perform, there is no state change to undo.
*   **Scenario:** Single-step interactions that automatically reset.
*   **Reason:** If the interaction is momentary (e.g., a tooltip on hover) and does not persist state, an undo stack is unnecessary.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Development effort. Implementing a state history stack for custom visualizations is significantly more complex than allowing one-way state changes.
*   **The Risk:** Compliance tools may not flag this as an error. Because standard automated checkers follow WCAG (which limits error prevention to data entry), a manual audit is required to identify this barrier [@elavsky_how_2022].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Providing only a "Reset All" button.
*   **Why it fails:** This destroys the user's entire exploration path rather than correcting a specific, recent mistake.
*   **The Wrong Fix:** Relying solely on the browser's "Back" button.
*   **Why it fails:** Many visualization states do not update the browser's history API, meaning the back button may navigate the user away from the page entirely rather than undoing the chart interaction.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for "Undo" and "Redo" controls, or check for keyboard shortcuts (like Ctrl+Z).
*   **The Test:** Interact with the visualization (e.g., filter a category). Attempt to reverse that specific action using provided controls. Then, attempt to re-apply the action.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Ensure the visualization updates the browser URL parameters, allowing the browser's native "Back" and "Forward" buttons to function as undo/redo.
*   **Best Fix:** Implement a dedicated history stack within the visualization interface, providing explicit "Undo" and "Redo" buttons that manage the view state.
