---
id: support-selection-to-reduce-clutter-and-focus-attention
title: Support Selection That Greys Out Unselected Items
bibliography: references.bib
description: Provide selection-based highlighting to reduce clutter and help users
  focus on specific trajectories.
labels:
- chart:scatter
- task:focus
- visual:highlight
- impact:clarity
- data:temporal
- audience:expert
- interaction:selection
---

## The Rule <!-- role: advice -->

Provide selection that highlights chosen items and greys out (and de-emphasizes) all others when inspecting trends.

## The Logic <!-- role: reason -->

De-emphasizing non-selected items reduces clutter and makes the selected trajectories more salient, improving the user’s ability to inspect specific trends within dense displays.

- **The Principle:** Salience through de-emphasis of competing marks
- **The Evidence:** In both Animation and Traces, the study’s tools allowed selecting bubbles to show traces while unselected bubbles/traces were greyed out to deal with clutter and occlusion [@robertsonEffectivenessAnimationTrend2008].

## Where to Apply <!-- role: context -->

- **User Goal:** Verifying an anomaly, following a particular entity, or comparing a few entities against the background
- **Data Type:** Dense multi-entity trend displays (animated or overlaid traces)
- **Audience:** Analysts exploring or presenters demonstrating specific cases

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is to judge distributional behavior of all entities equally (no focal subset).
- **Reason:** Grey-out emphasis can bias attention away from the full population pattern [@robertsonEffectivenessAnimationTrend2008].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced visibility of the overall context when a subset is emphasized.
- **The Risk:** Users may over-focus on selected items and miss broader patterns [@robertsonEffectivenessAnimationTrend2008].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Highlighting selected items without de-emphasizing others in a crowded view.
- **Why it fails:** Salience gains are limited when everything remains equally strong; clutter remains [@robertsonEffectivenessAnimationTrend2008].

## How to Check <!-- role: check -->

- **Visual Sign:** Selected trajectories do not stand out clearly from the background.
- **The Test:** Select one item; if it’s still hard to follow its path, the de-emphasis is too weak [@robertsonEffectivenessAnimationTrend2008].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Grey non-selected marks and reduce their opacity.
- **Best Fix:** Combine greying with showing traces only for selected items (as implemented in the paper’s animation tool) [@robertsonEffectivenessAnimationTrend2008].
