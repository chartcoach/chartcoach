---
id: prefer-bar-graphs-over-line-graphs-for-average-position-judgments
title: Prefer bar graphs over line graphs when viewers must estimate an average height
  from memory
bibliography: references.bib
description: Bar graphs yield less biased and more precise average-position estimates
  than line graphs in short-delay recall tasks.
labels:
- chart:bar
- chart:line
- task:estimate
- task:aggregate
- visual:position
- impact:accuracy
- data:quantitative
- audience:novice
- complexity:basic
---

## Use bars (not lines) for average-height recall judgments <!-- role: advice -->

Prefer a bar graph instead of a line graph when people must remember and report the average vertical position of a single series after a brief delay. Use this especially for dashboards or slides where viewers cannot continuously reference the mark while answering.

## Average-position memory is directionally biased by mark type <!-- role: reason -->

Average position reports can be systematically shifted even when position is the only relevant encoding, and the direction of that shift depends on whether the series is drawn as a line or as bars.

**Mechanism:** A line’s average height is remembered lower than it was, while a bar set’s average height is remembered higher than it was, creating predictable under- vs over-estimation depending on mark type.

**Evidence:** Average line positions were underestimated and average bar positions were overestimated in short-delay reproduction tasks, including when the stimulus was uniform (not noisy), indicating a systematic bias rather than an outlier-driven strategy [@xiongBiasedAveragePosition2020a].

**Notes:** This guideline is about average-position estimation across a delay, not about point-by-point reading with a visible axis.

## Applies when users must report an average height after viewing <!-- role: context -->

- **User Goal:** Recall and report the typical/average level of a single series.
- **Task:** Estimate an average vertical position (ensemble mean) after a brief presentation.
- **Data:** One quantitative series; values distributed over x-position.
- **Chart Setting:** Static viewing or brief exposure; response happens after the chart is removed or de-emphasized.
- **Audience:** General audiences or mixed expertise.
- **Success Criterion:** Lower systematic bias and lower variance in reported averages.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task is to communicate continuity or interpolate between points rather than report an average level. **Why:** The evidence here targets average-position reproduction, not interpretation of trends or continuity.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Bars can reduce perceived continuity compared with lines. **Risk:** Switching to bars may change what viewers infer about the underlying process (discrete vs continuous). **Mitigation:** Treat this choice as task-dependent: average-level recall vs continuity/trend reading.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming position encodings are unbiased and therefore interchangeable between lines and bars for average judgments. **Why it fails:** Average-position recall shows systematic underestimation for lines and overestimation for bars even in simple single-series displays [@xiongBiasedAveragePosition2020a].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers consistently report a lower-than-true mean for a line series or a higher-than-true mean for bars in recall questions. **Quick Check:** Run a small internal test where viewers view the chart briefly, then place a probe at the remembered average; look for consistent directional error. **Stronger Test:** Compare a line and bar version with identical data in a counterbalanced pilot and measure mean signed error.

## What to do instead <!-- role: fix -->

- Use bars rather than a line when the primary question is “what is the average level?” under time pressure or memory load.
- Replace a recall-based question with an on-chart reference that keeps the series visible while answering.
- Reframe the task to avoid average reproduction (e.g., ask higher/lower comparisons while the chart remains present).
- If a line must be used, avoid designing interactions that require users to answer from memory after the line disappears.
