---
id: separate-semantic-groups-with-white-space
title: Separate Semantic Groups with White Space Gaps
bibliography: references.bib
description: Use whitespace boundaries to carve a word cloud into clearly separated
  semantic regions for better analytic performance and preference.
labels:
- chart:word-cloud
- task:summarize
- task:categorize
- visual:position
- visual:whitespace
- impact:clarity
- data:categorical
- audience:general
- source:hearst-2020
---

## The Rule <!-- role: advice -->

Use visible whitespace gaps to separate semantic groups so group boundaries are unmistakable.

## The Logic <!-- role: reason -->

Whitespace creates strong visual boundaries that help viewers isolate one group at a time. In the experiments, column-style layouts (which inherently use whitespace separation) dramatically outperformed Wordle-style layouts on time-limited topic/category understanding, and organized layouts with gaps were also preferred for analytic tasks [@hearstEvaluationSemanticallyGrouped2020].

- **The Principle:** Boundary salience via spatial separation.
- **The Evidence:** Column layouts (with clear separation) beat Wordles; participants preferred more organized, gapped layouts for analytic tasks [@hearstEvaluationSemanticallyGrouped2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify multiple topics quickly from one display.
- **Data Type:** Multiple distinct semantic groups shown simultaneously.
- **Audience:** People doing analytic reading/interpretation of the display.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must minimize whitespace for extreme space constraints.
- **Reason:** The paper shows that performance can remain high with semantic spatial clustering plus color even when whitespace is reduced (BSC vs. columns differences were not statistically distinguishable) [@hearstEvaluationSemanticallyGrouped2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Lower packing density; fewer words fit in a fixed area.
- **The Risk:** Overly large gaps can make the visualization feel sparse or wasteful.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keep a tight pack and assume proximity alone will be noticed without clear “breaks.”
- **Why it fails:** Without clear separators, viewers may not perceive group structure reliably, undermining the benefit of semantic organization [@hearstEvaluationSemanticallyGrouped2020].

## How to Check <!-- role: check -->

- **Visual Sign:** It is ambiguous where one group ends and another begins.
- **The Test:** Ask a viewer to trace group boundaries with their finger/cursor; if they hesitate or disagree with others, boundaries aren’t visually strong enough [@hearstEvaluationSemanticallyGrouped2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase spacing between groups more than spacing within groups.
- **Best Fix:** Use a layout that inherently creates separated regions (e.g., columns or other explicit partitions) while keeping within-group words close [@hearstEvaluationSemanticallyGrouped2020].
