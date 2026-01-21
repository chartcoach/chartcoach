---
id: avoid-inappropriate-tab-stops-in-charts
title: Control Tab Stops for Interactive Chart Elements
bibliography: references.bib
description: Ensure only meaningful interactive chart controls are focusable, and
  prevent dense per-mark tabbing by using progressive keyboard navigation.
labels:
- chart:interactive
- task:navigate
- visual:position
- impact:accessibility
- data:any
- audience:keyboard-users
- source:chartability
---

## The Rule <!-- role: advice -->

Give tab stops only to truly interactive chart controls, and avoid assigning a tab stop to every mark in a chart; instead, provide a small number of entry points (e.g., one root tab stop) and let users progressively navigate deeper with keyboard controls.

## The Logic <!-- role: reason -->

- **The Principle:** Keyboard focus must preserve operability and meaning without creating unnecessary navigation burden.
- **The Evidence:** Chartability flags “inappropriate tab stops” as a common web chart failure where authors tabindex every element, creating tedious keyboard exploration; it recommends progressive disclosure (single entry point, then structured keyboard navigation) for complex charts [@elavskyHowAccessibleMy2022]. WCAG focus order requires that focusable elements be encountered in a logical sequence that preserves meaning and operability, making predictable, structured focus critical for keyboard users [@w3c_understanding_focus_order]. A chart-component accessibility template illustrates implementing keyboard navigation, tab order, and focus management so complex charts can be explored without making every element a tab stop [@observablehq_chart_component].

## Where to Apply <!-- role: context -->

- **User Goal:** Navigating and operating interactive chart functionality efficiently using a keyboard.
- **Data Type:** Charts with many marks (dense) and/or multi-layer interactions (e.g., stacks, groups, drilldowns) where per-mark tabbing becomes burdensome.
- **Audience:** Keyboard-only users and users of assistive technologies that rely on keyboard APIs [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** A small chart or sparse interactive display where each interactive mark can reasonably be navigated via Tab without tedium.
- **Reason:** Chartability allows per-element tab stops only when the chart is small or when tab stops are programmatically revealed (progressive disclosure), because dense per-mark focus creates excessive navigation effort [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** More engineering/design work to implement focus management and structured keyboard navigation rather than relying on default tabbing.
- **The Risk:** If progressive navigation is implemented poorly, users may have difficulty discovering how to “enter” and “exit” chart layers, reducing operability [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assigning `tabindex` to every SVG mark (including non-interactive marks) so screen readers/keyboard users can reach everything.
- **Why it fails:** It creates an overwhelming number of tab stops and makes navigation tedious; Chartability notes this is a common failure pattern and recommends progressive disclosure instead [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Giving non-interactive decorative elements a tab stop.
- **Why it fails:** It adds focusable items that do not provide operable functionality, harming logical focus order expectations [@w3c_understanding_focus_order].

## How to Check <!-- role: check -->

- **Visual Sign:** Pressing Tab causes focus to move through many chart marks that do not act like controls, or focus lands on elements that do nothing.
- **The Test:** Use only the keyboard and press Tab through the page: confirm that (1) interactive controls have a tab stop, (2) non-interactive elements do not, and (3) the focus sequence remains logical and usable rather than forcing per-mark tabbing in dense charts [@elavskyHowAccessibleMy2022] [@w3c_understanding_focus_order].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove tab stops from non-interactive chart elements and ensure only actual controls (buttons/links/selectable features) are focusable [@elavskyHowAccessibleMy2022].
- **Best Fix:** Provide a single (or small number of) chart entry tab stop(s) and implement programmatic focus management and keyboard navigation to traverse chart structure/layers without requiring every mark to be a tab stop (progressive disclosure) [@elavskyHowAccessibleMy2022] [@observablehq_chart_component].
