---
id: use-staircase-titration-and-titer-thresholds-to-compare-deceptiveness-of-bar-chart-proxies
title: Estimate proxy deceptiveness with staircase titration and a 75% titer threshold
bibliography: references.bib
description: Measure how strongly adversarial proxy manipulations mislead bar-chart
  comparisons by estimating the titer needed for 75% accuracy.
labels:
- chart:bar
- task:compare
- visual:multiple
- impact:evaluation
- data:categorical
- audience:research
- method:psychophysics
---

## Titer-threshold measurement for deceptive proxy strength <!-- role: advice -->

To quantify how deceptive a proxy manipulation is in bar-chart comparisons, use a staircase procedure to adjust the mean/range ratio (titer) and estimate the titer at which viewers reach 75% correct.

## Why titer thresholds summarize proxy-driven confusion <!-- role: reason -->

A proxy is more deceptive if viewers need a larger true difference in the target statistic (mean or range) to overcome the proxy and answer correctly. A titer threshold operationalizes this by converting many binary trials across difficulty levels into a single discriminability estimate.

**Mechanism:** Staircase titration concentrates trials around the perceptual boundary, efficiently estimating the statistic ratio needed for reliable discrimination under a given proxy condition.

**Evidence:** The experiment defined titer as a normalized ratio difference in mean or range and used a staircase design to approach a 75% discriminability threshold, then compared thresholds across proxy-manipulated conditions to infer which proxies most misled judgments [@ondovRevealingPerceptualProxies2021].

**Notes:** The approach supports comparing proxy conditions and capturing individual differences via participant-level thresholds.

## When this applies <!-- role: context -->

- **User Goal:** Evaluate susceptibility of a bar-chart comparison task to specific perceptual proxies.
- **Task:** Binary forced-choice (“which has larger mean/range?”) under controlled viewing.
- **Data:** Paired datasets where the “correct” chart differs by a controlled ratio in mean or range.
- **Chart Setting:** User study or internal validation where you can run repeated trials per participant.
- **Audience:** Researchers and practitioners doing perceptual evaluation.
- **Success Criterion:** Comparable thresholds across conditions with interpretable uncertainty.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot run repeated trials per person or cannot control difficulty parametrically. **Why:** Staircase titration depends on adaptive difficulty adjustment and enough trials to estimate a psychometric function.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Requires more design effort (stimulus generation and adaptive control) than a fixed set of trials. **Risk:** Thresholds can be noisy with too few trials per condition or heterogeneous strategies. **Mitigation:** Model uncertainty explicitly and retain participant-level estimates rather than only aggregating.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Comparing proxy conditions using raw accuracy at a single difficulty level. **Why it fails:** Accuracy conflates difficulty choice with proxy influence and can hide shifts in discriminability that appear only near threshold [@ondovRevealingPerceptualProxies2021].

## Quick tests <!-- role: check -->

**Failure Sign:** Accuracy is near ceiling or floor across most trials, offering little sensitivity to proxy effects. **Quick Check:** Plot accuracy versus titer and verify responses span the transition region. **Stronger Test:** Fit participant-level logistic models and extract the 75% threshold with uncertainty for each condition.

## What to do instead <!-- role: fix -->

- Increase the range of titer values so the psychometric curve is identifiable (avoid all-easy or all-hard trials).
- Use participant-level modeling to estimate thresholds rather than relying on aggregate means.
- If adaptive staircases are infeasible, run a small fixed grid of titer levels and fit a psychometric function post hoc.
- If the task cannot be parameterized by a single ratio, switch to a different dependent measure (e.g., preference consistency) and state the limitation explicitly.
