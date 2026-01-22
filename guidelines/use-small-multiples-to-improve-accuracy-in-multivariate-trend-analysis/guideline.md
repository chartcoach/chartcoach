---
id: use-small-multiples-to-improve-accuracy-in-multivariate-trend-analysis
title: Use small multiples of per-entity traces to improve anomaly detection accuracy
  in multivariate trends
bibliography: references.bib
description: A small multiples layout of individual traces reduces clutter and improves
  accuracy versus animation.
labels:
- chart:small-multiples
- task:detect
- visual:layout
- impact:accuracy
- data:temporal
- audience:expert
- usecase:analysis
---

## Use small multiples per entity when accuracy matters more than scanning time <!-- role: advice -->

Use a small multiples layout that shows one entity’s trace per panel when analysts must accurately find counter-trends or reversals across many entities.

## Why small multiples reduce errors in trend search <!-- role: reason -->

Overlaying many paths in one space increases occlusion and visual interference; separating each entity into its own panel removes clutter, making deviations easier to see even though users must scan more panels.

**Mechanism:** Partitioning into aligned mini-views converts a cluttered global search into repeated local judgments with fewer confounds from overlapping trajectories.

**Evidence:** Small multiples yielded significantly higher accuracy than animation in the study’s tasks [@robertsonEffectivenessAnimationTrend2008]. In analysis mode, small multiples was also significantly faster than animation [@robertsonEffectivenessAnimationTrend2008].

**Notes:** The benefit is strongest when many entities move similarly and overplotting would hide the rare exceptions.

## When to apply small multiples traces <!-- role: context -->

- **User Goal:** Correctly identify which specific items show unusual trend behavior.
- **Task:** Spot counter-trends, reversals, or unusually large changes.
- **Data:** Dozens to ~200 entities with time paths in 2D (plus optional size encoding).
- **Chart Setting:** Static view suitable for careful inspection; consistent axes across panels.
- **Audience:** Analysts and reviewers who value correctness.
- **Success Criterion:** Fewer selection errors on anomaly-finding tasks.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The audience must get a single global overview of all entities at once. **Why:** Small multiples require serial scanning, which can slow holistic impression formation [@robertsonEffectivenessAnimationTrend2008].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More screen space and more time spent scanning. **Risk:** Panels become too small as the number of entities grows, making traces hard to read. **Mitigation:** Limit the number of entities shown or group/filter before displaying.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Packing too many small multiples into a fixed area until each panel is barely legible. **Why it fails:** The trace becomes too small to perceive reliably, eroding the accuracy advantage [@robertsonEffectivenessAnimationTrend2008].
- **Mistake:** Mixing axes or scales across panels. **Why it fails:** Comparisons across entities become unreliable because movement no longer means the same thing in each panel [@robertsonEffectivenessAnimationTrend2008].

## Quick tests <!-- role: check -->

**Failure Sign:** Users squint/zoom frequently or misread direction/shape of traces in individual panels. **Quick Check:** Pick a random panel and ask what changed over time; if the answer is uncertain, the panels are too small. **Stronger Test:** Time a short anomaly-finding task set with 50 vs 100 panels to see when accuracy drops.

## What to do instead <!-- role: fix -->

- Filter to a smaller subset of entities before using small multiples when the panel grid becomes too dense.
- Use an overlaid traces view for a global overview, then switch to small multiples for confirmation.
- Group entities (e.g., by category) into separate blocks so scanning is structured.
- Provide selection/highlighting to focus attention on a small set of panels during review.
