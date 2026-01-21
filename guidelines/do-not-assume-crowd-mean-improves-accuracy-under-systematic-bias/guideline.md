---
id: do-not-assume-crowd-mean-improves-accuracy-under-systematic-bias
title: Do Not Assume the Crowd Mean Improves Accuracy Under Systematic Bias
bibliography: references.bib
description: Collective summaries may fail to improve accuracy when individual perceptual
  errors are systematically biased.
labels:
- chart:general
- task:aggregate
- visual:annotation
- impact:accuracy
- data:quantitative
- audience:general
- social:collective-intelligence
---

## The Rule <!-- role: advice -->

Do not assume that showing the aggregate of prior viewers’ answers (e.g., mean-centered histogram) will be more accurate than an individual’s judgment.

## The Logic <!-- role: reason -->

Averaging cancels error only when errors are not systematically aligned. Hullman et al. found cases where showing an “unbiased” social histogram (based on the control mean) did not significantly improve accuracy over no-social control, consistent with systematic biases in perception that can persist at the group level [@hullmanImpactSocialInformation2011].

- **The Principle:** Systematic bias undermines averaging benefits
- **The Evidence:** [@hullmanImpactSocialInformation2011]

## Where to Apply <!-- role: context -->

- **User Goal:** Accurate numeric reading/estimation from a visualization.
- **Data Type:** Perceptual tasks known to have consistent directional errors (e.g., proportion judgment; correlation estimation is also error-prone in the study).
- **Audience:** Any users relying on social summaries as “grounding” or “calibration” in collaborative visualization tools.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You have evidence that the task’s errors are unbiased (or you have corrected them) for your specific user population and chart design.
- **Reason:** The failure mode depends on systematic bias; if bias is removed, aggregation may help, but that condition is not established by this paper [@hullmanImpactSocialInformation2011].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose a simple, compelling social feature (“here’s what others answered”) that feels like collective intelligence.
- **The Risk:** Over-correcting by removing all aggregation might reduce useful coordination signals even when they would be harmless in some contexts [@hullmanImpactSocialInformation2011].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating “mean of prior answers” as a quality guarantee.
- **Why it fails:** The paper shows that even an aggregate derived from many responses can still be systematically wrong and not reliably better than individual judgment [@hullmanImpactSocialInformation2011].

## How to Check <!-- role: check -->

- **Visual Sign:** The crowd summary repeatedly differs from the true value in the same direction across many items.
- **The Test:** Track signed error of the crowd aggregate vs. truth across multiple charts; persistent sign indicates systematic bias [@hullmanImpactSocialInformation2011].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Avoid presenting the aggregate as “correct”; label it as “previous responses” rather than an implied answer key.
- **Best Fix:** Validate whether your specific task/chart exhibits systematic bias before using crowd aggregates as accuracy aids, and evaluate with a no-social baseline as Hullman et al. did [@hullmanImpactSocialInformation2011].
