---
id: balance-min-and-max-bar-cues-when-testing-range-comparisons-in-bar-charts
title: Balance min-bar and max-bar cues so they do not always reveal range in range-comparison
  tests
bibliography: references.bib
description: Remove trivial range cues by ensuring min and max bars do not consistently
  correspond to the larger range in bar-chart range comparisons.
labels:
- chart:bar
- task:compare
- visual:position
- impact:validity
- data:categorical
- audience:general
- method:experiment-design
---

## Control min/max-bar confounds in range-comparison evaluations <!-- role: advice -->

When testing “which bar chart has the larger range?”, construct trials so the chart with the larger range does not always have the shorter minimum bar or the longer maximum bar.

## Why min/max bars can trivialize range judgments <!-- role: reason -->

Range is defined by the minimum and maximum, so naïvely generated stimuli make “pick the chart with the shortest bar” (or longest bar) a perfect strategy. That prevents you from learning whether viewers use other proxies (e.g., slopes or hull-based summaries) and can inflate apparent range-discrimination ability.

**Mechanism:** If the smaller-range chart’s endpoints are always strictly inside the larger-range chart’s endpoints, then min/max alone perfectly identifies the larger range; balancing endpoint overlap breaks that.

**Evidence:** The experiment design manipulated range so the smaller range spanned either the minimum or maximum of the larger-range chart, making min-bar or max-bar correspond to the correct answer only 50% of the time and eliminating the confound [@ondovRevealingPerceptualProxies2021].

**Notes:** This was paired with side randomization and balancing of deceptive/non-deceptive cases.

## When this applies <!-- role: context -->

- **User Goal:** Decide which of two groups has more variability (range) at a glance.
- **Task:** Forced-choice comparison of ranges between two bar charts.
- **Data:** Two series with the same number of bars and comparable scaling.
- **Chart Setting:** Experimental evaluation or robustness testing where you need to isolate nontrivial perceptual strategies.
- **Audience:** Any; particularly important when participants might use simple heuristics under time pressure.
- **Success Criterion:** Performance reflects range extraction, not a single-bar shortcut.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The real-world task genuinely allows using only extremes (because extremes are what matter). **Why:** Removing endpoint cues would test a different task than the operational requirement.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Balancing endpoint overlap adds complexity to stimulus generation and may reduce ecological realism for some datasets. **Risk:** Some viewers may still use endpoints opportunistically when they happen to align with the correct answer. **Mitigation:** Track and report how often endpoint-based strategies would succeed in your stimulus set.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating range-comparison accuracy as evidence of robust range perception without checking whether min/max bars trivially determine the answer. **Why it fails:** The task can collapse into “find the shortest/longest bar,” preventing inference about other perceptual proxies [@ondovRevealingPerceptualProxies2021].

## Quick tests <!-- role: check -->

**Failure Sign:** A rule like “pick the chart with the shortest bar” predicts correct answers nearly perfectly in your trials. **Quick Check:** Compute whether min-bar or max-bar alone identifies the larger range and confirm it is near chance across trials. **Stronger Test:** Re-run the task with endpoint-balanced trials and compare thresholds or accuracy.

## What to do instead <!-- role: fix -->

- Design the stimulus set so the smaller-range chart overlaps one endpoint (min or max) of the larger-range chart and balance those cases.
- Add explicit range annotations (e.g., markers at min and max) if your goal is to support accurate range reading rather than study proxy use.
- Switch to a representation where range is directly encoded as a single interval mark per group if extremes-based shortcuts are undesirable.
- Use adversarial optimization targeted at non-endpoint proxies (e.g., slope) only after endpoint confounds are controlled.
