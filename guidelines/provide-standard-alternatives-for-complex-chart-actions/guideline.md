---
id: provide-standard-alternatives-for-complex-chart-actions
title: Provide Standard Alternatives for Complex Chart Actions
bibliography: references.bib
description: Ensure every complex chart interaction (e.g., brushing, zooming, filtering,
  gestures) has a clear, standard UI alternative usable via keyboard, screen reader,
  and touch.
labels:
- chart:interactive
- task:navigate
- task:filter
- task:zoom
- visual:interaction
- impact:accessibility
- data:any
- audience:all
- source:chartability
- category:operable
---

## The Rule <!-- role: advice -->

Provide a standard UI alternative for every complex or custom chart action (e.g., brushing, zooming, filtering, gesturing), and ensure the alternative is clear and usable with keyboard, screen reader, and touch.

## The Logic <!-- role: reason -->

Interactive charts often implement “special actions” that depend on complex pointer gestures or motion-based input, which can block access when a user cannot perform that input mode. Providing alternative ways to perform the same task reduces reliance on a single interaction method and supports error-tolerant, discoverable operation across modalities [@elavskyHowAccessibleMy2022].

- **The Principle:** Multiple ways to operate and locate/perform actions in an interface reduces exclusion from single-mode interactions.
- **The Evidence:** [@w3c_understanding_multiple] [@elavskyHowAccessibleMy2022]

## Where to Apply <!-- role: context -->

Apply this whenever a visualization uses custom interactions beyond basic “activate a control” patterns.

- **User Goal:** Explore, select, filter, pan/zoom, or otherwise manipulate data to reach insights.
- **Data Type:** Any data shown in interactive charts where actions like brushing/zooming/filtering/gesturing are offered.
- **Audience:** Users who rely on keyboard-only operation, screen readers, touch interfaces, or cannot use motion/pointer gestures reliably [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

Do not omit alternatives simply because the gesture interaction exists.

- **Scenario:** The visualization is strictly non-interactive (no brushing/zooming/filtering/gesturing exists at all).
- **Reason:** There is no “special action” to provide an alternative for [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

Providing alternatives adds design and implementation work.

- **The Sacrifice:** More UI surface area (e.g., extra controls like search, menus, or form elements) and additional development complexity [@elavskyHowAccessibleMy2022].
- **The Risk:** Poorly designed alternatives can be confusing or feel like a weaker “copy” of the primary interaction if they are unclear or hard to operate [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Making the gesture itself “keyboard equivalent” only as a 1:1 translation (e.g., tabbing through every mark to simulate hover/brush) without offering an easier standard control path.
- **Why it fails:** It can remain difficult, slow, and unclear even if technically operable, and may not provide a genuinely usable alternative way to complete the action [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Offering the complex action only via motion or multi-point gesture.
- **Why it fails:** It creates a single-mode interaction path rather than “multiple ways,” leaving users without viable access to the feature [@w3c_understanding_multiple] [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Key features (filter, brush, zoom, select) appear to require dragging, multi-touch gestures, or motion to work, and there is no obvious standard control (buttons, inputs, search) that does the same thing [@elavskyHowAccessibleMy2022].
- **The Test:** Identify each special action the chart supports (brushing/zooming/filtering/gesturing). For each one, verify there is at least one standard UI alternative for accomplishing it, and that it can be used via keyboard, screen reader, and touch [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a standard control that triggers the same outcome as the special action (e.g., explicit filter controls instead of brush-only filtering), and make it usable across keyboard, screen reader, and touch [@elavskyHowAccessibleMy2022].
- **Best Fix:** Provide genuinely different alternative paths (not only 1:1 translations), such as adding a search function across the data or chart space to directly select elements, alongside clear, standard controls for the complex action [@elavskyHowAccessibleMy2022] [@w3c_understanding_multiple].
