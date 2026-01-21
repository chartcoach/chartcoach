---
id: prefer-grouped-bars-for-filter-like-selection-over-overlay-variants
title: Prefer grouped bar charts for filter-like selection tasks over overlay variants
bibliography: references.bib
description: For filter-style tasks, the plain grouped bar chart ranks best in accuracy
  and time compared to overlay variants in the reported results.
labels:
- chart:bar
- task:filter
- visual:length
- visual:color
- impact:accuracy
- impact:speed
- data:categorical
- audience:general
- comparison:multi-series
---

## The Rule <!-- role: advice -->

For **filter-like selection tasks** in a multi-series bar-chart context, use a **plain grouped bar chart** instead of adding difference overlays.

## The Logic <!-- role: reason -->

Overlays add marks that do not improve (and can slightly worsen) performance for selection-oriented tasks where users primarily need to identify categories/series values, not differences.

- **The Principle:** Avoid extra encodings when the task is selection rather than comparison of derived values.
- **The Evidence:** The collated filter-task results rank **E-1 (grouped bar chart)** above the overlay designs for both accuracy and time; one filter condition shows a significant advantage of **E-1 over E-4** for accuracy [@srinivasanWhatsDifferenceEvaluating2018]. This task mapping and ranking representation is part of the collation workflow in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Select categories meeting a condition (selection/filter behavior, not computing differences).
- **Data Type:** Two series shown as grouped bars (e.g., dashboard bar panels).
- **Audience:** General dashboard users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The “filter” interaction is explicitly about filtering on *change* (e.g., “show categories with positive difference”).
- **Reason:** The evidence here supports grouped bars for the reported filter tasks, not for change-threshold filtering [@srinivasanWhatsDifferenceEvaluating2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a direct visual cue for differences between series.
- **The Risk:** Users may be slower on difference-centric tasks if you use only grouped bars.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding difference overlays “just in case” for every dashboard bar chart.
- **Why it fails:** For selection-oriented tasks, added overlays do not improve performance and can add clutter [@srinivasanWhatsDifferenceEvaluating2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart looks busier (extra marks) but users are still just clicking categories/series.
- **The Test:** Remove overlays and see if users complete the selection task faster with the simpler chart.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove difference overlays and keep grouped bars with clear color separation between series.
- **Best Fix:** Offer overlays as an optional toggle only when the user switches into a change/comparison task mode [@srinivasanWhatsDifferenceEvaluating2018; @zengReviewCollationGraphical2023].
