---
id: prefer-area-over-position-line-for-4-to-8-mark-value-recall
title: "Prefer Area Over Line Position for 4\u20138 Value Recall"
bibliography: references.bib
description: "For recalling multiple quantitative values (4\u20138), area encodings\
  \ ranked best for reproduction accuracy while line-position ranked worst."
labels:
- chart:line
- chart:scatter
- task:retrieve-value
- visual:area
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- marks:4
- marks:8
- source:empirical
---

## The Rule <!-- role: advice -->

For immediate recall/reproduction of **4–8 quantitative values**, prefer **area (bubble)** encodings and avoid **position-based line charts**.

## The Logic <!-- role: reason -->

- **The Principle:** As the number of marks increases, channel choice interacts with memory limits; effectiveness rankings can shift by task and mark-count.
- **The Evidence:** In the retrieve-value reproduction task, **area** ranked best for **4 marks**, **6 marks**, and **8 marks**, while **position(line)** ranked worst in each corresponding condition [@mccolemanRethinkingRanksVisual2022]. These results are captured in the collation and structured rankings in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Briefly view a chart and then reproduce/recall several values (4–8 marks).
- **Data Type:** Quantitative series shown as discrete marks.
- **Audience:** Any audience; especially relevant when expecting “glance then act/compare” behaviors.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must use a line chart because continuity/line-connection itself is required by the analytic intent (not tested here as a separate factor).
- **Reason:** The evidence isolates performance in a reproduction task, not broader reasons to use connected lines [@mccolemanRethinkingRanksVisual2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Area/bubble encodings may trade away some conventions users expect for series.
- **The Risk:** If users treat the visualization as requiring exact axis reading, they may find area encodings less natural despite reproduction performance benefits in this study.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Scaling up a line chart for multi-value recall tasks because lines are common for sequences.
- **Why it fails:** In these conditions, **position(line)** is consistently ranked worst for reproduction accuracy compared to other tested channels [@mccolemanRethinkingRanksVisual2022; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users recall the overall “shape” but misstate individual values after a brief line-chart exposure.
- **The Test:** A/B test line-position vs bubble-area with a timed show–mask–reproduce protocol and compare absolute errors.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap the line chart to a bubble/area mark encoding for the same values.
- **Best Fix:** Use **area (bubble)** encoding when the key success metric is lower reproduction error for 4–8 marks, as supported by the reported rankings [@mccolemanRethinkingRanksVisual2022; @zengReviewCollationGraphical2023].
