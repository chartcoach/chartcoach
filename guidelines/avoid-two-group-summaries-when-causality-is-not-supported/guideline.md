---
id: avoid-two-group-summaries-when-causality-is-not-supported
title: Avoid Two-Group Summaries When Causality Is Not Supported
bibliography: references.bib
description: Do not collapse a continuous predictor into two groups when you want
  to prevent a treatment-control causal reading.
labels:
- chart:bar
- chart:text
- task:interpret
- impact:clarity
- data:bivariate
- custom:aggregation-2
- risk:causality
---

## The Rule <!-- role: advice -->

Do not summarize a relationship by splitting X into two groups and comparing two averages (whether as two bars or as text) if the data is observational and you want to avoid causal inference.

## The Logic <!-- role: reason -->

- **The Principle:** Binary grouping encourages viewers to reason in “condition A vs condition B” terms, which supports causal stories.
- **The Evidence:** In Experiment 1, the two-group text description (written to parallel the two-bar summary) and the bar chart elicited higher causality agreement than scatterplots/line charts; the authors also flag two-bar bar graphs as a “special case” that consistently invited strong causal interpretations [@xiongIllusionCausalityVisualized2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Communicate association without implying that changing X will change Y.
- **Data Type:** Continuous/ordinal X where a two-bin split is an arbitrary summarization choice.
- **Audience:** Broad audiences who may interpret grouped comparisons as experimental contrasts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The study design truly is a two-condition comparison (and you intend that interpretation).
- **Reason:** The caution is about *unwarranted* causality; if the underlying design supports it, a two-group summary may be appropriate [@xiongIllusionCausalityVisualized2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** A clean, simple “before/after” or “low/high” summary.
- **The Risk:** More granular displays may reduce perceived decisiveness of the message.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Rewriting the two-group summary as prose (text) instead of showing the full data, assuming text will be “less misleading.”
- **Why it fails:** Text descriptions that mirror the two-group summary also produced high causality agreement in Experiment 1 [@xiongIllusionCausalityVisualized2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Only two summarized values are shown for X (two bars, or “less than/greater than” thresholds in text).
- **The Test:** Ask: “Did we create exactly two X categories from a richer scale?” If yes, you are using the two-group pattern associated with higher causal impressions [@xiongIllusionCausalityVisualized2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the two-group summary with more bins (e.g., 8 or 16) rather than 2.
- **Best Fix:** Show unaggregated data (e.g., scatterplot with individual points) to reduce the binary-comparison cue [@xiongIllusionCausalityVisualized2020].
