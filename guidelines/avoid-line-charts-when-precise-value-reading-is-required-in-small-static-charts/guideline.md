---
id: avoid-line-charts-when-precise-value-reading-is-required-in-small-static-charts
title: Avoid line charts when precise value reading is required in small static charts
bibliography: references.bib
description: For several tasks requiring precise reading (e.g., retrieval and aggregation),
  line charts perform worst in accuracy and/or time compared to bars and tables in
  small static aggregated settings.
labels:
- chart:line
- task:retrieve-value
- task:aggregate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- scale:small-n
---

## Do not rely on line charts for precise value identification <!-- role: advice -->

Avoid using a line chart as the primary display when users must precisely identify values (such as retrieve-value or aggregate questions) in small static charts.

## Precise value tasks favor direct lookup or aligned magnitude reading <!-- role: reason -->

Tasks that depend on identifying specific values can be harmed when value reading is less direct, especially in static settings where the display does not privilege exact lookup.

**Mechanism:** When exact values are not immediately readable, users spend more time and make more errors, particularly on tasks that require extracting or combining specific values.

**Evidence:** In small (5–34 mark) aggregated chart settings, line-chart designs ranked last for retrieve-value in both accuracy and time, and ranked last for aggregate in accuracy and time compared with table and bar designs [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about precise value-based tasks, not about correlation judgments.

## Context: Exact value or arithmetic tasks on small static charts <!-- role: context -->

- **User Goal:** Read an exact value or compute a value from specific read-offs.
- **Task:** retrieve-value or aggregate.
- **Data:** Aggregated tabular summaries with limited marks (roughly 5–34).
- **Chart Setting:** Static 2D chart in a standard display.
- **Audience:** General readers or mixed visualization literacy.
- **Success Criterion:** Higher accuracy and faster completion on value-based questions.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The task is correlation judgment rather than exact value identification. **Why:** Line charts ranked highest for correlate in accuracy, time, and preference in the evidence.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Switching away from lines may reduce the sense of continuity that some audiences expect. **Risk:** If users expect trend depiction, replacing a line with a table may reduce perceived “chart-ness.” **Mitigation:** Align the primary chart type to the dominant task, and provide an alternate view for secondary tasks.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Using a line chart for value lookup tasks without providing a more direct lookup representation. **Why it fails:** Line designs ranked worst on retrieve-value and aggregate outcomes in the evidence.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users take noticeably longer on value questions or report difficulty reading exact values from the chart. **Quick Check:** Ask a user to answer a retrieve-value question from your line chart without pausing; if they need repeated back-and-forth scanning, the chart is a poor fit. **Stronger Test:** Compare error rates for the same retrieve-value questions using a line chart versus a table.

## Fix: What to do instead <!-- role: fix -->

- Use a table as the primary view for retrieve-value tasks in the same setting.
- Use a bar chart as the primary view for precise comparisons and ordered reading tasks.
- Separate correlation views (lines) from lookup/aggregation views (tables/bars) instead of forcing one chart to do both.
