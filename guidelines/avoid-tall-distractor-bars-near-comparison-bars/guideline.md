---
id: avoid-tall-distractor-bars-near-comparison-bars
title: Reduce tall distractor bars when viewers must compare specific bar heights
bibliography: references.bib
description: Tall distractor bars can increase error for bar-height comparisons, including
  adjacent and separated comparisons.
labels:
- chart:bar
- task:compare
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- layout:distractors
---

## Limit tall distractors around the bars people must compare <!-- role: advice -->

Reduce or remove other bars that are tall and visually prominent near the bars that viewers must compare. Keep the compared bars visually distinct from surrounding bars.

## Prominent distractors increase comparison difficulty <!-- role: reason -->

When nearby bars are tall, they add visual competition that increases errors in height comparison tasks.

**Mechanism:** Visually salient nearby bars draw attention and make it harder to isolate the endpoints of the target bars, increasing perceptual noise during relative judgments.

**Evidence:** Tall distractors increased absolute error for bar comparison tasks in the tested conditions, while short distractors had little clear impact; stacked-bar distractors also increased difficulty for unaligned comparisons. [@talbotFourExperimentsPerception2014; @zengReviewCollationGraphical2023]

**Notes:** The effect was observed as an increase in absolute error on the percent-of-height estimation task.

## Context: When this applies <!-- role: context -->

- **User Goal:** Compare two highlighted bars accurately.
- **Task:** Percent/ratio estimation between two marked bars in a bar chart (including stacked variants).
- **Data:** Quantitative measures with additional non-target categories present.
- **Chart Setting:** Multi-bar displays where non-target bars appear between/around the target bars.
- **Audience:** General audiences performing quick judgments.
- **Success Criterion:** Lower error and less confusion about which bars to compare.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The presence of all categories is essential context and cannot be reduced without changing the question. **Why:** Removing or shrinking bars can remove necessary reference information for interpretation.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Reducing distractors may require filtering, aggregation, or additional views. **Risk:** Over-simplifying the chart can hide important context or alternative comparisons. **Mitigation:** Preserve context with supplemental views or annotations while keeping the comparison region clean.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Highlighting two bars but leaving many similarly salient neighboring bars in place. **Why it fails:** The surrounding tall bars still raise error in the comparison task.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Viewers frequently compare the wrong bars or give noisy estimates even when the target bars are marked. **Quick Check:** Visually scan for non-target bars that are taller than the comparison bars and adjacent to them. **Stronger Test:** A/B test the same task with and without prominent neighboring bars and compare absolute error.

## Fix: What to do instead <!-- role: fix -->

- Filter the view to the subset of categories needed for the comparison task.
- Group or collapse non-target categories so fewer tall bars compete for attention.
- Provide a focused comparison inset that isolates the two target bars.
- Separate the comparison into a dedicated small panel that excludes unrelated bars.
