---
id: avoid-plotting-multiple-series-when-average-position-accuracy-matters
title: "Avoid plotting multiple series in one frame when users must estimate each\
  \ series\u2019 average height"
bibliography: references.bib
description: "When multiple series share a frame, average-position estimates are pulled\
  \ toward the other series\u2019 position."
labels:
- chart:line
- chart:bar
- task:estimate
- task:compare
- visual:position
- impact:accuracy
- data:multivariate
- audience:novice
- complexity:intermediate
---

## Separate series to prevent perceptual pull in average-height judgments <!-- role: advice -->

Avoid combining multiple data series in the same plotting frame when viewers must recall and report each series’ average vertical position. Use separate panels (small multiples) when average-position accuracy is a primary requirement.

## Nearby series act as an irrelevant positional anchor <!-- role: reason -->

When two series appear together, the remembered average position of a target series shifts toward the other series’ position, changing the size and sometimes the direction of bias relative to single-series viewing.

**Mechanism:** The visual system blends or anchors ensemble position representations across series, so the target’s average height drifts toward the non-target series (a “perceptual pull”).

**Evidence:** In two-series displays (line–line, bar–bar, and line–bar), average position estimates for the target series were pulled toward the irrelevant series, exaggerating or diminishing the baseline underestimation (lines) and overestimation (bars) observed in single-series displays [@xiongBiasedAveragePosition2020a].

**Notes:** The pull changes error even when the target series itself is unchanged; the mere presence and placement of another series is enough.

## Applies when multiple series share a coordinate frame <!-- role: context -->

- **User Goal:** Accurately report the average level of each series (not just compare trends).
- **Task:** Estimate each series’ mean position after a brief delay or without continuous reference.
- **Data:** Two or more quantitative series that can be plotted concurrently.
- **Chart Setting:** Overlaid or stacked series in a single frame; brief viewing; recall-based prompts.
- **Audience:** General audiences, especially when multitasking or under time pressure.
- **Success Criterion:** Reduced cross-series contamination in average estimates.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary task is to judge the relationship between series (e.g., convergence/divergence) rather than recover each mean accurately. **Why:** The combined view may be required to support relational judgments, even if it introduces pull in mean recall.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Using separate panels costs space and can make direct pointwise comparison harder. **Risk:** Small multiples may increase scanning effort and reduce perceived correlation. **Mitigation:** Decide based on the dominant task: average accuracy vs relational comparison.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Adding a second series “for context” while still expecting accurate mean reports for the first. **Why it fails:** The non-target series can pull the target mean estimate toward itself, changing signed error compared with single-series displays [@xiongBiasedAveragePosition2020a].
- **Mistake:** Treating pull as a similarity problem that only occurs between same-mark series (line with line, bars with bars). **Why it fails:** Pull generalizes across mark types (lines pull bars and bars pull lines) [@xiongBiasedAveragePosition2020a].

## Quick tests <!-- role: check -->

**Failure Sign:** Mean estimates change when a second series is added, even though the target series data are identical. **Quick Check:** Show the target alone vs with an additional series and compare signed error distributions. **Stronger Test:** Counterbalance which series is designated as target and measure whether target errors move toward the non-target mean.

## What to do instead <!-- role: fix -->

- Use small multiples so each series is estimated without another series present in the same frame.
- Provide separate single-series views for any task step that asks for an average estimate from memory.
- If multiple series must be shown, move mean-estimation questions to a state where the relevant series is isolated.
- Avoid workflows where viewers encode a mean from a multi-series display and then reproduce it after a mask or delay.
