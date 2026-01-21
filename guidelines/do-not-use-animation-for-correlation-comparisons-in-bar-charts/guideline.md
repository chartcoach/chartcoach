---
id: do-not-use-animation-for-correlation-comparisons-in-bar-charts
title: Avoid Animation for Correlation Judgments in Bar-Chart Comparisons
bibliography: references.bib
description: Animated transitions do not improve correlation comparison performance
  for bar charts compared to static alternatives.
labels:
- chart:bar
- task:correlate
- visual:motion
- impact:accuracy
- data:quantitative
- audience:general
- comparison:between-series
- layout:animated
---

## The Rule <!-- role: advice -->

Do not rely on animated transitions to help viewers judge correlation (overall similarity) between two bar-chart series.

## The Logic <!-- role: reason -->

In the studied correlation task, animation did not provide a performance benefit versus static arrangements, indicating that motion cues that help highlight single-item deltas do not translate into better extraction of overall correlation structure. This rule is derived from the synthesis in [@zengReviewCollationGraphical2023] based on results reported by [@ondovFaceFaceEvaluating2019].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which series-pair is more correlated (more similar overall).
- **Data Type:** Two quantitative series (bar charts) where the judgment is global pattern similarity, not a single largest change.
- **Audience:** General audiences and analysts doing quick similarity screening.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your objective is *not* correlation, but identifying the largest change between states.
- **Reason:** The same study shows animation can help for max-delta (“biggest mover”) judgments, which is a different task [@ondovFaceFaceEvaluating2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up a potentially engaging dynamic effect.
- **The Risk:** If you use animation anyway, viewers may focus on motion rather than extracting correlation, without gaining accuracy [@ondovFaceFaceEvaluating2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding animation because it “worked well for comparisons” in general.
- **Why it fails:** The evidence is task-specific; animation benefits max-delta, not correlation, as emphasized in [@ondovFaceFaceEvaluating2019] and collated in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers describe “movement” but can’t reliably identify the more correlated pair.
- **The Test:** Compare performance with and without animation for the same correlation prompt; if accuracy doesn’t improve, remove animation [@ondovFaceFaceEvaluating2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Turn off the animated transition and present static comparisons.
- **Best Fix:** Use a static layout optimized for correlation judgments (e.g., mirrored small multiples), aligning with the task-dependent guidance summarized in [@zengReviewCollationGraphical2023] from [@ondovFaceFaceEvaluating2019].
