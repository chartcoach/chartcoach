---
id: use-animated-transitions-and-object-continuity-to-avoid-disorientation
title: Use Animated Transitions and Object Continuity to Avoid Disorientation
bibliography: references.bib
description: Animate changes between states so viewers can track what changed and
  keep their mental map.
labels:
- task:track-change
- impact:clarity
- custom:transition-guidance
- custom:animated-transitions
- audience:general
---

## The Rule <!-- role: advice -->

When changing views or chart states, use animated transitions that preserve object continuity and, when needed, stage complex transitions into smaller steps.

## The Logic <!-- role: reason -->

The paper treats transition guidance (animated transitions, object continuity, continuity editing ideas) as a key narrative tactic: it helps viewers remain oriented across scene changes and understand correspondence between old and new states. The Gapminder case highlights staged transitions when changing chart types to prevent confusion.

- **The Principle:** Smooth, staged transitions preserve correspondence and reduce reorientation.
- **The Evidence:** [@segelNarrativeVisualizationTelling2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand how the view changes over time, filters, or narrative steps.
- **Data Type:** Time-series updates, state changes, and especially transitions between different chart forms.
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When instantaneous switching is necessary to support rapid scanning of alternatives.
- **Reason:** Animation can slow navigation and frustrate experienced users in high-speed comparison tasks [@segelNarrativeVisualizationTelling2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Development effort and time-on-task.
- **The Risk:** Poorly designed animation can distract or obscure the data change rather than clarify it [@segelNarrativeVisualizationTelling2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Hard cuts between radically different encodings without guidance.
- **Why it fails:** Viewers must rebuild their mental model from scratch and may misinterpret changes as data differences rather than form differences [@segelNarrativeVisualizationTelling2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Users say “Wait—what happened?” after a step change.
- **The Test:** Ask a viewer to describe what changed between two states; if they can’t, transitions are not preserving correspondence [@segelNarrativeVisualizationTelling2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a simple animated interpolation for position/shape changes.
- **Best Fix:** Stage major transitions (especially chart-type morphs) into multiple readable steps and keep key objects visually continuous [@segelNarrativeVisualizationTelling2010].
