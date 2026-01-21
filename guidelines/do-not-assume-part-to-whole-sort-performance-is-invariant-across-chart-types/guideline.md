---
id: do-not-assume-part-to-whole-sort-performance-is-invariant-across-chart-types
title: Evaluate Chart Type Choice for Part-to-Whole Sorting Instead of Assuming Equivalence
bibliography: references.bib
description: Accuracy and time rankings differed across five part-to-whole chart types
  in an experiment, indicating chart choice changes performance.
labels:
- chart:pie
- chart:treemap
- chart:stacked-bar
- chart:radial
- task:sort
- impact:quality-control
- data:categorical
- data:quantitative
- audience:general
- custom:process
---

## The Rule <!-- role: advice -->

Do not treat part-to-whole chart types as interchangeable for **sort** tasks; pick the chart type explicitly based on whether you need **accuracy** or **speed**.

## The Logic <!-- role: reason -->

- **The Principle:** Chart design changes user performance; different designs trade off accuracy vs time.
- **The Evidence:** The experiment reports different rankings for **accuracy** (with treemap worst and pie below the top group) and for **time** (with circular variants fastest and significantly faster than pie/stacked bar/treemap) on the same sort task [@kosaraImpactDistributionChart2019]. The review emphasizes translating such empirical rankings into actionable recommendation rules [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Sorting/ordering part-to-whole segments (e.g., “rank categories by share”).
- **Data Type:** A small set of categorical parts of a whole with quantitative percentages.
- **Audience:** Any audience where mistakes or delays have material cost (dashboards, reports with decisions).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot change chart type due to strict brand or platform limitations.
- **Reason:** This rule is about choosing among chart types; if you have no choice, you must mitigate via other means (not covered by this evidence).

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires time to prototype and possibly A/B test chart alternatives.
- **The Risk:** Over-optimizing for one metric (speed) may harm the other (accuracy), since rankings are not identical across metrics [@kosaraImpactDistributionChart2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** “Always use pie for part-to-whole” or “always replace pie with treemap.”
- **Why it fails:** The study shows measurable performance differences across these alternatives for the same part-to-whole sorting task [@kosaraImpactDistributionChart2019; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Stakeholders disagree on the ordering of slices/segments or take noticeably long to answer.
- **The Test:** Identify whether your key KPI is accuracy or response time; then compare at least two chart candidates against that KPI with representative users.

## How to Fix <!-- role: fix -->

- **Quick Fix:** If accuracy problems appear with treemaps, move to stacked bars (accuracy-ranked above treemap).
- **Best Fix:** Maintain two recommended defaults in your design system—one optimized for accuracy and one for speed—based on the empirical rankings captured in the collation [@zengReviewCollationGraphical2023; @kosaraImpactDistributionChart2019].
