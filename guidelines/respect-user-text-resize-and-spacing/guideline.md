---
id: respect-user-text-resize-and-spacing
title: Respect User Text Resizing and Spacing
bibliography: references.bib
description: Ensure chart text reflows correctly when users change font size or text
  spacing via browser/OS settings without losing content or functionality.
labels:
- chart:any
- task:read
- visual:text
- impact:accessibility
- data:any
- audience:low-vision
- category:flexible
- source:chartability
---

## The Rule <!-- role: advice -->

Do not block or override user-driven font-size, zoom, or text-spacing adjustments; ensure all chart text and related layout reflow so no content or functionality is lost when users enlarge text or change spacing.

## The Logic <!-- role: reason -->

Users with low vision and other access needs rely on programmatic text resizing (e.g., browser zoom) and spacing adjustments to make content readable; if charts prevent these changes or break layout, critical information becomes unreadable or unusable. Chartability frames this as a **Flexible** accessibility requirement: the visualization must respect user agent settings and remain robust under user customization [@elavskyHowAccessibleMy2022]. WCAG guidance requires that text can be resized substantially without assistive technology and without loss of content or functionality [@w3c_understanding_resize].

## Where to Apply <!-- role: context -->

This advice is designed for chart experiences where text conveys meaning.

- **User Goal:** Read titles, captions, annotations, labels, legends, tooltips, and instructions to understand or operate the chart.
- **Data Type:** Any data; this is triggered by the presence of textual elements in the visualization or its controls.
- **Audience:** People who increase font size or adjust spacing for readability (including people with low vision) [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization contains no text elements (no title, labels, legend text, instructions, or textual controls).
- **Reason:** There is no text to resize or reflow; the specific failure mode described by the heuristic cannot occur [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** More layout space may be needed for labels, titles, and controls at larger sizes.
- **The Risk:** Resized text can cause overlaps or push content, requiring redesign of spacing and responsive behavior to preserve readability and function [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Locking font sizes or text containers so zoomed/resized text clips, overlaps, or disappears.
- **Why it fails:** It interferes with programmatic user changes and leads to loss of content or functionality when users adjust text settings, violating the intended behavior described in WCAG guidance and Chartability’s Flexible heuristic [@elavskyHowAccessibleMy2022] [@w3c_understanding_resize].

## How to Check <!-- role: check -->

- **Visual Sign:** After increasing text size or spacing, labels/legend/title/annotations clip, overlap, become truncated, or controls become unusable.
- **The Test:** Use the browser’s built-in zoom and/or apply a custom stylesheet that changes font size and text spacing; confirm the chart’s text and layout adjust without losing content or functionality [@elavskyHowAccessibleMy2022] [@w3c_understanding_resize].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove or reduce constraints that prevent reflow (e.g., rigid containers that clip text) so text can expand and remain visible under zoom/spacing changes [@elavskyHowAccessibleMy2022].
- **Best Fix:** Redesign text and layout behavior so titles, labels, legends, annotations, and instructions reflow predictably under user text resizing and spacing adjustments without loss of content or functionality, aligning with Chartability’s Flexible principle and WCAG expectations [@elavskyHowAccessibleMy2022] [@w3c_understanding_resize].
