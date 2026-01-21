---
id: avoid-aspect-ratio-changes-when-users-must-recall-bar-values
title: Keep Bar Aspect Ratios Consistent When Users Must Recall Values
bibliography: references.bib
description: Changing bar mark aspect ratios can systematically bias recalled bar
  heights, distorting across-time comparisons.
labels:
- chart:bar
- task:recall
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- risk:memory-bias
---

## The Rule <!-- role: advice -->

Keep bar mark aspect ratios consistent across views when users will compare values from memory (e.g., across tabs, pages, time, or separate charts).

## The Logic <!-- role: reason -->

Aspect ratio is an *incidental* property of bars that biases memory for the intended encoding (vertical position). People recall bar positions as being pulled toward a “square” prototype: wide bars are remembered as taller (overestimated), tall bars as shorter (underestimated). This bias appears in memory-based reproduction tasks, and largely disappears when the target is simultaneously visible.

- **The Principle:** Categorical prototype bias in memory for position (attraction toward a square)
- **The Evidence:** [@cejaTruthSquareAspect2021a]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare or audit values across time/space (dashboards, small multiples across pages, before/after states, step-through narratives)
- **Data Type:** Quantitative values encoded by bar-top position
- **Audience:** Anyone relying on short-term memory rather than direct side-by-side viewing

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users only compare values within a single, simultaneously visible chart (no memory gap).
- **Reason:** The paper’s strongest bias pattern is shown for memory-based recall; concurrent “tracing” reduces/reverses the pattern. [@cejaTruthSquareAspect2021a]

## The Price <!-- role: costs -->

- **The Sacrifice:** Less flexibility to resize bars or adapt layouts responsively.
- **The Risk:** Forcing uniform aspect ratios may require more whitespace or fewer panels.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming “position is precise so it’s safe” and freely changing mark widths/heights across views.
- **Why it fails:** Precision of position does not prevent systematic memory bias introduced by mark shape. [@cejaTruthSquareAspect2021a]

## How to Check <!-- role: check -->

- **Visual Sign:** The same category/value is shown with noticeably different bar “shapes” (very wide in one view, very tall in another).
- **The Test:** Flip rapidly between the two views; if the mark’s aspect ratio changes, you are creating conditions for biased recall. [@cejaTruthSquareAspect2021a]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Lock bar widths (and overall chart geometry) across views so a given value range yields similar aspect ratios.
- **Best Fix:** Redesign the workflow so key comparisons are side-by-side (minimize reliance on memory for bar positions). [@cejaTruthSquareAspect2021a]
