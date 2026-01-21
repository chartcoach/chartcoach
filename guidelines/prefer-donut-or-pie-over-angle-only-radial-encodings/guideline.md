---
id: prefer-donut-or-pie-over-angle-only-radial-encodings
title: Use Full Pie/Donut Wedges, Not Angle-Only Diagrams, for Percentage Reading
bibliography: references.bib
description: For reading percentages, full pie/donut wedges are more accurate than
  angle-only variants.
labels:
- chart:pie
- chart:donut
- task:retrieve-value
- visual:angle
- visual:area
- visual:arc-length
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception
---

## The Rule <!-- role: advice -->

Use a standard pie chart or donut chart (full wedges) instead of an angle-only chart when users must read a percentage value.

## The Logic <!-- role: reason -->

Angle alone is a weak cue for estimating part-to-whole in these designs; adding the other cues available in standard pie/donut wedges (the filled sector area and the circular arc boundary) improves accuracy.

- **The Principle:** Single-cue angle judgments are error-prone in this setting; redundant wedge cues support more accurate estimation.
- **The Evidence:** In a retrieve-value task, baseline donut and baseline pie outperformed both angle-only variants in accuracy rankings, with significant differences reported for baseline pie and baseline donut vs angle-only charts [@skauArcsAnglesAreas2016]. This finding is recorded as actionable guidance in the graphical-perception collation [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Retrieve a percentage (part-to-whole) from a single highlighted segment.
- **Data Type:** Quantitative values expressed as proportions/percentages (shown as a single segment against the remainder).
- **Audience:** General audiences (e.g., dashboards, reports, infographics).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally want a less-precise, schematic depiction of an angular interval rather than a part-to-whole percentage.
- **Reason:** The evidence here only supports accuracy for percentage retrieval; it does not claim angle-only is best for communicating “an angle” as a concept [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose the minimalist look of angle-only designs.
- **The Risk:** Full wedges may take more visual ink and can be harder to integrate into very constrained layouts.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Replacing a pie/donut with an angle-only depiction to “make the angle clearer.”
- **Why it fails:** Angle-only variants ranked worst for retrieve-value accuracy compared to baseline pie/donut in the reported results [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers frequently misread the highlighted segment magnitude or show high variability in estimates.
- **The Test:** A/B test your design: compare an angle-only version vs a baseline pie/donut on a simple “What percent is highlighted?” question set; if angle-only produces noticeably larger errors, it violates this rule (as observed in the study outcomes) [@skauArcsAnglesAreas2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert the angle-only display to a standard donut (filled ring segment) while preserving the same percentage.
- **Best Fix:** Use a baseline donut or baseline pie wedge design for the percentage-retrieval view, reserving angle-only marks only for non-quantitative, illustrative uses [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023].
