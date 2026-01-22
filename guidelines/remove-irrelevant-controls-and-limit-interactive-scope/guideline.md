---
id: remove-irrelevant-controls-and-limit-interactive-scope
title: "Remove irrelevant controls and limit the chart\u2019s interactive scope to\
  \ the task"
bibliography: references.bib
description: "Include only interactive controls that directly support the chart\u2019\
  s message, question, or user task to reduce cognitive load."
labels:
- chart:interactive
- task:explore
- visual:interaction
- impact:clarity
- data:unknown
- audience:general
- accessibility:understandable
- complexity:reduced
---

## Keep only task-relevant controls in interactive charts <!-- role: advice -->

Remove controls and interactive features that do not directly support the chart’s message, question, or user task. Keep the chart’s interactive scope narrow enough that users are not forced to parse or operate extra functionality to understand the data.

## Irrelevant controls increase cognitive load and reduce understandability <!-- role: reason -->

Irrelevant or excessively broad controls add choices, interaction paths, and UI elements that users must interpret, which increases cognitive load and creates cognitive barriers even when the data itself is otherwise clear.

**Mechanism:** Reducing nonessential controls reduces decision overhead and interaction work, helping users focus on interpreting the data rather than managing the interface.

**Evidence:** Interactive data visualizations should minimize cognitive barriers by avoiding unnecessary controls and functionality that do not add value to the user’s task [@elavskyHowAccessibleMy2022]. Including only features that add value and removing unnecessary options and complexity reduces cognitive load and prevents interactive elements from distracting from the task [@inclusivedesignprinciples_add_value].

**Notes:** This guideline targets understandability failures caused by interaction-by-default patterns where charts expose broad, generic interactions even when those interactions do not contribute to the intended reading or decision.

## Apply when interaction exists but the task is narrow <!-- role: context -->

- **User Goal:** Understand the chart’s message or complete a specific decision with minimal distraction.
- **Task:** Read, interpret, filter, or explore data in a way aligned with the chart’s stated purpose.
- **Data:** Any dataset where comprehension depends more on interpretation than on extensive exploratory manipulation.
- **Chart Setting:** Interactive charts, dashboards, or data apps with multiple widgets, controls, or interaction modes.
- **Audience:** General audiences, including people who experience higher cognitive load from complex interfaces.
- **Success Criterion:** Users can reach the intended takeaway without engaging with irrelevant controls or complex interaction paths.

## Allow broader controls only when exploration is the purpose <!-- role: exceptions -->

**Break it when:** The primary goal is open-ended exploration that genuinely requires a broad set of controls. **Why:** Constraining interaction in that case can prevent users from performing the intended analysis.

## Simplifying controls may reduce flexibility for expert workflows <!-- role: costs -->

**Sacrifice:** Removing controls can reduce flexibility for power users or exploratory analysis. **Risk:** Over-pruning can eliminate a control that some users rely on for a valid task. **Mitigation:** Frame the chart’s intended question clearly so “relevance” is evaluated against an explicit task.

## “Interaction by default” adds controls that do not add value <!-- role: mistakes -->

**Mistake:** Keeping generic interactions (e.g., hover, click, drag-select) enabled even when they do not support the chart’s purpose. **Why it fails:** Users spend effort discovering or interpreting interaction affordances that do not improve understanding of the data.

## Spot irrelevant controls by checking whether they support the stated task <!-- role: check -->

**Failure Sign:** Users can interact in multiple ways, but those actions do not change or clarify anything related to the chart’s message or task.\
**Quick Check:** For each control or interaction, ask “What user question does this help answer?” and mark anything without a clear answer as irrelevant.\
**Stronger Test:** Ask a small set of users to complete the chart’s intended task and note any controls they ignore or find distracting.

## Reduce the control surface and align interaction to the purpose <!-- role: fix -->

- Remove controls and interaction modes that are not necessary for the chart’s stated message, question, or task.
- Replace multiple overlapping controls with a smaller set that supports the same intended outcome.
- Narrow the chart’s interactive scope to the minimal functionality required to complete the intended task.
- If broad exploration is required, separate it into a dedicated exploratory view rather than bundling it into a message-focused chart.
