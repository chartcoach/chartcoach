---
id: connected-scatterplot-remind-viewers-to-read-both-axes
title: Remind connected-scatterplot readers to interpret both axes, not only the vertical
  axis
bibliography: references.bib
description: Prevent misreadings caused by treating connected scatterplots like single-axis
  trend charts.
labels:
- chart:scatter
- task:interpret
- visual:annotation
- impact:clarity
- data:temporal
- audience:novice
- custom:connected-scatterplot
---

## Make it explicit that both the horizontal and vertical values matter in a connected scatterplot <!-- role: advice -->

Add design cues that encourage reading both axes for any claim about “high” or “low” values. Do not let the vertical axis dominate the interpretation.

## Viewers may default to y-axis-centric reading habits from more familiar charts <!-- role: reason -->

Many readers are habituated to charts where the main variable is on the vertical axis and time is on the horizontal axis, so they may overweight the vertical position and underweight the horizontal position. In a connected scatterplot, that habit can produce incorrect statements about the data because each point is defined by two values.

**Mechanism:** Explicit reminders counter a learned heuristic (“look at y to judge magnitude”) that is valid in many common charts but invalid for full interpretation of points in a connected scatterplot.

**Evidence:** In qualitative questioning, a viewer concluded both variables were “minimal” in a highlighted region even though the horizontal-axis variable was relatively high, consistent with overweighting the vertical axis in a connected scatterplot [@harozConnectedScatterplotPresenting2016].

**Notes:** This problem is distinct from time-direction confusion; it is about interpreting magnitudes in a 2D value space.

## Situations where y-axis dominance is likely <!-- role: context -->

- **User Goal:** Decide whether both variables are high/low, increasing/decreasing, or “in tandem.”
- **Task:** Describe a highlighted segment or summarize a period.
- **Data:** Connected scatterplots with regions where one axis is low while the other is high.
- **Chart Setting:** Static charts with brief callouts, where readers may skim and anchor on the vertical axis.
- **Audience:** Viewers with strong familiarity with line charts but low familiarity with connected scatterplots.
- **Success Criterion:** Readers correctly describe both variables’ levels and changes in the targeted region.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization’s message is intentionally about one variable’s value while the other serves only as an index-like dimension. **Why:** Over-emphasizing both axes can distract from a deliberately single-variable takeaway.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional labels, cues, or annotation space. **Risk:** Over-cueing can feel didactic and may reduce the clean aesthetic that makes the format engaging. **Mitigation:** Keep cues lightweight and integrate them with existing annotations.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming that a low vertical position implies the overall state is “low.” **Why it fails:** The horizontal-axis value may be high at the same point, so the joint state is not low across variables [@harozConnectedScatterplotPresenting2016].

## Quick tests for axis-balance problems <!-- role: check -->

**Failure Sign:** Viewers make statements that only reference one axis (“it’s low here”) when both variables are relevant. **Quick Check:** Pick a point with low y but high x and see whether the chart makes that obvious. **Stronger Test:** Ask readers to report both coordinates qualitatively (high/medium/low) for marked points.

## What to do instead <!-- role: fix -->

- Add point labels or callouts that reference both variables for key regions.
- Add start/end annotations and intermediate notes that explicitly mention changes in each variable.
- If the narrative is mainly about each series over time rather than their joint states, use a dual-axis line chart instead.
