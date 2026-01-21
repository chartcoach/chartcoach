---
id: do-not-use-color-alone-to-communicate-meaning
title: Add a Non-Color Encoding for Every Meaningful Distinction
bibliography: references.bib
description: Do not rely on color alone to convey essential information; add redundant
  encodings like textures, shapes, size, or dash patterns.
labels:
- chart:general
- task:identify
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- source:chartability
---

## The Rule <!-- role: advice -->

Do not use color as the only way to communicate meaningful or essential information in a chart; add at least one redundant, non-color channel. For categorical color schemes, add textures, shapes, size (for filled marks), or dash patterns (for lines/paths) alongside color.

## The Logic <!-- role: reason -->

Relying on color alone creates a single point of failure: if a user cannot perceive color differences, the encoded categories/statuses become indistinguishable, blocking access to the information [@w3c_understanding_use]. Chartability includes this as a Perceivable accessibility heuristic for data visualizations and interfaces [@elavskyHowAccessibleMy2022], and demonstrates that adding patterns (e.g., textures) allows categories to remain distinguishable even when color cannot be used effectively [@observablehq_no_use].

- **The Principle:** Redundant (multi-channel) encoding preserves meaning when color perception is limited.
- **The Evidence:** [@w3c_understanding_use] [@observablehq_no_use] [@elavskyHowAccessibleMy2022]

## Where to Apply <!-- role: context -->

This advice is designed for charts where color currently carries meaning by itself.

- **User Goal:** Identify groups, categories, or status states that are currently distinguished only by color.
- **Data Type:** Categorical groupings encoded with a color scheme (e.g., multiple series, legend-based categories, colored segments).
- **Audience:** Any audience, including people who cannot reliably perceive color differences [@w3c_understanding_use].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Color is purely decorative and does not encode any meaningful or essential distinction.
- **Reason:** If color communicates no information, then it is not serving as the sole channel for meaning and this rule is not applicable [@w3c_understanding_use].

## The Price <!-- role: costs -->

- **The Sacrifice:** Visual simplicity and available “ink” or space (e.g., textures, shapes, and dashes add visual elements).
- **The Risk:** Added encodings can increase chart complexity and may require additional design effort to implement well, reflecting Chartability’s note that this is difficult for data visualization practice and needs more effective strategy research [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping categories distinguishable only through different hues (or adding a legend without changing the marks themselves).
- **Why it fails:** The information is still carried only by color, so users who cannot perceive those color differences still cannot distinguish the marks [@w3c_understanding_use].
- **The Wrong Fix:** Using color-only schemes for categories without any texture/shape/dash redundancy.
- **Why it fails:** Categories collapse into visually identical marks when color differences are not perceivable [@observablehq_no_use].

## How to Check <!-- role: check -->

- **Visual Sign:** Multiple categories/series become indistinguishable if you ignore color (e.g., a scatterplot where groups are only different by hue).
- **The Test:** Review whether any category/status distinction would remain identifiable if color were unavailable; if not, the chart violates the rule [@w3c_understanding_use] [@observablehq_no_use].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a redundant encoding that maps to the same categories—e.g., textures for filled areas/segments, shapes for points, or dash patterns for lines/paths [@elavskyHowAccessibleMy2022] [@observablehq_no_use].
- **Best Fix:** Redesign the encoding so each meaningful distinction is conveyed through at least one non-color channel by default (textures/shapes/size/dashes), using the Chartability heuristic as an explicit audit check for Perceivable accessibility [@elavskyHowAccessibleMy2022] and aligning with the WCAG requirement that color not be the only means of conveying information [@w3c_understanding_use].
