---
id: use-animated-transitions-to-find-the-biggest-mover-between-two-series
title: Use an animated transition to find the biggest absolute change between two
  series
bibliography: references.bib
description: Animated transitions help viewers identify which item changed the most
  between two datasets when comparing exactly two series.
labels:
- chart:bar
- chart:donut
- task:compare
- task:detect-change
- visual:motion
- impact:accuracy
- data:categorical
- audience:novice
- comparison:two-series
---

## Animated transitions for maximum-delta comparison <!-- role: advice -->

Use an animated transition that morphs one dataset into the other when the user’s task is to pick the single item with the largest absolute change between two series. Keep the transition time fixed so the largest change produces the strongest motion signal.

## Motion-as-delta signal for maximum change <!-- role: reason -->

Animating a mark from its old value to its new value converts “difference” into a motion cue, so viewers can use relative motion strength (e.g., perceived speed) as a direct perceptual proxy for absolute delta. This reduces reliance on holding values in visual working memory across separated views.

**Mechanism:** The largest delta produces the most salient motion, making the target “pop out” relative to smaller-moving distractors during the transition.

**Evidence:** In a maximum-delta (biggest mover) task, animated bar charts required smaller signals (lower titers) than all tested static arrangements, including overlaid charts [@ondovFaceFaceEvaluating2019a]. In the same task, animated donut charts also outperformed the static arrangements tested for donuts [@ondovFaceFaceEvaluating2019a].

**Notes:** This benefit did not appear for the correlation task, and it was not observed for slope charts in this study.

## Context for using animation to find the biggest mover <!-- role: context -->

- **User Goal:** Identify which category/item changed the most between two snapshots.
- **Task:** MAXDELTA: choose the single largest absolute change (increase or decrease).
- **Data:** Exactly two series; a small set of comparable items (e.g., a handful of bars/slices) where one item is the “biggest mover.”
- **Chart Setting:** Interactive or screen-based setting where a brief, fixed-time animation can be shown.
- **Audience:** Non-expert viewers performing quick perceptual judgments.
- **Success Criterion:** Higher accuracy at smaller differences (better discrimination threshold).

## Exceptions for animated biggest-mover comparison <!-- role: exceptions -->

- **Break it when:** The user’s primary task is to judge overall similarity/correlation across two series rather than a single largest change. **Why:** Animation did not improve correlation judgments in this study and viewers struggled to use motion to compare correlation [@ondovFaceFaceEvaluating2019a].
- **Break it when:** You are using slope charts for the same biggest-mover task. **Why:** Overlaid slope charts outperformed animated slope charts for maximum-delta detection in this study [@ondovFaceFaceEvaluating2019a].

## Costs of animated comparison <!-- role: costs -->

**Sacrifice:** Animation is time-based, so the user must attend during the transition rather than inspecting a fully static display. **Risk:** If many marks move simultaneously, viewers may miss changes or feel overloaded. **Mitigation:** Keep the number of compared series at two and keep the animation duration brief and consistent.

## Mistakes with animated biggest-mover displays <!-- role: mistakes -->

- **Mistake:** Using animation for “overall similarity” judgments (e.g., correlation) without additional support. **Why it fails:** Viewers did not gain performance benefits for correlation comparison from animation in this study [@ondovFaceFaceEvaluating2019a].
- **Mistake:** Varying transition duration between items or across trials. **Why it fails:** The comparison relies on motion as a standardized cue for delta; inconsistent timing weakens comparability.

## Check for whether animation helps the biggest-mover task <!-- role: check -->

**Failure Sign:** Viewers often pick a large absolute value rather than the item that changed the most. **Quick Check:** Show a few representative transitions and confirm that the largest changer is immediately noticeable during the motion. **Stronger Test:** Run a small threshold-style pilot (e.g., titrate deltas) and verify that users maintain similar accuracy at smaller deltas than with your best static alternative.

## Fixes when animation is not feasible or not working <!-- role: fix -->

- Use an overlaid view of the two series so both values are co-located for direct comparison.
- Use a mirrored small-multiples arrangement (center-aligned) to reduce correspondence distance for paired items.
- Reduce the number of items shown at once (e.g., filter to a subset) so motion cues remain discriminable.
- Add an interactive toggle that lets the user replay the transition on demand.
