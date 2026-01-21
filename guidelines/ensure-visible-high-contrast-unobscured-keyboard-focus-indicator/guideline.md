---
id: ensure-visible-high-contrast-unobscured-keyboard-focus-indicator
title: Provide a Visible, High-Contrast Keyboard Focus Indicator
bibliography: references.bib
description: Ensure every keyboard-focusable chart control shows an unobscured, easy-to-see
  focus indicator with sufficient contrast and thickness.
labels:
- chart:interactive
- task:navigate
- visual:contrast
- impact:accessibility
- data:any
- audience:keyboard-users
- category:operable
---

## The Rule <!-- role: advice -->

For every keyboard-focusable element in your visualization, show a visible focus indicator that is not fully obscured, uses at least a 2px border, and has at least 4.5:1 contrast against the background.

## The Logic <!-- role: reason -->

A clear focus indicator makes keyboard navigation discoverable by visually communicating *where* interaction will occur next; without it, users can lose their place while tabbing through chart controls and marks, undermining operability in data interfaces [@elavskyHowAccessibleMy2022].

- **The Principle:** Visible focus communicates current interaction target during keyboard navigation.
- **The Evidence:** WCAG’s focus appearance guidance specifies minimum size/area and contrast requirements so users can reliably locate focus [@w3c_understanding_focus]. Chartability highlights focus indication as frequently missing or left to fragile defaults in chart implementations, motivating explicit authoring in visualization contexts [@elavskyHowAccessibleMy2022].

## Where to Apply <!-- role: context -->

This advice is designed for keyboard operation of visualization interfaces.

- **User Goal:** Navigate and operate interactive chart elements using a keyboard (e.g., tabbing between controls/marks).
- **Data Type:** Any (applies to the interface elements, not the dataset).
- **Audience:** Keyboard users, including people using assistive technologies that rely on keyboard interaction [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization contains no keyboard-focusable elements (no interactive controls and nothing that can receive focus).
- **Reason:** If nothing can receive keyboard focus, a focus indicator cannot appear; the rule is not applicable in that case [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional visual styling (e.g., borders/outlines) that may affect the chart’s aesthetic or visual density.
- **The Risk:** Over-relying on default focus styles can lead to inconsistent or hard-to-see focus across environments, which Chartability notes is common in practice [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Leaving focus indication entirely to browser/library defaults without checking visibility on chart marks and controls.
- **Why it fails:** Defaults often assume enclosure, size, and color that may not work for visualization marks or custom SVG/canvas UI; Chartability observes custom, author-provided focus indication is rare in chart ecosystems [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Adding a focus style that is present but too subtle (thin line, low-contrast color, or hidden behind other elements).
- **Why it fails:** The indicator may be technically present but effectively invisible if obscured or low contrast, violating the intent of focus appearance guidance [@w3c_understanding_focus].

## How to Check <!-- role: check -->

- **Visual Sign:** While tabbing through the visualization, focus “disappears,” is hard to locate, or is hidden behind chart marks/overlays [@elavskyHowAccessibleMy2022].
- **The Test:** Use keyboard navigation (e.g., Tab) and verify the focus indicator is always visible; sample its colors with a dropper and confirm the focus indicator meets the stated contrast requirement against the background, using a contrast checker such as WebAIM’s tool [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an explicit focus style (e.g., an outline or border) that is at least 2px thick, not obscured, and meets the required contrast against the background [@elavskyHowAccessibleMy2022].
- **Best Fix:** Implement author-controlled focus handling for chart elements so focus indication is consistently applied to interactive marks and controls (e.g., using utility patterns like adding focus listeners to highlight elements during keyboard navigation) [@github_visa_chart_2].
