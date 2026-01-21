---
id: avoid-blues-for-small-quantitative-differences-in-retrieve-value
title: Avoid Blues for Small Quantitative Differences in Retrieve-Value Tasks
bibliography: references.bib
description: When users must judge small value differences via color, avoid the blues
  single-hue colormap due to reduced accuracy at small spans.
labels:
- chart:color-scale
- task:retrieve-value
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- colormap:single-hue
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

If users must distinguish small quantitative differences using color, do not rely on a blues single-hue sequential colormap.

## The Logic <!-- role: reason -->

- **The Principle:** Single-hue sequential ramps can lose discriminable resolution for near values, increasing judgment errors.
- **The Evidence:** The collated findings summarized by [@zengReviewCollationGraphical2023] attribute reduced accuracy for blues at low spans in the triplet retrieve-value task, as reported in the experiment results of [@liuSomewhereRainbowEmpirical2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which of two values is closer to a reference value (retrieve-value / similarity judgment) using a quantitative colormap.
- **Data Type:** Quantitative data where comparisons frequently involve near-neighbor values (small spans).
- **Audience:** General audiences doing quick comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Comparisons are mostly coarse (values are far apart on the scale).
- **Reason:** The evidence indicates the main degradation is tied to small spans; for larger separations, the same colormap can perform comparably better [@zengReviewCollationGraphical2023; @liuSomewhereRainbowEmpirical2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose the simplicity and aesthetic consistency of a single-hue ramp.
- **The Risk:** Switching palettes may introduce additional hue variation that some stakeholders interpret as “more complex.”

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping blues and “solving it” by adding more legend ticks.
- **Why it fails:** The task performance issue in the study arises from discrimination limits for near colors, not a lack of tick marks or labeling detail [@liuSomewhereRainbowEmpirical2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Adjacent or near-adjacent values look nearly identical in the scale, and users frequently pick the wrong “closer” color.
- **The Test:** Sample pairs of close values from your scale and run a small internal triplet test (reference + two options) to see if error spikes for near differences, mirroring the retrieve-value judgment setup [@zengReviewCollationGraphical2023; @liuSomewhereRainbowEmpirical2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from a blues single-hue sequential scale to viridis for this task.
- **Best Fix:** Use a multi-hue sequential colormap (e.g., viridis) specifically for workflows dominated by small-difference judgments, encoding this as a recommendation rule/constraint in your system [@zengReviewCollationGraphical2023; @liuSomewhereRainbowEmpirical2018].
