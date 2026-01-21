---
id: show-learning-by-separating-periods-before-and-after-market-experience
title: Separate Pre- and Post-Experience Periods to Show Learning
bibliography: references.bib
description: Use explicit period segmentation (e.g., A vs. B) to reveal whether bias
  shrinks after market experience.
labels:
- chart:small-multiples
- task:trend
- visual:position
- impact:clarity
- data:temporal
- audience:expert
- domain:experimental-markets
---

## The Rule <!-- role: advice -->

When you claim learning or bias reduction over time, split the visualization into clearly labeled time blocks (e.g., Period A vs. Period B) and show values for each block.

## The Logic <!-- role: reason -->

The paper evaluates bias changes by comparing A and B periods and observing movement away from pure-bias predictions; without explicit segmentation, the “learning” inference is not inspectable.

- **The Principle:** Periodized comparison to isolate experience effects
- **The Evidence:** [@camererCurseKnowledgeEconomic1989]

## Where to Apply <!-- role: context -->

- **User Goal:** Detect whether experience/feedback/market participation changes judgments or prices
- **Data Type:** Repeated measures within the same item/market (before vs. after a treatment)
- **Audience:** Readers evaluating causal claims about learning

## When to Break It <!-- role: exceptions -->

- **Scenario:** Only a single observation exists per item (no repeated periods).
- **Reason:** Period splitting would fabricate a time structure that isn’t present.

## The Price <!-- role: costs -->

- **The Sacrifice:** Less room per period for detailed within-period variation.
- **The Risk:** Readers may overinterpret small differences if uncertainty is not shown.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Aggregating across periods and reporting a single mean price/judgment.
- **Why it fails:** It hides the directional movement that the paper uses to argue that market experience reduces bias [@camererCurseKnowledgeEconomic1989].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart cannot answer “Did bias shrink from A to B for this item?”
- **The Test:** Try to compare A vs. B without reading the caption; if you can’t, the chart fails.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add two labeled points per item (A and B) connected by a thin line.
- **Best Fix:** Use small multiples or grouped panels per item with shared benchmarks (no-bias and pure-bias) to make directionality obvious.
