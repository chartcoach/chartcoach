---
id: show-progress-and-enable-navigation-with-progress-bars-or-timebars
title: Show Progress and Enable Navigation with Progress Bars or Timebars
bibliography: references.bib
description: Use progress indicators to orient users and let them control pacing in
  multi-step narratives.
labels:
- task:navigate
- impact:clarity
- data:temporal
- custom:visual-structuring
- audience:general
---

## The Rule <!-- role: advice -->

In multi-step narratives, include a progress bar/timebar that both indicates position and supports navigation.

## The Logic <!-- role: reason -->

The paper identifies progress bars and timebars as structuring devices that help users track their place, set expectations about length, and control pacing—especially in interactive slideshows.

- **The Principle:** Visible structure and position cues reduce disorientation and support user-controlled pacing.
- **The Evidence:** [@segelNarrativeVisualizationTelling2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Move through a narrative sequence at their own pace; revisit prior steps.
- **Data Type:** Sequenced frames (slides) and time-based narratives.
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Single-frame narratives (e.g., a single annotated chart).
- **Reason:** Progress UI can add clutter without meaningful navigation benefit [@segelNarrativeVisualizationTelling2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Screen real estate and design complexity.
- **The Risk:** Users may skip critical context if navigation makes jumping too easy without cues [@segelNarrativeVisualizationTelling2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing steps without indicating how many exist or where the user is.
- **Why it fails:** Readers can’t form a mental model of the narrative structure and may abandon early [@segelNarrativeVisualizationTelling2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Users ask “How much is left?” or “Where am I?”
- **The Test:** Remove explanatory text; if users can’t infer position/length from the UI, add/strengthen progress indicators [@segelNarrativeVisualizationTelling2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a simple segmented progress bar reflecting steps/sections.
- **Best Fix:** Bind progress to navigation (clickable steps) and keep it persistent across scenes [@segelNarrativeVisualizationTelling2010].
