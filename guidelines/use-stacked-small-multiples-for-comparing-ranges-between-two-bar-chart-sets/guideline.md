---
id: use-stacked-small-multiples-for-comparing-ranges-between-two-bar-chart-sets
title: Stack Bar Charts Vertically to Compare Ranges Between Two Sets
bibliography: references.bib
description: "Use vertically stacked bar-chart small multiples to support precise\
  \ judgments of which set has the wider min\u2013max range."
labels:
- chart:bar
- task:compare
- task:rank
- visual:position
- visual:length
- impact:accuracy
- impact:clarity
- data:categorical
- audience:novice
- comparison:set-to-set
- source:jardine-2020
---

## The Rule <!-- role: advice -->

When users must judge which of two bar-chart sets has the wider **range (max–min)**, present them as **vertically stacked** charts.

## The Logic <!-- role: reason -->

Range comparisons benefit when viewers can isolate extremes and differences within each set; in this paper, stacked charts yielded the best performance for **MAXRANGE**, and superposed charts the worst [@jardinePerceptualProxiesVisual2020a].

- **The Principle:** Arrangement determines which perceptual cues are available for estimating within-set spread
- **The Evidence:** Stacked produced the highest precision for MAXRANGE; superposed produced the lowest precision [@jardinePerceptualProxiesVisual2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which group varies more (greater spread between smallest and largest values)
- **Data Type:** Two sets of values shown as bars (e.g., distributions across categories)
- **Audience:** General audiences; especially when “range” requires reinforcement/teaching

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not comparing ranges, but comparing **pairwise changes** between corresponding items across sets.
- **Reason:** The paper’s broader synthesis argues that different tasks rely on different perceptual proxies; layouts optimal for range are not optimal for item-change tasks [@jardinePerceptualProxiesVisual2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Increased vertical footprint.
- **The Risk:** If the number of categories is high, stacked panels can force small bar heights, potentially undermining quick reading.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Superposing both sets in one plot “so extremes are in the same place.”
- **Why it fails:** Superposition reduced precision for MAXRANGE in the study; separating sets helped observers more [@jardinePerceptualProxiesVisual2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers confuse overlap or fail to identify each set’s min and max reliably.
- **The Test:** Ask a tester to point out each set’s smallest and largest bar quickly; if overlap makes that slow/error-prone, the layout is fighting the task.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Split the two sets into a stacked pair with consistent category order.
- **Best Fix:** Use stacked small multiples and keep the two sets visually separable so within-set extremes are easy to pick out, consistent with the paper’s observed performance pattern [@jardinePerceptualProxiesVisual2020a].
