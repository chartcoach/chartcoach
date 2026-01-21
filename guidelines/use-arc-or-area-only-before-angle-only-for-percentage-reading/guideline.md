---
id: use-arc-or-area-only-before-angle-only-for-percentage-reading
title: Prefer Arc-Length-Only or Area-Only Over Angle-Only for Percentage Reading
bibliography: references.bib
description: If you must simplify a pie/donut, arc-length-only or area-only encodings
  yield better accuracy than angle-only.
labels:
- chart:pie
- chart:donut
- task:retrieve-value
- visual:arc-length
- visual:area
- visual:angle
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception
---

## The Rule <!-- role: advice -->

When simplifying a pie/donut-style display for reading percentages, use an arc-length-only or area-only encoding rather than an angle-only encoding.

## The Logic <!-- role: reason -->

For percentage retrieval, the study’s accuracy ranking places the arc-length-only and area-only designs above both angle-only variants.

- **The Principle:** For part-to-whole estimation here, arc length and filled area provide more usable magnitude cues than isolated angle marks.
- **The Evidence:** In retrieve-value accuracy rankings, the arc-length chart and area-only chart both ranked ahead of the angle-only pie and angle-only donut, and all four (pie, donut, arc, area) showed significant advantages over the angle-only variants via reported significant-difference pairs [@skauArcsAnglesAreas2016]. This ordering is preserved in the extracted knowledge base described by the collation work [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Read a single highlighted segment’s percentage.
- **Data Type:** Quantitative proportion/percentage.
- **Audience:** General audiences; scenarios where a stylized or minimal radial encoding is desired but you still want reasonable numeric reading accuracy.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need to communicate an explicit angular quantity (the concept of an angle) rather than a percent-of-whole value.
- **Reason:** The evidence here is specific to retrieve-value for percentages; it does not evaluate conceptual angle communication goals [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Arc-only and area-only variants may be less familiar than standard pie/donut wedges.
- **The Risk:** Users may require brief explanation if the form is uncommon in your context (the rule is about accuracy, not familiarity).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using “clean” angle-only lines/arrows to reduce ink while expecting pie-like readability.
- **Why it fails:** Angle-only variants were the worst performers for retrieve-value accuracy in the ranked results and were significantly worse than other variants [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Wide spread of answers (high variability) for angle-only encodings compared to arc-only/area-only.
- **The Test:** Run a small internal test: show users the same percentage set in arc-only, area-only, and angle-only formats; if angle-only yields noticeably larger errors, replace it [@skauArcsAnglesAreas2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the angle-only depiction with an arc-length ring segment (thin donut) or a filled proportional-area shape.
- **Best Fix:** Use a baseline pie or baseline donut (full wedges) if you can afford the extra ink; they ranked best overall among the compared designs [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023].
