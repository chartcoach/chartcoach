---
id: avoid-obscure-graph-formats-for-general-audiences
title: Prefer Familiar Chart Formats Over Obscure Ones
bibliography: references.bib
description: "Use graph types that match viewers\u2019 learned schemas to reduce misinterpretation."
labels:
- chart:any
- task:interpret
- visual:schema
- impact:clarity
- data:any
- audience:novice
- complexity:basic
---

## The Rule <!-- role: advice -->

Prefer conventional, widely learned chart formats; avoid obscure formats unless you can train the audience and verify comprehension.

## The Logic <!-- role: reason -->

- **The Principle:** Comprehension depends on learned schemas for mapping visual features to meaning and on learned attention routines for reading axes and marks.
- **The Evidence:** The paper explains that viewers bring strong prior knowledge about graph formats, and that understanding requires those schemas; unfamiliar or unconventional mappings raise errors [@zacksDesigningGraphsDecisionMakers2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Fast, correct interpretation without instruction.
- **Data Type:** Any, especially high-stakes policy/decision communication.
- **Audience:** Broad public, mixed-expertise stakeholders.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Specialist audiences with shared expertise in a domain-specific visualization.
- **Reason:** Experts may have the relevant schema already, reducing the penalty of novelty [@zacksDesigningGraphsDecisionMakers2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some novelty or compactness that a bespoke format might offer.
- **The Risk:** Over-reliance on standard forms might limit expressing an unusual structure.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Introducing a new visual form without teaching what the encodings mean.
- **Why it fails:** Viewers will substitute the closest familiar schema and draw unintended conclusions [@zacksDesigningGraphsDecisionMakers2020].

## How to Check <!-- role: check -->

- **Visual Sign:** People ask “What am I looking at?” before they can answer any data question.
- **The Test:** Give the chart without explanation; if viewers cannot correctly identify what the axes/encodings represent, the format is too obscure.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add clear annotation explaining how to read the chart (near the relevant elements).
- **Best Fix:** Convert to a familiar chart type that uses well-learned mappings for the key variables [@zacksDesigningGraphsDecisionMakers2020].
