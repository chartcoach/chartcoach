---
id: prefer-log-y-scale-over-juxtaposed-linear-for-time-series-comparison-tasks
title: Prefer a Log Y-Scale Line Chart Over a Juxtaposed Linear Small-Multiple for
  Time-Series Comparison
bibliography: references.bib
description: For time-series comparison tasks, use a log-scaled superimposed line
  chart rather than a row-faceted linear one to improve performance.
labels:
- chart:line
- task:correlate
- task:aggregate
- visual:position
- visual:color
- data:temporal
- audience:general
- scale:log
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When supporting **correlate** or **aggregate** tasks on time-series line plots, choose a **log-scaled Y-axis** superimposed line chart instead of a **row-faceted (juxtaposed) linear-scale** line chart.

## The Logic <!-- role: reason -->

A log scale changes how vertical position maps to values, enabling users to more effectively judge changes and comparisons along the Y dimension in this setting.

- **The Principle:** Scale choice affects comparative judgments from position on a shared axis.
- **The Evidence:** This guideline is derived from collated empirical rankings in [@zengReviewCollationGraphical2023], based on results reported in [@aignerBertinWasRight2011], where the log-scale superimposed design outperformed the juxtaposed linear design in both accuracy and time for the recorded tasks.

## Where to Apply <!-- role: context -->

- **User Goal:** Compare series (correlate) and summarize/compare across series (aggregate).
- **Data Type:** Time-series shown as lines with time on X (ordinal) and values on Y (quantitative), potentially with multiple series distinguished by color hue.
- **Audience:** General audiences doing visual comparisons (no specialized training assumed).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your primary need is to preserve linear-unit interpretability on the Y-axis for the viewer.
- **Reason:** A log transform changes the mapping between vertical distance and raw units, which can conflict with expectations of linear reading.

## The Price <!-- role: costs -->

- **The Sacrifice:** Direct “in original units” interpretation of vertical distances on Y.
- **The Risk:** Viewers may misread magnitudes if they assume the Y-axis is linear.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the Y-axis linear and just splitting series into rows (small multiples) to “make it clearer.”
- **Why it fails:** In the collated evidence, the row-faceted linear design is ranked below the log-scale superimposed design for the captured tasks [@zengReviewCollationGraphical2023; @aignerBertinWasRight2011].

## How to Check <!-- role: check -->

- **Visual Sign:** You are using a linear Y-axis and separating series by rows (small multiples) for comparison tasks.
- **The Test:** Prototype both versions (log superimposed vs linear row-faceted) and run a quick timed accuracy check on representative correlate/aggregate questions; prefer the log superimposed if it yields fewer errors and faster responses, consistent with the reported ranking [@zengReviewCollationGraphical2023; @aignerBertinWasRight2011].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the Y scale from **linear** to **log** while keeping the rest of the line chart design stable.
- **Best Fix:** Use a **superimposed** multi-series log-scale line chart (distinguish series with color hue) rather than splitting series into separate row facets, matching the better-ranked design in the collated results [@zengReviewCollationGraphical2023; @aignerBertinWasRight2011].
