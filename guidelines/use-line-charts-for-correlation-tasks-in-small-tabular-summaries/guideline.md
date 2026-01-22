---
id: use-line-charts-for-correlation-tasks-in-small-tabular-summaries
title: Use line charts for correlation tasks on small aggregated tabular data
bibliography: references.bib
description: For correlation judgments in small aggregated tabular data, line charts
  yield higher accuracy, faster completion, and higher user preference than other
  basic chart types.
labels:
- chart:line
- task:correlate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- scale:small-n
---

## Use line charts for correlation judgments <!-- role: advice -->

Use a line chart when the user’s task is to judge whether two quantitative variables are correlated in a small aggregated dataset.

## Correlation perception benefits from line-based position patterns <!-- role: reason -->

Correlation judgments can be supported when a chart makes the overall relationship pattern easy to perceive as a coherent positional structure across values.

**Mechanism:** A continuous line connecting values can make overall co-variation easier to judge than designs that emphasize discrete lookup or part-to-whole encoding.

**Evidence:** For the correlate task, line-chart designs ranked best for both accuracy and time, and also ranked best in user-preference compared with bar, scatterplot, table, and pie designs in a crowdsourced experiment on small (5–34 mark) aggregated charts [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].

**Notes:** This guideline applies to the small, aggregated chart settings captured in the evidence.

## Context: Correlation task on small aggregated charts <!-- role: context -->

- **User Goal:** Decide whether two attributes are strongly correlated.
- **Task:** correlate.
- **Data:** Two quantitative attributes, shown in small aggregated views (roughly 5–34 marks).
- **Chart Setting:** Static 2D chart in a standard display.
- **Audience:** General readers or mixed visualization literacy.
- **Success Criterion:** Higher accuracy and faster completion, with good user preference.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The user must read exact values precisely for specific points rather than judge the overall relationship. **Why:** The evidence separates correlation from value-retrieval, and different chart types ranked highest for retrieve-value.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Precise value lookup can be less direct than a table or bar chart in small static displays. **Risk:** Viewers may over-focus on the connected shape rather than individual values. **Mitigation:** Keep the focus on correlation questions rather than exact-value questions.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Using a pie chart for correlation. **Why it fails:** Pie designs ranked last for both accuracy and user preference on correlate in the study evidence.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Readers answer correlation questions slowly or inconsistently across similar charts. **Quick Check:** Ask two people to judge “strong vs not strong correlation” on the same data in a line chart vs a pie chart; the line chart should feel easier. **Stronger Test:** Run a small timed comprehension test for correlate questions using line vs alternatives.

## Fix: What to do instead <!-- role: fix -->

- Switch from pie or table to a line chart when the primary question is correlation.
- If you must stay with a non-line option, prefer a scatterplot design over pie or table for correlate questions.
- Separate correlation questions into a dedicated view instead of overloading a value-lookup view.
