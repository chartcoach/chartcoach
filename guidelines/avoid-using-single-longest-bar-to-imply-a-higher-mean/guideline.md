---
id: avoid-using-single-longest-bar-to-imply-a-higher-mean
title: Avoid Using a Single Longest Bar to Imply a Higher Mean
bibliography: references.bib
description: Prevent viewers from mistaking one extreme bar for evidence of a higher
  average in bar-chart comparisons.
labels:
- chart:bar
- task:compare
- visual:length
- visual:position
- impact:clarity
- data:categorical
- audience:general
- concept:perceptual-proxies
- risk:adversarial-data
---

## The Rule <!-- role: advice -->

When the task is to judge which series has the larger mean, do not let a single extreme (very long) bar stand out as the dominant feature; reduce or neutralize single-bar extremes.

## The Logic <!-- role: reason -->

A prominent extreme can act as a perceptual proxy (e.g., “max bar”) that competes with true mean computation, increasing the chance of incorrect “larger mean” judgments under brief viewing. The paper demonstrates adversarial datasets where one chart has a smaller arithmetic mean but can be made to look larger by exaggerating the longest bar, indicating that viewers may rely on such proxies rather than arithmetic averaging [@ondovRevealingPerceptualProxies2021].

- **The Principle:** Proxy-based summarization (heuristic extraction over exact statistics)
- **The Evidence:** Adversarial “max bar” manipulations can sway mean judgments in their design and observed threshold shifts [@ondovRevealingPerceptualProxies2021].

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing which of two groups has the larger average (MaxMean-style comparisons)
- **Data Type:** Small-multiple or side-by-side bar charts with multiple bars per series
- **Audience:** General audiences, especially under quick/glance viewing (the study used 1000ms impressions) [@ondovRevealingPerceptualProxies2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The point of the graphic is to highlight outliers/extremes (e.g., “largest value” is the intended message).
- **Reason:** Downplaying extremes would undermine the intended task and hide relevant structure.

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose visibility of rare but important extremes.
- **The Risk:** Over-smoothing or clipping can make distributions look more uniform than they are.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the extreme but adding a caption like “mean is lower.”
- **Why it fails:** The study’s premise is that fast perceptual judgments can be driven by the visual proxy before text is integrated, especially under brief exposure [@ondovRevealingPerceptualProxies2021].

## How to Check <!-- role: check -->

- **Visual Sign:** One bar visually dominates the entire chart area/shape.
- **The Test:** Glance-test: show the chart briefly (about a second) and ask a colleague which mean is larger; if they pick based on the dominant bar, the design is vulnerable [@ondovRevealingPerceptualProxies2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use a scale/transform or annotate extremes so they don’t dominate the overall shape.
- **Best Fix:** Choose a representation that supports mean comparison without inviting max-bar substitution (e.g., include a direct mean indicator prominently and ensure extremes don’t overpower it), then validate with a quick glance test [@ondovRevealingPerceptualProxies2021].
