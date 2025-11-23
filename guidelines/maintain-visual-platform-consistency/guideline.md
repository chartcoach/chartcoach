---
id: maintain-visual-platform-consistency
title: Maintain a Consistent Visual Platform
bibliography: references.bib
description: Keep the layout and primary visual elements meaningful and constant while
  changing the data content to prevent disorientation.
labels:
- chart:multiview
- task:compare
- visual:layout
- impact:clarity
- data:temporal
---

## The Rule <!-- role: advice -->
Keep the general layout, axes, and visual encoding consistent as the user moves through different narrative beats. Only change the content within the frame, not the frame itself.

## The Logic <!-- role: reason -->
Drastic changes in layout require the user to re-orient themselves, breaking the narrative flow.
*   **The Principle:** Change Blindness / Orientation. Preserving the "visual platform" allows the user to focus on the data changes rather than processing a new interface.
*   **The Evidence:** [@segel_narrative_2010] praise the "Budget Forecasts" (Section 3.2) and "Afghanistan" (Section 3.3) examples for maintaining a "consistent visual platform," where transitions update the chart without altering the general layout of visual elements.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing data across time, categories, or scenarios (e.g., switching from "Security" to "Nation Building" tabs).
*   **Data Type:** Multi-dimensional data presented in steps or tabs.
*   **Audience:** Any audience, as re-orientation requires cognitive effort for everyone.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** "Scene-to-Scene" Transitions.
*   **Reason:** If the narrative explicitly moves to a completely different topic or location where the previous visual metaphor no longer applies (e.g., moving from a map to a scatter plot), the layout must change.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Novelty. You cannot use a fresh, flashy chart type for every slide.
*   **The Risk:** Boredom. If the visuals are too repetitive, the user might not notice that the data has actually changed.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Changing color encodings between views.
*   **Why it fails:** The paper notes that the Afghanistan example uses a "semantically consistent color encoding" (Section 3.3). Changing what "red" means on the next slide destroys consistency.
*   **The Wrong Fix:** Radical "Camera" Jumps.
*   **Why it fails:** Moving the viewer's perspective arbitrarily confuses spatial relationships (Section 4.1, Transition Guidance).

## How to Check <!-- role: check -->
*   **Visual Sign:** Flip between two slides or tabs rapidly.
*   **The Test:** Do the axes jump? Does the legend move? If the "container" elements wobble or shift, you have broken consistency.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Lock the axis scales across all slides, even if some slides have smaller data ranges.
*   **Best Fix:** Design a master template (wireframe) that accommodates the densest data view, and use that template for every single state of the narrative.
