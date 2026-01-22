---
id: do-not-rely-on-formula-based-rules-training-alone-to-improve-uncertainty-reasoning
title: Do Not Rely on Formula-Based Rules Training Alone to Improve Uncertainty Recall
  or Transfer
bibliography: references.bib
description: Explicit rule training on sampling distributions did not improve recall
  or transfer compared to baseline in the evaluated tasks.
labels:
- chart:distribution
- task:learn
- visual:annotation
- impact:comprehension
- data:uncertainty
- audience:novice
- training:rules
---

## Avoid adding formula-only training as your main method for uncertainty comprehension <!-- role: advice -->

Do not assume that presenting formulas and a calculation exercise about sampling distributions will improve users’ recall of the shown uncertainty or their ability to estimate uncertainty for a new study. If you add instruction, treat it as supplementary to interactive methods rather than the primary intervention.

## Procedural calculation practice may not translate to distribution reasoning <!-- role: reason -->

A short rules-based exercise can focus attention on computation steps without creating a robust mental model of what the distribution means or how it should look. Without strong conceptual grounding, users may not improve on recall or transfer tasks that require constructing or reasoning about distributions.

**Mechanism:** Rule training can encourage shallow procedural processing that does not generalize to visual judgment and prediction tasks about replication uncertainty.

**Evidence:** In the controlled study, explicit rule training about sampling distributions did not produce reliable improvements in graphical recall or in a graphical transfer task compared to baseline conditions [@hullmanImaginingReplicationsGraphical2018].

**Notes:** The study suggests that interactive prediction can improve transfer even when rule training does not.

## When this warning applies <!-- role: context -->

- **User Goal:** Understand what reported uncertainty implies for replications.
- **Task:** Recall a sampling distribution later or estimate replication uncertainty for a new study.
- **Data:** Experiment summary statistics used to communicate uncertainty.
- **Chart Setting:** Educational explainers embedded in reports or interfaces that add “how to compute it” panels.
- **Audience:** Novices who may complete the steps without internalizing meaning.
- **Success Criterion:** Better distribution recall or better transfer estimates after the intervention.

## When rule training might still be acceptable <!-- role: exceptions -->

**Break it when:** The goal is explicitly to teach computation of sampling distribution quantities rather than to improve recall or transfer judgments. **Why:** The evaluated outcomes were distribution recall and transfer estimation, not procedural calculation accuracy.

## Costs of deprioritizing rules training <!-- role: costs -->

**Sacrifice:** Some users may want a formula explanation for transparency. **Risk:** Removing computation detail can reduce perceived rigor for some audiences. **Mitigation:** Provide optional expandable rule explanations while keeping the main flow focused on interactive uncertainty reasoning.

## Common missteps with instructional add-ons <!-- role: mistakes -->

**Mistake:** Adding a formula box and a single calculation exercise and expecting improved uncertainty reasoning. **Why it fails:** The evaluated rule-training approach did not reliably improve recall or transfer outcomes [@hullmanImaginingReplicationsGraphical2018].

## Quick checks to validate your instructional approach <!-- role: check -->

**Failure Sign:** Users complete the training but still misestimate or poorly reconstruct the uncertainty distribution. **Quick Check:** Compare recall/transfer performance between users who did and did not complete the rules module. **Stronger Test:** A/B test rule training versus prediction-based elicitation on the same uncertainty tasks.

## Better alternatives to formula-only instruction <!-- role: fix -->

- Add a prediction-then-reveal interaction so users confront the mismatch between expectation and displayed uncertainty.
- Use short, task-aligned prompts that ask users to interpret replication outcomes rather than compute parameters.
- Provide optional rule training only after users have interacted with a distribution and attempted an estimate.
- If instruction is required, incorporate multiple practice-and-feedback cycles rather than a single computation step.
