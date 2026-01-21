---
id: prompt-and-mark-interactive-elements-explicitly
title: Prompt and Mark Interactive Elements Explicitly
bibliography: references.bib
description: Make interactive affordances visible and unambiguous, especially in dense
  displays.
labels:
- task:interact
- impact:usability
- custom:interactivity
- audience:general
---

## The Rule <!-- role: advice -->

Clearly mark interactive elements with visible affordances and short prompts that indicate what can be done.

## The Logic <!-- role: reason -->

The paper’s case study of a tabbed map notes the value of explicitly adorned markers of interactivity (messages and pointers indicating lists are clickable). Without clear signaling, readers may not discover available actions, undermining narrative goals.

- **The Principle:** Discoverable affordances are necessary for interaction to support narrative.
- **The Evidence:** [@segelNarrativeVisualizationTelling2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Use interaction to reveal details, highlight subsets, or navigate sections.
- **Data Type:** Dense views where interactive targets are not self-evident (maps, lists, multi-panel graphics).
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** An experience designed to be non-interactive (purely author-driven).
- **Reason:** Affordance cues would be misleading and distract from linear storytelling [@segelNarrativeVisualizationTelling2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some visual clutter from cues/prompts.
- **The Risk:** Too many prompts can feel patronizing or noisy [@segelNarrativeVisualizationTelling2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Hiding interaction behind unlabeled UI elements or expecting “hover to discover” without indication.
- **Why it fails:** Users may never engage the interaction, losing both story and exploration value [@segelNarrativeVisualizationTelling2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Interactive features go unused in testing.
- **The Test:** Ask a viewer “What can you interact with?”; if they can’t name key controls, cues are insufficient [@segelNarrativeVisualizationTelling2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a short inline prompt (“Click a country to highlight provinces”).
- **Best Fix:** Combine explicit marking with a tacit tutorial that demonstrates the interaction effect [@segelNarrativeVisualizationTelling2010].
