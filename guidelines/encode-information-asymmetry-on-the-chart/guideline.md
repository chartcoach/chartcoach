---
id: encode-information-asymmetry-on-the-chart
title: Encode What Each Actor Knows
bibliography: references.bib
description: Explicitly show which information is available to which agents when visualizing
  forecasts or decisions under asymmetric information.
labels:
- chart:annotation
- task:compare
- visual:position
- impact:clarity
- data:categorical
- audience:expert
- domain:behavioral-economics
---

## The Rule <!-- role: advice -->

Explicitly encode each actor’s information set (e.g., I0 vs. I1) on the visualization, and keep them visually distinct.

## The Logic <!-- role: reason -->

When people know more than others, they systematically overestimate what the less-informed know (“curse of knowledge”), so readers will misinterpret whose expectations a value represents unless information sets are made explicit.

- **The Principle:** Curse of Knowledge as a violation of the law of iterated expectations
- **The Evidence:** [@camererCurseKnowledgeEconomic1989]

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding predictions about others’ beliefs, pricing under asymmetric information, or “forecasts of forecasts”
- **Data Type:** Comparisons involving informed vs. uninformed forecasts, beliefs, prices, or outcomes
- **Audience:** Analysts, economists, decision researchers, market designers

## When to Break It <!-- role: exceptions -->

- **Scenario:** All series/values are computed from the same information set.
- **Reason:** The distinction adds redundancy and visual complexity without reducing confusion.

## The Price <!-- role: costs -->

- **The Sacrifice:** More labeling/legend space and increased cognitive load.
- **The Risk:** Over-annotation can clutter small charts.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a single label like “forecast” for values that come from different information sets.
- **Why it fails:** Viewers assume all values reflect the same knowledge, which is exactly the misperception documented by the bias [@camererCurseKnowledgeEconomic1989].

## How to Check <!-- role: check -->

- **Visual Sign:** A reader cannot tell whether a number reflects the informed view, uninformed view, or an informed estimate of the uninformed view.
- **The Test:** Ask a reviewer to point to the chart element that represents I0-only knowledge; if they hesitate, the chart fails.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add direct text labels “I0 (uninformed)” and “I1 (informed)” next to the relevant marks.
- **Best Fix:** Structure the chart into clearly separated panels or layers by information set (e.g., small multiples: I0 vs. I1 vs. estimate-of-I0).
