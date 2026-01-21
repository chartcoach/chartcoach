---
id: respect-user-style-overrides
title: Respect User Style Overrides
bibliography: references.bib
description: Ensure charts do not block or override user-selected styling and presentation
  settings from browsers, operating systems, or custom stylesheets.
labels:
- chart:any
- task:any
- visual:any
- impact:accessibility
- data:any
- audience:all
- category:flexible
- source:chartability
---

## The Rule <!-- role: advice -->

Do not override or prevent user-applied styling. Ensure the chart remains usable and readable when users change styles via their user agent (e.g., custom CSS, browser zoom, reflow, text spacing, high-contrast modes).

## The Logic <!-- role: reason -->

Blocking user style changes removes a primary accessibility mechanism users rely on to make content perceivable and operable in their own environment.

- **The Principle:** User agency through system/user-agent presentation controls must be preserved for robust access.
- **The Evidence:** Chartability marks “User style change not respected” as a critical Flexible heuristic and ties it to WCAG criteria for resizing text, reflow, text spacing, and avoiding disruptive time-based or motion-related behavior [@elavskyHowAccessibleMy2022]. This heuristic is explicitly grounded in standards (WCAG) [@Ini].

## Where to Apply <!-- role: context -->

This advice applies whenever the visualization is displayed in an environment where users can change presentation/interaction settings.

- **User Goal:** Access and operate the chart under their own readability and interaction preferences (e.g., larger text, higher contrast, more spacing).
- **Data Type:** Any (static or interactive charts, dashboards, embedded charts in web apps).
- **Audience:** Users who depend on user-agent styling controls, including people using high contrast modes, custom stylesheets, zoom/reflow, or other accessibility settings [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** A strictly controlled, non-user-facing rendering pipeline (e.g., server-side image export with no user customization possible).
- **Reason:** If there is no user agent or no mechanism for users to apply styles, “respecting user style changes” is not applicable as an interaction requirement (though alternative accessible representations may still be needed) [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less pixel-perfect visual control and more engineering effort to support responsive/reflowing layouts and variable typography.
- **The Risk:** Without careful implementation, layouts may wrap, overlap, or require redesign to remain legible under extreme user settings [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Hard-coding font sizes and containers (e.g., fixed px text, fixed-height SVG) so zoom/reflow can’t work.
  - **Why it fails:** Users cannot enlarge text or reflow content without losing information or functionality, violating standards-based expectations [@Ini].
- **The Wrong Fix:** Overriding high-contrast or forced-colors behavior with custom colors.
  - **Why it fails:** It defeats the user’s system-level accessibility setting and can make content unreadable in high-contrast contexts [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Disabling text selection, focus outlines, or user stylesheet influence for “design consistency.”
  - **Why it fails:** It blocks user-agent adaptations needed for operability and perceivability [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Text doesn’t resize, content overlaps/clips on zoom, colors become unreadable in high contrast/forced colors, or spacing settings cause breakage rather than graceful reflow.
- **The Test:** Change user-agent presentation settings and confirm the chart still works: apply zoom/reflow, adjust text spacing, and toggle high-contrast/forced-colors modes; verify the chart does not suppress these changes and remains readable/operable [@elavskyHowAccessibleMy2022] [@Ini].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove chart code/styles that forcibly override user-agent settings (e.g., avoid fixed text sizing and prevent clipping that breaks reflow); allow default focus indicators and system color modes to apply [@elavskyHowAccessibleMy2022].
- **Best Fix:** Design the visualization to be robust under user-controlled presentation: support reflowing layouts and scalable typography, and ensure the chart remains perceivable and operable when user settings (including custom stylesheets and high-contrast modes) are applied [@elavskyHowAccessibleMy2022] [@Ini].
