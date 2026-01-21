---
id: make-the-key-slice-stand-out-and-avoid-rainbow-colors-in-pie-charts
title: Highlight One Slice and Use Muted Shades for the Rest
bibliography: references.bib
description: 'Use color sparingly in pie charts: make the most important slice stand
  out and keep other slices in shades of one color.'
labels:
- chart:pie
- task:highlight
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

In a pie chart, use color to emphasize the most important slice, and render the remaining slices as shades of a single color; do not use rainbow colors. [@muth_pie_charts_2018]

## The Logic <!-- role: reason -->

Bright, varied colors pull attention away from the comparison of slice sizes; a single highlighted slice focuses readers on what matters while subdued, related hues keep the rest readable without distraction. [@muth_pie_charts_2018]

- **The Principle:** Direct attention with selective emphasis rather than competing signals.
- **The Evidence:** [@muth_pie_charts_2018]

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Identify the most important share quickly while still seeing the overall split. [@muth_pie_charts_2018]
- **Data Type:** Part-to-whole pie chart with a clear “key” category to emphasize. [@muth_pie_charts_2018]
- **Audience:** General audiences who may be distracted by unnecessary color variation. [@muth_pie_charts_2018]

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** There is no single most important value to highlight.\
  **Reason:** Emphasis would be arbitrary; use consistent subdued styling across slices instead. [@muth_pie_charts_2018]

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** You lose strong categorical color separation across all slices. [@muth_pie_charts_2018]
- **The Risk:** If you choose the “most important” slice incorrectly, you may guide attention to the wrong takeaway. [@muth_pie_charts_2018]

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Assigning every slice a different bright hue (rainbow palette).\
  **Why it fails:** It distracts readers from comparing the pie shares. [@muth_pie_charts_2018]
- **The Wrong Fix:** Giving multiple slices equally strong emphasis colors.\
  **Why it fails:** Competing highlights dilute the intended focus on the key value. [@muth_pie_charts_2018]

## How to Check <!-- role: check -->

- **Visual Sign:** Every slice is equally saturated/different in hue, and no single takeaway visually leads. [@muth_pie_charts_2018]
- **The Test:** Ask: “Does one slice clearly read as the focus at a glance?” If not—or if all slices compete—revise the palette. [@muth_pie_charts_2018]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Pick one slice to highlight; convert the rest to lighter/darker shades of one base color. [@muth_pie_charts_2018]
- **Best Fix:** Rework the narrative focus so only one slice needs emphasis, then apply a restrained palette that supports that hierarchy. [@muth_pie_charts_2018]
