---
id: use-interactive-slideshow-for-stepwise-narrative-within-slide-exploration
title: Use an Interactive Slideshow for Stepwise Narrative with Within-Slide Exploration
bibliography: references.bib
description: Present a paced sequence of slides while allowing constrained interaction
  inside each slide.
labels:
- task:explain
- task:explore
- impact:clarity
- custom:structure:interactive-slideshow
- audience:general
---

## The Rule <!-- role: advice -->

Use a slideshow sequence to control narrative order, and limit interaction to single-frame (within-slide) exploration before advancing.

## The Logic <!-- role: reason -->

The paper describes interactive slideshows as a hybrid: you keep discrete narrative segments (like film cuts) while allowing readers to explore each step without leaving the current scene. This supports complex datasets and narratives by controlling cognitive load and preserving orientation.

- **The Principle:** Segment complex explanations into ordered scenes with bounded interaction.
- **The Evidence:** [@segelNarrativeVisualizationTelling2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand a multi-step argument and optionally inspect details at each step.
- **Data Type:** Multi-dimensional or temporally evolving data needing incremental revelation.
- **Audience:** General audiences; learners.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The story is best consumed as a single, simultaneously visible composition (e.g., poster-like overview comparisons).
- **Reason:** Slides can hide global context that a single-frame, multi-panel layout would preserve [@segelNarrativeVisualizationTelling2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** More time to produce consistent slide states and transitions.
- **The Risk:** If navigation is unclear, users may not realize they control pace or may skip necessary context [@segelNarrativeVisualizationTelling2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding interactions that jump to new scenes without strong orientation cues.
- **Why it fails:** It breaks the “single-frame interactivity” benefit and can disorient readers [@segelNarrativeVisualizationTelling2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Users get lost about which slide they’re on or what changed.
- **The Test:** Ensure each slide maintains a consistent platform (layout) and that interaction does not transport users away from the current narrative step [@segelNarrativeVisualizationTelling2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Constrain interactions to hover details and simple within-slide selectors.
- **Best Fix:** Keep layout constant across slides, add progress/navigation controls, and use animated transitions for within-slide updates [@segelNarrativeVisualizationTelling2010].
