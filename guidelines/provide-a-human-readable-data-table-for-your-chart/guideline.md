---
id: provide-a-human-readable-data-table-for-your-chart
title: Provide a Human-Readable Data Table for Your Chart
bibliography: references.bib
description: Include a human-readable data table for the data underlying a chart unless
  the surrounding text already conveys all relevant information.
labels:
- chart:any
- task:read-values
- visual:any
- impact:accessibility
- data:any
- audience:general
- principle:compromising
- source:chartability
---

## The Rule <!-- role: advice -->

Provide a human-readable table containing the data your chart is based on, unless the chart title, summary, context, or annotations already convey all relevant information in the chart.

## The Logic <!-- role: reason -->

A table provides a transparent, redundant information flow that can be consumed in a non-visual, text-based format and can support understanding when the visualization alone is not accessible or not sufficient for interpretation [@elavskyHowAccessibleMy2022]. Guidance for describing scientific visuals also emphasizes including data tables where appropriate to make complex visuals understandable to blind readers and to support clear definition of variables and relationships [@wgbh_effective_practices_2; @wgbh_effective_practices_3].

- **The Principle:** Redundant, transparent information flows (Compromising: Understandable + Robust) [@elavskyHowAccessibleMy2022]
- **The Evidence:** Guidance that includes providing data tables where appropriate to support non-visual understanding [@wgbh_effective_practices_2; @wgbh_effective_practices_3]

## Where to Apply <!-- role: context -->

This advice is designed for charts where users may need access to the underlying values in a text form.

- **User Goal:** Retrieve or confirm specific values and details that the chart encodes
- **Data Type:** Any chart-backed dataset where underlying values matter for interpretation
- **Audience:** People using assistive technologies (including screen readers) and anyone who benefits from a text-based representation [@elavskyHowAccessibleMy2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart title, summary, context, or annotations already convey all relevant information contained in the chart.
- **Reason:** The table is optional when the surrounding text fully communicates what the table would add, making it redundant without improving access [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional space and authoring effort to include a complete, human-readable table [@elavskyHowAccessibleMy2022].
- **The Risk:** Teams may treat the table as a full substitute for accessibility work and stop improving the chart’s own accessibility and interaction support, even though Chartability explicitly warns that “having a table doesn’t mean everything else about a chart can pass” [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Providing only a table and claiming it is an equivalent replacement for the visualization.
- **Why it fails:** Chartability notes that chart structures can communicate relationships that are not inherently tabular, and that a table alone does not guarantee an accessible or equivalent experience (especially for interaction and navigation) [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart is presented without any accompanying table of the underlying data.
- **The Test:** Verify whether a human-readable table exists for the same dataset, and if not, check whether the title/summary/context/annotations fully convey all relevant information contained in the chart [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a basic human-readable table that lists the chart’s underlying data values.
- **Best Fix:** Provide the table and also ensure the chart’s meaning is conveyed through sufficient title/summary/context/annotations so users have multiple, transparent ways to access the same information [@elavskyHowAccessibleMy2022; @wgbh_effective_practices_2; @wgbh_effective_practices_3].
