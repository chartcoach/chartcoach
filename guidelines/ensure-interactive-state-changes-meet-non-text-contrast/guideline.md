---
id: ensure-interactive-state-changes-meet-non-text-contrast
title: Ensure Interactive State Changes Are Distinguishable
bibliography: references.bib
description: Make hover, focus, and selection states visually distinguishable with
  at least 3:1 contrast change or an equivalent non-color cue.
labels:
- chart:any
- task:interact
- visual:color
- impact:accessibility
- data:any
- audience:general
- category:operable
- standard:wcag-2-1
---

## The Rule <!-- role: advice -->

For every hover, focus, and selection state on an interactive element, ensure the new state is distinguishable from the previous state by **either**:

- a **≥ 3:1 contrast** difference between the two states, **or**
- a **non-color indicator** such as a **stroke thickness change (≥ 2px)**, a **dash pattern**, a **marker**, or another high-contrast technique.

Prefer using **both** color and non-color indicators redundantly.

## The Logic <!-- role: reason -->

- **The Principle:** Operability depends on clearly perceivable state changes; if users cannot detect a control’s current state, they cannot reliably operate it through interaction modes like hover and keyboard focus [@elavskyHowAccessibleMy2022].
- **The Evidence:** WCAG’s guidance on non-text contrast requires sufficient contrast for user interface components and graphical objects so they remain distinguishable, supporting a ≥ 3:1 threshold for UI-related visual differences [@w3c_understanding_non_text_2]. Implementations such as accessible interactivity utilities explicitly add focus/interaction handlers and semantic interaction support to make interactive states clearer across inputs [@github_visa_chart].

## Where to Apply <!-- role: context -->

- **User Goal:** Knowing what is interactive and what state it is in (hovered, focused, selected) to successfully operate chart interactions.
- **Data Type:** Any data shown with interactive marks (e.g., bars, points, lines, legend items, filters) where interaction changes appearance.
- **Audience:** People using keyboard navigation, people with low vision, and anyone relying on clear state change signals during interaction [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The interaction state change is communicated through a clear non-color indicator (e.g., a ≥ 2px stroke increase, pattern change, or marker) and does not rely on color difference.
- **Reason:** The guideline explicitly allows skipping the contrast-difference requirement when an additional high-contrast indication is provided [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional visual styling (thicker strokes, markers, patterns) can increase visual complexity and may alter the chart’s aesthetic.
- **The Risk:** Overuse of redundant cues can make interactive styling feel heavy or distract from the data marks if applied indiscriminately [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Indicating hover/focus/selection only by subtly changing opacity, saturation, or hue.
- **Why it fails:** Small color shifts may not reach a ≥ 3:1 contrast difference between states, making the change hard to detect and therefore hard to operate reliably [@elavskyHowAccessibleMy2022] [@w3c_understanding_non_text_2].
- **The Wrong Fix:** Relying on color-only changes when a clear non-color cue would be needed for redundancy.
- **Why it fails:** The heuristic expects either sufficient contrast difference or an additional indication, and recommends redundant strategies for clarity [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Hover/focus/selection looks “almost the same” as the default state (only a faint tint/opacity shift), or the difference disappears at a glance.
- **The Test:** Sample the two state colors (before vs. after) using a dropper, then compute the contrast ratio between them with a contrast tool (e.g., WebAIM Contrast Tool) to confirm **≥ 3:1**, unless a qualifying non-color cue is present [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a non-color state cue: increase stroke thickness by **≥ 2px**, add a dash pattern, or add a marker for hover/focus/selection [@elavskyHowAccessibleMy2022].
- **Best Fix:** Implement redundant state signaling that works across input modes: ensure state color changes meet the ≥ 3:1 threshold while also adding a strong non-color cue, and wire focus/interaction handling so keyboard users receive the same highlight and semantics support [@elavskyHowAccessibleMy2022] [@github_visa_chart] [@w3c_understanding_non_text_2].
