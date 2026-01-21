---
id: do-not-treat-line-charts-as-exempt-from-truncation-bias
title: Do Not Treat Line Charts as Exempt from Truncation Bias
bibliography: references.bib
description: Expect y-axis truncation to increase perceived severity in line charts
  similarly to bar charts.
labels:
- chart:line
- chart:bar
- task:judge
- task:compare
- visual:axis
- impact:integrity
- data:temporal
- data:quantitative
- audience:general
- source:correll-bertini-franconeri-2020
---

## The Rule <!-- role: advice -->

Do not assume line charts are safer than bar charts with respect to y-axis truncation; expect similar inflation of perceived effect size.

## The Logic <!-- role: reason -->

Even though line charts encode value via position/angle rather than filled length, truncating the y-axis still increases the visual slope and separation, which drives higher subjective severity ratings.

- **The Principle:** Perceived severity responds to visual steepness and scaled separation, not just encoding type.
- **The Evidence:** Experiment 1 found truncation significantly increased perceived severity, with no significant difference between bar vs. line charts in the truncation effect [@correllTruncatingYAxisThreat2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Interpreting how fast something is changing, or how big the difference is.
- **Data Type:** Time series or ordered sequences shown as lines; categorical sequences sometimes shown as lines.
- **Audience:** Broad audiences who may rely on visual impression rather than numeric reading.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your task is to make small but important variation visible where a zero baseline would compress the trend into illegibility.
- **Reason:** The paper emphasizes designers must align the axis range with meaningful variation; not all truthful communication requires a zero baseline [@correllTruncatingYAxisThreat2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You cannot rely on “use a line chart” as a mitigation strategy.
- **The Risk:** You may inadvertently produce persuasive/biased impressions of trend severity by tightening the y-axis [@correllTruncatingYAxisThreat2020a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching from bars to a line chart to “avoid deception” while keeping the same truncated y-axis.
- **Why it fails:** The subjective inflation from truncation persists across both chart types [@correllTruncatingYAxisThreat2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** A modest numeric change appears as a steep line segment.
- **The Test:** Compare perceived severity ratings internally (or with reviewers) between a truncated and less-truncated version; if the “urgency” changes a lot, truncation is driving the message [@correllTruncatingYAxisThreat2020a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce truncation or provide a companion view with a broader y-axis range.
- **Best Fix:** Decide the y-axis range by the effect size scale you want viewers to judge (what differences should read as small vs. large), rather than by chart type conventions [@correllTruncatingYAxisThreat2020a].
