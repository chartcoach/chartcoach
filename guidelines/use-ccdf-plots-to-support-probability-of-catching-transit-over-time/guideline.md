---
id: use-ccdf-plots-to-support-probability-of-catching-transit-over-time
title: Use a complementary CDF plot when users ask 'what is the chance I still catch
  it if I arrive at time X?'
bibliography: references.bib
description: Complementary cumulative distribution plots support near-best decision
  quality for bus-catching by aligning the graphic with the 'chance of still catching'
  question.
labels:
- chart:cdf
- task:estimate
- visual:position
- impact:decision-quality
- data:uncertainty
- audience:novice
- domain:transit
- complexity:intermediate
---

## Use a complementary CDF plot when users ask "chance I still catch it if I arrive at time X?" <!-- role: advice -->

Use a complementary cumulative distribution function (CCDF) plot to show the probability of arrival at or after each time when the decision is when to show up. Present it so users can read “probability of still catching the bus” directly as time increases.

## Why CCDFs map well to catch-or-miss decisions <!-- role: reason -->

A CCDF directly encodes a one-sided probability (“arrives later than my chosen arrival time”), which matches the mental question in a bus-catching decision and avoids needing users to integrate areas. This alignment supports learning and consistent strategy use across repeated decisions.

**Mechanism:** By matching the decision query to a directly readable probability curve, users can evaluate the tradeoff between waiting longer (less waiting time) and risking a miss (lower CCDF value).

**Evidence:** In an incentivized repeated-trial bus-catching experiment, CCDF plots performed nearly as well as the best condition (quantile dotplots with 50 outcomes) and outperformed a no-uncertainty control and several other uncertainty displays in decision quality and/or consistency after learning over trials [@fernandesUncertaintyDisplaysUsing2018].

**Notes:** The CCDF was selected over a standard CDF during iterative design because it better corresponds to the “still catch it if I delay” question.

## When CCDF plots apply <!-- role: context -->

- **User Goal:** Choose a departure/arrival time that balances waiting cost against missing risk.
- **Task:** Read a one-sided probability for a proposed time and adjust the time to fit scenario payoffs.
- **Data:** Predictive distribution over arrival times; uncertainty is consequential; single-vehicle catch-or-miss outcome.
- **Chart Setting:** Mobile/glanceable display where direct probability reading is preferred over area estimation.
- **Audience:** Non-expert public making quick decisions.
- **Success Criterion:** Near-optimal expected payoff and reduced decision variance over repeated use.

## When not to use CCDF plots <!-- role: exceptions -->

**Break it when:** Users must reason about central tendency (like an expected arrival time) as the primary task rather than catch-or-miss probability at a threshold time. **Why:** The CCDF emphasizes tail probability over mean-focused judgments.

## Tradeoffs and risks of CCDF plots <!-- role: costs -->

**Sacrifice:** Less immediate depiction of distribution “shape” than dot-based density metaphors for some users. **Risk:** Users unfamiliar with cumulative curves may misread slope or treat it as a trajectory rather than probability. **Mitigation:** Use labeling that explicitly frames the vertical axis as “chance you still catch it.”

## Common mistakes with CCDF plots <!-- role: mistakes -->

- **Mistake:** Using a standard CDF when the question is about arriving later than a chosen time. **Why it fails:** It forces users to mentally invert the probability to answer the catch-or-miss question.
- **Mistake:** Omitting clear probability labeling, leaving the curve’s meaning implicit. **Why it fails:** Users may not map the curve to a one-sided chance at a time threshold.

## Quick tests for whether the CCDF is working <!-- role: check -->

**Failure Sign:** Users cannot answer “what chance do I still have if I arrive in X minutes?” without confusion or inversion errors. **Quick Check:** Give a few example times and ask users to read the “still catch it” chance from the plot. **Stronger Test:** Run a short repeated-decision pilot and compare expected/optimal payoff and variance versus a point-estimate control.

## What to do instead if CCDFs confuse users <!-- role: fix -->

- Use a quantile dotplot with about 50 dots to enable frequency-based reasoning by counting outcomes.
- Add explicit axis wording that frames the CCDF as “chance bus arrives after your arrival time.”
- Provide repeated outcome feedback so users can calibrate their reading and strategy over time.
- If the interface must be text-only, present a single one-sided probability statement matched to the decision (with awareness that fixed thresholds can be brittle).
