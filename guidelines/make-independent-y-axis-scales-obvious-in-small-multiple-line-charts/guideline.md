---
id: make-independent-y-axis-scales-obvious-in-small-multiple-line-charts
title: Make Per-Panel Y-Axis Scales Obvious
bibliography: references.bib
description: If small-multiple panels use different y-scales, explicitly warn and
  visually cue the difference to prevent misreads.
labels:
- chart:line
- task:interpret
- visual:scale
- impact:accuracy
- data:temporal
- audience:general
- chart:small-multiples
- complexity:advanced
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

If your small multiple line chart uses different y-axis scales across panels, explicitly signal it in the chart description and with visual cues so readers notice.

## The Logic <!-- role: reason -->

Readers may assume all panels share one y-scale; when scales differ, that assumption produces false insights. Making the scaling difference salient reduces the chance of misinterpretation [@muth_small_multiple_line_charts_2024].

- **The Principle:** Prevent false equivalence from implied common scale
- **The Evidence:** [@muth_small_multiple_line_charts_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly interpret trends without assuming comparable magnitudes across panels
- **Data Type:** Small multiple line charts with independent y-axes
- **Audience:** General readers who may not inspect every axis carefully

## When to Break It <!-- role: exceptions -->

- **Scenario:** All panels share the same y-axis scale.
- **Reason:** No special warning is needed; adding one could create confusion about a problem that doesn’t exist [@muth_small_multiple_line_charts_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra explanatory text and possibly less elegant visuals.
- **The Risk:** Even with cues, some readers may still overlook the note and misread magnitudes [@muth_small_multiple_line_charts_2024].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using independent scales but presenting panels with normal-looking gridlines and no explanation.
- **Why it fails:** Readers don’t notice the change and assume comparability across panels [@muth_small_multiple_line_charts_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Panels look comparable at a glance, but their y-axis ticks/labels differ.
- **The Test:** Hide axes mentally and ask, “Could a reader assume these panels share a scale?” If yes, your cues are insufficient [@muth_small_multiple_line_charts_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a clear sentence in the description (e.g., instruct readers to notice that y-axis scalings differ).
- **Best Fix:** Avoid independent scales where possible; if you keep them, combine explicit description with noticeable visual cues (e.g., gridlines that don’t look “normal”) so the difference is hard to miss [@muth_small_multiple_line_charts_2024].
