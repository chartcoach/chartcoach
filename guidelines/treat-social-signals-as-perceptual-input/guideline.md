---
id: treat-social-signals-as-perceptual-input
title: Treat Social Signals as Perceptual Input
bibliography: references.bib
description: "Assume that showing prior viewers\u2019 responses will directly shift\
  \ later viewers\u2019 visual judgments."
labels:
- chart:general
- task:judge
- visual:annotation
- impact:accuracy
- data:quantitative
- audience:general
- social:influence
---

## The Rule <!-- role: advice -->

Assume that displaying other people’s prior responses (e.g., “what others answered”) will change users’ visual judgments, and design as if it is part of the visualization encoding.

## The Logic <!-- role: reason -->

Showing a distribution of prior answers acts as **social proof**: viewers incorporate others’ behavior into their own estimate, shifting their numeric judgment toward the shown responses. Hullman et al. found that adding a histogram of previous answers measurably changed accuracy in graphical perception tasks, demonstrating that the social layer is not neutral decoration but an influence on perception and estimation [@hullmanImpactSocialInformation2011].

- **The Principle:** Social proof / informational social influence
- **The Evidence:** [@hullmanImpactSocialInformation2011]

## Where to Apply <!-- role: context -->

- **User Goal:** Making a quantitative estimate from a chart (e.g., proportion judgment, strength of association).
- **Data Type:** Quantitative values where an error can be measured against a true value.
- **Audience:** Any audience in social visualization environments (e.g., ManyEyes-like systems) where prior judgments are visible.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally want social influence to steer users toward a consensus for coordination (not accuracy).
- **Reason:** The rule is about protecting perceptual accuracy; if your objective is alignment rather than correctness, influence may be acceptable [@hullmanImpactSocialInformation2011].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced “independent” interpretation; users’ judgments are no longer purely individual.
- **The Risk:** You may unintentionally amplify early errors or community biases by treating social features as harmless add-ons [@hullmanImpactSocialInformation2011].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding “most people answered…” widgets without treating them as part of the perceptual task.
- **Why it fails:** The paper shows these signals measurably shift judgments, so ignoring them in design and evaluation leads to hidden accuracy regressions [@hullmanImpactSocialInformation2011].

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ responses cluster around the displayed social distribution rather than around the true value.
- **The Test:** A/B test the same chart with vs. without the social-response display; compare absolute error distributions across conditions [@hullmanImpactSocialInformation2011].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove or hide prior-response summaries on tasks where accuracy is critical.
- **Best Fix:** Redesign the social layer as a controlled experimental factor (e.g., only show it when you can verify it is not misleading), and measure accuracy impacts explicitly [@hullmanImpactSocialInformation2011].
