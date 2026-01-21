---
id: ensure-sufficient-contrast-for-text-and-chart-geometry
title: Ensure Sufficient Contrast for Text and Chart Geometry
bibliography: references.bib
description: Make regular text exceed 4.5:1 contrast and chart geometries/large text
  exceed 3:1 against adjacent background colors.
labels:
- chart:any
- task:read
- visual:color
- impact:accessibility
- data:any
- audience:all
- source:chartability
---

## The Rule <!-- role: advice -->

Ensure contrast meets thresholds everywhere it conveys meaning: regular text must be >4.5:1, and large text plus chart geometries (non-text graphical objects) must be >3:1 against adjacent/background colors [@elavskyHowAccessibleMy2022].

## The Logic <!-- role: reason -->

Low contrast prevents users from reliably distinguishing text and graphical marks from their background, making chart content hard to perceive and interpret; Chartability flags this as a critical and very common accessibility failure [@elavskyHowAccessibleMy2022]. WCAG 2.1 explicitly requires at least 3:1 contrast for non-text graphical objects and UI components, which includes chart elements that users must see to understand the visualization [@w3c_understanding_non_text]. Practical auditing guidance and examples for measuring and achieving these thresholds are documented for data visualization workflows [@observablehq_high_contrast].

- **The Principle:** Perceivability of meaningful marks and text via sufficient luminance contrast
- **The Evidence:** [@elavskyHowAccessibleMy2022] [@w3c_understanding_non_text] [@observablehq_high_contrast]

## Where to Apply <!-- role: context -->

This advice is designed for any visualization where people must visually identify text or marks.

- **User Goal:** Identifying labels, reading values, and distinguishing chart marks from the background
- **Data Type:** Any (applies to all data encodings that are rendered as text or graphical objects)
- **Audience:** People with low vision and, more broadly, all viewers in varied viewing conditions [@elavskyHowAccessibleMy2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** None supported by the provided sources.
- **Reason:** Chartability marks low contrast as a critical issue and the cited standards require minimum contrast for relevant content [@elavskyHowAccessibleMy2022] [@w3c_understanding_non_text].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced freedom to use very light, subtle palettes or faint mark styling.
- **The Risk:** Adjusting colors to meet contrast can change the intended aesthetic, and may require redesigning encodings or styling choices rather than keeping “barely visible” treatments [@observablehq_high_contrast].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Leaving low-contrast fills as-is and assuming the chart is acceptable because the overall page “looks clean.”

- **Why it fails:** The meaningful marks still do not meet the required contrast thresholds for non-text objects or text, so users may not be able to perceive them [@w3c_understanding_non_text] [@elavskyHowAccessibleMy2022].

- **The Wrong Fix:** Checking contrast for only one element (e.g., axis text) and ignoring mark states or other geometries.

- **Why it fails:** Chartability treats contrast as a broad critical failure; any meaningful geometry or text that falls below thresholds remains inaccessible [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Text or marks appear faint, washed out, or hard to distinguish from the background (especially when the viewer’s vision or display conditions are not ideal) [@elavskyHowAccessibleMy2022].
- **The Test:** Sample the foreground and background colors and compute the contrast ratio using a contrast checker tool, verifying >4.5:1 for regular text and >3:1 for large text and chart geometries [@webaim_contrast_checker] [@observablehq_high_contrast].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust the foreground and/or background colors until measured contrast clears the thresholds (>4.5:1 for regular text; >3:1 for large text and geometries) [@webaim_contrast_checker].
- **Best Fix:** Redesign mark styling so the encoding remains the same but contrast passes reliably (for example, modify visual treatments using documented high-contrast chart techniques and re-measure) [@observablehq_high_contrast] [@elavskyHowAccessibleMy2022].
