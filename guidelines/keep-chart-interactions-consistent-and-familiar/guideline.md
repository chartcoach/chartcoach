---
id: keep-chart-interactions-consistent-and-familiar
title: Keep Chart Styling and Interactions Consistent Across Charts
bibliography: references.bib
description: Use consistent labels, styling, user-set preferences, and interaction
  patterns for charts that perform the same function to reduce confusion.
labels:
- chart:multi
- task:navigate
- visual:layout
- impact:accessibility
- data:any
- audience:all
- principle:flexible
- source:chartability
---

## The Rule <!-- role: advice -->

Make charts consistent and familiar by default: for charts that perform the same function, keep labeling, default styling/settings, user-set styling/settings, and interaction defaults (e.g., keybindings or interaction patterns) the same across the application or environment.

## The Logic <!-- role: reason -->

Consistent identification of components that share the same function helps users recognize controls and reduces confusion, especially for people with cognitive or memory impairments, by lowering the need to relearn labels and interaction patterns between charts [@w3c_understanding_consistent]. Chartability includes this as a Flexible (Perceivable/Operable yet Robust) heuristic to ensure chart experiences remain predictable across contexts and respect user and environment settings [@elavskyHowAccessibleMy2022].

- **The Principle:** Consistent identification for the same function
- **The Evidence:** [@w3c_understanding_consistent] [@elavskyHowAccessibleMy2022]

## Where to Apply <!-- role: context -->

This advice is designed for multi-chart applications or environments where users move between charts that support similar operations.

- **User Goal:** Repeatedly use the same function across multiple charts (e.g., navigate, select, filter, toggle, or otherwise operate chart components)
- **Data Type:** Any
- **Audience:** People who benefit from predictable interfaces, including users with cognitive or memory impairments [@w3c_understanding_consistent]

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** There are no repeated functions across charts (each chart provides entirely distinct controls and tasks).
- **Reason:** The consistency requirement targets components with the same function; if functions do not repeat, there is nothing to keep consistent [@w3c_understanding_consistent].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Reduced freedom to tailor styling or interaction patterns per-chart.
- **The Risk:** Over-standardization can constrain chart-specific design decisions even when a different pattern might feel more optimized for a particular chart.

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Using different labels, icons, or placements for controls that do the same thing in different charts.
- **Why it fails:** Users must relearn identification for the same function, increasing confusion and memory burden [@w3c_understanding_consistent].
- **The Wrong Fix:** Changing keybindings or interaction patterns between charts that perform the same task.
- **Why it fails:** Users cannot reliably transfer what they learned from one chart to another, breaking familiarity and predictability [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** The same function appears under different labels/icons/positions or behaves differently across charts.
- **The Test:** Pick a function that exists in multiple charts and verify it is identified the same way each time (same label/icon/placement) and behaves the same way (same interaction default/keybinding pattern) across those charts [@w3c_understanding_consistent] [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Standardize the identification of same-function components across charts (make labels/icons/positions match) [@w3c_understanding_consistent].
- **Best Fix:** Define and apply shared chart defaults across the environment—including default styling/settings, user-set styling/settings, and interaction defaults (such as keybindings/interaction patterns) for charts that perform the same function—so behavior remains consistent across charts [@elavskyHowAccessibleMy2022].
