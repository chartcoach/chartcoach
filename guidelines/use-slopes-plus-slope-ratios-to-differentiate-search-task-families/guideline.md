---
id: use-slopes-plus-slope-ratios-to-differentiate-search-task-families
title: Use slope plus slope-ratio patterns to differentiate search task families (not
  slope alone)
bibliography: references.bib
description: Task classes differ not only in mean slopes but also in target-absent/target-present
  slope ratios at matched efficiency.
labels:
- chart:scatter
- task:compare
- visual:position
- impact:interpretability
- data:quantitative
- audience:expert
- domain:psychophysics
- metric:multimetric-diagnostic
---

## Combine slope magnitude with slope ratios when diagnosing task type <!-- role: advice -->

When trying to distinguish visual search task families (e.g., feature vs conjunction vs spatial-configuration), use a joint diagnostic that includes both target-present slope and the target-absent/target-present slope ratio. Do not treat “similar target-present slopes” as evidence that tasks are equivalent in how search terminates.

## Matched efficiency can hide systematic task differences <!-- role: reason -->

If different task families produce different target-absent behavior even when target-present slopes are matched, then “efficiency” is not fully captured by target-present slope alone. The slope ratio reflects how readily observers stop on target-absent trials, which varies by task type and therefore provides additional discriminatory information beyond slope magnitude.

**Mechanism:** Target-present slopes index how quickly targets are found when present, while slope ratios index stopping behavior and decision criteria when targets are absent; these components can vary independently across task structures.

**Evidence:** Feature, conjunction, and spatial-configuration searches differed significantly in mean slopes, yet their slope distributions overlapped so slope alone could not reliably identify task type [@wolfeWhatCan11998]. Even after excluding unstable near-zero cases, feature searches showed substantially lower mean slope ratios than conjunction and spatial-configuration searches, and conjunction and spatial-configuration searches could also differ in ratio within an asymptotic slope range, demonstrating task-specific termination patterns at similar target-present slopes [@wolfeWhatCan11998].

**Notes:** This supports diagnostics that treat slope and ratio jointly as a pattern rather than searching for a single “magic number.”

## When you need to classify or compare search tasks from RT × set size results <!-- role: context -->

- **User Goal:** Decide whether a task behaves more like feature, conjunction, or spatial-configuration search using performance metrics.
- **Task:** Compare tasks with similar target-present slopes; assess differences in target-absent behavior.
- **Data:** Condition-level slopes for target-present and target-absent trials; slope ratios computed per session/condition.
- **Chart Setting:** Overlaid distributions of slopes by task class; slope ratio vs target-present slope plot.
- **Audience:** Researchers building or testing models; reviewers assessing claims about “feature-like” behavior.
- **Success Criterion:** Identify task-family signatures without relying on a single slope threshold.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** Target-absent trials are not collected or are too sparse to estimate a reliable target-absent slope. **Why:** The ratio diagnostic cannot be computed, so it cannot add information beyond target-present performance.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Comparisons require more statistics and careful handling of ratio instability. **Risk:** Ratios can appear inflated when target-present slopes are very small. **Mitigation:** Apply explicit rules for excluding or separately summarizing near-zero target-present slopes.

## Mistakes: Common failure modes <!-- role: mistakes -->

- **Mistake:** Declaring two tasks “the same” because they have similar target-present slopes. **Why it fails:** Tasks with matched target-present slopes can have systematically different slope ratios, reflecting different termination behavior on target-absent trials [@wolfeWhatCan11998].
- **Mistake:** Using only mean slopes to “diagnose” whether something is feature-like. **Why it fails:** Slope distributions overlap across task classes, so slope alone is not diagnostic [@wolfeWhatCan11998].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Two conditions match on target-present slope but show visibly different target-absent increases with set size. **Quick Check:** Plot slope ratio against target-present slope, stratified by task type, and look for systematic separation. **Stronger Test:** Compare mean log(slope ratio) across task classes within a restricted target-present slope band.

## Fix: What to do instead <!-- role: fix -->

- Report target-present slope and target-absent slope together, not in separate sections, so the joint pattern is visible.
- Add a slope-ratio summary (preferably with a log-ratio check) alongside slope summaries when comparing task families.
- Compare tasks within matched target-present slope ranges before concluding that termination behavior is equivalent.
- Treat “feature-like” claims as requiring both shallow slopes and appropriately low slope ratios relative to other task classes.
