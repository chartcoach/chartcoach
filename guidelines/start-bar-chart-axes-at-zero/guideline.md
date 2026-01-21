---
id: start-bar-chart-axes-at-zero
title: Start Bar-Chart Axes at Zero
bibliography: references.bib
description: Use a zero baseline for bar charts to avoid exaggerating differences
  that viewers perceive at a glance.
labels:
- chart:bar
- task:compare
- visual:position
- impact:honesty
- data:quantitative
- audience:general
- source:szafir-2018
---

## The Rule <!-- role: advice -->

In bar charts, start the value axis at zero; do not truncate the y-axis above zero.

## The Logic <!-- role: reason -->

Bar charts are read by judging the distance from the baseline to the bar top; truncating the baseline inflates perceived differences, and viewers often form conclusions from the at-a-glance ratio rather than reading axis labels, as described in [@szafirGoodBadBiased2018].

- **The Principle:** Baseline-dependent magnitude perception + “gist” reading
- **The Evidence:** [@szafirGoodBadBiased2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare magnitudes across categories
- **Data Type:** Non-negative quantitative measures shown as bars
- **Audience:** Any audience, especially when quick “headline” takeaways matter

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart is not baseline-dependent for interpretation (i.e., not a bar chart)
- **Reason:** The specific distortion mechanism discussed is about baseline-to-mark distance in common bar interpretations in [@szafirGoodBadBiased2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Small differences may become visually subtle
- **The Risk:** Viewers may miss fine-grained variation if the full range is large

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Truncating the axis but “fixing” it by labeling ticks clearly
- **Why it fails:** People often do not read axis labels; they rely on perceived ratios, per [@szafirGoodBadBiased2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Bars look dramatically different while axis labels indicate a small difference
- **The Test:** Compare the visual ratio of bar heights to the numeric ratio—if they diverge due to a non-zero baseline, the chart is misleading (as in [@szafirGoodBadBiased2018])

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reset the axis minimum to zero
- **Best Fix:** If the goal is to emphasize change rather than magnitude, compute the change relative to a baseline and visualize that metric with honest axes, as suggested in [@szafirGoodBadBiased2018]
