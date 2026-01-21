---
id: use-difference-chart-for-fast-difference-measurement
title: Use a difference chart to speed up per-category difference measurement
bibliography: references.bib
description: For measuring the difference for a specific category, a difference chart
  is fastest, with overlay-based designs also faster than plain grouped bars.
labels:
- chart:bar
- task:aggregate
- visual:position
- impact:speed
- data:categorical
- audience:general
- comparison:multi-series
- derived:difference
---

## The Rule <!-- role: advice -->

When users must **measure the difference for a specific category**, use a **difference chart**; if you must keep the original bars visible, use **difference overlays** rather than a plain grouped bar chart.

## The Logic <!-- role: reason -->

Encoding differences directly (or via overlays) reduces the time needed versus mentally subtracting between two bars.

- **The Principle:** Externalize arithmetic by encoding the derived value.
- **The Evidence:** For difference measurement time, the ranks place **E-2 (difference chart)** fastest, and consistently place overlay designs ahead of the plain grouped bar (**E-4/E-3 faster than E-1**) with multiple significant differences reported [@srinivasanWhatsDifferenceEvaluating2018]. This task-specific performance knowledge is collated in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Read/enter the absolute change for a named category (e.g., “What is the change for April?”).
- **Data Type:** Two-series categorical/ordinal data requiring per-category delta reading.
- **Audience:** Dashboard users doing quick reporting/checks.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You prioritize raw series value lookup over delta reading.
- **Reason:** A difference chart focuses on derived differences, not raw series values, in the extracted design representation [@srinivasanWhatsDifferenceEvaluating2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Difference charts may require an additional view to also show the originals.
- **The Risk:** Users may lose baseline context when only differences are shown.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a grouped bar chart and expecting users to reliably subtract values for many categories.
- **Why it fails:** The plain grouped bar chart is slowest for this task in the reported time rankings [@srinivasanWhatsDifferenceEvaluating2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users repeatedly glance between two bars and take longer to answer a “difference for X” question.
- **The Test:** Ask for a numeric delta on a few categories; if response times are high with grouped bars, switch to difference encoding.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add difference overlays to the bar chart variant to externalize differences.
- **Best Fix:** Use a difference chart for the measurement task (and provide an adjacent raw-values chart if needed) [@srinivasanWhatsDifferenceEvaluating2018; @zengReviewCollationGraphical2023].
