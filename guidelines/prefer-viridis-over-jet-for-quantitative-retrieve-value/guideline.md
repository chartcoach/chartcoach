---
id: prefer-viridis-over-jet-for-quantitative-retrieve-value
title: Prefer Viridis Over Jet for Quantitative Retrieve-Value Tasks
bibliography: references.bib
description: For quantitative color scales in retrieve-value judgments, prefer viridis
  over jet to improve accuracy.
labels:
- chart:color-scale
- task:retrieve-value
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a viridis-like multi-hue sequential colormap instead of a jet/rainbow colormap for quantitative retrieve-value judgments.

## The Logic <!-- role: reason -->

- **The Principle:** Not all sequential colormaps support equally accurate relative distance judgments; poor ordering and confusing hue transitions can increase errors.
- **The Evidence:** In the retrieved structured results collated by [@zengReviewCollationGraphical2023], the underlying experiment shows viridis (E-5) has higher accuracy than jet (E-9) for retrieve-value, with a significant advantage (E-5 > E-9) reported in [@liuSomewhereRainbowEmpirical2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Retrieve/choose the closest value (relative similarity judgment) from a quantitative color encoding.
- **Data Type:** Quantitative values mapped to a continuous colormap (sequential).
- **Audience:** General audiences performing quick judgments (e.g., analysts, dashboard viewers).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Jet is already fixed by a legacy standard you cannot change.
- **Reason:** The rule is about selecting colormaps; if the palette is non-negotiable, you can’t apply it directly (you’ll need mitigations instead).

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up the familiar “rainbow” look some users expect.
- **The Risk:** If users are accustomed to jet, changing palettes may initially feel unfamiliar even if it improves accuracy.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching from jet to another arbitrary multi-hue palette without checking performance.
- **Why it fails:** The evidence here specifically supports viridis outperforming jet for accuracy in retrieve-value judgments, not that all multi-hue palettes behave identically [@zengReviewCollationGraphical2023; @liuSomewhereRainbowEmpirical2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate or make frequent mistakes when judging which color is closer to a reference.
- **The Test:** A/B test the same tasks with viridis vs jet and compare error rates (the study used accuracy/error outcomes for this task) [@liuSomewhereRainbowEmpirical2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace jet with viridis for the quantitative color scale.
- **Best Fix:** Standardize viridis as the default sequential palette for quantitative retrieve-value tasks in your system’s design rules or constraints [@zengReviewCollationGraphical2023; @liuSomewhereRainbowEmpirical2018].
