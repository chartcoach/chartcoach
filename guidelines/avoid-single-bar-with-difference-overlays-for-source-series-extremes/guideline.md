---
id: avoid-single-bar-with-difference-overlays-for-source-series-extremes
title: Avoid single-bar charts with difference overlays for source-series extreme
  finding
bibliography: references.bib
description: For identifying extremes in the source series, do not rely on a single-bar-with-overlays
  design; use grouped bars (with or without overlays) instead.
labels:
- chart:bar
- task:find-extremum
- visual:overlay
- impact:accuracy
- impact:speed
- data:categorical
- audience:general
- comparison:multi-series
---

## The Rule <!-- role: advice -->

When users must identify an extreme (min/max) in the **source series**, do **not** use a **single bar chart with difference overlays**; use a **grouped bar chart** (with or without difference overlays).

## The Logic <!-- role: reason -->

The single-bar-with-overlays design forces users to infer source values indirectly, increasing errors and time.

- **The Principle:** Avoid forcing users to mentally reconstruct values needed for a precise selection task.
- **The Evidence:** For source-series extreme identification, accuracy ranks **GB (E-1) > GB+D (E-3) > SB+D (E-4)**, with significant differences showing both **E-1** and **E-3** outperform **E-4** [@srinivasanWhatsDifferenceEvaluating2018]. Time similarly ranks **E-1 faster than E-4** with significance reported [@srinivasanWhatsDifferenceEvaluating2018]. This finding is included in the collation framework described by [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Find the maximum/minimum in the **source** year/series (not the displayed target bars).
- **Data Type:** Two-series categorical/ordinal comparisons in dashboards.
- **Audience:** General dashboard users (non-experts included).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users never need to retrieve or identify extremes for the source series (only need target values or differences).
- **Reason:** The disadvantage is tied to tasks requiring direct source-series reading [@srinivasanWhatsDifferenceEvaluating2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Grouped bars require showing both series (more marks/space than a single-series bar view).
- **The Risk:** Side-by-side bars can create additional distractors, though they still outperform the single-bar-with-overlays design for this task in the reported results [@srinivasanWhatsDifferenceEvaluating2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping SB+D and expecting users to “just read the overlay” to infer source extremes.
- **Why it fails:** Users must mentally add/subtract the overlay from the target bar to derive source values, which degraded accuracy and speed [@srinivasanWhatsDifferenceEvaluating2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users select the wrong category when asked “Which category is highest/lowest in the previous year?”
- **The Test:** Give a quick source-extreme task; if users take noticeably longer or make frequent errors with SB+D, switch away.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch SB+D to a grouped bar chart (GB) to show both series directly.
- **Best Fix:** Use **grouped bar chart with difference overlays (GB+D)** if you also want to support change-focused tasks while preserving source value readability [@srinivasanWhatsDifferenceEvaluating2018; @zengReviewCollationGraphical2023].
