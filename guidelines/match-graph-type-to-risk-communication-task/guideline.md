---
id: match-graph-type-to-risk-communication-task
title: Match chart type to the risk communication task (comparison, trend, or proportion)
bibliography: references.bib
description: Choose bar charts for comparisons, line graphs for trends over time,
  and pie charts for part-to-whole judgments when communicating health risks.
labels:
- chart:bar
- chart:line
- chart:pie
- task:compare
- task:trend
- task:proportion
- visual:position
- impact:clarity
- data:categorical
- data:temporal
- audience:novice
- domain:risk-communication
---

## Choose bar charts for comparisons, line graphs for trends, and pie charts for proportions <!-- role: advice -->

Use bar charts to compare risk magnitudes across groups, line graphs to show how risk changes over time, and pie charts to show part-to-whole proportions.

## Why chart-type-to-task alignment improves comprehension <!-- role: reason -->

Graph types differ in the perceptual judgments they make easy (comparison, trend detection, or proportion estimation). Aligning the chart with the viewer’s intended judgment reduces interpretive effort and makes the intended inference more direct.

**Mechanism:** Matching the display to the judgment leverages familiar visual mappings (e.g., height for “more”) and supports the intended mental operation (e.g., compare heights, track a trajectory, estimate a share of a whole).

**Evidence:** Bar charts are described as well-suited for comparisons (including subgroup comparisons), line graphs for trends over time and interactions, and pie charts for judging proportions (with known biases) in reviews of graphical risk communication. [@lipkusNumericVerbalVisual2007]

**Notes:** This is about the primary task the graphic must support; secondary tasks may require additional annotation or a different display.

## When the chart type decision matters most <!-- role: context -->

- **User Goal:** Understand and compare health risk likelihoods or their change over time.
- **Task:** Compare groups; understand a trajectory; judge part-to-whole.
- **Data:** Categorical groups, temporal series, or proportions within a whole.
- **Chart Setting:** Patient education materials, decision aids, clinical discussions, or public health communications.
- **Audience:** General public and patients with mixed graph literacy.
- **Success Criterion:** Viewers can make the intended judgment (comparison, trend, proportion) without misreading the display.

## When not to follow it <!-- role: exceptions -->

- **Break it when:** The audience is unfamiliar with the proposed chart type in the given domain (for example, survival curves). **Why:** Unfamiliar displays can be misunderstood without extra explanation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose the ability to show multiple patterns in a single compact figure. **Risk:** A “task-matched” chart can still mislead if the audience lacks graph literacy or if the display is complex. **Mitigation:** Use clear explanations of what the viewer should conclude from the graph.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using an unfamiliar or complex plot type for a lay audience. **Why it fails:** People may not know how to interpret it and will default to superficial cues or ignore it.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers can describe the graphic but cannot answer the core question it was meant to support. **Quick Check:** Ask a pilot reader what conclusion they take from the chart in one sentence. **Stronger Test:** Run a small comprehension check comparing two candidate chart types for the same task.

## What to do instead <!-- role: fix -->

- Use a bar chart when the key message is a magnitude comparison across groups.
- Use a line graph when the key message is risk changing over time or differing trajectories.
- Use a proportion-focused display only when the key message is part-to-whole, and keep it simple.
- Add a short textual explanation that states the intended inference from the chart.
