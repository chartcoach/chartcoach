---
id: use-blues-for-faster-retrieve-value-than-blueorange-or-jet
title: Use Blues to Reduce Time Versus BlueOrange or Jet in Retrieve-Value Tasks
bibliography: references.bib
description: For retrieve-value judgments, blues can be faster than blueorange or
  jet in response time.
labels:
- chart:color-scale
- task:retrieve-value
- visual:color
- impact:speed
- data:quantitative
- audience:general
- colormap:single-hue
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When optimizing for speed in retrieve-value judgments, prefer a blues sequential colormap over blueorange or jet.

## The Logic <!-- role: reason -->

- **The Principle:** Some colormaps yield faster perceptual distance judgments than others, reducing decision time.
- **The Evidence:** In the collated results of [@zengReviewCollationGraphical2023], the original experiment reports that blues (E-2) is faster than both blueorange (E-8) and jet (E-9) in retrieve-value timing, with significant pairwise differences (E-2 < E-8, E-2 < E-9) in [@liuSomewhereRainbowEmpirical2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Make quick similarity/closest-value judgments from a quantitative color encoding.
- **Data Type:** Quantitative values mapped to a sequential colormap.
- **Audience:** Users under time pressure where latency matters (e.g., rapid scanning).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Accuracy on small value differences is the priority.
- **Reason:** The same study reports cases where blues can suffer accuracy issues for low spans; optimizing only for time can increase mistakes [@zengReviewCollationGraphical2023; @liuSomewhereRainbowEmpirical2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may trade away accuracy in some hard cases if your users often compare near values.
- **The Risk:** Faster completion times may mask higher error rates if you don’t evaluate both metrics.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing the fastest palette without tracking error.
- **Why it fails:** The evidence separates time and accuracy outcomes; a palette that reduces time may not minimize errors in all conditions [@liuSomewhereRainbowEmpirical2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users complete judgments quickly but later show inconsistencies or disagreement about which value is closer.
- **The Test:** Measure both response time and error rate for representative tasks; don’t accept speed improvements alone [@zengReviewCollationGraphical2023; @liuSomewhereRainbowEmpirical2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** If you currently use blueorange or jet, switch to blues to reduce time for retrieve-value judgments.
- **Best Fix:** If you need both speed and strong accuracy, use viridis as the default and reserve blues only for contexts where near-value discrimination is not common (encode as conditional recommendation logic) [@zengReviewCollationGraphical2023; @liuSomewhereRainbowEmpirical2018].
