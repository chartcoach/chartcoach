---
id: avoid-within-the-bar-bias-from-mean-bars
title: Avoid Mean-Only Bar Charts That Trigger Within-the-Bar Bias
bibliography: references.bib
description: Do not use bars to depict means when that framing implies values inside
  the bar are more likely than values outside it.
labels:
- chart:bar
- task:infer
- visual:length
- impact:accuracy
- data:distribution
- audience:general
- source:szafir-2018
---

## The Rule <!-- role: advice -->

Do not use bar charts of means as your primary display for comparing sample populations; use a distribution-revealing alternative.

## The Logic <!-- role: reason -->

Bars depicting averages can cause viewers to treat values within the bar as more likely than values outside it (“within-the-bar bias”), leading to incorrect inferences about uncertainty and typicality, as explained in [@szafirGoodBadBiased2018].

- **The Principle:** Within-the-bar bias from bar-as-range interpretation
- **The Evidence:** [@szafirGoodBadBiased2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare groups while understanding variability/uncertainty
- **Data Type:** Sampled measurements per condition (experimental results, benchmark runtimes)
- **Audience:** Broad audiences and decision-makers who may over-interpret bars

## When to Break It <!-- role: exceptions -->

- **Scenario:** The bar truly represents a bounded quantity (a real range from zero to a maximum) rather than a mean of samples
- **Reason:** The bias described arises when the bar is used to depict an average and invites misreading about likelihood, per [@szafirGoodBadBiased2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Familiarity and quick simplicity of mean bars
- **The Risk:** Distribution plots may be harder to explain in some settings

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping mean bars and adding error bars
- **Why it fails:** The paper cautions that this common approach still leads to biased interpretation and hides distribution shape in [@szafirGoodBadBiased2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers talk as if the bar spans likely values (treating the filled rectangle as a probability mass)
- **The Test:** Ask a viewer what values are “most likely”—if they point to the interior of the bar as a range rather than understanding it as a mean, the bias is present as described in [@szafirGoodBadBiased2018]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace mean bars with a distribution-oriented summary that shows shape around the mean
- **Best Fix:** Use a violin plot (highlighted in the paper) to show the distribution alongside the mean, exposing skew/bimodality and reducing within-the-bar bias, per [@szafirGoodBadBiased2018]
