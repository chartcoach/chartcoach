---
id: avoid-splitting-daily-patterns-into-two-12h-panels
title: "Avoid Splitting Daily Patterns Into Two 12\u2011Hour Panels"
bibliography: references.bib
description: For daily patterns, prefer a single 24-hour view over two 12-hour panels
  to improve speed and (often) accuracy and preference.
labels:
- chart:bar
- chart:small-multiples
- task:find-extremum
- task:retrieve-value
- impact:efficiency
- data:temporal
- data:binned
- audience:novice
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Show the full day in one continuous 24-hour chart rather than splitting into AM/PM (two 12-hour panels).

## The Logic <!-- role: reason -->

- **The Principle:** Splitting a continuous temporal sequence introduces cross-panel searching and comparison overhead.
- **The Evidence:** In this study’s rankings, single 24-hour linear (E-4) is consistently faster than the split 12-hour linear variant (E-3) for each recorded task (filter, retrieve value, find extremum, sort) and is also the most preferred overall [@waldnerComparisonRadialLinear2020]. This is represented as actionable comparative knowledge in the collation dataset approach [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Fast task completion when filtering, retrieving a value, sorting, or finding an extremum in daily patterns.
- **Data Type:** Hourly (or similarly binned) 24-hour periodical data.
- **Audience:** Non-expert users performing quick lookups or comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must present in constrained horizontal space where a 24-bin chart becomes unreadable at the chosen fixed size.
- **Reason:** The underlying evidence compares specific fixed-size designs; extreme layout constraints may force paneling even if it slows tasks [@waldnerComparisonRadialLinear2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** A single 24-hour chart can require more horizontal resolution to keep bars legible.
- **The Risk:** If you compress too much, labels/bars may become hard to read, potentially offsetting the speed advantage.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Splitting into two 12-hour panels to “reduce clutter,” even when a 24-hour linear chart fits.
- **Why it fails:** The split linear variant (E-3) is slower than the 24-hour linear (E-4) across tasks in the recorded time rankings [@waldnerComparisonRadialLinear2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Users repeatedly shift attention between AM and PM panels to answer simple questions.
- **The Test:** Time users on the same tasks using a 24-hour chart vs 2×12; if 24-hour is faster (as observed), keep it [@waldnerComparisonRadialLinear2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Merge AM/PM panels into a single 24-hour x-axis.
- **Best Fix:** Prefer a 24-hour linear bar chart recommendation for these tasks, consistent with the collated performance ordering [@zengReviewCollationGraphical2023; @waldnerComparisonRadialLinear2020].
