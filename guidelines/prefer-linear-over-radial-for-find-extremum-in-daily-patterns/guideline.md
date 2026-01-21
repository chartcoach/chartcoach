---
id: prefer-linear-over-radial-for-find-extremum-in-daily-patterns
title: "Use a 24\u2011Hour Linear Bar Chart to Find Extremes in Daily Patterns"
bibliography: references.bib
description: For finding extrema in daily patterns, a 24-hour linear bar chart is
  fastest and at least as accurate as radial options.
labels:
- chart:bar
- chart:radial
- task:find-extremum
- impact:efficiency
- impact:accuracy
- data:temporal
- data:binned
- audience:novice
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

For find-extremum tasks on daily patterns, use a single 24-hour linear bar chart.

## The Logic <!-- role: reason -->

- **The Principle:** A continuous linear scan supports fast detection of the tallest bar.
- **The Evidence:** For find-extremum, time ranks E-4 fastest; accuracy has E-4 tied at the top (grouped with E-2) and above the other conditions, with radial split (E-1) worst [@waldnerComparisonRadialLinear2020]. This task-specific outcome is exactly the kind of rule the collation paper aims to operationalize [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Find the maximum (or other extremum) hour/bin.
- **Data Type:** 24 hourly bins with quantitative magnitude.
- **Audience:** Non-expert users performing quick checks.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must keep a radial format for strict consistency with an existing radial-only dashboard, and speed is not important.
- **Reason:** The measured advantage here is primarily in completion time and preference, not an exclusive accuracy win [@waldnerComparisonRadialLinear2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less compact circular footprint than some radial layouts.
- **The Risk:** If rendered too narrow, bars may become hard to select/identify visually.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using split charts (AM/PM) and assuming extrema will “pop out” anyway.
- **Why it fails:** Time rankings place the split linear (E-3) behind E-4, and the split radial (E-1) last [@waldnerComparisonRadialLinear2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Users take longer than expected to identify the peak hour or choose a wrong bar.
- **The Test:** Ask “Which hour has the maximum?” and time responses; E-4-style linear should be fastest as observed [@waldnerComparisonRadialLinear2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Consolidate into one 24-hour linear bar chart.
- **Best Fix:** In automated recommendation, prefer the 24-hour linear bar layout for find-extremum tasks on daily patterns, consistent with the collated evidence [@zengReviewCollationGraphical2023; @waldnerComparisonRadialLinear2020].
