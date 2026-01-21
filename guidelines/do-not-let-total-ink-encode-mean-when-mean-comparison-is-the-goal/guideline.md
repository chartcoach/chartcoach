---
id: do-not-let-total-ink-encode-mean-when-mean-comparison-is-the-goal
title: Do Not Let Total Ink Encode Mean When Mean Comparison Is the Goal
bibliography: references.bib
description: Avoid making total filled area (ink) a reliable shortcut for mean comparisons
  in bar charts.
labels:
- chart:bar
- task:compare
- visual:area
- visual:length
- impact:clarity
- data:categorical
- audience:general
- concept:perceptual-proxies
---

## The Rule <!-- role: advice -->

If you want viewers to compare means across two bar charts, prevent “amount of ink” (total filled area) from being a perfectly reliable cue for the mean.

## The Logic <!-- role: reason -->

With equal bar thickness, total ink (sum of bar areas) is directly proportional to the arithmetic mean for charts with the same number of bars, so viewers can answer by judging area rather than the intended mean-comparison process. The paper treats ink area as a confounding proxy for MaxMean and explicitly decouples it by varying bar thickness between the two charts so ink area cannot determine the correct answer [@ondovRevealingPerceptualProxies2021].

- **The Principle:** Confound removal (eliminate shortcuts that trivially determine the answer)
- **The Evidence:** Their MaxMean control manipulates bar thickness specifically to break the ink-area→mean linkage [@ondovRevealingPerceptualProxies2021].

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing average level across two multi-bar series (MaxMean)
- **Data Type:** Two bar charts with the same number of bars displayed side-by-side
- **Audience:** General audiences; especially when you are studying or stress-testing perceptual strategies (as in the paper) [@ondovRevealingPerceptualProxies2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally want area/ink to communicate the aggregate (e.g., sum) rather than mean.
- **Reason:** Then ink area is not a confound—it is the encoding.

## The Price <!-- role: costs -->

- **The Sacrifice:** Varying thickness can reduce visual uniformity and may confuse readers who assume thickness is meaningful.
- **The Risk:** Viewers might infer an unintended variable from thickness differences.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping constant thickness and assuming people will “compute” the mean from lengths.
- **Why it fails:** The paper motivates that the visual system uses proxies/heuristics rather than explicit arithmetic; ink is an easy proxy unless controlled [@ondovRevealingPerceptualProxies2021].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart with the higher mean also looks like it obviously contains more colored area.
- **The Test:** Ask: if I blur/squint, does the larger-looking mass always correspond to larger mean? If yes, ink is acting as the decision rule [@ondovRevealingPerceptualProxies2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce reliance on area by ensuring thickness differences (or other design constraints) prevent ink from being determinative, as done in the study [@ondovRevealingPerceptualProxies2021].
- **Best Fix:** If the goal is mean comparison robustness (not area comparison), redesign and validate so mean must be judged from the intended cues, not from total ink [@ondovRevealingPerceptualProxies2021].
