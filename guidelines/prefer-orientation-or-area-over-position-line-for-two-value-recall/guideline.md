---
id: prefer-orientation-or-area-over-position-line-for-two-value-recall
title: Prefer orientation or area over position-as-line when viewers must recall two
  quantitative values
bibliography: references.bib
description: For immediate recall of two values, orientation and area produced higher
  accuracy than a line-position encoding.
labels:
- chart:line
- chart:scatter
- chart:bar
- task:retrieve
- visual:orientation
- visual:area
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- complexity:advanced
---

## Prefer orientation/area over line-position for 2-value recall <!-- role: advice -->

When viewers must reproduce or recall two quantitative values immediately after a brief view, use an orientation encoding or an area encoding instead of a line chart position encoding.

## Why orientation/area can beat line-position in 2-value recall <!-- role: reason -->

This task depends on what the viewer can store and reproduce from short-term visual memory after a brief exposure, and some encodings can yield more accurate reproductions than others even when they are traditionally considered lower-precision for other tasks.

**Mechanism:** Orientation and area can produce memory representations that lead to smaller reproduction errors than line-position under brief, glance-like viewing and immediate redraw.

**Evidence:** For a retrieve-value reproduction task with 2 marks, orientation (E-6) and area (E-4) ranked highest in accuracy, and all non-line-position designs (orientation, area, luminance, length, bar-position) were significantly more accurate than line-position (E-2) under a Bayesian threshold of 0.9 [@mccolemanRethinkingRanksVisual2022; @zengReviewCollationGraphical2023].

**Notes:** This guidance is specific to the study’s immediate reproduction setting rather than general value reading with persistent axes.

## When immediate 2-value recall is the goal <!-- role: context -->

- **User Goal:** Reproduce or recall exact or near-exact values after a brief look.
- **Task:** Retrieve Value (immediate reproduction from memory).
- **Data:** Quantitative values with 2 marks (two items to remember).
- **Chart Setting:** Brief exposure and then redraw/reproduction (glance-like).
- **Audience:** General audiences with typical visual working memory limits.
- **Success Criterion:** Higher accuracy of recalled/reproduced values.

## When not to follow this for 2-value recall <!-- role: exceptions -->

**Break it when:** The user needs persistent, inspectable, absolute values over time with conventional reading support (axes, labels) rather than immediate recall. **Why:** The evidence is from a brief show–mask–reproduce task and may not transfer to sustained reading contexts.

## Tradeoffs of avoiding line-position here <!-- role: costs -->

**Sacrifice:** You may give up familiar time-series conventions and direct alignment to a shared axis baseline. **Risk:** Orientation or area may be harder to interpret for some audiences outside a controlled recall setting. **Mitigation:** Keep the task framing explicit (recall vs read-off) and validate with a small pilot in your target context.

## Common mistakes in applying this result <!-- role: mistakes -->

**Mistake:** Treating this as a universal rule that line charts are “worse” than orientation or area for quantitative values. **Why it fails:** The measured outcome was immediate reproduction accuracy for two marks, not general-purpose reading, trend detection, or comparison in typical analytic workflows.

## Quick checks for this decision <!-- role: check -->

**Failure Sign:** Users misremember the two values after a short look, especially when using line-position. **Quick Check:** Run a short “look for a second, then write down the two values” spot test with a handful of users on your intended encodings. **Stronger Test:** Replicate a show–remove–reproduce mini-study with your data ranges and measure absolute error across candidate encodings.

## What to do instead of line-position for 2-value recall <!-- role: fix -->

- Use an orientation-based mark encoding when the task is immediate reproduction of two values.
- Use an area-based encoding when the task is immediate reproduction of two values.
- If you must use position, prefer a bar-position encoding over a line-position encoding for this recall setting.
- Reduce cognitive load by ensuring only two marks must be remembered and reproduced in the view.
