---
id: use-quantile-dotplots-with-about-50-dots-for-glanceable-transit-decisions
title: Use quantile dotplots with about 50 dots to support quick transit arrival decisions
bibliography: references.bib
description: Quantile dotplots with roughly 50 outcomes improve decision quality and
  consistency for bus-catching choices compared to point estimates and several other
  uncertainty displays.
labels:
- chart:dotplot
- task:decide
- visual:position
- impact:decision-quality
- data:uncertainty
- audience:novice
- domain:transit
- complexity:intermediate
---

## Use quantile dotplots with about 50 dots to support quick transit arrival decisions <!-- role: advice -->

Use a quantile dotplot with roughly 50 dots to show the predictive distribution of arrival times when users must decide when to leave for transit. Keep the display glanceable so users can reason using dot counts rather than area.

## Why quantile dotplots with ~50 dots improve transit decisions <!-- role: reason -->

A frequency-based display turns probability reasoning into counting discrete outcomes, which supports more consistent choices in time-pressured decisions. With sufficient but not overwhelming dot density, users can perceive uncertainty shape while still making interval judgments from counts.

**Mechanism:** Discrete outcomes encourage probability judgments via counting, which reduces reliance on harder area-based estimation and supports more stable decision strategies over repeated use.

**Evidence:** In an incentivized bus-catching experiment, decisions using 50-outcome quantile dotplots achieved expected payoffs about 97% of optimal and were about 5 percentage points higher than a no-uncertainty control, with lower within-subject variability (around 4 percentage points less standard deviation than control) [@fernandesUncertaintyDisplaysUsing2018].

**Notes:** Performance improved over repeated trials, indicating users can learn and calibrate their strategy with feedback.

## When quantile dotplots with ~50 dots apply <!-- role: context -->

- **User Goal:** Decide when to arrive at a stop to maximize benefit (less waiting) while avoiding missing the vehicle.
- **Task:** Make a time choice under probabilistic arrival uncertainty with asymmetric costs (waiting vs missing).
- **Data:** Predictive distribution over arrival times (unimodal, bounded horizon); uncertainty is decision-relevant.
- **Chart Setting:** Mobile or space-constrained interface; glanceable, fast interpretation; repeated use with feedback.
- **Audience:** General public / non-experts interpreting everyday predictions.
- **Success Criterion:** Higher expected utility (near-optimal choices) and reduced variance across users and trials.

## When not to use quantile dotplots with ~50 dots <!-- role: exceptions -->

**Break it when:** Users only need a single fixed probability threshold that never changes across contexts. **Why:** The extra expressiveness of a full distribution may not add decision value relative to a threshold-only communication.

## Tradeoffs and risks of quantile dotplots with ~50 dots <!-- role: costs -->

**Sacrifice:** More visual complexity and screen space than a single point estimate or a single textual interval. **Risk:** If implemented too densely or too small, dots may become hard to distinguish, undermining the counting advantage. **Mitigation:** Maintain dot legibility and avoid compressing the dot field below a glanceable size.

## Common mistakes with quantile dotplots for transit uncertainty <!-- role: mistakes -->

- **Mistake:** Rendering dots so small or crowded that users cannot reliably count or compare them. **Why it fails:** The display stops functioning as a frequency representation and loses the consistency benefits.
- **Mistake:** Treating the dotplot as decorative while users still rely on the point estimate alone. **Why it fails:** The decision benefit comes from incorporating the distribution, not just showing it.

## Quick tests for whether the dotplot is working <!-- role: check -->

**Failure Sign:** Users make highly variable choices across similar predictions or behave like they only saw a point estimate. **Quick Check:** Ask a few users to estimate a “chance of catching the bus if I arrive in X minutes” from the dotplot and see if they use dot counting. **Stronger Test:** Run a small repeated-trial pilot with feedback and compare expected/optimal payoff and variance versus a point-estimate control.

## What to do instead if quantile dotplots are not feasible <!-- role: fix -->

- Use a complementary cumulative distribution function (CCDF) plot to support “chance I still catch it if I arrive at time X” reasoning.
- Reduce dot density (for example, fewer dots) only if it preserves dot separability on the target screen.
- If only a single risk threshold is truly needed, communicate one probability interval explicitly rather than a full distribution.
- Provide outcome feedback over time so users can calibrate decisions when introducing any uncertainty display.
