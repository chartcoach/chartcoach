---
id: report-target-present-and-absent-slopes-together
title: Report Target-Present and Target-Absent Slopes Together
bibliography: references.bib
description: "Always analyze both target-present and target-absent RT\xD7set-size\
  \ slopes rather than relying on only one."
labels:
- chart:scatter
- task:compare
- visual:position
- impact:validity
- data:experimental
- audience:expert
- domain:visual-search
---

## The Rule <!-- role: advice -->

Always compute and report both target-present and target-absent RT×set-size slopes for a visual search task.

## The Logic <!-- role: reason -->

Target-present and target-absent slopes are strongly positively correlated, but they are not interchangeable; their relationship includes a positive intercept and task-dependent ratio structure. Ignoring one condition loses key information about quitting/termination behavior and task differences.

- **The Principle:** Two-condition measurement reveals termination/decision structure not visible in a single slope.
- **The Evidence:** The paper shows strong correlation (high r²) but also systematic deviations from a simple 2:1 account and task-dependent slope ratios [@wolfeWhatCan11998].

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding search behavior and termination on target-absent trials.
- **Data Type:** Standard visual search with 50% target-present/absent and multiple set sizes.
- **Audience:** Researchers modeling or interpreting visual search performance.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your study design does not include target-absent trials.
- **Reason:** The measure cannot be computed; you must then avoid claims about absent-trial termination behavior [@wolfeWhatCan11998].

## The Price <!-- role: costs -->

- **The Sacrifice:** More data collection/analysis and more results to present.
- **The Risk:** If target-present slopes approach zero, ratios and comparisons can become unstable, requiring careful handling.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reporting only target-present slopes as “efficiency.”
- **Why it fails:** Tasks with similar target-present slopes can differ meaningfully in target-absent behavior (termination), which is lost if absent slopes are omitted [@wolfeWhatCan11998].

## How to Check <!-- role: check -->

- **Visual Sign:** Only one RT×set-size line or only one slope reported for a task.
- **The Test:** Verify that both present and absent slopes (or functions) are included and discussed.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a table row/figure panel with target-absent slopes.
- **Best Fix:** Plot present vs absent slopes (scatter) and report their relationship alongside ratios to capture systematic structure [@wolfeWhatCan11998].
