---
id: use-slope-ratio-as-a-diagnostic-not-just-slope
title: Use Target-Absent/Target-Present Slope Ratio as a Diagnostic
bibliography: references.bib
description: Complement slopes with the target-absent to target-present slope ratio
  to better characterize search behavior.
labels:
- chart:scatter
- task:diagnose
- visual:position
- impact:validity
- data:experimental
- audience:expert
- domain:visual-search
---

## The Rule <!-- role: advice -->

When characterizing a search task, compute the target-absent/target-present slope ratio and interpret it alongside the slopes.

## The Logic <!-- role: reason -->

Slope magnitude alone cannot reliably indicate task class because distributions overlap. The slope ratio adds information about termination behavior on target-absent trials and varies systematically with task type and efficiency.

- **The Principle:** Multi-metric diagnostics separate behaviors that look similar on a single metric.
- **The Evidence:** The paper finds mean slope ratios > 2.0 overall and shows systematic differences in ratios across task categories even when target-present slopes are similar [@wolfeWhatCan11998].

## Where to Apply <!-- role: context -->

- **User Goal:** Differentiating task types or testing whether a proposed feature behaves like established features.
- **Data Type:** RT×set-size functions for both present and absent trials.
- **Audience:** Researchers evaluating mechanisms or comparing tasks.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Target-present slope is near zero (or < ~1 ms/item) making ratios unstable.
- **Reason:** The paper notes denominator-near-zero instability and uses exclusions to stabilize ratio analysis [@wolfeWhatCan11998].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional computation and potential need for transforms or exclusions.
- **The Risk:** Ratios can be misleading if computed naively when present slopes are very small or negative.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating a 2:1 ratio as the universal benchmark of “serial self-terminating” search.
- **Why it fails:** Average ratios are systematically > 2.0 and differ by task type and efficiency, so 2.0 is not a general fit to observed behavior [@wolfeWhatCan11998].

## How to Check <!-- role: check -->

- **Visual Sign:** Claims of mechanism based only on slope magnitude, with no absent/present comparison.
- **The Test:** Compute the ratio distribution (or log ratio) and see whether it aligns with the task’s expected pattern.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add ratio values (and note instability when present slopes are very small).
- **Best Fix:** Use ratio patterns by task type/efficiency as a diagnostic benchmark rather than assuming a fixed theoretical 2.0 ratio [@wolfeWhatCan11998].
