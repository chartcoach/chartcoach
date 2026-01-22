---
id: anticipate-layout-dependent-bias-when-mixing-lines-and-bars
title: Anticipate layout-dependent mean bias when mixing a line series with a bar
  series
bibliography: references.bib
description: In combined line-and-bar charts, perceptual pull can amplify or reduce
  mean-estimation bias depending on vertical arrangement.
labels:
- chart:combo
- chart:bar
- chart:line
- task:estimate
- visual:position
- impact:accuracy
- data:multivariate
- audience:novice
- complexity:advanced
---

## Arrange mixed line-and-bar series knowing pull can amplify or dampen bias <!-- role: advice -->

When placing one line series and one bar series in the same frame, treat the vertical arrangement as a bias control: the series will pull each other’s remembered average heights. Do not assume the mixed encoding reduces interference.

## Pull interacts with baseline line-under and bar-over biases <!-- role: reason -->

Lines tend to be remembered lower than their true mean, while bars tend to be remembered higher; when combined, each series shifts toward the other, which can increase or decrease the net signed error depending on which one is higher in the frame.

**Mechanism:** Perceptual pull adds an attraction component toward the other series’ mean, which algebraically combines with the baseline underestimation (lines) and overestimation (bars).

**Evidence:** In line–bar displays, a line placed in the upper half showed more underestimation (pulled downward by the bars), and bars placed in the lower half showed more overestimation (pulled upward by the line); reversing the arrangement reduced those respective biases [@xiongBiasedAveragePosition2020a]. The strength of pull did not depend on whether the irrelevant series was a line or bars [@xiongBiasedAveragePosition2020a].

**Notes:** The effect concerns recall/reproduction of average position after a short delay with the chart removed.

## Applies when building combo charts that may prompt average judgments <!-- role: context -->

- **User Goal:** Recall and report average levels for both a line and a bar series.
- **Task:** Mean estimation for each series under brief viewing or memory load.
- **Data:** Two quantitative series shown together as a line and bars.
- **Chart Setting:** Single shared plotting frame; overlaid or vertically separated series regions.
- **Audience:** General audiences; especially in presentations or monitoring contexts.
- **Success Criterion:** Predictable, minimized signed bias in mean reports for each series.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Users read exact values directly from the chart with continuous access (no delay/mask) rather than reproducing a mean from memory. **Why:** The demonstrated biases were measured in a short-delay recall paradigm, not continuous reading.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Designing around bias can constrain aesthetic layout choices for combo charts. **Risk:** Over-optimizing arrangement for mean recall could harm other tasks like trend comparison. **Mitigation:** Validate with a task-based pilot when the chart must serve multiple tasks.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a line-and-bar combo expecting the different mark types to prevent interference. **Why it fails:** Perceptual pull occurs across mark types, not just within the same mark type [@xiongBiasedAveragePosition2020a].
- **Mistake:** Interpreting changes in mean estimates between layouts as “user inconsistency” rather than a systematic shift. **Why it fails:** The same target series can be estimated differently depending on the other series’ position in the frame [@xiongBiasedAveragePosition2020a].

## Quick tests <!-- role: check -->

**Failure Sign:** The same series’ reported mean changes when the accompanying series is moved higher or lower. **Quick Check:** Hold the target series constant and swap the other series’ vertical placement; measure signed error shifts. **Stronger Test:** Run a within-subject comparison across the two arrangements and confirm whether errors move toward the non-target mean.

## What to do instead <!-- role: fix -->

- Avoid mixing a line and bars in one frame when the key deliverable is an accurate average-level takeaway from memory.
- Use separate panels for the line and bars when viewers must report each mean independently.
- If a combo chart is required, validate the chosen arrangement with a brief mean-recall pilot using your real data ranges.
- Add a design step that isolates the series during any interaction that asks the user to report an average level.
