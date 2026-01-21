---
id: use-redundant-encodings-when-they-support-the-task
title: Use Redundant Encodings When They Support the Task
bibliography: references.bib
description: Add redundant cues (e.g., bars adding length/area) when they improve
  interpretation for the intended task, even if position already encodes values.
labels:
- chart:bar
- task:compare
- visual:position
- visual:length
- impact:clarity
- audience:designer
- source:bertini-why-not-scatterplots
---

## The Rule <!-- role: advice -->

Add redundant encodings (e.g., length/filled area in bars) when they make the intended judgments easier, even if position already encodes the same values.

## The Logic <!-- role: reason -->

The paper argues that designs with “extra” encodings can outperform pure position-only designs for certain perceptual tasks (e.g., a bar chart being more useful than a dot plot for seeing aspects of the “big picture”), because redundant cues can support interpretation beyond precise value extraction [@bertiniWhyShouldntAll2020].

- **The Principle:** Redundancy can aid perception and interpretation
- **The Evidence:** [@bertiniWhyShouldntAll2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Quick comparative scanning, overview judgments, or judgments that benefit from stronger visual mass/structure.
- **Data Type:** Small-to-medium categorical comparisons, repeated grids of values, and contexts where users need easy judgments rather than exact read-off.
- **Audience:** Mixed audiences (including novices) who benefit from stronger cues.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The design must be extremely compact or avoid visual clutter.
- **Reason:** Redundant marks can increase ink/space and potentially interfere with other encodings [@bertiniWhyShouldntAll2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** More space and visual weight than minimal dot/position-only marks.
- **The Risk:** Over-encoding can create clutter that hinders other tasks [@bertiniWhyShouldntAll2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating redundancy as “chartjunk” without considering task benefits.
- **Why it fails:** The paper’s argument is that “inefficiency” can be functional for tasks beyond value extraction [@bertiniWhyShouldntAll2020].

## How to Check <!-- role: check -->

- **Visual Sign:** A minimalist dot view makes users hunt mark-by-mark to understand differences.
- **The Test:** Time a quick “what stands out?” scan. If users must read many points explicitly, redundancy may help [@bertiniWhyShouldntAll2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from dots to bars (or otherwise add a redundant magnitude cue) for the same values.
- **Best Fix:** Select the minimal redundancy that improves the specific judgment you care about (overview vs exact read-off), consistent with the paper’s framing [@bertiniWhyShouldntAll2020].
