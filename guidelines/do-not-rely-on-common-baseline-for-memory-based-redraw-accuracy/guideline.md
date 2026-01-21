---
id: do-not-rely-on-common-baseline-for-memory-based-redraw-accuracy
title: Do Not Rely on a Common Baseline to Improve Memory-Based Read Accuracy
bibliography: references.bib
description: In redraw-from-memory tasks, aligned baselines did not meaningfully improve
  proportional accuracy compared to non-aligned locations.
labels:
- chart:bar
- task:read-value
- visual:position
- impact:robustness
- data:proportional
- audience:general
- finding:baseline-not-critical
---

## The Rule <!-- role: advice -->

Don’t assume that keeping marks on a shared baseline will protect accuracy when users must remember and reproduce a value across locations.

## The Logic <!-- role: reason -->

When participants reproduced values after a brief delay, accuracy did not meaningfully differ between redraws on a common baseline versus vertical/diagonal redraws. This suggests the classic common-baseline advantage may not transfer to this memory-based reproduction context.

- **The Principle:** Common-baseline benefits may be task-dependent (especially vs. memory reproduction)
- **The Evidence:** Experiments that varied redraw locations found no meaningful accuracy advantage for common-baseline redraws in proportion-corrected error (bars and dots) [@mccolemanNoMarkIsland2021].

## Where to Apply <!-- role: context -->

- **User Goal:** Recall a previously seen value and reproduce/act on it elsewhere (e.g., switching views, panels, or screens).
- **Data Type:** Single-value readings from bars/dots with a short retention interval.
- **Audience:** Users working across dashboards or multi-panel views where values must be remembered.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is an on-screen, simultaneous comparison or explicit ratio judgment rather than a redraw-from-memory.
- **Reason:** The paper’s finding is specific to the method-of-adjustment reproduction paradigm; other tasks may behave differently [@mccolemanNoMarkIsland2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need extra design effort beyond “align everything” to support accurate cross-view use.
- **The Risk:** Over-prioritizing baseline alignment could constrain layout without delivering the expected benefit for memory-based use.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Believing baseline alignment alone solves accuracy problems in multi-view workflows.
- **Why it fails:** The experiments found redraw accuracy was not improved by common-baseline locations in this paradigm [@mccolemanNoMarkIsland2021].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must look at one view, then later use that value in another location (not side-by-side).
- **The Test:** If the workflow includes a delay and a context switch, treat it as memory-based; don’t count on baseline alignment as your main accuracy lever.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the need for memory by keeping the relevant value visible during interaction (e.g., keep the source view present while adjusting in the target view).
- **Best Fix:** Rework the workflow so key values do not require recall-and-reproduce steps (support direct reading at point of use), consistent with the task constraints highlighted by the paper [@mccolemanNoMarkIsland2021].
