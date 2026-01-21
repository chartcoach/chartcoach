---
id: choose-chart-type-by-communication-goal
title: Choose Your Chart Type Based on the One Thing You Need to Show
bibliography: references.bib
description: "Pick chart types by first deciding whether you\u2019re showing change\
  \ over time, shares, absolute numbers, correlations, flows, or geographic patterns."
labels:
- task:choose
- impact:clarity
- data:categorical
- audience:novice
- complexity:foundational
- source:datawrapper
---

## The Rule <!-- role: advice -->

Decide your chart’s primary communication goal first, then select chart types only from the matching family (time, shares, absolute numbers, correlations, flows, or maps).

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Goal-first constraint reduces irrelevant options and keeps the chart’s main statement coherent.
- **The Evidence:** The post organizes chart selection by user goals (time, shares, absolute, correlation, flows, geography) and emphasizes the “chart’s main statement becomes a compass” for choosing chart type and design choices [@muth_chart_types_guide_2025].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Choosing a chart type without getting overwhelmed by many options.
- **Data Type:** Any dataset where you can articulate the main message as one of: change over time, proportions, amounts, relationships, movement through a system, or spatial distribution.
- **Audience:** Mainstream/general audiences, especially beginners [@muth_chart_types_guide_2025].

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You truly need to communicate two different goals in one view (e.g., both “shares” and “absolute size” simultaneously).
- **Reason:** A single-goal selection may be insufficient; you may need a chart type that encodes both (or split into multiple charts) as hinted by options like Marimekko (absolute + relative) and small multiples for additional dimensions [@muth_chart_types_guide_2025].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** You might ignore visually “exciting” chart types you like.
- **The Risk:** Over-simplifying the message if you force complex questions into one goal bucket instead of using multiple views [@muth_chart_types_guide_2025].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Browsing chart galleries and picking a chart because it looks cool rather than because it matches the message.
- **Why it fails:** It increases cognitive load and can lead to mismatched encodings (e.g., using a pie when the task is precise comparison) [@muth_chart_types_guide_2025].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart seems to “say” one thing (e.g., percentages) while readers are expected to do another (e.g., compare small differences precisely).
- **The Test:** Write a one-sentence “This chart shows…” statement; if it doesn’t clearly map to one of the six goal families, re-scope or split the chart [@muth_chart_types_guide_2025].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Rewrite the chart’s main statement to match exactly one goal family, then swap to a chart type from that family.
- **Best Fix:** If you have multiple goals, split into a short sequence of charts that progresses from simple to more complex (as suggested in the post’s complexity guidance) [@muth_chart_types_guide_2025].
