---
id: choose-pull-up-handle-interfaces-for-novice-distribution-sketching
title: Use Pull-Up Handles to Let Novices Sketch Distributions
bibliography: references.bib
description: Prefer pull-up handle interactions for distribution sketching because
  they balance speed, satisfaction, and accuracy for novices.
labels:
- chart:distribution
- task:elicit
- visual:interaction
- impact:usability
- data:uncertainty
- audience:novice
- custom:interface-design
---

## The Rule <!-- role: advice -->

For interactive distribution elicitation, use a pull-up-handles interaction (drag handles upward to allocate probability mass), for both continuous and discrete variants.

## The Logic <!-- role: reason -->

A handle-based “pull-up” interaction reduces training burden (direct manipulation) while remaining expressive; in the paper’s interface evaluation it performed competitively on accuracy and was preferred (especially in continuous form).

- **The Principle:** Direct manipulation supports learnability and efficient elicitation
- **The Evidence:** The authors’ interface study found continuous interfaces were generally preferred and faster, and the discrete pull-up interface performed among the best discrete options; they selected pull-up designs for the main experiment to minimize differences beyond discrete vs continuous [@hullmanImaginingReplicationsGraphical2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Drawing/eliciting a subjective probability distribution (e.g., expected replication outcomes).
- **Data Type:** Univariate distributions over a numeric effect-size axis.
- **Audience:** Novices with little statistical training.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need very fine-grained, high-resolution elicitation and users can tolerate longer interaction.
- **Reason:** The paper shows more outcomes can increase time without reliably improving accuracy; high-resolution elicitation may require different workflows than quick sketching [@hullmanImaginingReplicationsGraphical2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Handle count constrains expressiveness (users can only shape the curve at a limited number of x-positions).
- **The Risk:** Users may create artifacts (e.g., overly angular shapes) if smoothing or interpolation is not handled well.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using click-heavy interfaces (e.g., increment/decrement buttons per bin) for novices.
- **Why it fails:** More clicking increases time and frustration; the authors avoided higher-click designs after early feedback and observed time costs with higher outcome counts [@hullmanImaginingReplicationsGraphical2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users take unusually long or abandon shaping, leaving near-default distributions.
- **The Test:** Track interaction time and the number of adjustments; if time is high with low shape change, the interaction is too effortful.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of handles/bins for the initial sketching step.
- **Best Fix:** Use pull-up handles with sensible smoothing (for continuous) and a clear fixed “budget” of outcomes (for discrete) to keep interaction lightweight and interpretable, as implemented in the paper’s chosen interfaces [@hullmanImaginingReplicationsGraphical2018].
