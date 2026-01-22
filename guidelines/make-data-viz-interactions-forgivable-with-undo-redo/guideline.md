---
id: make-data-viz-interactions-forgivable-with-undo-redo
title: Provide undo and redo for all visualization interactions that change state
bibliography: references.bib
description: "Make interactive visualizations error-tolerant by ensuring users can\
  \ undo or redo any action that changes the visualization\u2019s state."
labels:
- chart:interactive
- task:explore
- visual:interaction
- impact:accessibility
- data:any
- audience:all
- principle:compromising
- a11y:forgiveness
---

## Forgivable interaction with undo/redo for state changes <!-- role: advice -->

Provide undo and redo for every interaction that changes the visualization’s state. If undo/redo is not feasible for a specific operation, provide an explicit recovery path that returns the user to a known safe state.

## Error-tolerant interaction reduces the cost of mistakes <!-- role: reason -->

Forgivable interactions reduce the consequence of inevitable slips during exploration and operation. When users can recover, they can try actions, learn the interface, and continue without losing progress or becoming stuck in a broken state.

**Mechanism:** Undo/redo turns an interaction error from a failure into a reversible detour, reducing the time, effort, and cognitive load needed to recover while keeping the user oriented in the interaction flow.

**Evidence:** Error-tolerant interactive systems improve recoverability by explicitly supporting undo/redo and other recovery mechanisms as part of designing for user mistakes [@baber_task_analysis_1994]. Visualization accessibility auditing heuristics include “Interactions are not forgivable” as a barrier and require that interactive visualization operations be undoable/redoable to support tolerant information flows [@elavskyHowAccessibleMy2022].

**Notes:** This applies to interaction errors in data experiences, which can be broader than form-style “data entry” errors.

## Where undo/redo is required in visualization experiences <!-- role: context -->

- **User Goal:** Explore, filter, compare, or inspect data without fear of losing context or breaking the view.
- **Task:** Interactive analysis tasks such as filtering, selecting, drilling down, sorting, re-encoding, zooming/panning, or changing parameters.
- **Data:** Any dataset where interactions can change the visible subset, aggregation, or configuration of the view.
- **Chart Setting:** Interactive charts or dashboards with stateful controls (e.g., filters, selections, view toggles) and multi-step interaction sequences.
- **Audience:** People with diverse access needs, including users of assistive technologies and users who benefit from error-tolerant workflows.
- **Success Criterion:** Users can return to a prior valid state after any action, without needing to reload, restart, or reconstruct their work.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization has no state-changing interactions (purely static viewing with no operations beyond passive reading). **Why:** There is no interaction state to revert, so undo/redo would add non-functional controls.

## Tradeoffs and risks of adding undo/redo <!-- role: costs -->

**Sacrifice:** Additional interface complexity and engineering effort to track state transitions. **Risk:** Poorly designed history can confuse users if the undone/redone state is unclear. **Mitigation:** Favor a small, consistent, clearly described interaction history over many hidden state changes.

## Common ways teams fail to make interactions forgivable <!-- role: mistakes -->

- **Mistake:** Provide only a “Reset” that clears all changes and cannot step backward. **Why it fails:** Users cannot recover from a single mistake without losing all progress and context.
- **Mistake:** Allow state-changing interactions (e.g., filter, select, drill) but offer no way to reverse them except reloading the page. **Why it fails:** Recovery becomes costly and can strand users who cannot easily reconstruct the previous state.
- **Mistake:** Record state changes but hide the recovery controls or make them inconsistent across interaction types. **Why it fails:** Users cannot reliably predict how to recover, defeating the purpose of tolerance.

## Quick tests for forgivable interactions <!-- role: check -->

**Failure Sign:** After a wrong click/keypress, the view changes and there is no clear way to revert to the immediately prior state. **Quick Check:** Perform a state-changing action (filter, select, drill, reconfigure) and verify there is an undo control that restores the previous state and a redo control that re-applies it. **Stronger Test:** Execute a three-step interaction sequence, undo step-by-step back to the start, then redo step-by-step to the end, confirming the view and state match at each step.

## How to make interaction state recoverable <!-- role: fix -->

- Implement an explicit undo and redo control that operates on the same state changes triggered by chart interactions.
- Capture state transitions for all state-changing interactions (including compound interactions) so recovery can step backward and forward predictably.
- Provide a clear “return to known safe state” action when an operation cannot be represented in undo/redo history, and ensure it does not require restarting the experience.
- Reduce or eliminate irreversible interactions by redesigning the workflow so exploratory actions do not commit permanent state changes.
