---
id: use-scatterplots-to-reduce-unwarranted-causal-inference
title: Use Scatterplots to Reduce Unwarranted Causal Inference
bibliography: references.bib
description: Prefer scatterplots over text or bar charts when you want viewers to
  see an association without inferring causation.
labels:
- chart:scatter
- chart:bar
- chart:text
- task:interpret
- impact:clarity
- data:bivariate
- audience:novice
- risk:causality
---

## The Rule <!-- role: advice -->

When showing correlational observational data, use a scatterplot (showing individual points) instead of text descriptions or bar charts if you want to minimize viewers’ causal interpretations.

## The Logic <!-- role: reason -->

- **The Principle:** Visual form can cue different reasoning routines; some forms trigger stronger causal stories than others.
- **The Evidence:** In Experiment 1, participants agreed with causal interpretations more for bar charts and text than for scatterplots (and line graphs), even though the underlying relationship was the same [@xiongIllusionCausalityVisualized2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Understand “these variables co-vary” without concluding “X causes Y.”
- **Data Type:** Two-variable observed data (no randomized intervention shown).
- **Audience:** General-public or mixed-expertise readers prone to conflating correlation and causation.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your analysis goal is explicitly to encourage causal interpretation (e.g., communicating an intended causal claim).
- **Reason:** This rule is specifically for mitigating *unwarranted* causality impressions; using scatterplots may weaken the causal reading you intend [@xiongIllusionCausalityVisualized2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less immediate “summary” readability than highly aggregated displays.
- **The Risk:** With many points, viewers may have more difficulty extracting a simple takeaway than from an aggregated chart.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to a line chart while keeping the same aggregated structure and expecting causality impressions to disappear.
- **Why it fails:** The paper shows that both aggregation and encoding affect perceived causality; changing only one aspect may not reduce causal impressions as much as showing less-aggregated point-level data [@xiongIllusionCausalityVisualized2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can easily restate your message as “if we increase X, Y will increase.”
- **The Test:** Ask a colleague to paraphrase the chart’s message; if they spontaneously use counterfactual/causal phrasing, your design is likely cueing causality.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace a two-group bar chart/text summary with a scatterplot showing the underlying individual observations.
- **Best Fix:** Reduce aggregation and use point marks to present the relationship more as “data cloud/trend” than as “treatment vs control” comparison [@xiongIllusionCausalityVisualized2020].
