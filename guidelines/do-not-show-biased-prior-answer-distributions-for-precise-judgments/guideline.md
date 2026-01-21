---
id: do-not-show-biased-prior-answer-distributions-for-precise-judgments
title: Do Not Show Biased Prior-Answer Distributions for Precise Judgments
bibliography: references.bib
description: If the social signal is biased away from the true value, it increases
  visual judgment error.
labels:
- chart:bar
- chart:stacked-bar
- chart:bubble
- task:estimate
- visual:annotation
- impact:accuracy
- data:quantitative
- audience:general
- social:proof
---

## The Rule <!-- role: advice -->

Do not display a “previous answers” distribution (e.g., histogram of prior estimates) if it may be biased away from the true value for the task.

## The Logic <!-- role: reason -->

When the social signal is shifted away from the correct answer, viewers’ estimates move toward that signal, increasing error. In proportion-judgment tasks, Hullman et al. showed significantly higher error when the displayed histogram was biased (their “Target 1SD” condition) compared to both unbiased and control conditions [@hullmanImpactSocialInformation2011].

- **The Principle:** Social proof can amplify error when the crowd signal is wrong
- **The Evidence:** [@hullmanImpactSocialInformation2011]

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating a numeric value from a chart (e.g., “what percent is A of B?”).
- **Data Type:** Charts with an objectively correct answer (ground truth), including classic graphical perception tasks.
- **Audience:** Novices and experts alike in social visualization sites that attach aggregated prior responses to visualizations.

## When to Break It <!-- role: exceptions -->

- **Scenario:** No ground truth exists (pure opinion elicitation), and the goal is to surface community sentiment rather than correctness.
- **Reason:** The paper’s accuracy claim depends on bias relative to a true value; without ground truth, “biased vs. unbiased” cannot be evaluated the same way [@hullmanImpactSocialInformation2011].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less social context and less sense of “what others saw.”
- **The Risk:** If you hide social signals, you may reduce engagement or collaborative navigation cues that social systems often rely on [@hullmanImpactSocialInformation2011].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing a histogram generated from early, low-quality, or systematically biased judgments and assuming “more data later will fix it.”
- **Why it fails:** The study provides evidence that biased social information increases error; waiting does not guarantee the displayed signal is trustworthy at any given moment [@hullmanImpactSocialInformation2011].

## How to Check <!-- role: check -->

- **Visual Sign:** Estimates drift in the direction of the shown social distribution even when it contradicts the chart.
- **The Test:** Compare error vs. a control (no-social) baseline; if error increases when the social distribution is shown, treat it as harmful bias [@hullmanImpactSocialInformation2011].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Suppress the prior-answer histogram for tasks requiring accuracy.
- **Best Fix:** Only display social-response summaries when you can ensure they are not misleading for the current task (e.g., via validation or calibration) and continuously monitor accuracy impact [@hullmanImpactSocialInformation2011].
