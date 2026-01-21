---
id: use-bar-encodings-over-dots-or-lines-to-dampen-causal-impressions-when-aggregation-is-held-constant
title: Use Bar Encodings (Not Dots/Lines) to Dampen Causal Impressions When Aggregation
  Is Fixed
bibliography: references.bib
description: When you cannot change aggregation, bar marks may elicit slightly weaker
  causal interpretations than line or dot marks.
labels:
- chart:bar
- chart:line
- chart:scatter
- visual:mark
- task:interpret
- impact:clarity
- data:bivariate
- risk:causality
---

## The Rule <!-- role: advice -->

If aggregation level must stay the same, prefer bar marks over line or dot marks to slightly reduce perceived causality.

## The Logic <!-- role: reason -->

- **The Principle:** Mark/encoding choice changes how strongly viewers perceive a relationship as a coherent causal link.
- **The Evidence:** In Experiment 2 (with aggregation controlled), bars had the lowest average causation ratings among bars/lines/dots; in Experiment 3 (non-aggregated adapted displays), bar encodings again had the lowest causation ratings, with dots highest and lines in between [@xiongIllusionCausalityVisualized2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Communicate an association while reducing causal overreach, but you cannot redesign the data pipeline (e.g., must show binned summaries).
- **Data Type:** Binned/aggregated summaries where you must choose a mark type.
- **Audience:** Mixed audiences making fast inferences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are using a two-bar bar chart.
- **Reason:** The paper identifies two-bar bar graphs as a special case that can strongly invite causal interpretations, potentially undermining this guideline [@xiongIllusionCausalityVisualized2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may reduce perceived “connectedness” or trend readability compared to lines/dots.
- **The Risk:** Viewers may find it harder to see the overall trend, which can reduce both correlation and causation impressions.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to dots assuming “dots always mean raw data, so people won’t infer causality.”
- **Why it fails:** Across experiments, dot encodings tended to produce higher causality ratings than bars when other factors were held constant [@xiongIllusionCausalityVisualized2020].

## How to Check <!-- role: check -->

- **Visual Sign:** The same binned values could be drawn as bars, a connected line, or points; you chose line/points by default.
- **The Test:** Re-encode the same summarized data with bars and compare whether the display feels less like a deterministic functional relationship.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace dot/line marks with bars without changing binning.
- **Best Fix:** Change both: reduce aggregation and choose encodings that do not heighten causal reading, consistent with the paper’s aggregation findings [@xiongIllusionCausalityVisualized2020].
