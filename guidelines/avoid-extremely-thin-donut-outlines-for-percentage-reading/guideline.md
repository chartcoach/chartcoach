---
id: avoid-extremely-thin-donut-outlines-for-percentage-reading
title: Avoid Extremely Thin Donut Outlines When People Must Read Percentages
bibliography: references.bib
description: Very thin donut outlines reduce accuracy compared to thicker donuts for
  percentage retrieval.
labels:
- chart:donut
- task:retrieve-value
- impact:accuracy
- visual:arc-length
- visual:area
- data:quantitative
- audience:general
- custom:donut-inner-radius
- source:graphical-perception
---

## The Rule <!-- role: advice -->

Do not use an extremely thin donut outline (very large inner radius) if users must read percentage values; keep the donut ring reasonably thick.

## The Logic <!-- role: reason -->

As the donut becomes extremely thin, the display approaches an arc-length-only cue and accuracy degrades relative to thicker donut forms.

- **The Principle:** Removing too much ring thickness reduces usable magnitude cues for percent estimation.
- **The Evidence:** In the inner-radius comparison (retrieve-value-2), the 20% inner-radius donut and the 80% inner-radius donut ranked above the 97% inner-radius variant, with significant differences reported specifically showing 20% and 80% outperforming 97% [@skauArcsAnglesAreas2016]. This relationship is included as structured evidence in the collation dataset [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Retrieve a numeric percentage from a donut-like proportion chart.
- **Data Type:** Quantitative part-to-whole values.
- **Audience:** General audiences; especially when donut thickness is being adjusted for styling.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your goal is a minimalist “outline” aesthetic and you accept reduced numeric reading accuracy.
- **Reason:** The evidence shows a measurable accuracy penalty for the thinnest condition relative to at least some thicker ones [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up ultra-minimal thin-ring styling and some whitespace.
- **The Risk:** Thicker rings can crowd internal labels or central annotations.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Making the donut ring as thin as possible to “modernize” the look while keeping it a quantitative reading chart.
- **Why it fails:** The very thin (97% inner radius) variant performed worse than thicker donuts in the ranked results, and was significantly worse than at least the 20% and 80% conditions [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The ring looks like a hairline arc; users hesitate or give inconsistent numeric estimates.
- **The Test:** Compare user error on your thinnest ring vs a thicker ring for the same values; if thin-ring error jumps, thicken it (consistent with the study’s significant pair results) [@skauArcsAnglesAreas2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the inner radius so the ring is visibly thick (move away from an outline).
- **Best Fix:** Use a baseline donut (moderate ring) or baseline pie wedge if precise percentage reading matters most [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023].
