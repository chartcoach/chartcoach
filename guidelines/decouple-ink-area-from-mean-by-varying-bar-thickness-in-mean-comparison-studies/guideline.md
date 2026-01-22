---
id: decouple-ink-area-from-mean-by-varying-bar-thickness-in-mean-comparison-studies
title: Vary bar thickness to prevent ink-area from trivially encoding mean in mean-comparison
  tests
bibliography: references.bib
description: Avoid confounding mean judgments with total ink by varying bar thickness
  when evaluating mean comparisons in bar charts.
labels:
- chart:bar
- task:compare
- visual:size
- impact:validity
- data:categorical
- audience:general
- method:experiment-design
---

## Bar-thickness variation to remove ink-area confounding in mean tasks <!-- role: advice -->

When testing “which bar chart has the larger mean?” in side-by-side bar charts, vary bar thickness between the two charts so total ink area cannot reliably indicate the larger mean.

## Why ink area can confound mean-comparison evaluation <!-- role: reason -->

If bar thickness is constant, the total filled area (“amount of ink”) is proportional to the sum of bar lengths and therefore proportional to the mean when the number of bars is fixed. That makes the task solvable via an unintended proxy, masking whether viewers are actually using the intended statistic or other perceptual proxies.

**Mechanism:** Constant thickness makes total bar area a shortcut to mean; varying thickness breaks that direct mapping so accuracy reflects other perceptual computations.

**Evidence:** The experiment design explicitly randomized one chart to have skinnier bars to decouple ink area from mean, because otherwise ink area would always indicate the correct mean in fixed-count bar charts [@ondovRevealingPerceptualProxies2021].

**Notes:** The paper used a fixed “skinniness” chosen so the thin-bar chart always had the least ink even when its mean was larger.

## When this applies <!-- role: context -->

- **User Goal:** Compare averages across two groups shown as bar-chart series.
- **Task:** Forced-choice “larger mean” between two bar charts with equal bar counts.
- **Data:** Same number of bars per chart; shared axis scale.
- **Chart Setting:** Experimental evaluations or QA tests where you want to measure proxy use, not allow trivial solutions.
- **Audience:** Any; especially relevant when glance-based judgments are expected.
- **Success Criterion:** The evaluation measures mean perception rather than detection of total area.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your product goal is to let viewers use total area as a legitimate cue (e.g., because area is the intended encoding). **Why:** Varying thickness would intentionally remove that cue and change the task.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Unequal thickness can reduce aesthetic consistency and may introduce its own perceptual biases. **Risk:** Viewers may treat thickness differences as a signal of importance rather than a control. **Mitigation:** Randomize and balance which side is thin across trials/conditions to prevent systematic bias.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Evaluating mean-comparison performance with identical bar thickness and concluding viewers can accurately judge means. **Why it fails:** They may be using ink area, not mean extraction from bar lengths, so the evaluation overestimates robustness [@ondovRevealingPerceptualProxies2021].

## Quick tests <!-- role: check -->

**Failure Sign:** Accuracy remains very high even when other proxy manipulations are introduced, suggesting a trivial cue dominates. **Quick Check:** Compute total ink area (bar length × thickness summed) and verify it does not correlate with the correct answer across trials. **Stronger Test:** Repeat the evaluation with thickness randomized and check whether performance and inferred thresholds change materially.

## What to do instead <!-- role: fix -->

- Keep thickness constant only if you explicitly want area to be a valid cue and report that choice as part of the task definition.
- If thickness variation is undesirable, redesign the stimulus so mean is not recoverable from area (e.g., vary bar counts across charts) and validate the new confound structure.
- Add an explicit mean indicator and evaluate judgments on that indicator rather than on aggregated bar lengths.
- Use adversarial dataset generation that holds mean constant while varying candidate proxies, then verify ink area is not predictive.
