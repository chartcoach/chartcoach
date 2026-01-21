---
id: make-interactions-forgivable-with-undo-redo
title: Make Interactions Forgivable With Undo/Redo
bibliography: references.bib
description: Ensure users can undo or redo actions in interactive visualizations to
  recover from mistakes.
labels:
- chart:interactive
- task:explore
- task:filter
- task:select
- task:navigate
- visual:interaction
- impact:accessibility
- impact:robustness
- impact:usability
- principle:compromising
- source:chartability
---

## The Rule <!-- role: advice -->

Provide a clear way to undo and redo user actions for any interactive operation in a visualization.

## The Logic <!-- role: reason -->

Forgiving interactions reduce the consequences of inevitable human error by allowing recovery after a mistaken action, rather than forcing users to restart or accept an unintended state. This supports error-tolerant interaction design (including undo/redo and recovery paths) in interactive systems [@baber_task_analysis_1994], and is included as an auditing heuristic for visualization accessibility in Chartability [@elavskyHowAccessibleMy2022].

- **The Principle:** Error-tolerant, recoverable interaction
- **The Evidence:** [@baber_task_analysis_1994]

## Where to Apply <!-- role: context -->

This advice is designed for interactive visualization states where users can change what they see or do.

- **User Goal:** Exploring, operating, or completing tasks without being trapped by mistakes (e.g., refining views via interaction)
- **Data Type:** Any data shown through interactions that modify state (e.g., filtered subsets, selections, navigation states)
- **Audience:** Especially users who rely on assistive technologies or have disabilities and may experience higher interaction effort or error risk in complex data experiences [@elavskyHowAccessibleMy2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization has no interactions or operations that change state.
- **Reason:** There is nothing to undo/redo if no user action changes the system state [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional design and engineering effort to track user actions and state changes.
- **The Risk:** Poorly implemented undo/redo can confuse users if state changes are not transparent or consistent [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating error prevention guidance as only relevant to data-entry fields and ignoring interaction errors in visualizations.
- **Why it fails:** Interaction errors in data experiences can be complex and still require recovery mechanisms; limiting scope to form fields leaves users without a way to recover from mistaken interactive actions [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** After a mistaken interaction (e.g., unintended filter/selection/navigation), the user cannot return to the previous state or re-apply a reverted state.
- **The Test:** Perform common interactions and intentionally make a mistake; verify you can undo the change and redo it to restore the modified state [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a single, obvious “Undo” control that restores the immediate previous visualization state.
- **Best Fix:** Implement full undo/redo across interactive operations so users can step backward and forward through meaningful state changes in the visualization [@baber_task_analysis_1994; @elavskyHowAccessibleMy2022].
