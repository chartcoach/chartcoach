---
id: do-not-expect-wrapped-bars-to-change-find-extremum-time-vs-standard-bars
title: Do not rely on wrapped bar charts to reduce find-extremum completion time compared
  to standard bar charts
bibliography: references.bib
description: In the extracted results, wrapped and standard bar charts were not significantly
  different in completion time for find-extremum tasks.
labels:
- chart:bar
- task:find-extremum
- visual:length
- impact:time
- data:categorical
- audience:general
- variant:wrapped-bar
---

## Treat wrapped bars as an accuracy lever, not a speed lever, for extreme-value tasks <!-- role: advice -->

Use wrapped bar charts to improve correctness in find-extremum tasks, but do not select them expecting faster completion time than a standard bar chart.

## Why time is not the deciding factor in the extracted evidence <!-- role: reason -->

The extracted timing results place wrapped and standard conditions in the same performance group with no significant pairwise differences, so choosing wrapping for speed is not supported by the reported comparisons.

**Mechanism:** Wrapping changes the visual form but can introduce additional reading steps (counting or parsing wraps), which can offset any speed gains from improved visibility of small bars.

**Evidence:** For find-extremum time, the extracted ranking groups standard and wrapped bar charts together with no significant pairs indicating faster performance for either variant [@karduniBoisWrappedBar2020]. This “no time advantage” is preserved in the structured collation intended for visualization recommendation logic [@zengReviewCollationGraphical2023].

**Notes:** This guideline concerns time only; it does not negate observed accuracy advantages under some conditions.

## Context: When this applies <!-- role: context -->

- **User Goal:** Complete extreme-value identification quickly.
- **Task:** find-extremum.
- **Data:** Nominal categories with quantitative values shown as bar lengths.
- **Chart Setting:** Comparing standard vs. wrapped bar chart variants in a static setting.
- **Audience:** Any audience where speed is prioritized.
- **Success Criterion:** Lower completion time.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** Your use case optimizes for accuracy rather than speed. **Why:** The extracted evidence supports accuracy differences more than time differences.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** If you optimize for speed alone, wrapping may add complexity without measurable time savings. **Risk:** Selecting wrapped bars for speed can disappoint users or stakeholders expecting faster task completion. **Mitigation:** Define success criteria explicitly (accuracy vs. time) before choosing the variant.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Claiming wrapped bars are “more efficient” without measuring time-on-task. **Why it fails:** The extracted comparisons do not show a reliable time improvement.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users take just as long to identify extremes in the wrapped version as in the standard version. **Quick Check:** Time a handful of representative users on “find smallest” and “find largest” using both variants. **Stronger Test:** Run an A/B test with task-timed instrumentation and compare distributions of completion time.

## Fix: What to do instead <!-- role: fix -->

- Keep standard bar charts when speed is the top priority and accuracy is already acceptable.
- Add direct cues (such as explicit highlighting) for the extreme categories if you need faster extreme identification.
- Reduce the number of categories shown at once if extreme identification time is driven by scanning load rather than scale issues.
