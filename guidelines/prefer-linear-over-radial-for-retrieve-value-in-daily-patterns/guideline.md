---
id: prefer-linear-over-radial-for-retrieve-value-in-daily-patterns
title: Use Linear Charts for Retrieve-Value Tasks Over Daily Patterns
bibliography: references.bib
description: For retrieving specific values from daily patterns, linear bar charts
  outperform radial rose charts in accuracy and time.
labels:
- chart:bar
- chart:radial
- task:retrieve-value
- impact:accuracy
- impact:efficiency
- data:temporal
- data:binned
- audience:novice
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When users must read the value for a specific hour/bin, use a linear bar chart instead of a radial rose chart.

## The Logic <!-- role: reason -->

- **The Principle:** Linear length reading is more straightforward than radial decoding for precise value lookup.
- **The Evidence:** For retrieve-value, accuracy ranks the 24-hour linear (E-4) highest and both linear designs (E-4, E-3) above radial designs (E-2, E-1); time also ranks E-4 fastest with radial last [@waldnerComparisonRadialLinear2020]. These results are included in the broader collation for recommendation use [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Retrieve the value at a specified time bin.
- **Data Type:** Binned daily time series (e.g., hourly counts).
- **Audience:** Non-expert users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Exact value retrieval is not needed (only rough impression).
- **Reason:** The evidence is specifically about task performance for retrieving values [@waldnerComparisonRadialLinear2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose any perceived “clock-like” thematic match.
- **The Risk:** If you later reintroduce radial for style, expect worse lookup performance.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the rose chart and adding more visual scaffolding while still requiring precise reading.
- **Why it fails:** In the study, radial variants remain slower and less accurate for retrieve-value than linear variants [@waldnerComparisonRadialLinear2020].

## How to Check <!-- role: check -->

- **Visual Sign:** High lookup time or frequent misreads when asked “What is the value at hour X?”
- **The Test:** Timed retrieve-value questions; compare radial vs linear and keep the faster/more accurate approach (linear, per results) [@waldnerComparisonRadialLinear2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use a 24-hour linear bar chart (E-4 style) for the view.
- **Best Fix:** Encode recommendation rules that select linear bars for retrieve-value tasks on daily patterns using the collated findings as constraints/heuristics [@zengReviewCollationGraphical2023; @waldnerComparisonRadialLinear2020].
