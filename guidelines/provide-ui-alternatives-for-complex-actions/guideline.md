---
id: provide-ui-alternatives-for-complex-actions
title: Provide Standard UI Alternatives for Complex Actions
bibliography: references.bib
description: Ensure complex chart interactions like brushing, zooming, or filtering
  have accessible, standard user interface equivalents.
labels:
- impact:accessibility
- impact:operability
- task:interact
- task:filter
- visual:interface
- chart:interactive
---

## The Rule <!-- role: advice -->
Provide standard user interface controls—such as buttons, text inputs, or menus—as alternatives to complex pointer gestures like brushing, zooming, panning, or drag-filtering within a visualization.

## The Logic <!-- role: reason -->
Complex interaction patterns that rely on specific physical gestures (dragging, pinching, drawing a box) exclude users who cannot perform fine motor movements or who utilize assistive technologies. Standard interface elements ensure operability across different modes of use.

*   **The Principle:** Operable and Robust Design (POUR).
*   **The Evidence:** According to Chartability, relying solely on custom controls creates barriers for users with motor, visual, or cognitive impairments [@elavsky_how_2022]. This aligns with WCAG 2.1 standards regarding "Pointer Gestures," "Motion Actuation," and "Multiple Ways" [@w3c_understanding_multiple]. Offering redundant methods, such as search functions or menus, reduces reliance on specific physical capabilities and memory [@w3c_understanding_multiple].

## Where to Apply <!-- role: context -->
This applies to any data interface containing "special actions" beyond simple static consumption.

*   **User Goal:** Filtering data, exploring deep zoom levels, or selecting specific data points.
*   **Interaction Type:** Visualizations utilizing brushing, lasso selection, canvas dragging, or scroll-to-zoom.
*   **Audience:** All users, specifically those using keyboards, screen readers, voice control software, or touch devices without multi-touch support.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Strictly static media (images or print).
*   **Reason:** If the media is non-interactive by nature, interaction alternatives are not applicable (though accessible data descriptions are still required).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate. Adding standard UI controls (like dropdowns, search bars, or zoom buttons) takes up space that might otherwise be used for the data graphic.
*   **The Risk:** Increased interface complexity. Poorly organized controls can lead to visual clutter, potentially affecting the "Understandable" principle if not grouped logically.

## Common Mistakes <!-- role: mistakes -->
*   **The 1-to-1 Translation Fallacy:** Attempting to exactly replicate a complex mouse gesture (like drawing a lasso) with a keyboard, rather than providing a functional alternative (like a "Select All in Region" button or a search filter) [@elavsky_how_2022].
*   **Hidden Controls:** Hiding the alternative controls deep in a context menu that is not discoverable via keyboard navigation.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there buttons or inputs visible near the chart that control the data view?
*   **The Test:** unplug your mouse or ignore your trackpad. Can you perform the exact same filtering, zooming, or selection tasks using *only* the Tab, Arrow, and Enter keys? If you cannot, the visualization fails this heuristic [@elavsky_how_2022].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add simple HTML buttons for "Zoom In," "Zoom Out," and "Reset View" alongside the chart.
*   **Best Fix:** Implement a "Multiple Ways" approach. For example, if a chart allows drag-selection to filter points, add a text-based search function or a faceted checkbox list that filters the data in the same way [@elavsky_how_2022].
