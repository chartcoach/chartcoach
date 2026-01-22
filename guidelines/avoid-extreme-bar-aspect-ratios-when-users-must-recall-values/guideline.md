---
id: avoid-extreme-bar-aspect-ratios-when-users-must-recall-values
title: Avoid Extreme Bar Aspect Ratios When Users Must Recall Values
bibliography: references.bib
description: Wide bars tend to be remembered as higher and tall bars as lower, biasing
  recalled bar values toward a square-like shape.
labels:
- chart:bar
- task:recall
- visual:position
- impact:accuracy
- data:quantitative
- audience:novice
- cognitive:memory
---

## Prefer near-square bar marks for value recall tasks <!-- role: advice -->

Prefer bar mark aspect ratios closer to a square when viewers will need to remember or reproduce bar heights after a delay or across views. Avoid very wide or very tall bars in these situations.

## Square-prototype memory bias in position recall <!-- role: reason -->

When people encode a bar’s value via the vertical position of its top, they also incidentally encode the bar’s shape. In memory-based reproduction, the remembered position is biased toward a “prototypical” square-like shape, pulling wide bars upward (overestimation) and tall bars downward (underestimation).

**Mechanism:** Memory reconstruction blends the actual position with a category prototype for shape (a square), shifting recalled bar-top position toward the position that would make the mark more square-like.

**Evidence:** In memory-based position reproduction, wide bars were overestimated, tall bars were underestimated, and square bars showed little to no systematic bias across experiments [@cejaTruthSquareAspect2021a]. When the stimulus remained visible during response (tracing), the wide/tall under/over pattern largely disappeared, indicating the bias is mainly rooted in memory rather than direct perception alone [@cejaTruthSquareAspect2021a].

**Notes:** The same directional bias appeared in both single-bar and grouped-bar contexts discussed in the work, helping reconcile prior conflicting findings.

## When memory-based bar value comparisons are likely <!-- role: context -->

- **User Goal:** Remember exact or approximate values from bars and use them later.
- **Task:** Reproduce a bar’s height, compare values across time-separated views, or carry a value from one chart to another.
- **Data:** Quantitative values shown as bar heights.
- **Chart Setting:** Dashboards, small multiples, pagination/scrolling, presentations, or any interaction that hides the original chart before comparison.
- **Audience:** Any audience; risk increases when viewers cannot continuously refer back to the original bar.
- **Success Criterion:** Low bias (not just low random error) in recalled bar-top position.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task is done with continuous on-screen reference to the original bar during judgment (no reliance on memory). **Why:** The square-attraction pattern is largely absent when the original stimulus remains visible during response [@cejaTruthSquareAspect2021a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Constraining aspect ratios can reduce layout flexibility, especially with many categories or tight containers. **Risk:** Forcing near-square marks may increase chart height/width demands or require scrolling. **Mitigation:** Treat this as a priority specifically for cross-view or delayed comparisons, not for every bar chart.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using very wide “strip” bars (or very tall “needle” bars) in situations where viewers must remember values across steps. **Why it fails:** Wide bars bias recalled heights upward and tall bars bias recalled heights downward, distorting remembered values [@cejaTruthSquareAspect2021a].
- **Mistake:** Assuming that because bars encode position (a precise channel), memory for that position will be unbiased. **Why it fails:** Even position encodings can show systematic memory bias driven by incidental mark shape [@cejaTruthSquareAspect2021a].

## Quick tests <!-- role: check -->

**Failure Sign:** Users consistently report higher values for very wide bars and lower values for very tall bars when asked later. **Quick Check:** Identify bars with highly elongated width:height ratios in any view-to-view comparison workflow. **Stronger Test:** Run a short reproduction-from-memory pilot: show a bar briefly, mask it, and ask users to reproduce its top position; look for signed error that flips with aspect ratio [@cejaTruthSquareAspect2021a].

## What to do instead <!-- role: fix -->

- Use bar widths/heights that keep individual marks closer to square when recall across time or views is required.
- Keep the original bar visible during value matching tasks (a tracing-style interaction) so judgments rely less on memory.
- Redesign workflows so comparisons happen within the same view rather than across sequential displays when precise values matter.
- If extreme aspect ratios are unavoidable, add persistent reference aids that reduce the need to remember positions (for example, keep the compared marks simultaneously visible).
