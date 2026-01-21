---
id: remove-irrelevant-controls
title: Remove Irrelevant Controls
bibliography: references.bib
description: "Include only interactive controls that directly support the chart\u2019\
  s message or user task, and remove functionality that adds no value."
labels:
- chart:interactive
- task:explore
- impact:clarity
- impact:accessibility
- audience:novice
- source:chartability
---

## The Rule <!-- role: advice -->

Remove any control, widget, or interaction that is not directly relevant to the chart’s message, question, or user task, and keep the chart’s interactive scope narrowly focused.

## The Logic <!-- role: reason -->

Unnecessary controls increase the amount of decision-making and interaction work required, creating cognitive barriers and distracting from the intended communication of the chart [@elavskyHowAccessibleMy2022].

- **The Principle:** Add Value (only include features that add value; avoid unnecessary options and complexity).
- **The Evidence:** [@inclusivedesignprinciples_add_value]

## Where to Apply <!-- role: context -->

This advice is designed for interactive data visualizations where multiple controls or interaction modes are present.

- **User Goal:** Use the chart to answer a specific question or complete a specific task without distraction.
- **Data Type:** Any data type, especially when presented through dashboards or multi-control interfaces.
- **Audience:** People who may experience higher cognitive load from extra options, including accessibility novices and general audiences [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart is explicitly intended as an open-ended analysis tool where broad exploration is the primary purpose.
- **Reason:** Removing controls may prevent legitimate exploratory workflows, reducing the tool’s intended value [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less flexibility for users who want to explore beyond the primary question.
- **The Risk:** Over-pruning controls can remove capabilities some users rely on for their specific analysis tasks [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping default interaction behaviors (e.g., hover, drag-select, click actions) even when they do not help answer the chart’s intended question.
- **Why it fails:** The interface still demands attention and effort from users without providing value, increasing cognitive load instead of reducing it [@elavskyHowAccessibleMy2022]; this violates the “Add Value” principle [@inclusivedesignprinciples_add_value].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart presents many controls or interaction affordances that do not clearly connect to the chart’s purpose.
- **The Test:** For each control, state the exact message/question/task it supports; if you cannot name one, the control is irrelevant and should be removed [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Disable or hide irrelevant default interactions and controls that do not contribute to the chart’s message or task [@elavskyHowAccessibleMy2022].
- **Best Fix:** Redesign the interaction model so every control has a clear, task-aligned purpose and the overall interactive scope is intentionally constrained to adding user value [@elavskyHowAccessibleMy2022] [@inclusivedesignprinciples_add_value].
