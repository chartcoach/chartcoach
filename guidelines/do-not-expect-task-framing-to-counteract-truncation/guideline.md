---
id: do-not-expect-task-framing-to-counteract-truncation
title: Do Not Expect Task Framing to Counteract Truncation
bibliography: references.bib
description: Changing prompts from value-focused to trend-focused has only small effects
  compared to y-axis truncation.
labels:
- chart:bar
- chart:line
- task:judge
- visual:text
- visual:axis
- impact:integrity
- data:quantitative
- audience:general
- source:correll-bertini-franconeri-2020
---

## The Rule <!-- role: advice -->

Do not rely on wording changes (value-focused vs. trend-focused prompts) as your main mitigation for y-axis truncation effects.

## The Logic <!-- role: reason -->

Text framing can slightly shift judgments, but truncation produces much larger changes in perceived severity; the visual scaling dominates the subjective assessment.

- **The Principle:** Visual scale effects outweigh modest framing effects in severity judgments.
- **The Evidence:** In Experiment 1, truncation had a strong significant effect on perceived severity, while framing effects were small and not robust in post-hoc comparisons; truncation shifts were larger than framing shifts on the 1–5 scale [@correllTruncatingYAxisThreat2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Rating how different values are, or how quickly values change.
- **Data Type:** Simple sequences (2–3 points) displayed as bars or lines.
- **Audience:** Mixed literacy audiences in surveys, dashboards, or explanatory graphics [@correllTruncatingYAxisThreat2020a].

## When to Break It <!-- role: exceptions -->

- **Scenario:** You have already chosen an axis range aligned with meaningful effect sizes and are fine-tuning interpretation.
- **Reason:** Framing may still provide marginal steering, but it should not be the primary control compared to axis scaling [@correllTruncatingYAxisThreat2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Over-investing in copy changes instead of fixing scale can waste time and still leave the main bias intact.
- **The Risk:** You may believe you “balanced” interpretation while the chart’s scale continues to drive severity impressions [@correllTruncatingYAxisThreat2020a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a heavily truncated y-axis and switching the prompt to “trend” to make it feel more appropriate.
- **Why it fails:** The truncation-driven increase in perceived severity remains large relative to the framing shift [@correllTruncatingYAxisThreat2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ severity ratings track the y-axis start more than the question wording.
- **The Test:** Swap wording (value vs. trend) without changing the chart; if judgments barely change compared to changes from rescaling the y-axis, framing is not your lever [@correllTruncatingYAxisThreat2020a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust the y-axis start/end to reduce unwanted severity inflation.
- **Best Fix:** Treat axis range as the dominant driver of perceived effect size; use framing text only as a secondary, fine-grained complement [@correllTruncatingYAxisThreat2020a].
