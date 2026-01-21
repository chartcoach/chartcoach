---
id: assume-perceptual-pull-occurs-across-lines-and-bars
title: "Assume Any Nearby Series Will Pull a Target Series\u2019 Average"
bibliography: references.bib
description: Perceptual pull affects average position estimates even when the other
  series is a different mark type (line vs bar).
labels:
- chart:line
- chart:bar
- task:average
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- bias:perceptual-pull
---

## The Rule <!-- role: advice -->

Do not assume that using different mark types (line vs bar) prevents cross-series bias in average position estimates.

## The Logic <!-- role: reason -->

Perceptual pull is not limited to same-type pairings. A line can pull bar average estimates and bars can pull line average estimates, and the paper finds the strength of pull does not depend on whether the non-target series is the same type or a different type.

- **The Principle:** Cross-type contextual attraction in positional averaging
- **The Evidence:** In Experiment 3 (line+bar displays) and combined analyses, the non-target series type did not significantly change the target’s estimation error relative to same-type pairings [@xiongBiasedAveragePosition2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Accurately estimate each series’ average level in a composite chart (e.g., bar+line combo charts).
- **Data Type:** Quantitative multi-series charts where series are vertically separated within the same frame.
- **Audience:** Any; the evidence suggests a general effect across mark types.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not asking for average judgments (e.g., using the combo chart for illustrating co-movement qualitatively).
- **Reason:** The paper’s demonstrated bias is specific to average position estimates across a short delay.

## The Price <!-- role: costs -->

- **The Sacrifice:** Avoiding combo charts may reduce compactness and layered storytelling.
- **The Risk:** Separate views can make integrated comparison less immediate.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a bar+line combo and assuming the different shapes “separate perception,” so averages stay accurate.
- **Why it fails:** Perceptual pull generalized across lines and bars; different mark types did not eliminate the effect [@xiongBiasedAveragePosition2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ average estimates for the target series shift when you add/remove the other series (even if it’s a different mark type).
- **The Test:** Hold the target series constant; A/B test with vs without the other series and measure the change in signed estimation error [@xiongBiasedAveragePosition2020a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove the secondary series from the same frame when the task is average estimation [@xiongBiasedAveragePosition2020a].
- **Best Fix:** Use separate panels for each series (or otherwise isolate series) and validate via an average-estimation task test similar to the paper’s method [@xiongBiasedAveragePosition2020a].
