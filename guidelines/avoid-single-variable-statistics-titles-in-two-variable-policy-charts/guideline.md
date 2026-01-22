---
id: avoid-single-variable-statistics-titles-in-two-variable-policy-charts
title: Avoid titles that mention only one variable when the chart supports opposing
  policy interpretations
bibliography: references.bib
description: A title can look neutral while subtly steering attention to the variable
  that supports one side of a debated issue.
labels:
- chart:general
- task:frame
- visual:text
- impact:fairness
- data:multivariate
- audience:general
- topic:controversial
---

## Do not title a two-variable contentious chart by mentioning only the variable that favors one side <!-- role: advice -->

When your visualization includes multiple measures that can imply opposite conclusions, do not write a title that highlights only one measure unless you intentionally want that framing to dominate.

## Why “neutral-sounding” statistics can still be slanted <!-- role: reason -->

Titles that reference “just the data” can still act as framing by selecting which part of the data is salient, especially when only one of multiple variables is mentioned.

**Mechanism:** A “statistics frame” title can appear objective while cueing attention to a particular variable, prompting viewers to connect the dots toward the implied stance.

**Evidence:** The study identified a common “statistics frame” in titles (variable/trend/value) and found that slanted titles shift the perceived main message of the same visualization, even though viewers often judge the information as neutral [@kongFramesSlantsTitles2018].

**Notes:** The subtlety can increase persuasive power because it does not trigger skepticism.

## When this applies to your chart/title decisions <!-- role: context -->

- **User Goal:** Decide what the chart implies about a policy question or controversial claim.
- **Task:** Interpret which side the evidence supports.
- **Data:** Two (or more) variables where each can be used to argue different sides (e.g., totals vs shares).
- **Chart Setting:** News, social media, advocacy, or dashboards used in debate.
- **Audience:** Viewers likely to scan the title and form a takeaway quickly.
- **Success Criterion:** The title does not hide that multiple measures matter for interpretation.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The publication explicitly presents a single-variable argument and the visualization is intended as supporting evidence for that argument. **Why:** The title is serving advocacy rather than balanced summarization.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Balanced titles may be longer or less striking. **Risk:** Over-balancing can reduce memorability or make the title feel noncommittal. **Mitigation:** Use a concise main title plus a short subtitle listing the second measure.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Titling a chart with only the normalized metric (or only the absolute metric) and implying it is the whole story. **Why it fails:** Viewers treat the highlighted metric as the chart’s core message and may ignore the other measure.

## Quick tests <!-- role: check -->

**Failure Sign:** The title could apply equally well to a chart that omitted the other variable entirely. **Quick Check:** Ask whether a reader could infer that a second measure exists from the title. **Stronger Test:** Have readers describe what “the chart is about”; if they mention only the titled variable, the title is likely steering attention.

## What to do instead <!-- role: fix -->

- Mention both measures in the title or use a subtitle to list the second measure.
- Replace a single-variable title with an open-ended topic title when neutrality is required.
- Add a short phrase that signals dual-metric structure (e.g., “in totals and per-capita terms”).
- If you must emphasize one measure, disclose the selection explicitly (e.g., “By share of population…”).
