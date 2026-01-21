---
id: use-delta-encodings-for-judging-which-relation-direction-is-more-prevalent
title: Use Delta Encodings for Proportion Judgments of Relation Direction
bibliography: references.bib
description: "To judge whether increases or decreases are more common across many\
  \ pairs, encode each pair\u2019s signed delta to improve accuracy."
labels:
- chart:bar
- chart:dot
- chart:slope
- task:compare
- task:aggregate
- visual:length
- visual:position
- visual:orientation
- impact:accuracy
- data:paired
- audience:novice
- audience:expert
- source:nothelfer-franconeri-2020
---

## The Rule <!-- role: advice -->

For “are there more increases or more decreases?” questions across multiple pairs, encode each pair as a delta with sign (positive vs. negative) rather than two separate values.

## The Logic <!-- role: reason -->

A prevalence judgment is easier when each item’s category (increase/decrease) is directly legible as a single feature, rather than requiring pairwise comparison for every item before tallying.

- **The Principle:** Reduce per-item computation before aggregation.
- **The Evidence:** In Experiment 2, participants were significantly more accurate judging which relation direction was more prevalent with delta encodings than with individual value encodings; the paper reports about a 30% accuracy improvement (and larger when considering performance above chance) [@nothelferMeasuresBenefitDirect2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which relation direction dominates across categories (e.g., more up than down).
- **Data Type:** Paired comparisons across a fixed number of categories (the study used 10 pairs per display) where direction is the key attribute.
- **Audience:** Broad; especially useful for quick “gist” understanding.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The audience must also interpret the magnitude distribution of the underlying absolute values (not just direction).
- **Reason:** Delta-only direction-focused encodings can obscure base-value patterns and context [@nothelferMeasuresBenefitDirect2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced access to base levels unless you add them separately.
- **The Risk:** Viewers may over-focus on direction and ignore important absolute-value constraints [@nothelferMeasuresBenefitDirect2020a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Present grouped bars and ask users to mentally categorize each pair as “up” or “down” and then estimate which is more common.
- **Why it fails:** It forces a two-step process (compute relation → aggregate), which is less accurate than direct delta encoding [@nothelferMeasuresBenefitDirect2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate or count manually to answer “more increases or decreases.”
- **The Test:** Briefly show the chart (single-glance). If users can’t reliably answer direction prevalence without recounting, direction is not directly encoded.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a delta encoding that clearly separates positive vs. negative deltas (e.g., above/below baseline for bars/dashes, or up/down slope).
- **Best Fix:** Use a delta-only layout for this view so each category contributes one directly classifiable mark [@nothelferMeasuresBenefitDirect2020a].
