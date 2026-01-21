---
id: show-both-normative-and-biased-benchmarks
title: Show Normative and Biased Reference Values Side by Side
bibliography: references.bib
description: Include explicit benchmarks for unbiased and fully biased predictions
  when presenting curse-of-knowledge effects.
labels:
- chart:reference-line
- task:benchmark
- visual:position
- impact:interpretability
- data:categorical
- audience:expert
- domain:behavioral-economics
---

## The Rule <!-- role: advice -->

When visualizing curse-of-knowledge outcomes, plot both the unbiased benchmark and the “pure bias” benchmark as explicit reference values.

## The Logic <!-- role: reason -->

The paper operationalizes bias as judgments lying between two anchors: the no-bias prediction (w=0) and pure-bias prediction (w=1). Without both anchors visible, viewers cannot interpret magnitude or direction of bias.

- **The Principle:** Bias as a convex combination between E(X|I0) and E(X|I1)
- **The Evidence:** [@camererCurseKnowledgeEconomic1989]

## Where to Apply <!-- role: context -->

- **User Goal:** Assessing bias magnitude, testing whether outcomes converge to unbiased vs. biased levels
- **Data Type:** Forecasts, prices, or estimates that should fall between two theoretically defined endpoints
- **Audience:** Researchers comparing behavior to normative models

## When to Break It <!-- role: exceptions -->

- **Scenario:** Only one benchmark is theoretically meaningful (e.g., no defined “pure bias” endpoint).
- **Reason:** Forcing a second benchmark can mislead by implying a theoretical bound that does not exist.

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional visual elements (lines/labels) consume space.
- **The Risk:** Too many reference lines can compete with the main data marks.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing only the observed outcome and calling it “biased” without showing where unbiased would be.
- **Why it fails:** The viewer cannot tell whether the outcome is slightly or substantially biased, which is central to the paper’s conclusions [@camererCurseKnowledgeEconomic1989].

## How to Check <!-- role: check -->

- **Visual Sign:** A reader cannot compute “how far between” unbiased and pure-bias the observed value is.
- **The Test:** Remove the data marks mentally—if you can’t still point to two anchors that define the bias interval, the chart fails.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add two labeled horizontal (or vertical) reference lines: “No bias (w=0)” and “Pure bias (w=1)”.
- **Best Fix:** Add both reference lines and directly label the observed mark with its position “between” them (e.g., as a percentage or index).
