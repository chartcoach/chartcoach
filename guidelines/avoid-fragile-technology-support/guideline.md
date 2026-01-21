---
id: avoid-fragile-technology-support
title: Support Multiple Input Mechanisms and Platforms
bibliography: references.bib
description: Ensure chart information and interaction are not restricted to one browser,
  device, OS, or single input method.
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

Do not restrict chart access to a single browser, device, software, operating system, or input method; provide multiple technological means to access the chart’s information and functionality, including the ability to switch between input mechanisms.

## The Logic <!-- role: reason -->

Restricting supported platforms or locking users into one input mechanism makes access fragile: users of assistive technologies and alternative input devices may need to switch between keyboard, mouse, touch, or other mechanisms, and prohibiting or requiring specific inputs excludes them [@w3c_understanding_concurrent]. Chartability frames this as a Robustness requirement: designs should work with users’ compliant assistive technologies of choice across environments rather than being dependent on a single, narrow tech setup [@elavskyHowAccessibleMy2022].

- **The Principle:** Robust compatibility across environments and concurrent input mechanisms
- **The Evidence:** [@elavskyHowAccessibleMy2022] [@w3c_understanding_concurrent]

## Where to Apply <!-- role: context -->

This advice is designed for charts where users must operate or explore information through interaction.

- **User Goal:** Access and operate chart information and functionality even when using different devices, browsers, operating systems, or input methods
- **Data Type:** Any chart whose meaning or functionality depends on interactive access
- **Audience:** Users who rely on assistive technologies or alternative inputs, and mixed-device audiences broadly [@elavskyHowAccessibleMy2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** None stated in the provided sources.
- **Reason:** The cited guidance treats restriction of input mechanisms and narrow technology support as an exclusion risk rather than a conditional preference [@w3c_understanding_concurrent] [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Increased implementation and testing effort across multiple environments and input modes [@elavskyHowAccessibleMy2022].
- **The Risk:** Supporting multiple access paths can introduce inconsistencies between interaction behaviors across technologies if not carefully validated [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Building chart interaction that only works with one input (e.g., mouse-only) or that requires a specific gesture, while assuming others can “just use” that method.
- **Why it fails:** It restricts users’ ability to switch between input mechanisms and can exclude users who depend on different inputs or assistive technologies [@w3c_understanding_concurrent] [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Chart interaction or access fails or becomes unavailable when switching device/browser/OS or when attempting to use a different input method.
- **The Test:** Try operating the chart by switching between input mechanisms (e.g., keyboard vs. mouse vs. touch where applicable) without losing access to information or functionality, consistent with the need to allow concurrent input mechanisms [@w3c_understanding_concurrent].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove restrictions that block switching input mechanisms (e.g., do not require a specific gesture or prohibit a given input path) so users can change how they interact without losing access [@w3c_understanding_concurrent].
- **Best Fix:** Provide a diversity of technological means to access the chart and its information and functionality so it is not isolated to one browser, device, software, or operating system, aligning with Chartability’s Robust “Fragile technology support” heuristic [@elavskyHowAccessibleMy2022].
