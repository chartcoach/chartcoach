---
id: avoid-rainbow-colormaps-for-quantitative-encoding
title: Avoid Rainbow Colormaps for Quantitative Data
bibliography: references.bib
description: Rainbow colormaps (e.g., jet) produce slower and more error-prone quantitative
  judgments than well-designed alternatives.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- colormap:rainbow
---

## The Rule <!-- role: advice -->

Avoid rainbow colormaps (such as jet) for encoding scalar quantitative values.

## The Logic <!-- role: reason -->

- **The Principle:** Non-monotonic and categorical-looking hue transitions create misleading perceived distances and ordering cues.
- **The Evidence:** In triplet distance-judgment experiments, the jet colormap was the slowest and most error-prone among those tested, while newer sequential maps (e.g., viridis) performed better [@liuSomewhereRainbowEmpirical2018a].

## Where to Apply <!-- role: context -->

- **User Goal:** Judging which values are closer / more similar (relative distance) from color.
- **Data Type:** Continuous scalar fields or ordered numeric ranges mapped to color (0–100 style scales).
- **Audience:** Mixed audiences, especially when you care about decoding accuracy.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally want sharp categorical separations aligned with meaningful thresholds, not smooth quantitative reading.
- **Reason:** The paper’s task is quantitative similarity judgment; rainbow-like banding may be intentionally used for thresholding, which is a different goal [@liuSomewhereRainbowEmpirical2018a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up a familiar “classic” look that some communities expect.
- **The Risk:** Stakeholders accustomed to rainbow may resist or mistrust the change.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping jet but “adding a legend” and assuming that solves perception problems.
- **Why it fails:** The experiments included legends and jet still underperformed in time and error [@liuSomewhereRainbowEmpirical2018a].

## How to Check <!-- role: check -->

- **Visual Sign:** Large apparent “bands” at hue boundaries; regions that look equally different despite unequal value steps.
- **The Test:** Run a quick internal triplet test: pick a reference value and two alternatives on either side; if people often pick the wrong “closer” color, the map is likely misleading (as observed for jet) [@liuSomewhereRainbowEmpirical2018a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace jet/rainbow with a perceptually-designed sequential multi-hue map such as viridis-like schemes.
- **Best Fix:** Choose a sequential colormap with strong perceptual ordering and validated performance for similarity judgments (the paper’s best-performing option was viridis) [@liuSomewhereRainbowEmpirical2018a].
