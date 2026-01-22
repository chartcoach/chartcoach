---
id: directly-encode-pairwise-deltas-for-relation-perception-tasks
title: Directly Encode Pairwise Deltas When Users Must Judge Increases vs Decreases
bibliography: references.bib
description: When people need to perceive the direction or size of change between
  paired values, showing the delta directly yields markedly better performance than
  showing only the two original values.
labels:
- chart:bar
- chart:dot
- chart:slope
- task:compare
- task:search
- task:aggregate
- visual:length
- visual:position
- visual:orientation
- impact:efficiency
- impact:accuracy
- data:paired
- audience:novice
- audience:expert
- complexity:foundational
---

## Encode change as deltas, not just the two values <!-- role: advice -->

Directly encode the difference (delta) between each pair of values when the user’s goal is to perceive relations such as increases vs. decreases or average change across pairs.

## Why direct delta encoding improves relational judgments <!-- role: reason -->

Relation perception from two separately encoded values requires the viewer to extract a spatial relationship between two marks before they can decide direction or magnitude of change, which is comparatively inefficient. A delta encoding converts the relation into a single, directly readable feature (e.g., a single bar above/below a baseline), reducing the need for pairwise relational extraction.

**Mechanism:** Collapsing a two-mark relationship into one mark makes the relation itself the perceptual object, avoiding slow, attention-demanding extraction of configurations across two marks.

**Evidence:** Across three tasks—visual search for one anomalous relation, judging which relation type is more prevalent, and estimating average delta—performance was consistently better with delta encodings than with individual-value encodings, with improvements ranging from roughly 25% to 95% depending on task and encoding. [@nothelferMeasuresBenefitDirect2020a]

**Notes:** The size of the delta advantage depends strongly on the task: it was largest for finding a specific target relation and smaller (but still meaningful) for ensemble summary tasks.

## When this applies to paired-value visualizations <!-- role: context -->

- **User Goal:** Detect, compare, or summarize changes between paired values (before/after, A vs. B, this year vs. last year).
- **Task:** Find a specific increase/decrease; decide whether increases or decreases dominate; estimate the average change magnitude.
- **Data:** Naturally paired observations (two values per entity/category) where the relation is the primary analytic object.
- **Chart Setting:** Static displays and dashboards where users must visually forage across many pairs.
- **Audience:** Any audience; especially when speed/efficiency matters (quick scanning, oversight, monitoring).
- **Success Criterion:** Faster search, higher accuracy for direction judgments, and lower error in average-change estimation.

## When not to rely on delta-only encodings <!-- role: exceptions -->

**Break it when:** The user must use the original absolute values as primary evidence (not just the differences). **Why:** Delta-only displays remove value context and can hide insights tied to individual values.

## Tradeoffs of adding or switching to deltas <!-- role: costs -->

**Sacrifice:** Space and layout simplicity, especially if you need to show both original values and deltas.\
**Risk:** Users may lose context about baseline levels when only deltas are shown.\
**Mitigation:** Preserve access to original values elsewhere in the display when those values are needed for interpretation.

## Common ways delta encodings fail in practice <!-- role: mistakes -->

**Mistake:** Showing only the two individual values and expecting users to efficiently spot increases/decreases across many pairs. **Why it fails:** Relational extraction across two marks scales poorly as the number of pairs grows.\
**Mistake:** Treating delta encoding as a universally “small” improvement. **Why it fails:** The benefit varies substantially by task, and can be very large for target-finding tasks.

## Quick checks that your design needs deltas <!-- role: check -->

**Failure Sign:** Users take noticeably longer as the number of pairs increases, or they miss whether most pairs increase or decrease.\
**Quick Check:** Ask a colleague to find one decreasing pair among many increasing pairs (or vice versa) using the current design.\
**Stronger Test:** Run a small timed pilot comparing your current encoding to a delta encoding on the same tasks (find-one, majority-direction, average-change).

## What to do instead if delta-only is not acceptable <!-- role: fix -->

- Add an explicit delta layer or a separate delta view when relations are the main decision variable.
- Provide interactions (e.g., reveal-on-demand) that expose deltas without permanently removing the base values.
- Reduce the number of pairwise comparisons shown at once if you cannot encode deltas and users must still compare relations.
- Split workflows: use an overview delta display for relation scanning, then a value display for contextual drill-down.
