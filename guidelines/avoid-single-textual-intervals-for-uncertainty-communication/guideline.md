---
id: avoid-single-textual-intervals-for-uncertainty-communication
title: Avoid Single Textual Probability Intervals as the Only Uncertainty Cue
bibliography: references.bib
description: Do not rely on one fixed textual probability threshold to communicate
  uncertainty; it can be highly sensitive to the chosen level and harm decisions.
labels:
- chart:text
- task:decide
- visual:text
- impact:decision-quality
- data:temporal
- audience:novice
- domain:transit
---

## The Rule <!-- role: advice -->

Do not communicate arrival uncertainty using only one textual one-sided predictive interval (e.g., “85% chance of arriving in X minutes or later”) as the primary decision aid.

## The Logic <!-- role: reason -->

A single fixed probability threshold is not flexible across varying costs of waiting vs. missing the bus. In the experiment, textual displays were highly sensitive to the probability level shown; one level (text85) performed poorly with little learning, while other levels (text60, text99) were closer to better visual displays—indicating instability as a design strategy [@fernandesUncertaintyDisplaysUsing2018].

- **The Principle:** Avoid under-expressive uncertainty summaries when optimal thresholds vary by context.
- **The Evidence:** Text conditions varied widely by interval; text85 resembled no-uncertainty performance while other text intervals did better [@fernandesUncertaintyDisplaysUsing2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Make repeated, utility-sensitive decisions (leave now vs. wait) where the “right” risk tolerance changes by scenario.
- **Data Type:** Predictive uncertainty where multiple probability cutoffs could be relevant.
- **Audience:** General public relying on a quick glance or short read.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You have strong domain justification that one probability level is always the policy-relevant decision threshold.
- **Reason:** If the decision is standardized to a single risk tolerance, the sensitivity problem is less relevant (the paper’s concern is varying optimality across situations) [@fernandesUncertaintyDisplaysUsing2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Text-only summaries are compact; replacing them with richer visuals costs space and some onboarding.
- **The Risk:** Richer displays may require slightly more initial learning, though learning effects were observed for better-performing visuals [@fernandesUncertaintyDisplaysUsing2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking a “reasonable-sounding” probability (like 85%) and assuming it generalizes.
- **Why it fails:** The study showed the 85% textual interval yielded poor decisions relative to other uncertainty displays and even other text thresholds [@fernandesUncertaintyDisplaysUsing2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ decisions do not improve over repeated exposure, or performance resembles point-estimate control.
- **The Test:** A/B test different textual thresholds; if outcomes swing materially by the chosen percentage, the design is too sensitive.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a richer uncertainty display (e.g., dotplot or CCDF) alongside text so users can adapt thresholds.
- **Best Fix:** Replace single-threshold text with a visualization that supports estimating many probability intervals (dotplot or CCDF) [@fernandesUncertaintyDisplaysUsing2018].
