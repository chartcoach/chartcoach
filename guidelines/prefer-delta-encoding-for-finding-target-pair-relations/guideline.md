---
id: prefer-delta-encoding-for-finding-target-pair-relations
title: Directly encode pairwise deltas to speed up finding target pair relations
bibliography: references.bib
description: When users must find a specific increase/decrease pattern among many
  paired values, encode the delta directly to reduce search time.
labels:
- chart:bar
- chart:dot
- chart:slope
- task:filter
- visual:position
- visual:length
- visual:orientation
- impact:speed
- data:quantitative
- audience:general
- comparison:deltas
---

## Use delta charts for relation-finding search tasks <!-- role: advice -->

Directly encode the difference (delta) between each pair of values instead of showing both individual values when the user’s job is to find a specific pairwise relation.

## Why delta encoding speeds relation search <!-- role: reason -->

Direct delta marks let viewers detect the relation as a single visual feature (e.g., sign and magnitude) rather than mentally comparing two separate marks per pair, which reduces visual search effort.

**Mechanism:** Collapsing a two-mark comparison into one mark reduces the number of visual comparisons needed per pair and avoids serial “relationship extraction” across many pairs.

**Evidence:** In a relation-search task (find the opposite relation among many pairs), delta encodings produced significantly faster search times than individual-value encodings across position, length, and slope variants (time ranking groups delta-dot and delta-bar above non-delta dot and bar, with delta-slope also outperforming non-delta slope) [@nothelferMeasuresBenefitDirect2020; @zengReviewCollationGraphical2023].

**Notes:** This guidance targets search-time efficiency (not absolute-value reading), and the tested designs compare delta vs non-delta for the same visual channel family.

## Context: Relation search over many paired values <!-- role: context -->

- **User Goal:** Quickly locate a data pair with a specific relation pattern (e.g., one “increase” among many “decreases,” or a specific direction pattern between paired values).
- **Task:** Filter.
- **Data:** Quantitative values that naturally form pairs (before/after, A vs B) across multiple categories/items.
- **Chart Setting:** Static display where multiple pairs are visible at once and the user scans for a target relation.
- **Audience:** General audiences performing rapid visual lookup.
- **Success Criterion:** Faster completion time for correctly locating the target relation.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The user must read or compare the original absolute values (not just differences). **Why:** Delta-only displays remove the base-value context needed for absolute judgments.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You give up immediate access to the original values because the display emphasizes differences rather than levels. **Risk:** Viewers may misinterpret whether a large delta comes from high values, low values, or both. **Mitigation:** Preserve access to base values elsewhere in the view or workflow.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Showing only individual paired values and expecting viewers to rapidly find a specific relation among many pairs. **Why it fails:** The relation must be derived via repeated two-mark comparisons, which slows scanning.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** People take noticeably longer as you add more paired items, even when the target relation stays visually “obvious.” **Quick Check:** If the task prompt can be answered from “difference and direction only,” a delta encoding is likely appropriate. **Stronger Test:** Run a small timed pilot where you add more pairs; if time grows steeply for the non-delta version, switch to delta encoding.

## Fix: What to do instead <!-- role: fix -->

- Encode each pair’s difference as a single mark (delta) with a linear scale.
- If you must keep the original paired values, provide a separate delta view for the search task.
- Reduce the number of pairs shown at once when delta encoding is not possible.
- Move relation-finding into an interactive filter or computed column so the viewer is not forced to visually derive deltas.
