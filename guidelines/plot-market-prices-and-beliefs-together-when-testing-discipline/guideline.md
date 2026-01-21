---
id: plot-market-prices-and-beliefs-together-when-testing-discipline
title: Plot Market Prices and Belief Judgments Together
bibliography: references.bib
description: "Overlay or co-display transaction prices with participants\u2019 judgments\
  \ to evaluate whether markets track biased beliefs."
labels:
- chart:overlay
- task:compare
- visual:position
- impact:diagnosis
- data:temporal
- audience:expert
- domain:experimental-markets
---

## The Rule <!-- role: advice -->

When evaluating bias in experimental markets, display market prices alongside participants’ belief estimates on the same scale.

## The Logic <!-- role: reason -->

The paper finds prices are “close together” with judgments and converge between unbiased and pure-bias benchmarks; co-display is necessary to see whether market outcomes mirror biased beliefs or diverge from them.

- **The Principle:** Joint interpretation of market outcomes and underlying beliefs
- **The Evidence:** [@camererCurseKnowledgeEconomic1989]

## Where to Apply <!-- role: context -->

- **User Goal:** Assess whether markets reduce bias relative to individual judgment, or whether prices reflect biased expectations
- **Data Type:** Market time series (trade prices) plus elicited belief judgments
- **Audience:** Experimental economists, market microstructure researchers

## When to Break It <!-- role: exceptions -->

- **Scenario:** Prices and beliefs are in different units or not directly comparable.
- **Reason:** Overlay implies commensurability; a shared axis would mislead.

## The Price <!-- role: costs -->

- **The Sacrifice:** More visual complexity (multiple mark types).
- **The Risk:** Overplotting can obscure either series if not styled carefully.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing only prices and inferring beliefs from them (or only beliefs and inferring market discipline).
- **Why it fails:** The paper’s key claim is about the relationship between belief bias and market outcomes; separating them hides that relationship [@camererCurseKnowledgeEconomic1989].

## How to Check <!-- role: check -->

- **Visual Sign:** You cannot tell whether prices are tracking beliefs, moving away from them, or converging differently across periods.
- **The Test:** Ask: “Are prices closer to beliefs or to the unbiased benchmark?” If the chart can’t answer, it fails.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add belief point estimates as distinct symbols (e.g., arrowheads) on the same axis as mean prices.
- **Best Fix:** Add uncertainty around beliefs (e.g., standard error bars) and show period-separated price summaries (A vs. B) to reveal movement.
