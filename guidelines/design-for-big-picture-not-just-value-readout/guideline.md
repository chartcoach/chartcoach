---
id: design-for-big-picture-not-just-value-readout
title: Design for the Big Picture, Not Just Value Readout
bibliography: references.bib
description: When users need holistic patterns, prefer encodings that support overview
  perception even if they reduce per-value precision.
labels:
- task:summarize
- task:pattern
- visual:color
- visual:orientation
- impact:clarity
- data:multivariate
- audience:analyst
- source:bertini-why-not-scatterplots
---

## The Rule <!-- role: advice -->

When the goal is to perceive global patterns, prioritize encodings that make patterns emerge over encodings that maximize precise reading of individual values.

## The Logic <!-- role: reason -->

The paper’s “big picture” example argues that a position-encoded dot plot can be comparatively poor for holistic understanding, while other designs (e.g., line orientations or heatmap color fields) can better support pattern perception despite being less precise for extracting individual ratios [@bertiniWhyShouldntAll2020].

- **The Principle:** Emergent features and holistic perception
- **The Evidence:** [@bertiniWhyShouldntAll2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly grasping overall structure, recurring patterns, differences between years/series, or other “overview first” judgments.
- **Data Type:** Grids, seasonality matrices, multi-series time series, or any dataset where users reason across many values.
- **Audience:** Analysts or readers scanning for patterns rather than auditing exact numbers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The viewer’s main task is auditing exact values or computing precise pairwise ratios.
- **Reason:** Pattern-forward encodings can make exact read-off harder, which conflicts with the goal [@bertiniWhyShouldntAll2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced precision for individual values.
- **The Risk:** Viewers may over-trust perceived patterns when they actually need exact comparisons [@bertiniWhyShouldntAll2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Converting a pattern-seeking view into a dot plot solely to follow “position is best.”
- **Why it fails:** It can suppress emergent cues (e.g., orientation-based deltas, dense color fields) that support holistic judgments [@bertiniWhyShouldntAll2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can read points but struggle to answer “what’s going on overall?”
- **The Test:** Ask users to describe the pattern without reading numbers. If they can’t, the design may be too value-centric [@bertiniWhyShouldntAll2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an overview-friendly encoding that emphasizes patterns (e.g., a field-like view or connected structure) while keeping the same data.
- **Best Fix:** Choose a chart form whose strongest affordance is pattern perception for your specific “big picture” task, as argued in the paper’s discussion of alternative designs [@bertiniWhyShouldntAll2020].
