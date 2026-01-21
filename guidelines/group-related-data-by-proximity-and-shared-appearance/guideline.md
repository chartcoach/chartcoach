---
id: group-related-data-by-proximity-and-shared-appearance
title: Make True Data Groups Look Like Visual Groups
bibliography: references.bib
description: Use proximity and shared color/shape to align perceptual grouping with
  real group structure.
labels:
- chart:bar
- task:group
- visual:proximity
- impact:comprehension
- data:categorical
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Arrange and style marks so that items that belong together in the data are grouped visually via proximity and shared appearance (e.g., contiguous placement plus consistent color).

## The Logic <!-- role: reason -->

- **The Principle:** Perceptual grouping is automatic; viewers see clusters formed by proximity and shared features.
- **The Evidence:** The paper describes grouping cues (proximity, shared color/shape, smooth continuation) and demonstrates how regrouping bars makes regional comparisons feasible [@zacksDesigningGraphsDecisionMakers2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing aggregates across groups (regions, categories) and seeing group structure quickly.
- **Data Type:** Categorical data with hierarchical or grouped categories.
- **Audience:** Viewers who must detect group differences without doing many pairwise comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When preserving another meaningful order (e.g., strict ranking) is more important than showing group contiguity.
- **Reason:** The design goal may prioritize order-based tasks over group-based tasks [@zacksDesigningGraphsDecisionMakers2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** A single global ordering (like overall descending rank) may be lost.
- **The Risk:** Outliers may be visually “orphaned” or mis-seen if they sit far from their group.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using color to indicate groups but leaving group members scattered across the chart.
- **Why it fails:** Color-only grouping is weaker than color + proximity; viewers still struggle to see the grouped pattern [@zacksDesigningGraphsDecisionMakers2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can identify individual items but cannot answer “Which group is larger overall?”
- **The Test:** Ask someone to summarize group differences without reading labels one by one. If they can’t, grouping cues are insufficient.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Sort within group and place group members contiguously.
- **Best Fix:** Use small multiples or faceted grouping (separate rows/sections per group) plus consistent color to reinforce grouping [@zacksDesigningGraphsDecisionMakers2020].
