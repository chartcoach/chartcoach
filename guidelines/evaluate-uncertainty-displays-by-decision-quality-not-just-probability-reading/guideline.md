---
id: evaluate-uncertainty-displays-by-decision-quality-not-just-probability-reading
title: Evaluate Uncertainty Displays by Decision Quality Under Incentives
bibliography: references.bib
description: Assess uncertainty visualizations using incentivized decision tasks and
  expected/optimal payoff, not just probability-extraction accuracy.
labels:
- chart:method
- task:evaluate
- visual:uncertainty
- impact:decision-quality
- data:probabilistic
- audience:designer
- domain:transit
---

## The Rule <!-- role: advice -->

When comparing uncertainty displays, run an incentivized decision-making evaluation and score designs by expected payoff relative to optimal payoff.

## The Logic <!-- role: reason -->

Probability-reading accuracy does not guarantee better decisions. The paper demonstrates a decision-focused methodology: participants make repeated choices, receive outcome feedback, and decision quality is measured as expected payoff divided by optimal expected payoff, isolating choice quality from random outcome noise [@fernandesUncertaintyDisplaysUsing2018].

- **The Principle:** Measure what you actually care about (decision utility), not just intermediate comprehension.
- **The Evidence:** The study’s conclusions about dotplots/CDFs being best are based on expected/optimal payoff and its variance over time, not only on probability extraction [@fernandesUncertaintyDisplaysUsing2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Make choices under uncertainty where errors and precaution both have costs (e.g., waiting vs. missing).
- **Data Type:** Predictive distributions used for real-time operational decisions.
- **Audience:** Product/design/research teams selecting an uncertainty display.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your system has no meaningful utility tradeoffs or consequences (purely informational view).
- **Reason:** If there is no decision to optimize, payoff-based evaluation may be inappropriate or artificial [@fernandesUncertaintyDisplaysUsing2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** More complex study design than comprehension questions.
- **The Risk:** Utility functions may not match every user; the paper notes real-world utility varies by person and situation [@fernandesUncertaintyDisplaysUsing2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Evaluating displays only by asking users to read off probabilities or by subjective preference.
- **Why it fails:** Displays that are liked or legible for extraction may not yield the best decisions; the paper explicitly targets this gap [@fernandesUncertaintyDisplaysUsing2018].

## How to Check <!-- role: check -->

- **Visual Sign:** A display “tests well” on comprehension but produces inconsistent or suboptimal choices in realistic tasks.
- **The Test:** Compute expected payoff of chosen actions under the shown predictive distribution and compare it to the trial’s optimal expected payoff.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add outcome feedback and incentives to your study protocol; switch your primary metric to expected/optimal payoff.
- **Best Fix:** Use repeated trials with feedback and analyze both mean performance and variance over time, as done in the paper [@fernandesUncertaintyDisplaysUsing2018].
