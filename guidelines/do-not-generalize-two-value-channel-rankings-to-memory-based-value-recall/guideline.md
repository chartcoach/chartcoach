---
id: do-not-generalize-two-value-channel-rankings-to-memory-based-value-recall
title: Do Not Generalize Two-Value Channel Ranks to Memory-Based Value Recall
bibliography: references.bib
description: Classic channel rankings do not reliably transfer to immediate reproduction
  (memory) retrieve-value tasks, even with only two marks.
labels:
- task:retrieve-value
- visual:position
- visual:length
- visual:area
- visual:orientation
- visual:color-saturation
- impact:robustness
- data:quantitative
- audience:designer
- source:empirical
---

## The Rule <!-- role: advice -->

When your task is **immediate memory-based value recall**, do not assume a single fixed “best visual channel” ranking; validate channel choice for the **specific mark-count and objective**.

## The Logic <!-- role: reason -->

- **The Principle:** Perceptual effectiveness rankings can be **non-transferable across tasks**; memory demands and mark-count can dominate performance.
- **The Evidence:** The paper reports that the channel ranking pattern **does not hold** for a reproduction-based retrieve-value task, and that the resulting ranking is **inconsistent across different numbers of marks** [@mccolemanRethinkingRanksVisual2022]. This limitation and its implications for recommendation is emphasized in the collation context [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Reproduce values from a brief glance (a “show–mask–reproduce” style setting).
- **Data Type:** Quantitative values; small to moderate mark counts (2–8 in the reported results).
- **Audience:** Visualization designers and visualization recommendation system builders.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your task is not memory-based reproduction (e.g., slow careful reading where the chart remains visible).
- **Reason:** The evidence is specific to immediate reproduction after brief exposure [@mccolemanRethinkingRanksVisual2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose the simplicity of a single universal rule-of-thumb.
- **The Risk:** Additional evaluation or task modeling is required before making a recommendation.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Hard-coding channel preferences as universal without conditioning on task and mark-count.
- **Why it fails:** The reported ranks change across mark-counts and differ from traditional expectations under this task framing [@mccolemanRethinkingRanksVisual2022; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** A recommended encoding “should be best” by conventional wisdom, but users still make large recall errors.
- **The Test:** Add a task-specific micro-benchmark (brief display + reproduction) for your candidate encodings and compare error distributions.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Condition your design rules on mark-count (e.g., treat 2-mark vs 8-mark displays differently).
- **Best Fix:** Incorporate task- and mark-count-specific evidence (like the reproduced rankings) into your recommendation logic rather than relying on a universal channel order [@mccolemanRethinkingRanksVisual2022; @zengReviewCollationGraphical2023].
