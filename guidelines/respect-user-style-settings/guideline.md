---
id: respect-user-style-settings
title: Respect User-Defined Styling and Settings
bibliography: references.bib
description: Ensure data visualizations inherit and adapt to user-agent settings,
  such as high contrast modes, custom fonts, and animation preferences, rather than
  overriding them.
labels:
- impact:accessibility
- impact:flexibility
- visual:style
- visual:color
- compliance:wcag
- complexity:intermediate
---

## The Rule <!-- role: advice -->
Design your visualization to inherit and respect user-agent settings and custom stylesheets. Do not use hard-coded styles, `!important` overrides, or rigid definitions that prevent users from adjusting text size, spacing, color themes (such as High Contrast Mode), or animation preferences.

## The Logic <!-- role: reason -->
This guideline is based on the **Flexible** principle of the Chartability framework, which asserts that designs must not be rigid in their opinions and ability assumptions. Users must have the agency to adjust the Perceivable and Operable traits of a data experience to suit their needs [@elavsky_how_2022].

*   **The Principle:** Robust User Agency. The preferences a user sets in lower-level systems (operating systems, browsers) must be respected in higher-level environments (the data visualization).
*   **The Evidence:** This heuristic synthesizes multiple WCAG standards, including 1.4.4 (Resize text), 1.4.12 (Text Spacing), and 2.3.3 (Animation from Interactions). Chartability identifies "User style change not respected" as a **Critical** heuristic, noting that designs failing to respect these settings (e.g., forcing textures or specific colors) create high risks of assistive failure [@elavsky_how_2022].

## Where to Apply <!-- role: context -->
This applies to all web-based and digital interactive data visualizations.

*   **User Goal:** The user needs to modify the display to make it readable (e.g., enabling Windows High Contrast White Mode to see boundaries, or increasing text spacing to improve legibility).
*   **Data Type:** Any HTML, SVG, or Canvas-based visualization.
*   **Audience:** Users with low vision, cognitive disabilities, or light sensitivity who rely on custom stylesheets or system-level accessibility overrides.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Rasterized Static Media (PNG/JPG).
*   **Reason:** Pre-rendered images cannot dynamically accept CSS changes or user-agent styles. However, auditors are advised to be "especially critical of static designs" for this very reason, as they represent a high risk of failure [@elavsky_how_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose absolute control over the specific color palette or pixel-perfect layout of the visualization when a user overrides it.
*   **The Risk:** If not tested, a chart in High Contrast Mode might render invisible elements (e.g., white bars on a white background) if system colors are not mapped correctly.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Hard-coding hex values (e.g., `fill="#000000"`) directly on SVG elements or using `!important` in CSS to force brand colors.
*   **Why it fails:** This blocks the user's browser from applying their preferred color scheme (e.g., High Contrast Mode), potentially making the chart invisible or painful to view.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart appearance change when you alter your browser or OS settings?
*   **The Test:** As recommended in Chartability's validation process: "Auditors should first try to change system settings (such as toggling high contrast modes) to see whether a data experience respects these settings" [@elavsky_how_2022]. Additionally, attempt to inject a custom stylesheet to increase text spacing or change fonts.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove inline styles and `!important` declarations that prevent text resizing or color changes.
*   **Best Fix:** Use CSS variables (custom properties) or system color keywords (e.g., `CanvasText`, `Highlight`) for chart fills and strokes. Ensure layout containers use relative units (like `em` or `rem`) rather than pixels to support text reflow.
