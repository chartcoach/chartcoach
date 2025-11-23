---
id: ensure-multimodal-input-redundancy
title: Enable Keyboard and Touch Input for All Interactions
bibliography: references.bib
description: Ensure interactive data visualizations are operable via keyboard and
  touch interfaces, not just a mouse cursor.
labels:
- impact:accessibility
- impact:operability
- task:interact
- task:navigate
- visual:interaction
- audience:impaired-motor
- audience:blind
---

## The Rule <!-- role: advice -->
Ensure that every interaction available via a mouse (such as hovering or clicking) is also operable using a keyboard and touch interface. Map focusing to hovering behavior, and map selecting (via Enter or Spacebar) to clicking behavior. Do not rely on a single input modality.

## The Logic <!-- role: reason -->
Interactive charts must be robust enough to handle input from various sources. The keyboard interface is the single most important technical foundation for interactive content because many assistive technologies (like screen readers and switch devices) utilize the keyboard API to drive navigation [@elavsky_how_2022]. 

*   **The Principle:** Operable (POUR). Controls must be error-tolerant and discoverable across modalities.
*   **The Evidence:** WCAG guidelines state that all functionality must be operable using a keyboard without requiring specific timings, ensuring that pointer-based interactions have equivalents for users who cannot use a mouse [@w3c_understanding_keyboard]. Furthermore, systems like Progressive Access demonstrate that features like menu-driven exploration and magnification rely on these underlying accessible structures [@progressiveaccess_accessible_chemistry].

## Where to Apply <!-- role: context -->
This guideline applies to any data interface that accepts user input.

*   **User Goal:** Filtering data, viewing tooltips, selecting data points, or drilling down into details.
*   **Data Type:** Interactive visualizations (e.g., bar charts with tooltips, scatterplots with selection brushing).
*   **Audience:** Users with motor impairments, screen reader users, and users on touch devices (mobile/tablet).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Static media.
*   **Reason:** If a chart is a static image (PNG/JPG) or a non-interactive SVG meant only for viewing, input modality checks are not applicable (though alternative text is still required).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Implementing robust keyboard navigation (such as managing focus within an SVG or Canvas) requires significantly more engineering effort than simple mouse events.
*   **The Risk:** Mobile touch interfaces often couple "pointer" logic with mouse logic but require much larger hit areas. Simply enabling touch without adjusting layout for finger size can lead to frustration due to the "fat finger" problem, which remains a difficult design challenge [@elavsky_how_2022].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding `onClick` events to non-interactive elements (like `<div>` or `<span>`) without adding `tabindex` or `onKeyDown` listeners.
*   **Why it fails:** The element remains invisible to the keyboard focus order, making it impossible to reach without a mouse.
*   **The Wrong Fix:** Assuming mobile accessibility is solved because the mouse logic "technically" works on touch screens.
*   **Why it fails:** Touch targets are often too small compared to the precision of a mouse cursor.

## How to Check <!-- role: check -->
*   **Visual Sign:** When pressing the `Tab` key, a visible focus indicator (ring or border) should appear around the interactive element.
*   **The Test:** Perform a "No Mouse" audit. Put the mouse away and attempt to access all chart information using only `Tab` (to navigate), `Arrow Keys` (to move between related data), and `Enter/Space` (to select) [@elavsky_how_2022]. Verify separately with a screen reader and a touch device.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Ensure all interactive elements have `tabindex="0"` and appropriate ARIA roles, allowing them to receive focus.
*   **Best Fix:** Implement a comprehensive keyboard navigation strategy where `Tab` enters the chart area and `Arrow Keys` allow traversal of the data structure (e.g., moving between bars or points), mirroring the exploration capability of a mouse hover [@progressiveaccess_accessible_chemistry].
