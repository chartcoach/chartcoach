---
id: keep-relative-values-signed-everywhere
title: Keep Relative Values Signed Everywhere
bibliography: references.bib
description: "Preserve the minus sign and relative framing on axes and tooltips so\
  \ viewers don\u2019t misread indexed values as absolute."
labels:
- chart:line
- task:interpret
- visual:annotation
- impact:clarity
- data:temporal
- audience:novice
- concept:index
- source:datawrapper-fix-my-chart
---

## The Rule <!-- role: advice -->

Show indexed/relative values with their correct sign and framing everywhere (y-axis labels and tooltip values), e.g., “−11%” rather than “11.”

## The Logic <!-- role: reason -->

When relative measures lose their sign, the chart stops communicating direction and can imply the opposite meaning. Repeating the “negative percentage from baseline” representation across axis and tooltips reinforces the intended interpretation and prevents confusion, as explicitly recommended in [@mintzer_y_axis_2024].

- **The Principle:** Maintain consistent encoding of direction for relative metrics
- **The Evidence:** [@mintzer_y_axis_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand whether values are above/below a baseline and by how much.
- **Data Type:** Differences from a reference point, especially when most values are negative (e.g., “how far below the record/current baseline past values were”).
- **Audience:** General audiences prone to interpret magnitudes without direction.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally transform the measure to an absolute distance (“distance from baseline”) and clearly relabel it as such.
- **Reason:** In that different measure, sign is not meaningful—but the unit/label must change to avoid deception.

## The Price <!-- role: costs -->

- **The Sacrifice:** Some viewers may find “all negatives” visually or emotionally counterintuitive.
- **The Risk:** If the baseline concept isn’t well explained, persistent negatives might be misread as “bad news” rather than “below current/reference.”

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Dropping the minus sign in tooltips (or formatting tooltips differently from the axis).
- **Why it fails:** It breaks the mental model established by the axis and reintroduces ambiguity about direction, a problem the post aims to solve via consistent negative framing [@mintzer_y_axis_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Axis shows negative ticks, but tooltips (or labels) show positive numbers for the same points.
- **The Test:** Hover (or inspect labels) on a clearly negative region; if the tooltip reads positive, your sign consistency is broken.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Update tooltip/label formatting to include the sign (e.g., “−11%”).
- **Best Fix:** Standardize formatting rules so every displayed value (axis + tooltip) expresses “% from [baseline]” consistently, as advocated in [@mintzer_y_axis_2024].
