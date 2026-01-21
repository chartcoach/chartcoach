---
id: prefer-dot-plots-for-comparing-group-averages
title: Use Dot Plots (Position-Only) to Compare Group Averages
bibliography: references.bib
description: When users must judge which group has a higher average, dot plots support
  more reliable averaging than filled bar encodings.
labels:
- chart:dot-plot
- task:compare
- visual:position
- impact:accuracy
- data:categorical
- audience:general
- statistic:mean
- source:paper-yuan-haroz-franconeri
---

## The Rule <!-- role: advice -->

Use dot plots (position-only marks) instead of filled bar charts when the task is to compare averages across groups.

## The Logic <!-- role: reason -->

Dot plots force judgments to rely on spatial position, whereas filled bars invite judgments based on spatial extent (length/area) that can act as a proxy for “average,” reducing precision for multi-value comparisons. The paper shows that for multi-value comparisons, bar graphs behave like extent-only encodings, and dot plots can be less impaired—especially when group sizes differ—suggesting access to a position-based proxy such as a center-of-mass judgment.

- **The Principle:** Multivalue “average” judgments drift from position to extent-based proxies (summed area/length)
- **The Evidence:** [@yuanPerceptualProxiesExtracting2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which group has the higher mean (e.g., average salary, average completion time)
- **Data Type:** Two (or more) groups each containing multiple observations (e.g., 2vs2, 6vs6, 10vs10, 6vs10)
- **Audience:** Anyone making quick perceptual judgments (lay audiences, analysts scanning dashboards)

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must communicate totals (sums) rather than averages
- **Reason:** Dot plots are not optimized for showing total magnitude; the paper’s concern is specifically that bar area encourages sum-like proxies when the goal is the mean [@yuanPerceptualProxiesExtracting2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Dot plots may feel less “standard” than bars for some audiences and can require more explanation
- **The Risk:** Viewers may focus on spread/outliers unless the design clearly frames “average”

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching from aligned bars to misaligned/stacked-like bars for group means
- **Why it fails:** Misalignment removes position cues and still supports extent-based proxies; performance for multivalue comparisons was similarly imprecise for normal vs misaligned bars [@yuanPerceptualProxiesExtracting2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Users seem to “see” the group with more/larger filled shapes as having the higher average even when it doesn’t
- **The Test:** Create a version where the two groups have different numbers of observations; if judgments change drastically, the display is likely triggering summed-extent proxies rather than mean extraction [@yuanPerceptualProxiesExtracting2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace bars with dots positioned on the value axis for each observation
- **Best Fix:** Use dot plots for observations when the task is mean comparison, especially if group sizes can differ [@yuanPerceptualProxiesExtracting2019].
