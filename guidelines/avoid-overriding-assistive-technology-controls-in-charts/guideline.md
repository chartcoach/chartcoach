---
id: avoid-overriding-assistive-technology-controls-in-charts
title: Limit custom keyboard and touch shortcuts to focused chart elements and never
  override assistive technology controls
bibliography: references.bib
description: Ensure custom chart shortcuts do not conflict with screen readers by
  activating them only on focus and avoiding global overrides.
labels:
- chart:interactive
- task:navigate
- visual:interaction
- impact:accessibility
- data:any
- audience:assistive-tech
- input:keyboard
- input:touch
- standard:wcag-2-1-4
- complexity:advanced
---

## Custom shortcuts must not override assistive technology controls <!-- role: advice -->

Do not override screen reader or other assistive technology keyboard behaviors with custom chart shortcuts; activate any custom keyboard or touch controls only when the chart (or a chart element) has focus. Avoid global page- or app-level key overrides, especially changes to native navigation keys.

## Why focus-scoped shortcuts prevent assistive technology conflicts <!-- role: reason -->

Assistive technologies rely on predictable, system-level key handling to navigate, read, and operate interfaces. Global or always-on shortcuts can intercept keys that users depend on (including screen-reader command patterns), producing traps, lost navigation, or unexpected mode switches that prevent operation of the visualization.

**Mechanism:** Restricting shortcuts to focused components preserves the user’s primary navigation model and prevents inadvertent interception of keys outside the intended interaction context.

**Evidence:** Single-character and other custom shortcuts must be disableable, remappable to include a modifier, or active only when the target component has focus to prevent conflicts with assistive technologies [@w3c_character_key]. Providing explicit keyboard instructions for entering and navigating interactive chart regions supports operable keyboard and screen reader interaction in practice [@sf_covid19_data_2]. This requirement is treated as a critical operability heuristic for accessible visualization auditing [@elavskyHowAccessibleMy2022].

**Notes:** This guideline applies to both keyboard and touch-triggered controls that emulate keyboard-like shortcuts or gestures that can interfere with assistive technology interaction patterns.

## When custom shortcut scoping is required in visualizations <!-- role: context -->

- **User Goal:** Navigate, explore, and operate an interactive visualization without losing their assistive technology’s control model.
- **Task:** Move focus, select marks, filter, change views, or enter/exit chart interaction modes.
- **Data:** Any data type; risk increases with multi-step interactions (filtering, drilling, brushing, cross-highlighting).
- **Chart Setting:** Web/app visualizations with custom interactions, keyboard shortcuts, gesture controls, or scripted key handlers.
- **Audience:** Screen reader users and other assistive technology users who depend on keyboard APIs and consistent focus behavior.
- **Success Criterion:** All chart functionality remains operable without disabling or degrading assistive technology navigation and reading.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart has no custom keyboard or touch shortcuts at all. **Why:** There is nothing to scope to focus or risk overriding assistive technology controls.

## Tradeoffs of focus-only custom controls <!-- role: costs -->

**Sacrifice:** Some “power-user” global shortcuts and always-on interactions. **Risk:** Users may not discover chart-specific shortcuts if they only activate on focus. **Mitigation:** Provide clear keyboard instructions for entering the chart region and operating controls once focused.

## Common ways teams accidentally override assistive technology controls <!-- role: mistakes -->

- **Mistake:** Binding single-letter shortcuts globally (active anywhere on the page/app). **Why it fails:** It can conflict with assistive technology command patterns and trigger unexpected actions outside the chart context.
- **Mistake:** Overriding native navigation keys (such as Tab) for chart movement. **Why it fails:** It can create a keyboard trap or break standard focus navigation needed by keyboard and screen reader users.

## How to quickly detect assistive technology shortcut conflicts <!-- role: check -->

**Failure Sign:** Pressing navigation keys causes unexpected chart actions outside the chart region, or focus cannot reliably leave the chart once entered. **Quick Check:** Use the keyboard to move focus into and out of the chart; confirm custom shortcuts do nothing when focus is outside the chart. **Stronger Test:** Validate that shortcuts are disableable, remappable with modifiers, or focus-scoped, and verify the chart’s keyboard interaction cues match actual behavior.

## Remediations for shortcut and focus conflicts <!-- role: fix -->

- Scope all custom keyboard handlers so they only run when the chart container or an interactive chart element has focus.
- Provide a way to turn off single-character shortcuts or remap them to include modifier keys, rather than intercepting unmodified character keys.
- Add explicit keyboard instructions for how to enter the chart region, navigate within it, operate controls, and exit back to the page.
- Remove or redesign any shortcut that requires overriding native focus navigation keys, replacing it with focusable controls and standard key activation behavior.
