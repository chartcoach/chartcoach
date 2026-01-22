---
id: expect-distractor-classes-and-conflicting-cues-to-matter-only-in-combination-for-mean-comparison
title: Avoid combining distractor classes and conflicting cues when mean comparison
  accuracy matters in multiclass scatterplots
bibliography: references.bib
description: For mean-comparison tasks, the combination of additional distractor classes
  and conflicting cues can reduce accuracy even if each factor alone does not.
labels:
- chart:scatter
- task:aggregate
- visual:color
- visual:shape
- impact:accuracy
- data:categorical
- audience:general
- complexity:advanced
---

## Avoid piling on distractor classes and conflicting encodings for mean comparisons <!-- role: advice -->

Avoid simultaneously adding extra distractor classes and introducing conflicting visual cues when users must compare class means in a multiclass scatterplot.

## Why the combination can reduce mean-comparison accuracy <!-- role: reason -->

Each added source of heterogeneity increases the burden of separating which marks belong to which relevant class for aggregation. While a single extra complexity may be tolerated, multiple concurrent complexities can exceed viewers’ ability to reliably isolate sets for averaging.

**Mechanism:** Combined visual heterogeneity makes set selection noisier, which degrades the accuracy of estimating and comparing class means.

**Evidence:** In an accuracy-based aggregate task, a comparison between a simpler color-encoded design and a more complex design involving additional class/encoding complexity (E-1 vs. E-8) showed a significant difference, and the overall experimental results support that additional complexities can matter when layered together even when many individual variations do not separate strongly in accuracy rankings [@gleicherPerceptionAverageValue2013; @zengReviewCollationGraphical2023].

**Notes:** This guideline concerns the combined effect of multiple complexity sources, not a blanket ban on either one individually.

## When this applies to your scatterplot design <!-- role: context -->

- **User Goal:** Decide which class has the higher mean.
- **Task:** Aggregate (mean comparison).
- **Data:** Multiple classes, considering adding more classes and/or additional encodings that conflict with class identity.
- **Chart Setting:** Static scatterplot with class identity and additional attributes encoded in appearance.
- **Audience:** General audiences.
- **Success Criterion:** Maintain accuracy on mean-comparison judgments.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The user’s goal is to compare many classes at once and you cannot simplify the display. **Why:** The task requirement forces complexity, so the rule cannot be satisfied.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may have to reduce how many variables or classes are shown at once. **Risk:** Simplification can omit context that some users want. **Mitigation:** Provide alternative views or staged comparisons so users can still access the full set of classes without performing all mean comparisons in one view.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding more classes and also adding conflicting encodings “because each change alone seemed fine.” **Why it fails:** Combined complexity can reduce accuracy even when single-factor changes appear tolerable.

## Quick checks before shipping <!-- role: check -->

**Failure Sign:** Users spend longer scanning and still disagree about which class is higher on average. **Quick Check:** Temporarily remove either the extra classes or the conflicting cue; if the judgment becomes clearer, the combination is the issue. **Stronger Test:** A/B test accuracy with vs. without the combined complexities using the same mean-comparison questions.

## What to do instead when this fails <!-- role: fix -->

- Reduce the number of simultaneously displayed classes during mean comparison.
- Remove the conflicting cue and keep a single clear encoding for class identity.
- Split the visualization into multiple small multiples so each view has fewer competing cues.
- Provide an alternate comparison workflow that does not require comparing all classes in one dense view.
