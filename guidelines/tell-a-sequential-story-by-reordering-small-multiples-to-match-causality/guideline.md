---
id: tell-a-sequential-story-by-reordering-small-multiples-to-match-causality
title: Reorder small-multiple panels to match your narrative sequence (especially
  when metrics are related)
bibliography: references.bib
description: Arrange small-multiple time series in a deliberate order so readers can
  follow a connected story rather than scanning unrelated trends.
labels:
- chart:line
- task:explain
- visual:layout
- impact:comprehension
- data:temporal
- audience:general
- technique:small-multiples
---

## Make panel order tell the story, not just show the data <!-- role: advice -->

Reorder small-multiple panels so they read as a deliberate sequence that matches the story you want the reader to follow. Use a single-row (or otherwise clearly linear) layout when you want that sequence to feel like an unfolding narrative.

## Why sequencing panels improves comprehension of related trends <!-- role: reason -->

When multiple indicators are conceptually connected, readers understand them better if the chart provides an explicit reading path. A linear panel order turns separate time series into a step-by-step explanation, helping the audience connect “inputs” and “outcomes” rather than interpreting each line in isolation.

**Mechanism:** A clear visual sequence reduces scanning ambiguity and encourages readers to integrate trends across panels as a single narrative rather than four separate observations.

**Evidence:** Turning a multi-line small-multiple chart into a “comic strip” by placing panels in a single row and reordering them to match a narrative makes it easier to guide readers through interrelated demographic trends and their combined implication. [@mintzer_sequential_storytelling_2024]

**Notes:** The “right” order is the order that supports your intended explanation; different valid stories can justify different sequences.

## When to use narrative panel ordering in small multiples <!-- role: context -->

- **User Goal:** Understand how multiple related metrics connect to produce a larger outcome.
- **Task:** Follow a step-by-step explanation across indicators rather than compare all indicators equally.
- **Data:** Multiple time series with different units/scales that are meaningfully linked (e.g., drivers and result).
- **Chart Setting:** Static or lightly interactive presentation where you can control reading order (article, report, slide).
- **Audience:** Readers who may not infer causal/structural connections from trends without guidance.
- **Success Criterion:** Readers can summarize the intended story in the intended order after a quick scan.

## When not to force a single narrative sequence <!-- role: exceptions -->

**Break it when:** Your main goal is neutral comparison across indicators (no privileged storyline). **Why:** A forced sequence can imply a causal chain or hierarchy that you are not actually claiming.

## Tradeoffs of linear narrative layouts <!-- role: costs -->

**Sacrifice:** You may give up space-efficient grids if you commit to a single-row or strongly ordered layout. **Risk:** The chosen order can bias interpretation toward one storyline and away from alternative readings. **Mitigation:** Ensure the sequence matches the story you explicitly want to tell and that the chart text does not over-claim.

## Common ways panel sequencing fails <!-- role: mistakes -->

- **Mistake:** Keeping the default or arbitrary panel order (e.g., alphabetical or dataset order). **Why it fails:** Readers won’t naturally see the intended connections and will interpret the panels as separate facts.
- **Mistake:** Using a multi-row layout that doesn’t signal a clear reading path. **Why it fails:** The narrative order becomes ambiguous, weakening the “step-by-step” effect.

## Quick ways to verify the sequence is working <!-- role: check -->

**Failure Sign:** Readers describe the chart as “two up, two down” (or other disconnected takeaways) instead of explaining how the metrics relate. **Quick Check:** Ask someone to read the panels once and state the story in one sentence; if they jump around, the order is not doing its job. **Stronger Test:** Run a short hallway test with 3–5 readers and see whether they recount the same sequence you intended.

## Practical alternatives if sequencing still feels unclear <!-- role: fix -->

- Put the panels in a single row (or another unmistakably linear arrangement) to enforce a reading direction.
- Rearrange the panels so the conceptual “inputs” appear before the “result” in the story you are telling.
- Split the story across multiple figures if one ordering cannot support the message without distortion.
- Add brief text annotations to bridge panel-to-panel transitions so the sequence is explicit.
