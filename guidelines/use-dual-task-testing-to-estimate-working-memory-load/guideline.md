---
id: use-dual-task-testing-to-estimate-working-memory-load
title: Use a dual-task evaluation to estimate whether a visualization requires working
  memory
bibliography: references.bib
description: Dual-task interference can indicate whether users rely on Type 2 processing
  for a visualization-based decision.
labels:
- chart:general
- task:evaluate
- visual:experiment
- impact:validation
- data:general
- audience:novice
- method:dual-task
---

## Evaluate candidate visualizations with a working-memory secondary task to compare cognitive load <!-- role: advice -->

When choosing between competing visualization designs, test them with a dual-task setup that adds a working-memory-demanding secondary task. Prefer designs that preserve accuracy and speed under the dual-task when the real-world context involves cognitive load.

## Dual-task costs indicate reliance on Type 2 processing <!-- role: reason -->

If a visualization requires significant working memory to interpret, adding a concurrent working-memory task should impair performance (slower responses, more errors). Minimal interference suggests decisions rely more on Type 1 processing and perceptual inference, which is less capacity-limited.

**Mechanism:** Two tasks that both draw on working memory compete for limited resources, revealing which visualization decisions require controlled attention and capacity.

**Evidence:** A dual-process model for visualization decision making predicts that decisions requiring working memory (Type 2) will show interference under secondary-task load, and dual-task paradigms are proposed as a way to diagnose this in visualization use [@padillaDecisionMakingVisualizations2018].

**Notes:** The approach is most informative when the secondary task is clearly working-memory-demanding and the primary decision task is representative.

## When to use dual-task evaluation <!-- role: context -->

- **User Goal:** Select a design that will work under real cognitive constraints.
- **Task:** Compare visualization alternatives for the same decision question.
- **Data:** Any; especially complex comparisons, uncertainty interpretation, or schema-mismatch risks.
- **Chart Setting:** High-stakes or high-workload contexts (emergency, operations, clinical).
- **Audience:** Users with variable working-memory capacity.
- **Success Criterion:** Low interference (stable accuracy/time) under cognitive load.

## Exceptions <!-- role: exceptions -->

**Break it when:** The actual usage context is always low-load and reflective, and the task is intended to be slow and analytical. **Why:** Dual-task stress may be unrepresentative and could penalize acceptable designs.

## Costs <!-- role: costs -->

**Sacrifice:** More complex study design and analysis. **Risk:** A poorly chosen secondary task can measure the wrong resource or introduce confounds. **Mitigation:** Pilot the secondary task to ensure it is demanding and consistently administered.

## Mistakes <!-- role: mistakes -->

- **Mistake:** Using a trivial secondary task that does not tax working memory. **Why it fails:** It will not differentiate Type 1-like from Type 2-like reliance.
- **Mistake:** Comparing designs with different primary-task difficulty. **Why it fails:** Differences may reflect task mismatch rather than cognitive load.

## Check <!-- role: check -->

**Failure Sign:** Performance collapses for one design under load while another remains stable. **Quick Check:** Track response time and accuracy differences between single-task and dual-task conditions. **Stronger Test:** Test both verbal and visuospatial secondary tasks to see which resource the visualization depends on.

## Fix <!-- role: fix -->

- Redesign the visualization to reduce required mental transformations for the primary decision.
- Replace ambiguous encodings that require schema selection with more conventional or directly interpretable encodings.
- Add structure that externalizes computation (explicit comparisons, reference cues) so less must be held in working memory.
- Simplify the display to emphasize the single variable required for the decision under load.
