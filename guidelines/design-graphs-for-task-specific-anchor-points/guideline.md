---
id: design-graphs-for-task-specific-anchor-points
title: Design Graph Comparisons Around a Single Task-Relevant Anchor Point
bibliography: references.bib
description: "Make the intended comparison revolve around one salient, consistent\
  \ anchor to support the viewer\u2019s visual routine."
labels:
- chart:bar
- task:compare
- visual:attention
- impact:clarity
- data:categorical
- audience:novice
- source:michal-franconeri-2017
---

## The Rule <!-- role: advice -->

Make the intended comparison depend on a single, task-relevant anchor point (one “reference” bar/value viewers can reliably look at first), and keep that anchor consistent across the display.

## The Logic <!-- role: reason -->

People extract between-value relations with a serial “visual routine” that often begins by attending to an idiosyncratic but consistent anchor feature (e.g., “taller” for size judgments, “darker” for contrast judgments). When multiple potential relations are present, attention is guided by the task-relevant dimension’s anchor, and other dimensions can interfere.

- **The Principle:** Task-dependent visual routines anchored on a preferred feature
- **The Evidence:** Eye movements showed strong, consistent first-saccade biases to dimension-specific anchors (taller for size; darker for contrast), and those biases persisted only for the task-relevant dimension when size and contrast varied together [@michalVisualRoutinesAre2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which of two values is larger (or determine configuration/order)
- **Data Type:** Very small-N comparisons (e.g., two bars) where multiple visual dimensions could encode relations
- **Audience:** Learners/novices or any audience doing fast relational judgments

## When to Break It <!-- role: exceptions -->

- **Scenario:** You explicitly want users to explore multiple relations (e.g., both size and contrast) as part of the task
- **Reason:** A single-anchor design biases attention toward one relation; the paper shows other relations can compete and slow judgments when present [@michalVisualRoutinesAre2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less flexibility for open-ended exploration of alternative relations
- **The Risk:** Over-emphasizing one anchor can cause users to miss other patterns that might be meaningful for their broader goals

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding multiple relations simultaneously (e.g., varying both height and darkness) while assuming viewers will “just focus” on the right one
- **Why it fails:** Task-irrelevant relations can still interfere with performance even when viewers’ eye movements are guided by the relevant dimension [@michalVisualRoutinesAre2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Two different features each suggest a different “first thing to look at” (e.g., tallest bar is not the darkest)
- **The Test:** Ask: “If someone looks first at the most visually compelling element, is it guaranteed to be the task-relevant anchor?”

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove variation in task-irrelevant visual dimensions for that comparison (e.g., keep contrast constant if height is the comparison).
- **Best Fix:** Redesign so the intended relation is the only strong relational cue present, ensuring the anchor for the relevant dimension is unambiguous [@michalVisualRoutinesAre2017].
