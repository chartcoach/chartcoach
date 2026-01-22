---
id: do-not-add-quartile-ticks-to-pie-charts-expecting-better-part-to-whole-estimation
title: Do not add quartile ticks to pie charts expecting better part-to-whole estimation
bibliography: references.bib
description: Adding quartile ticks to a pie chart did not produce a clear accuracy
  improvement over a baseline pie in one experiment.
labels:
- chart:pie
- task:estimate
- visual:angle
- visual:annotation
- impact:accuracy
- data:categorical
- data:quantitative
- audience:general
- study:experiment
---

## Avoid quartile ticks on pies as an accuracy upgrade for percent estimation <!-- role: advice -->

Do not assume that adding quartile reference ticks to a pie chart will improve part-to-whole estimation accuracy over a baseline pie chart.

## Why extra cues may not help when the baseline already supports estimation <!-- role: reason -->

If viewers already use stable reference points in the baseline display, adding additional reference cues may provide little incremental benefit for estimation accuracy. In the tested pie variants, the pie with quartile ticks ranked slightly better than the baseline pie but showed no recorded significant difference, indicating no clear accuracy gain from the added ticks in this setup.

**Mechanism:** When a visual design already supports anchoring for estimation, extra anchors can have diminishing returns for reducing error.

**Evidence:** In a part-to-whole estimation task, the pie with quartile ticks ranked above the baseline pie, but no significant difference was recorded between them in the extracted results [@redmondVisualCuesEstimation2019; @zengReviewCollationGraphical2023].

**Notes:** This is not evidence that quartile ticks are harmful, only that they did not produce a clear accuracy improvement in this comparison.

## When you are considering embellishing pies for percent estimation <!-- role: context -->

- **User Goal:** Estimate a highlighted segment’s share of a whole as an integer percentage.
- **Task:** Characterize distribution (part-to-whole segment estimation).
- **Data:** One quantitative proportion per segment (sums to 100%); two segments shown (highlighted segment vs remainder).
- **Chart Setting:** Static pie; segment distinguished via color saturation; optional quartile ticks as added cues.
- **Audience:** General audience (crowdsourced participants).
- **Success Criterion:** Improved estimation accuracy (lower error) attributable to the added cue.

## When to ignore this caution <!-- role: exceptions -->

**Break it when:** Your main goal for ticks is not accuracy improvement (for example, you need consistent stylistic cues across multiple charts). **Why:** This guideline only addresses evidence for accuracy gains, not styling consistency.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up a small potential improvement in some untested contexts by omitting the ticks.
**Risk:** Adding ticks can increase visual clutter without measurable accuracy benefit.
**Mitigation:** If you add ticks, verify that they improve your target metric (error) rather than relying on intuition.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding quartile ticks to pies as a default “make it more readable” step. **Why it fails:** The extracted comparison did not show a clear accuracy improvement over the baseline pie.

## Quick tests <!-- role: check -->

**Failure Sign:** The pie looks more complex, but viewers’ estimates are no closer to the true percent.
**Quick Check:** Show a few examples to colleagues and collect quick percent estimates; compare absolute error with and without ticks.
**Stronger Test:** Run a small randomized evaluation measuring mean absolute error for baseline pie vs ticked pie.

## What to do instead <!-- role: fix -->

- Keep the baseline pie if you cannot verify that the extra cue improves accuracy.
- Shift effort to a chart change that is supported to improve accuracy for this task (for example, using a bar with an external scale when a bar is required).
- Add direct numeric labeling for the highlighted segment if the workflow can support reading instead of estimation.
