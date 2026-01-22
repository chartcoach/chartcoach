---
id: avoid-tables-and-pie-charts-for-correlation-tasks-in-small-aggregated-data
title: Avoid tables and pie charts for correlation tasks in small aggregated data
bibliography: references.bib
description: For correlation judgments, tables and pie charts perform worse than position-based
  charts in accuracy, time, and user preference in small aggregated settings.
labels:
- chart:table
- chart:pie
- task:correlate
- visual:angle
- impact:accuracy
- data:quantitative
- audience:general
- scale:small-n
---

## Do not use tables or pies to judge correlation <!-- role: advice -->

Avoid using a table or a pie chart when the user’s primary task is to judge correlation between two variables in a small aggregated dataset.

## Correlation needs relationship perception, not lookup or part-to-whole <!-- role: reason -->

Correlation tasks require perceiving a relationship between two attributes; encodings optimized for lookup (tables) or part-to-whole proportion (pies) can make that relationship harder to assess.

**Mechanism:** When the display does not strongly support perceiving co-variation patterns, viewers must infer correlation indirectly, increasing errors and time.

**Evidence:** For the correlate task, table and pie designs ranked lowest for accuracy and user preference, and pie designs also ranked slowest in completion time compared with line, scatter, and bar designs in a crowdsourced experiment on small aggregated charts [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].

**Notes:** This is specifically about correlation judgment, not about retrieving exact values.

## Context: Correlation questions on small aggregated views <!-- role: context -->

- **User Goal:** Decide whether two attributes are strongly correlated.
- **Task:** correlate.
- **Data:** Two quantitative attributes presented in a small aggregated chart setting (roughly 5–34 marks).
- **Chart Setting:** Static 2D chart in a standard display.
- **Audience:** General readers or mixed visualization literacy.
- **Success Criterion:** Higher accuracy, faster completion, and higher user preference.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The task is not correlation but exact-value retrieval or aggregation where tables may be competitive. **Why:** The evidence shows tables can rank highest for retrieve-value and aggregate tasks.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Removing tables may reduce support for exact numeric lookup in the same view. **Risk:** Users who strongly prefer tables may resist switching even if performance improves. **Mitigation:** Provide a table as a secondary view for lookup, not the primary view for correlation.

## Mistakes: Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a pie chart to show two quantitative variables and asking for correlation. **Why it fails:** Pie designs ranked lowest across correlate outcomes in the evidence.
- **Mistake:** Using a table and expecting users to infer correlation quickly. **Why it fails:** Table designs ranked lowest on accuracy for correlate in the evidence.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users respond “not sure” or show high disagreement on correlation judgments. **Quick Check:** If the view does not show two variables as a direct positional relationship, treat it as suspect for correlation. **Stronger Test:** Time a small set of correlate questions across your current chart vs a line chart and compare error rates.

## Fix: What to do instead <!-- role: fix -->

- Use a line chart for correlation questions in the same small aggregated setting.
- Use a scatterplot as an alternative position-based option for correlation questions.
- Keep tables for value lookup, not for relationship judgments like correlation.
- Move part-to-whole displays (pies) to tasks like composition or proportion rather than correlation.
