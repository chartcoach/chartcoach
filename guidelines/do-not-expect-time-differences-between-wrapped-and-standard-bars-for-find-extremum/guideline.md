---
id: do-not-expect-time-differences-between-wrapped-and-standard-bars-for-find-extremum
title: Do Not Assume Wrapped Bars Change Time for Find-Extremum
bibliography: references.bib
description: In the extracted results, wrapped and standard bar charts show no significant
  time differences for find-extremum tasks.
labels:
- chart:bar
- task:find-extremum
- impact:time
- data:categorical
- audience:general
- variant:wrapped-bar
- evidence:experiment
- source:zengReviewCollationGraphical2023
---

## The Rule <!-- role: advice -->

Choose wrapped vs. standard bar charts for find-extremum based on accuracy needs, not on expected time savings.

## The Logic <!-- role: reason -->

The extracted timing results show tied rankings (no separation) between wrapped and standard bar charts, and no significant pairwise differences reported for time in the recorded tasks.

- **The Principle:** Optimize for the metric that actually changes
- **The Evidence:** For find-extremum time (find-extremum-1), standard and wrapped are ranked as equivalent (E-1, E-2 grouped), with no significant pairs. For find-extremum time (find-extremum-2), standard variants (E-3–E-6) and wrapped variants (E-7–E-10) form grouped ranks with no reported significant pairs. This is captured in the collated perception-knowledge representation intended for recommendation systems [@zengReviewCollationGraphical2023] based on the underlying experiment [@karduniBoisWrappedBar2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly find extrema, where you are deciding between wrapped and standard bar variants
- **Data Type:** Categorical bar charts with quantitative values; includes the entropy-binned scenarios represented in the extracted record
- **Audience:** General audiences where completion time is a concern but accuracy is also important

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your implementation of wrapped bars differs substantially (e.g., interaction, labeling, or other changes not represented in the extracted designs).
- **Reason:** The timing equivalence is specific to the studied conditions captured in the structured record; different implementations may change time costs [@karduniBoisWrappedBar2020; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may still incur extra interpretation effort for wrapped bars even if total completion time does not measurably increase.
- **The Risk:** Over-indexing on time can cause you to miss accuracy benefits that the evidence indicates.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Avoiding wrapped bars because you assume they will necessarily slow users down.
- **Why it fails:** The extracted evidence does not show significant time penalties for find-extremum tasks in these conditions, while it does show accuracy advantages elsewhere in the same record [@karduniBoisWrappedBar2020; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Stakeholders object to wrapped bars on the grounds of “it will take longer.”
- **The Test:** Run a quick timed A/B on representative find-extremum questions; verify whether time meaningfully differs in your context.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reframe the choice: treat wrapped bars as an accuracy-driven variant, not a speed optimization.
- **Best Fix:** In recommendation logic, do not assign a time-based penalty or bonus to wrapped vs. standard bars for find-extremum solely based on this evidence; instead, weight accuracy where the record supports it [@zengReviewCollationGraphical2023; @karduniBoisWrappedBar2020].
