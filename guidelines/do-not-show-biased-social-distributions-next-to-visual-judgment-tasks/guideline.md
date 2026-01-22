---
id: do-not-show-biased-social-distributions-next-to-visual-judgment-tasks
title: Do not show biased social distributions next to visual judgment tasks
bibliography: references.bib
description: Biased prior-response histograms increase estimation error in graphical
  perception tasks.
labels:
- chart:bar
- task:estimate
- visual:annotation
- impact:accuracy
- data:quantitative
- audience:novice
- custom:histogram
---

## Avoid displaying prior-answer histograms that are shifted away from the true value <!-- role: advice -->

Do not display a prior-response histogram as guidance for a chart-reading task if its center is not known to be close to the true value for that task.

## Why a shifted distribution increases error <!-- role: reason -->

A displayed distribution provides a numeric focal point. When that focal point is inaccurate but plausible, it pulls estimates away from the correct answer and increases error.

**Mechanism:** Social proof operates as an informational cue; viewers partially substitute the shown “what others answered” distribution for their own perceptual read.

**Evidence:** In proportion-judgment tasks, showing a more biased social histogram (offset by about one standard deviation from the control mean) produced higher errors than showing a less-biased histogram and higher errors than a non-social control [@hullmanImpactSocialInformation2011]. Similar directionality appeared when social histograms were regrouped by whether they were closer to versus farther from truth in linear-association estimation [@hullmanImpactSocialInformation2011].

**Notes:** The increase occurs even when the biased signal remains believable rather than extreme.

## When you should apply this in visualization products <!-- role: context -->

- **User Goal:** Read a quantitative value accurately from a chart.
- **Task:** Proportion estimation (e.g., “smaller as a proportion of larger”) or similar numeric judgment.
- **Data:** Quantitative with a correct or reference value available.
- **Chart Setting:** Interfaces that place “community answers” next to the chart (e.g., a histogram of prior responses).
- **Audience:** Readers who may treat crowd distributions as authoritative cues.
- **Success Criterion:** Minimize systematic deviation from the correct answer.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** There is no meaningful notion of “true value” and the goal is to surface the community’s subjective distribution itself. **Why:** “Bias” is undefined when the metric is preference or sentiment rather than an accuracy task.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may need extra infrastructure to validate or calibrate the distribution before showing it. **Risk:** Hiding the distribution can reduce transparency about what others did. **Mitigation:** Make the distribution accessible in a separate view that is not part of the estimation workflow.

## Common ways this goes wrong <!-- role: mistakes -->

**Mistake:** Treating a histogram of prior answers as inherently corrective. **Why it fails:** If it is off-center, it becomes a consistent pull away from the truth.

## Quick ways to validate it worked <!-- role: check -->

**Failure Sign:** User estimates move in the direction of the displayed histogram mean even when that mean is wrong. **Quick Check:** Track correlation between histogram mean shifts and user estimate shifts across items. **Stronger Test:** Randomize viewers into “shifted histogram” vs “no histogram” and compare absolute error.

## What to do instead <!-- role: fix -->

- Require a calibration phase that checks whether displayed aggregates are closer to truth than unaided responses before enabling them.
- Show a distribution only after the viewer submits their estimate for that chart item.
- Provide an uncertainty-aware display of the aggregate (e.g., emphasize spread) without implying correctness.
- Remove numeric consensus summaries from accuracy-critical reading tasks and keep social information in a separate exploration context.
