---
id: provide-multi-input-interactions-for-charts
title: Provide Keyboard-Equivalent Controls for Every Interactive Chart Action
bibliography: references.bib
description: Ensure every interactive chart feature works via keyboard as well as
  pointer/touch, with consistent focus and activation behavior.
labels:
- chart:interactive
- task:explore
- visual:interaction
- impact:accessibility
- data:any
- audience:all
- principle:operable
- source:chartability
---

## The Rule <!-- role: advice -->

For any chart that supports pointer interaction (mouse/touch/pen), provide an equivalent keyboard interaction for every function, and verify it works with both keyboard-only use and screen readers.

## The Logic <!-- role: reason -->

People who cannot use a mouse (including many assistive-technology users) rely on the keyboard interface to reach and operate functionality. Requiring a single input modality creates an access barrier because the functionality becomes unusable without that modality [@w3c_understanding_keyboard]. Chartability treats this as a critical operability requirement for interactive visualizations and emphasizes that keyboard operability must be tested alongside screen-reader operability, with touch considered as a distinct experience as well [@elavskyHowAccessibleMy2022].

- **The Principle:** Input modality redundancy (keyboard-operable functionality)
- **The Evidence:** WCAG keyboard operability requirements and Chartability’s critical heuristic on single-modality interaction [@w3c_understanding_keyboard; @elavskyHowAccessibleMy2022]

## Where to Apply <!-- role: context -->

This advice is designed for interactive data experiences where users need to operate controls, not just view a static image.

- **User Goal:** Navigating, selecting, filtering, drilling down, triggering tooltips/details, or manipulating chart state
- **Data Type:** Any data type presented with interactive controls (e.g., dashboards, interactive articles, embedded charts)
- **Audience:** People using keyboards, screen readers, and alternative input devices that map to keyboard interaction; also relevant to touch users because touch behavior can diverge from mouse behavior [@elavskyHowAccessibleMy2022]

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** The chart has no interactive functionality (purely static content).
- **Reason:** There is no interaction to replicate; the guideline targets operability of interactive features [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Additional engineering and design work to define focus order, keyboard commands, and equivalent states (focus vs. hover; activation vs. click) across all interactive features [@elavskyHowAccessibleMy2022].
- **The Risk:** Inconsistent experiences across devices if keyboard, screen reader, and touch behaviors are implemented separately without coordinated testing; Chartability notes touch introduces distinct issues (e.g., larger hit areas) and remains a challenging area [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Supporting tab focus on the chart container but not on the actual interactive elements or actions.
- **Why it fails:** Users can reach the chart but cannot operate its functionality via keyboard, violating keyboard operability expectations [@w3c_understanding_keyboard; @elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Treating hover-only interactions (tooltips/details) as “optional” and not providing a focus-equivalent experience.
- **Why it fails:** If important information appears on hover, keyboard focus must expose the same information to be operable and perceivable for keyboard and screen reader users [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Assuming mouse and touch are the same because both are “pointer,” and skipping touch checks.
- **Why it fails:** Chartability warns touch can behave differently and can introduce unique accessibility failures (e.g., target size and accuracy issues) [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** You can hover/click to reveal data or change state, but keyboard users cannot reach the same elements, cannot trigger the same changes, or get “stuck” without a clear path through the interaction.
- **The Test:** Using only the keyboard, navigate to the chart and operate every interactive feature (Tab to move, Arrow keys where appropriate, Enter/Space to activate). Confirm that focus behavior mirrors hover and activation mirrors click. Then repeat key interactions with a screen reader enabled, and also test on a touch device to confirm the experience still works as intended [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add keyboard support so users can reach interactive elements and activate the same functions using standard keys (Tab for navigation; Enter/Space for activation), ensuring focus produces the same outcomes as hover [@elavskyHowAccessibleMy2022].
- **Best Fix:** Design and implement a fully keyboard-operable interaction model where the navigation pattern matches the chart’s data structure, and validate operability with both keyboard-only use and screen readers; additionally validate the interaction on touch devices to ensure pointer/touch differences do not break access [@elavskyHowAccessibleMy2022; @progressiveaccess_accessible_chemistry; @w3c_understanding_keyboard].
