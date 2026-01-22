---
id: use-position-on-a-common-scale-for-quantitative-sorting
title: Use position on a common scale to support accurate sorting of quantitative
  values
bibliography: references.bib
description: For sorting quantitative values, encode values as positions on a shared
  axis to improve accuracy versus length- or angle-based alternatives.
labels:
- chart:bar
- task:sort
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- source:collated
---

## Prefer position on a shared axis for sorting quantitative values <!-- role: advice -->

Use a position encoding on a common scale when people need to sort quantitative values. Prefer this over length-based bars and angle-based wedges for this task.

## Why shared-axis position improves sorting accuracy <!-- role: reason -->

Sorting requires reliably judging relative magnitude across multiple items; placing values on a single shared axis reduces perceptual error when comparing items.

**Mechanism:** A common axis gives viewers a consistent reference so they can compare values by alignment rather than estimating other geometric properties.

**Evidence:** In sorting judgments, a position-on-common-scale bar design outperformed length-based bar designs in accuracy, and it also outperformed an angle-based (pie-slice) design in accuracy with a significant difference. [@clevelandGraphicalPerceptionTheory1984; @zengReviewCollationGraphical2023]

**Notes:** The evidence here is specific to the “sort” task and the particular chart variants evaluated.

## When sorting quantitative values is the goal <!-- role: context -->

- **User Goal:** Order categories or items from smallest to largest (or the reverse).
- **Task:** Sort.
- **Data:** Quantitative values associated with discrete items (e.g., categories).
- **Chart Setting:** Static chart where multiple values must be compared on one view.
- **Audience:** General.
- **Success Criterion:** Higher accuracy in ordering.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** The viewer does not need to sort values (for example, they only need a qualitative impression without ordering). **Why:** The evidence supports sorting accuracy specifically, not other tasks.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Shared-axis position encodings may constrain layout choices compared to alternatives like wedges. **Risk:** Applying the rule to tasks other than sorting may not yield the same benefit. **Mitigation:** Confirm the user’s primary task is ordering before prioritizing this encoding.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using angle-based wedges (pie-style) to rank or sort categories by magnitude. **Why it fails:** Sorting accuracy can be lower than with position on a common scale.

## Quick tests <!-- role: check -->

**Failure Sign:** People disagree about the correct ordering, especially for mid-ranked items. **Quick Check:** Ask a few readers to rank the items without reading numbers; if rankings vary, the encoding is not supporting sorting well. **Stronger Test:** Run a small timed sorting task and compare error rates across candidate encodings.

## What to do instead <!-- role: fix -->

- Use a bar-style design where the quantitative value is encoded by position on a shared axis.
- Replace angle encodings used for ordering with a shared-axis position encoding.
- If you must keep multiple groups, keep each group’s values comparable via a consistent shared axis.
