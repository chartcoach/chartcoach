---
id: directly-label-instead-of-legend
title: Directly Label Marks Instead of Using a Legend
bibliography: references.bib
description: Replace color-lookup legends with direct labels to reduce memory and
  attention switching.
labels:
- chart:pie
- task:identify
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
---

## The Rule <!-- role: advice -->

Directly label categories on the marks (slices/lines/bars). Do not force viewers to decode colors via a separate legend.

## The Logic <!-- role: reason -->

- **The Principle:** Legends impose working-memory load and require repeated eye movements.
- **The Evidence:** The paper highlights that viewers must hold a feature in memory while searching elsewhere, which slows and degrades performance; direct labeling removes those memory-dependent lookups [@zacksDesigningGraphsDecisionMakers2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Identifying categories and comparing them (especially across multiple marks).
- **Data Type:** Multi-category charts using color keys.
- **Audience:** General audiences and time-pressured decision-makers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Severe space constraints with many tiny marks where labels would overlap and become unreadable.
- **Reason:** Illegible labels can be worse than a legend; the rule fails if direct labels cannot be read [@zacksDesigningGraphsDecisionMakers2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** More visual clutter or reduced white space.
- **The Risk:** Overlapping labels can create new reading difficulty.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the legend but moving it “closer,” assuming that solves the problem.
- **Why it fails:** Any separation still requires attention switching and memory, just slightly less [@zacksDesigningGraphsDecisionMakers2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Your eyes bounce repeatedly between the plot and legend to answer simple questions.
- **The Test:** Time yourself answering “Which is larger, A or B?” If you need multiple legend lookups, the design is failing.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Label only the most important categories directly; keep the rest in a legend.
- **Best Fix:** Redesign to enable full direct labeling (fewer categories per view, or a different chart arrangement) [@zacksDesigningGraphsDecisionMakers2020].
