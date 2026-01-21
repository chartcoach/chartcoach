---
id: preserve-base-rates-in-risk-graphics
title: Make Base Rates Visually Co-Salient with Highlighted Outcomes
bibliography: references.bib
description: Ensure the denominator/base rate is as perceptually available as the
  highlighted cases to prevent foreground bias.
labels:
- chart:icon-array
- task:risk-judge
- visual:foreground
- impact:accuracy
- data:proportion
- audience:novice
- bias:foreground
- mechanism:type-1
---

## The Rule <!-- role: advice -->

Visually encode the base rate (denominator) with the same perceptual prominence as the highlighted outcome count.

## The Logic <!-- role: reason -->

The review describes a foreground effect: viewers attend to salient foreground elements (e.g., a small set of icons) and ignore less-salient background context (e.g., a large base rate shown in text), producing distorted risk judgments and willingness-to-pay decisions [@padillaDecisionMakingVisualizations2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Evaluate how big a risk reduction is, or compare risks between options
- **Data Type:** Risks, rates, frequencies, “N out of M” comparisons
- **Audience:** Public-facing risk communication, consumer or patient decisions

## When to Break It <!-- role: exceptions -->

- **Scenario:** You deliberately want focus on absolute case counts and the base rate is irrelevant to the decision
- **Reason:** If the decision truly depends only on counts (not rates), emphasizing the denominator may distract [@padillaDecisionMakingVisualizations2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** More visual space and denser displays
- **The Risk:** Overloading the display can slow reading for quick decisions [@padillaDecisionMakingVisualizations2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Putting the denominator in a caption or small text next to the graphic
- **Why it fails:** Text-only base rates are easy to miss when icons dominate attention [@padillaDecisionMakingVisualizations2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers describe differences as “twice as many icons” rather than as a rate difference.
- **The Test:** Ask users to estimate the absolute difference in risk; if they ignore the denominator, base-rate salience is too low [@padillaDecisionMakingVisualizations2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase prominence of the base rate (placement, size, and integration with the mark set).
- **Best Fix:** Represent both numerator and denominator visually (so the base rate is not only textual) [@padillaDecisionMakingVisualizations2018].
