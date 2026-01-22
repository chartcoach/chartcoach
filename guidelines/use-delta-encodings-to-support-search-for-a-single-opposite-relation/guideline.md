---
id: use-delta-encodings-to-support-search-for-a-single-opposite-relation
title: Use Delta Encodings to Support Visual Search for a Single Opposite Relation
bibliography: references.bib
description: When users must locate one pair with a different relation among many,
  encoding the relation as a delta yields dramatically better search efficiency.
labels:
- chart:bar
- chart:dot
- chart:slope
- task:search
- visual:length
- visual:position
- visual:orientation
- impact:efficiency
- data:paired
- audience:novice
- audience:expert
- complexity:advanced
---

## Encode relations as single deltas for find-the-anomaly tasks <!-- role: advice -->

When the task is to find one pair with the opposite relation (e.g., one decrease among increases), encode each pair as a delta mark rather than two separate value marks.

## Why delta marks scale better with more pairs in search <!-- role: reason -->

Searching for a relation between two marks is inefficient because the viewer must repeatedly bind and compare the two components of each pair. A delta encoding turns the relation into one feature per pair, so search time increases much less as more pairs are added.

**Mechanism:** Delta encoding reduces per-item relational computation during search, improving the search rate (added time per added pair).

**Evidence:** In visual search displays containing 2 to 10 pairs, search rates were much slower for individual-value encodings than for delta encodings; each additional pair added roughly 164–266 ms with individual values versus about 8–135 ms with deltas, corresponding to about a 49–95% improvement depending on encoding. [@nothelferMeasuresBenefitDirect2020a]

**Notes:** The delta advantage in this study was strongest for target-finding compared to ensemble summary tasks.

## When this applies in monitoring and scanning displays <!-- role: context -->

- **User Goal:** Quickly locate a category/entity whose change direction differs from the rest.
- **Task:** Visual search for one target relation among many opposite-relation distractors.
- **Data:** Many paired comparisons (multiple entities, each with two values).
- **Chart Setting:** Static status boards, alerting dashboards, slide summaries where rapid scan is critical.
- **Audience:** Mixed audiences; especially operational roles scanning for exceptions.
- **Success Criterion:** Low additional time per additional pair (good scalability with set size).

## When to break this rule <!-- role: exceptions -->

**Break it when:** The user must identify the anomalous pair specifically by its absolute values rather than its relation. **Why:** Delta encodings alone do not preserve the original values needed for that judgment.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Immediate access to the two original values for each pair.\
**Risk:** Users may over-focus on change direction and miss that absolute levels matter in some decisions.\
**Mitigation:** Provide a secondary view or on-demand access to original values.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Encoding only individual values and expecting anomaly-finding to remain fast as the number of pairs grows. **Why it fails:** Search time rises steeply with set size when relations must be computed from two marks.\
**Mistake:** Using the same search-oriented view for tasks that require absolute-value context. **Why it fails:** Delta-only views remove needed information about baseline levels.

## Quick tests <!-- role: check -->

**Failure Sign:** Time to find the odd relation grows sharply as you add more categories.\
**Quick Check:** Double the number of pairs and see if users’ find-the-odd-one time roughly doubles with your current encoding.\
**Stronger Test:** Measure search rate (time increase per additional pair) for your current design versus a delta encoding on the same data.

## What to do instead <!-- role: fix -->

- Add a delta-only “exception scan” panel next to the main value chart.
- Provide a toggle between “Values” and “Change” modes for the same set of pairs.
- Reduce the number of displayed categories at once when only individual values can be shown.
- Use filtering so users search within a smaller subset of pairs.
