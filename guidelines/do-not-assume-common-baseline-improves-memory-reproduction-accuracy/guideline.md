---
id: do-not-assume-common-baseline-improves-memory-reproduction-accuracy
title: Do not assume a common baseline improves accuracy for memory-based reproduction
  of bars or dots
bibliography: references.bib
description: When people redraw a previously seen bar or dot, reproduction error was
  similar whether the redraw used a common baseline or not.
labels:
- chart:bar
- chart:dot
- task:estimate
- task:read-value
- visual:position
- visual:length
- impact:accuracy
- data:proportional
- audience:general
- topic:baseline
---

## Treat common-baseline alignment as optional for redraw-from-memory tasks <!-- role: advice -->

Do not rely on keeping a common baseline to improve accuracy when users must redraw or recall a bar height or dot position from memory. If you need better performance, use other supports beyond baseline alignment.

## Baseline advantages may not generalize to memory reproduction <!-- role: reason -->

A common baseline is often discussed as improving precision for certain graphical judgment tasks, but the reproduction paradigm isolates recall and adjustment of a single mark. In that setting, baseline alignment did not materially change proportional error, suggesting that memory and adjustment noise can dominate any baseline benefit.

**Mechanism:** When the task is to reproduce a single magnitude after it disappears, the limiting factor can be memory/adjustment rather than simultaneous perceptual comparison on a shared scale.

**Evidence:** Across experiments where participants redrew bars or dots in locations that were horizontally aligned (common baseline) versus vertically/diagonally displaced (non-common baseline), proportional error did not differ reliably by redraw location. [@mccolemanNoMarkIsland2021]

**Notes:** This applies to redraw-from-memory tasks; it does not claim that baseline alignment is irrelevant for all visualization tasks.

## When baseline alignment is not the lever you think it is <!-- role: context -->

- **User Goal:** Accurately recreate or carry forward a single value after a brief glance.
- **Task:** Recall-and-adjust (redraw) a mark to match a previously seen one.
- **Data:** Single values on a bounded numeric scale.
- **Chart Setting:** Workflows with view switching or transient marks.
- **Audience:** General audiences performing quick, memory-reliant operations.
- **Success Criterion:** Lower proportional error in reproduced values.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The user’s task is simultaneous visual comparison of two visible marks. **Why:** The evidence is from single-mark reproduction after the stimulus disappears, not from side-by-side comparison tasks.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Allowing non-aligned placements can reduce perceived tidiness or standardization. **Risk:** Misreading this as permission to ignore alignment in tasks that are actually comparative. **Mitigation:** Match the layout decision to whether the task is recall-based or comparison-based.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Spending layout budget to preserve a common baseline in a workflow where the value will be remembered and entered later. **Why it fails:** Baseline alignment did not measurably reduce proportional reproduction error in the tested recall-and-adjust tasks.

## Quick tests <!-- role: check -->

**Failure Sign:** Users still show similar variability after you “fix” alignment. **Quick Check:** If users must switch panels/pages before using a value, treat baseline alignment as low impact. **Stronger Test:** Compare a common-baseline vs non-common-baseline prototype using a redraw-from-memory task and evaluate proportional error distributions.

## What to do instead <!-- role: fix -->

- Keep a persistent reference of the original value while users respond, rather than requiring recall.
- Add explicit contextual anchors (while checking for midpoint repulsion effects when anchors imply a 50% boundary).
- Provide numeric readouts to reduce reliance on perceptual memory.
- Reduce the time or steps between viewing a value and acting on it.
