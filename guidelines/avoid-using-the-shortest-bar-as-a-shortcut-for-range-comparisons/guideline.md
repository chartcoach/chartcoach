---
id: avoid-using-the-shortest-bar-as-a-shortcut-for-range-comparisons
title: Avoid Using the Shortest Bar as a Shortcut for Range Comparisons
bibliography: references.bib
description: Prevent viewers from using the minimum bar length as a stand-in for range
  when comparing bar charts.
labels:
- chart:bar
- task:compare
- visual:length
- impact:clarity
- data:categorical
- audience:general
- concept:perceptual-proxies
---

## The Rule <!-- role: advice -->

When the task is to compare ranges, do not design the display so the chart with the larger range always also has the shortest bar (or always the longest bar).

## The Logic <!-- role: reason -->

In bar-chart range judgments, viewers may adopt perceptual shortcuts like “pick the chart with the shortest bar” or “pick the chart with the longest bar.” The paper explicitly identifies min-bar/max-bar as confounds for range and alters stimuli so that min/max no longer predict the correct range (only 50% aligned), because pilots suggested participants used the shortest bar strategy [@ondovRevealingPerceptualProxies2021].

- **The Principle:** Confounding proxy control (decoupling task-relevant statistic from trivial cues)
- **The Evidence:** Their experimental controls show min/max bars can dominate range judgments unless deliberately balanced/decoupled [@ondovRevealingPerceptualProxies2021].

## Where to Apply <!-- role: context -->

- **User Goal:** Determining which group varies more (larger max–min range)
- **Data Type:** Side-by-side bar charts where each chart contains multiple bars
- **Audience:** General audiences; especially in fast comparison settings (1500ms impressions for range in the study) [@ondovRevealingPerceptualProxies2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The intended analytic question is specifically “which has the smallest minimum?” or “which has the largest maximum?”
- **Reason:** Then min/max are not confounds—they are the target.

## The Price <!-- role: costs -->

- **The Sacrifice:** Reducing the salience of min/max can make it harder to spot true extremes.
- **The Risk:** Added design constraints (to avoid confounds) may reduce simplicity.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming range comprehension is “obvious” from bars without checking for min/max shortcuts.
- **Why it fails:** The study’s motivation and controls indicate participants may default to min/max proxies unless they are prevented from doing so [@ondovRevealingPerceptualProxies2021].

## How to Check <!-- role: check -->

- **Visual Sign:** In most comparisons, the “larger range” chart is also the one with the most extreme minimum or maximum.
- **The Test:** Audit pairs: verify whether “shortest bar wins” (or “longest bar wins”) predicts the range decision nearly all the time; if yes, viewers can bypass the true range judgment [@ondovRevealingPerceptualProxies2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Ensure comparisons sometimes place the smaller-range chart’s min/max within the larger-range chart’s span (so min/max alone can’t decide).
- **Best Fix:** Design and test range comparisons so that extracting range requires integrating both extremes (not just noticing one), mirroring the paper’s balancing approach [@ondovRevealingPerceptualProxies2021].
