---
id: use-low-count-quantile-dotplots-for-probability-estimation
title: Use Low-Count Quantile Dotplots for Precise Probability Reading
bibliography: references.bib
description: Prefer low-density quantile dotplots when users must estimate probabilities
  from a predictive distribution on mobile.
labels:
- chart:dotplot
- task:estimate
- visual:position
- impact:precision
- data:temporal
- audience:novice
- domain:transit
---

## The Rule <!-- role: advice -->

When users must estimate probabilities from an arrival-time distribution on a small screen, use a low-count quantile dotplot (e.g., ~20 dots) rather than a continuous density plot.

## The Logic <!-- role: reason -->

In a controlled experiment on transit prediction scenarios, a low-count quantile dotplot reduced variance in users’ probability estimates by about 1.15× compared to a density plot and increased users’ confidence in their estimates [@kayWhenIshMy2016]. The mechanism proposed is that small dot groups are easy to rapidly count/recognize, supporting frequency-style reasoning about probability intervals.

## Where to Apply <!-- role: context -->

- **User Goal:** Estimate “chance the bus arrives before X” or “chance it arrives within a window.”
- **Data Type:** Continuous predictive distributions displayed in compact rows.
- **Audience:** General public / non-expert riders.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Visual appeal is the dominant requirement and small precision gains are not worth a “busier” look.
- **Reason:** Participants rated density plots as more visually appealing even though dotplots were more precise [@kayWhenIshMy2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Lower visual appeal (in the study) relative to density plots.
- **The Risk:** Users may feel “forced to count” and perceive the display as more complex [@kayWhenIshMy2016].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Use a very dense dotplot (e.g., ~100 dots) and assume more dots means more accuracy.
- **Why it fails:** Dense dotplots performed similarly to density plots, suggesting users stop counting and revert to judging area/density [@kayWhenIshMy2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Users struggle to answer probability questions consistently or report low confidence.
- **The Test:** Give two similar probability questions; if answers vary widely, the encoding may not support precise estimation.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of dots (move toward a low-count quantile dotplot).
- **Best Fix:** Use a quantile dotplot designed as discrete outcomes from evenly spaced quantiles so counting maps directly to probability mass [@kayWhenIshMy2016].
