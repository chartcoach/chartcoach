---
id: provide-interaction-cues-and-keyboard-instructions
title: Provide Interaction Cues and Keyboard Instructions
bibliography: references.bib
description: "If a chart is interactive, explicitly explain what users can do and\
  \ how to do it\u2014including keyboard controls."
labels:
- chart:interactive
- task:navigate
- visual:interaction
- impact:accessibility
- data:any
- audience:all
- source:chartability
---

## The Rule <!-- role: advice -->

If a chart has any interactivity, provide clear instructions that describe the available interactions and how to perform them with different inputs, including keyboard controls. [@elavskyHowAccessibleMy2022]

## The Logic <!-- role: reason -->

- **The Principle:** Interaction discoverability requires explicit labels or instructions so users can understand what actions are possible and what information is required to operate controls.
- **The Evidence:** WCAG requires labels or instructions for interactive controls so users (particularly those with cognitive disabilities) can understand how to use them [@w3c_understanding_labels], and Chartability flags missing interaction cues as a critical operability failure for interactive charts [@elavskyHowAccessibleMy2022]. A real-world dashboard example shows that providing explicit keyboard instructions enables keyboard and screen reader users to navigate and operate interactive charts [@sf_covid19_data].

## Where to Apply <!-- role: context -->

- **User Goal:** Discovering and operating interactive chart features (e.g., entering a chart, navigating marks/controls, selecting/filtering). [@elavskyHowAccessibleMy2022]
- **Data Type:** Any data, as long as the chart or dashboard includes interactive capabilities. [@elavskyHowAccessibleMy2022]
- **Audience:** All users, including keyboard-only and screen reader users who need explicit cues to find and operate interactions. [@sf_covid19_data]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization has no interactive capabilities.
- **Reason:** There are no interactions to explain, so interaction instructions are not applicable. [@elavskyHowAccessibleMy2022]

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional on-screen text or UI space to display instructions. [@elavskyHowAccessibleMy2022]
- **The Risk:** Instructions can add perceived complexity or require maintenance if interactions change. [@elavskyHowAccessibleMy2022]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming “good design needs no instructions” and providing no cues for hover, click, or keyboard interaction.
- **Why it fails:** It makes interaction discoverability depend on ableist assumptions and leaves users unable to know what actions are available or how to perform them, especially via keyboard. [@elavskyHowAccessibleMy2022]

## How to Check <!-- role: check -->

- **Visual Sign:** An interactive chart provides no visible explanation of available actions or keyboard controls. [@elavskyHowAccessibleMy2022]
- **The Test:** Try to use the chart without a mouse: press Tab and use common keys (e.g., arrows, Enter/Space as applicable) and confirm the chart itself explains how to navigate and operate its interactive features. Compare against an example that publishes explicit keyboard instructions (e.g., “enter dashboard,” “navigate visuals,” “enter a chart/filter,” “select options”) [@sf_covid19_data].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a concise, visible “How to interact” note near the chart that states the chart’s interactive capabilities and the keyboard controls needed to use them. [@elavskyHowAccessibleMy2022]
- **Best Fix:** Provide complete, explicit interaction instructions for each supported input method (mouse/hover behaviors and keyboard navigation/activation), aligned with the expectation that controls have clear labels or instructions. [@w3c_understanding_labels] [@elavskyHowAccessibleMy2022] [@sf_covid19_data]
