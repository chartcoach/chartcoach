---
id: treat-circular-slice-charts-as-competitive-with-pies-for-part-to-whole-sort-accuracy
title: Use Circular Slice Charts as a Competitive Alternative to Pie Charts for Part-to-Whole
  Sorting
bibliography: references.bib
description: Circular slice variants performed on par with or better than pie charts
  for accuracy in part-to-whole sort judgments in one study.
labels:
- chart:pie
- chart:radial
- task:sort
- visual:angle
- visual:area
- data:categorical
- data:quantitative
- impact:accuracy
- audience:general
- custom:chart-variant
---

## The Rule <!-- role: advice -->

If you need a circular part-to-whole display for a **sort** task, consider **circular slice** (area-based) or **straight-line circular** variants as viable (and potentially better) options than a standard **pie chart**.

## The Logic <!-- role: reason -->

- **The Principle:** Different circular designs can change how precisely people compare part sizes in part-to-whole judgments.
- **The Evidence:** In an experiment comparing five part-to-whole chart designs, **circular slice** and **straight-line circular** conditions ranked alongside the top performer group and ahead of the **pie chart** for accuracy in a sort task (pie ranked below that top group) [@kosaraImpactDistributionChart2019]. This outcome is explicitly recorded in the structured collation intended for recommendation rules [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Sort/order parts of a whole by percentage.
- **Data Type:** Nominal categories with quantitative part-to-whole percentages.
- **Audience:** General audiences where a circular form is desired.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your tooling or style guide cannot render or maintain consistent semantics for these nonstandard circular variants.
- **Reason:** The evidence supports their comparative accuracy in a specific tested context; it does not claim they are universally appropriate in all environments [@kosaraImpactDistributionChart2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced familiarity compared with standard pies may affect acceptability (not measured here as a preference outcome).
- **The Risk:** Viewers may not immediately recognize the encoding without explanation or labeling, since these are less common chart forms.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming “all circular charts are the same as pie charts” and choosing randomly among radial designs.
- **Why it fails:** The study’s accuracy ranking differs across circular designs and the standard pie chart; design choice matters [@kosaraImpactDistributionChart2019; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users confuse which slice/segment is being compared or mis-rank slices in sorting tasks.
- **The Test:** Run a quick A/B test: have users perform the same sort task with your pie chart and with a circular slice variant; compare error rates.

## How to Fix <!-- role: fix -->

- **Quick Fix:** If using a pie chart now, prototype a circular-slice or straight-line circular alternative and re-test sorting accuracy.
- **Best Fix:** Choose the circular design variant that empirically supports your task (sorting parts) rather than defaulting to a standard pie chart [@kosaraImpactDistributionChart2019; @zengReviewCollationGraphical2023].
