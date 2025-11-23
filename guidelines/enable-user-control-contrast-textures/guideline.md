---
id: enable-user-control-contrast-textures
title: Enable User Control of Contrast and Textures
bibliography: references.bib
description: Ensure visualizations respect system-level contrast settings and provide
  interactive controls to toggle texture overlays.
labels:
- chart:all
- visual:texture
- visual:color
- impact:accessibility
- impact:flexibility
- audience:diverse
- task:customize
---

## The Rule <!-- role: advice -->
Design visualizations to inherently respect user agent contrast settings (such as High Contrast Mode) without overriding them. Additionally, provide interactive mechanisms that allow users to toggle supplementary textures or patterns on and off according to their preference.

## The Logic <!-- role: reason -->
This guideline operates on the "Flexible" principle of Chartability, acknowledging that a single design cannot satisfy every user's access needs simultaneously.
*   **The Principle:** **Competing Needs.** While textures provide necessary redundancy for users with Color Vision Deficiency (CVD), they can introduce visual complexity that creates barriers for users with cognitive disabilities or those relying on pre-attentive processing [@elavsky_how_2022].
*   **The Evidence:** Research indicates that forcing textures on by default can complicate visual processing. Elavsky et al. argue that designs must not be rigid; rather, they should adapt to the "tight coupling between a data experience and the larger technological context the user inhabits" [@elavsky_how_2022]. Experimental work on color scale textures demonstrates that while useful for distinguishing categories, the density and pattern require adjustment to suit different visual abilities [@observablehq_experimental_colour].

## Where to Apply <!-- role: context -->
*   **User Goal:** When the audience includes users with conflicting accessibility needs (e.g., CVD users needing texture vs. users with cognitive load sensitives needing clean visuals).
*   **Data Type:** Visualizations utilizing fill colors to encode categorical or quantitative data (e.g., bar charts, choropleth maps, area charts).
*   **Technical Context:** Digital, interactive interfaces where user input and system settings can be detected (Web, App).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Static Media (Print or rasterized images).
*   **Reason:** Interactive toggling is impossible. In these cases, a "Compromising" design approach is required, where textures are carefully selected to be distinct but minimally intrusive, as the user cannot adjust the display [@elavsky_how_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Increased engineering effort is required to detect system settings (like `forced-colors` media queries) and to build UI controls for toggling textures.
*   **The Risk:** Providing too many controls can lead to "feature bloat" or a cluttered interface if the settings menu is not designed intuitively.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Hard-coding textures to be "always on" to satisfy colorblindness requirements.
*   **Why it fails:** This ignores the cognitive load cost. As noted in the Chartability heuristics, "if some chart textures are on by default, we are creating accessibility barriers due to their visual complexity" [@elavsky_how_2022].
*   **The Wrong Fix:** Using CSS `!important` or specific fill colors that override OS-level High Contrast Modes.
*   **Why it fails:** This prevents the chart from adjusting to the user's explicit system-level requirements for high contrast [@elavsky_how_2022].

## How to Check <!-- role: check -->
*   **Visual Sign:** Toggle your operating system's "High Contrast" or "Invert Colors" mode. Does the chart adapt strictly to the system palette, or does it retain its original styling?
*   **The Test:** Look for a UI element (switch, button, or settings menu) that allows the user to enable or disable patterns/textures independently of the default view.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Ensure your CSS or SVG styling uses semantic system colors where possible and respects the `@media (prefers-contrast: more)` and `@media (forced-colors: active)` queries.
*   **Best Fix:** Implement a "Display Settings" menu near the visualization that includes a toggle for "Enable Pattern Fills," allowing the user to choose the optimal balance between distinguishability and visual clarity [@observablehq_experimental_colour].
