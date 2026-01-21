---
id: connected-scatterplot-reinforce-that-both-axes-matter
title: Remind Viewers to Read Both Axes
bibliography: references.bib
description: Prevent misinterpretations caused by over-weighting the vertical axis
  in connected scatterplots.
labels:
- chart:scatter
- task:interpret
- visual:annotation
- impact:clarity
- data:temporal
- audience:novice
- chart:connected-scatterplot
---

## The Rule <!-- role: advice -->

Include explicit cues that both x and y encode values (not time), and that “low on y” does not mean “low overall.”

## The Logic <!-- role: reason -->

Some viewers apply habits from more familiar chart types, over-attending to the y-axis; in a connected scatterplot that can produce incorrect conclusions about magnitude because x and y both carry meaning [@harozConnectedScatterplotPresenting2016].

- **The Principle:** Transfer errors from familiar chart conventions
- **The Evidence:** In qualitative tasks, an error occurred where a participant inferred both variables were low because y was low, despite x being high—reflecting y-axis overreliance in the connected scatterplot format [@harozConnectedScatterplotPresenting2016].

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly interpret levels and changes of both variables at specific times/segments.
- **Data Type:** Paired time series with meaningful variation on both axes.
- **Audience:** Viewers more familiar with time-on-x line charts than connected scatterplots.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Highly annotated, guided storytelling where each key point is explicitly labeled with both values.
- **Reason:** Direct value labeling can already force attention to both axes [@harozConnectedScatterplotPresenting2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra annotation and potentially less visual elegance.
- **The Risk:** Over-annotation can crowd the plot and compete with the path shape.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding only a y-axis title and assuming the x-axis will be read by default.
- **Why it fails:** The observed misinterpretation was specifically consistent with neglecting x-values [@harozConnectedScatterplotPresenting2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Important regions sit low on y but far right on x (or vice versa), making single-axis impressions misleading.
- **The Test:** Ask a colleague to describe the magnitude of both variables at a point without prompting; if they mention only y, add reinforcement.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add concise annotation like “x = [variable], y = [variable] (time follows the path).”
- **Best Fix:** Label key points with both coordinates (or add callouts) in regions where single-axis reading would be especially misleading [@harozConnectedScatterplotPresenting2016].
