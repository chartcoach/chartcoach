---
id: ensure-interactive-state-contrast
title: Ensure High Contrast or Visual Cues for Interaction States
bibliography: references.bib
description: Interactive states like hover or focus must distinguish themselves with
  a 3:1 contrast change or distinct non-color indicators.
labels:
- visual:color
- visual:shape
- impact:accessibility
- impact:operability
- task:interact
- audience:low-vision
---

## The Rule <!-- role: advice -->
Design interactive elements (such as chart marks or buttons) so that state changes—including hover, focus, or selection—exhibit at least a 3:1 contrast ratio against their previous state. Alternatively, or additionally, use strong non-color indicators such as a stroke thickness change of at least 2px, a dash pattern, or an added marker.

## The Logic <!-- role: reason -->
Users rely on visual feedback to confirm that a system has received an input or that a specific element is ready for interaction. If the change in state is too subtle, the system may appear unresponsive or "broken" to users with low vision or color vision deficiencies.
*   **The Principle:** The intersection of **Perceivable** and **Operable**. While contrast is a visual property, it functionally determines whether an interface is operable. If a user cannot perceive the focus state, they cannot effectively operate the interface [@elavsky_how_2022].
*   **The Evidence:** WCAG 2.1 guidelines require non-text contrast for graphical objects to ensure they are distinguishable [@w3c_understanding_non_text_2]. Tools like the Visa Chart Components library emphasize utilities to manage these states programmatically to meet these requirements [@github_visa_chart].

## Where to Apply <!-- role: context -->
This applies to any data visualization element that accepts user input.
*   **User Goal:** Navigating a chart via keyboard (tabbing through data points) or using a mouse to brush/select specific values.
*   **Data Type:** Interactive charts (e.g., bar charts, scatter plots) and control elements (filters, legends).
*   **Audience:** Essential for users with low vision, color blindness, and keyboard-only users who rely on focus indicators.

## When to Break It <!-- role: exceptions -->
The requirement for a 3:1 *color* contrast change can be bypassed if robust non-color indicators are used.
*   **Scenario:** When color palettes are strictly constrained or fully utilized for data encoding.
*   **Reason:** If a non-color indicator is sufficiently strong—such as adding a thick border (>2px), a pattern, or a distinct shape change—the color contrast shift is not strictly required, provided the non-color cue is high-contrast and obvious [@elavsky_how_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to use subtle aesthetic shifts (like slight opacity changes) as the sole indicator of interaction.
*   **The Risk:** Implementing heavy borders or patterns for every interaction state can increase visual clutter in dense datasets if not managed carefully.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Changing only the hue (e.g., blue to red) or slightly darkening a color without checking the contrast ratio.
*   **Why it fails:** This relies solely on color perception, which fails for colorblind users, and often fails the 3:1 ratio test for low-vision users.
*   **The Wrong Fix:** Adding a 1px border.
*   **Why it fails:** A 1px change is often too thin to be reliably noticed as a state change [@elavsky_how_2022].

## How to Check <!-- role: check -->
*   **Visual Sign:** Toggle the interaction state (hover or tab to the element). Is the change obvious if you look at the screen through a grayscale filter?
*   **The Test:** Use a dropper tool to sample the color of the element in its "default" state and its "active" (hover/focus) state. Compare these two colors using the WebAIM Contrast Checker or similar tools to ensure a 3:1 ratio [@elavsky_how_2022].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Significantly darken or lighten the element on hover/focus to achieve the 3:1 ratio.
*   **Best Fix:** Implement redundant encoding: use both a high-contrast color change *and* a non-color indicator (like a 2px+ border or a hatched pattern) to ensure the state change is undeniable to all users [@elavsky_how_2022].
