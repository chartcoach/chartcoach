---
id: prefer-orientation-or-area-over-position-line-for-2-mark-value-recall
title: Prefer Orientation or Area Over Line Position for 2-Value Recall
bibliography: references.bib
description: For recalling two quantitative values, orientation or area encodings
  yielded lower error than line-position in an immediate reproduction task.
labels:
- chart:line
- chart:scatter
- task:retrieve-value
- visual:orientation
- visual:area
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- marks:2
- source:empirical
---

## The Rule <!-- role: advice -->

When users must recall/reproduce **two quantitative values**, avoid **line charts that rely on position**; use an **orientation** encoding or an **area (bubble)** encoding instead.

## The Logic <!-- role: reason -->

- **The Principle:** Channel effectiveness can be **task- and context-dependent**, and “position is best” does not necessarily hold for memory-based value reproduction.
- **The Evidence:** In a retrieve-value reproduction task with **2 marks**, **orientation** and **area** were ranked best (tied), and both outperformed **position (line)**, with Bayesian pairwise evidence that each of these beat position(line) at the stated threshold [@mccolemanRethinkingRanksVisual2022]. This guideline is derived from the structured collation of that result in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Immediately reproduce/recall a very small set of values (two marks).
- **Data Type:** Quantitative values displayed as two marks.
- **Audience:** Any audience doing quick recall from a glance.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is not immediate value recall (e.g., you are not asking users to reproduce values from memory).
- **Reason:** The evidence here is specifically about a **reproduction (memory) retrieve-value** task; it does not claim superiority for other tasks [@mccolemanRethinkingRanksVisual2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Orientation/area encodings may reduce conventional “read-off-a-axis” familiarity compared to standard bar/line position charts.
- **The Risk:** Viewers may interpret the chart as less standard even if reproduction error is lower in this context.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming “position is always best,” then defaulting to a line chart for any retrieve-value scenario.
- **Why it fails:** The 2-mark reproduction rankings place **position(line)** last among the tested channels in this context [@mccolemanRethinkingRanksVisual2022; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users confuse or drift when asked to redraw/recall the two values from a briefly shown line chart.
- **The Test:** Run a quick internal reproduction test: show the chart briefly, mask it, and ask users to recreate the two values; compare errors across encodings.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the 2-point line with an encoding that uses **orientation** for magnitude.
- **Best Fix:** Use an **area (bubble)** encoding for the two values (or an orientation-based encoding), if the goal is lowest reproduction error in this recall setting [@mccolemanRethinkingRanksVisual2022; @zengReviewCollationGraphical2023].
