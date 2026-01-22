---
id: avoid-difference-overlays-as-the-only-cue-for-missingness-identification
title: Avoid relying on difference overlays as the only cue for identifying categories
  present in only one series
bibliography: references.bib
description: Difference overlays do not reliably improve performance for identifying
  categories that exist only in one of two series.
labels:
- chart:bar
- task:filter
- visual:position
- impact:accuracy
- impact:speed
- data:categorical
- data:missingness
- audience:novice
- comparison:multi-series
---

## Don’t rely only on overlays to find categories missing from one series <!-- role: advice -->

Do not assume that adding difference overlays will improve performance when people need to identify categories that appear only in one of the two series. Use another explicit way to distinguish “missing” from “zero” if that distinction matters.

## Why difference overlays are insufficient for missingness identification <!-- role: reason -->

The absence (or presence) of a difference mark can be too subtle or ambiguous as a signal of missingness, so overlays do not consistently improve speed or accuracy for identifying categories present in only one series.

**Mechanism:** Missingness requires categorical discrimination (“present in series A but not B”), and a missing overlay can be overlooked or misread as a valid zero-difference situation depending on how viewers interpret the marks.

**Evidence:** For tasks that require identifying categories only in the target series or only in the source series, chart design had limited or inconsistent benefits in accuracy, and no consistent accuracy advantage was observed for difference-overlay designs over the grouped bar chart across these missingness-identification tasks in the reported rankings and significance results [@srinivasanWhatsDifferenceEvaluating2018; @zengReviewCollationGraphical2023].

**Notes:** This guideline is scoped to missingness-identification tasks, not to difference or change tasks.

## When missingness identification applies <!-- role: context -->

- **User Goal:** Identify categories that exist in one series but not the other.
- **Task:** Filter/select categories by series presence (missingness detection).
- **Data:** Two-series categorical data with categories that can be absent in one series (true missing values, not zeros).
- **Chart Setting:** Static dashboard view without interactive disambiguation.
- **Audience:** Readers who may not carefully inspect subtle overlay absence.
- **Success Criterion:** Correctly identifying series-exclusive categories without confusion between “missing” and “zero.”

## When not to follow it <!-- role: exceptions -->

**Break it when:** Categories are guaranteed to be present in both series (no missingness scenario). **Why:** The missingness-identification task does not exist in that setting.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Adding explicit missingness cues can increase annotation or legend complexity. **Risk:** If missingness cues are over-emphasized, they can distract from value comparisons. **Mitigation:** Keep missingness cues visually distinct but lightweight.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Encoding missingness solely as “no difference overlay is drawn.” **Why it fails:** Users may overlook the absence or misinterpret it, leading to unreliable identification.

## Quick tests <!-- role: check -->

**Failure Sign:** Readers confuse “missing in one series” with “present and unchanged.” **Quick Check:** Ask a reader to point to categories present only in the source series; if they hesitate or select unchanged categories, the cue is insufficient. **Stronger Test:** Run a small accuracy check on series-exclusive category identification with and without an explicit missingness indicator.

## What to do instead <!-- role: fix -->

- Add an explicit indicator for missing categories that does not depend on noticing the absence of a mark.
- Separate the missingness task into a dedicated view (e.g., a list of categories present only in one series).
- Provide interaction that reveals series presence on hover/selection if a static cue is too subtle for your audience.
