---
id: clarify-interactive-context-and-state
title: Explicitly Communicate Interactive Relationships and Updates
bibliography: references.bib
description: Ensure clear text communication and programmatic alerts when charts affect
  page logic or receive external parameters.
labels:
- chart:interactive
- impact:accessibility
- impact:clarity
- task:interaction
- audience:assistive-tech-users
---

## The Rule <!-- role: advice -->
If a visualization affects the logic or layout of the wider page, or if it receives data and parameters from other UI controls, clearly communicate this relationship in text. Provide programmatic alerts or notifications for dynamic updates so they can be monitored without requiring the user to navigate to the changed area.

## The Logic <!-- role: reason -->
Interactive charts often sit within complex interfaces where they affect different areas of a page, or different areas of a page affect them. This cause-and-effect relationship must be transparent to reduce cognitive load and ambiguity [@elavsky_how_2022].

*   **The Principle:** Programmatic Determinability and Feedback. When users of assistive technologies interact with a system, they may not perceive visual updates that occur outside their current focus.
*   **The Evidence:** According to Chartability heuristics, ambiguity regarding state changes creates barriers [@elavsky_how_2022]. Furthermore, WCAG guidelines on Status Messages emphasize that important updates must be programmatically conveyed to assistive technologies (e.g., screen readers) without shifting focus, allowing users to remain informed of changes like dynamic alerts or form results [@w3c_understanding_status].

## Where to Apply <!-- role: context -->
This advice applies to data-driven interfaces and dashboards involving interaction.

*   **User Goal:** Filtering datasets, changing parameters, or triggering logic changes via a chart.
*   **Data Type:** Dynamic data that updates based on user input (parameters) or charts that act as inputs for other page elements.
*   **Audience:** Users of screen readers and users with cognitive disabilities who rely on clear cause-and-effect cues.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Static Visualizations.
*   **Reason:** If the visualization is a static image or SVG that accepts no input and triggers no external page changes, there is no interactive context to clarify.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Technical overhead. Developers must implement specific accessibility APIs (such as ARIA live regions) rather than relying solely on standard visual rendering updates.
*   **The Risk:** Notification fatigue. If implemented poorly (e.g., alerting on every single tick of a slider rather than the final value), the user may be overwhelmed by constant audio feedback.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying only on visual transitions (e.g., an animation) to indicate data has changed.
*   **Why it fails:** Screen reader users generally do not perceive the animation and will not know the data on the page has updated unless they manually explore the page again [@elavsky_how_2022].
*   **The Wrong Fix:** Assuming proximity implies relationship.
*   **Why it fails:** Placing a filter directly above a chart does not guarantee the user understands that one controls the other without explicit text instructions (e.g., WCAG 3.3.2 labels) [@elavsky_how_2022].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for text instructions linking controls to the chart (e.g., "Clicking the bar filters the table below").
*   **The Test:** Perform an action that updates the chart using a screen reader. Does the screen reader announce the result (e.g., "Chart updated, showing 5 items") without you having to move the cursor or focus?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add visible text instructions clarifying the relationship between controls and the visualization (e.g., "Select a year to update the graph").
*   **Best Fix:** Implement semantic status messages that alert assistive technology of changes programmatically (satisfying WCAG 4.1.3) and ensure all input/output relationships are clearly labeled [@w3c_understanding_status].
