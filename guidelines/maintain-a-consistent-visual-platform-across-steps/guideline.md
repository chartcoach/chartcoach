---
id: maintain-a-consistent-visual-platform-across-steps
title: Maintain a Consistent Visual Platform Across Steps
bibliography: references.bib
description: Keep layout stable across slides/tabs so viewers stay oriented while
  content changes.
labels:
- task:orient
- impact:clarity
- custom:visual-structuring
- custom:transition-guidance
- audience:general
---

## The Rule <!-- role: advice -->

Keep the overall layout and interface scaffolding constant across narrative steps; change content within that stable frame.

## The Logic <!-- role: reason -->

The paper notes that consistent visual platforms help preserve orientation during transitions (e.g., across slides or tabs), making it easier to follow the narrative and notice what changed rather than re-learn the interface.

- **The Principle:** Stable frames reduce reorientation costs during transitions.
- **The Evidence:** [@segelNarrativeVisualizationTelling2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Track changes across time/steps or compare successive narrative points.
- **Data Type:** Multi-step explanations, especially interactive slideshows and tabbed narratives.
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally need to signal a major story break (a new chapter) with a distinct scene.
- **Reason:** A strong scene change can be a deliberate narrative boundary, but should be treated as such [@segelNarrativeVisualizationTelling2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less flexibility in per-step layout optimization.
- **The Risk:** For very different chart types, forcing the same layout can feel awkward unless transitions are carefully guided [@segelNarrativeVisualizationTelling2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Re-layouting controls and legends each step.
- **Why it fails:** It increases cognitive load and can cause viewers to miss the narrative point of the change [@segelNarrativeVisualizationTelling2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers spend time searching for where controls/legends moved rather than reading the data change.
- **The Test:** Flip quickly between steps; if major UI elements jump position, platform consistency is broken [@segelNarrativeVisualizationTelling2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Lock persistent elements (titles, axes regions, legends, nav) to fixed positions.
- **Best Fix:** Design a reusable template grid for all steps and constrain each step’s content to that template [@segelNarrativeVisualizationTelling2010].
