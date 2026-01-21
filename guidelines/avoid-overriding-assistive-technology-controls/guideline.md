---
id: avoid-overriding-assistive-technology-controls
title: Keep Custom Shortcuts Scoped and Non-Overriding
bibliography: references.bib
description: Ensure custom keyboard and touch controls never override assistive-technology
  commands and only work when the chart is focused.
labels:
- chart:interactive
- task:navigate
- visual:interaction
- impact:accessibility
- data:any
- audience:assistive-technology-users
- principle:operable
- source:chartability
---

## The Rule <!-- role: advice -->

Do not override assistive-technology (AT) keyboard behavior with custom shortcuts. Any custom keyboard or touch controls must be active only when the chart (or a chart element) has focus, and must not take over page- or app-level keys.

## The Logic <!-- role: reason -->

Custom shortcuts that intercept keys can conflict with screen readers and other AT, preventing users from operating or escaping the interface and creating severe navigation failures (e.g., keyboard traps) [@elavskyHowAccessibleMy2022]. WCAG requires that single-character key shortcuts be avoidable or constrained—by providing a way to turn them off, remap them to include modifier keys, or ensuring they are active only when the relevant component has focus [@w3c_character_key].

- **The Principle:** Avoid AT input conflicts by scoping shortcuts to focused components.
- **The Evidence:** [@elavskyHowAccessibleMy2022] [@w3c_character_key]

## Where to Apply <!-- role: context -->

Apply this to any interactive visualization that adds custom key or gesture handling.

- **User Goal:** Navigate, operate, and exit chart interactions using keyboard or assistive technology.
- **Data Type:** Any data displayed through interactive charts, dashboards, or filters.
- **Audience:** Keyboard-only users and screen reader users interacting with data experiences [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization has no custom key controls (it relies entirely on default browser/AT interaction patterns).
- **Reason:** There are no custom shortcuts to scope or remediate; the rule is not applicable [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer global or “always-on” shortcuts, which may reduce speed for power users.
- **The Risk:** If shortcut design is constrained to focus and modifiers, interactions may feel less “slick” or require more deliberate user steps [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Overriding standard navigation keys (e.g., Tab) to drive chart navigation.
- **Why it fails:** It can block expected keyboard and screen reader workflows and may trap users inside the widget [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Using single-character shortcuts globally without an off switch or remapping.
- **Why it fails:** It can conflict with AT commands and violates the required mitigations for character key shortcuts [@w3c_character_key].

## How to Check <!-- role: check -->

- **Visual Sign:** Keyboard navigation becomes “stuck” in the chart, or focus cannot move past the visualization.
- **The Test:** With the keyboard, try navigating the page into and out of the chart; verify custom shortcuts only work when the chart is focused. Confirm single-character shortcuts can be turned off, remapped with modifier keys, or are focus-scoped [@w3c_character_key]. If the page provides keyboard instructions, confirm they describe focus-based entry/exit behavior (e.g., explicit instructions for entering and navigating charts) [@sf_covid19_data_2].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Restrict custom shortcuts so they trigger only when the chart (or a chart element) has focus, and avoid overriding standard keys used for navigation or AT workflows [@elavskyHowAccessibleMy2022].
- **Best Fix:** For any single-character shortcuts, implement one of the permitted mitigations—provide a way to turn them off, remap them to include a modifier key (e.g., Ctrl/Alt), or keep them active only on focus—and document the keyboard interaction model for users [@w3c_character_key] [@sf_covid19_data_2] [@elavskyHowAccessibleMy2022].
