---
id: use-alpha-0-2-as-a-safe-default-for-gridline-contrast
title: Default Gridlines to About 0.2 Alpha for Non-Intrusive Visibility
bibliography: references.bib
description: A gridline alpha around 0.2 is a safe compromise between visibility and
  intrusiveness across conditions.
labels:
- chart:scatter
- task:read
- visual:opacity
- impact:clarity
- data:quantitative
- audience:general
---

## The Rule <!-- role: advice -->

Use an alpha (opacity) value around 0.2 as a default for gridlines to keep them visible but not dominant.

## The Logic <!-- role: reason -->

Replicating Stone & Bartram, Heer & Bostock found alpha preferences depend more on plot density than background intensity, and their crowdsourced results corroborated the recommendation that alpha ≈ 0.2 is a “safe” default [@heerCrowdsourcingGraphicalPerception2010a]. This value balances being perceptible without forming a foreground “fence.”

- **The Principle:** Luminance layering for reference elements
- **The Evidence:** Crowdsourced replication supports alpha=0.2 as safe default [@heerCrowdsourcingGraphicalPerception2010a]

## Where to Apply <!-- role: context -->

- **User Goal:** Use gridlines as subtle references without stealing attention from data marks
- **Data Type:** Scatterplots (and similar plots) where gridlines are optional aids
- **Audience:** General web users on varied displays

## When to Break It <!-- role: exceptions -->

- **Scenario:** Extremely dense data or situations where gridlines must be minimized or removed.
- **Reason:** Density significantly affects acceptable alpha; heavier grids can become intrusive (“fence”) [@heerCrowdsourcingGraphicalPerception2010a].

## The Price <!-- role: costs -->

- **The Sacrifice:** A single default may not be optimal for every density/display.
- **The Risk:** On some displays/users, 0.2 may still be too strong or too faint.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Setting gridlines near fully opaque “for readability.”
- **Why it fails:** Users report a fence-like effect where gridlines sit in front of the data [@heerCrowdsourcingGraphicalPerception2010a].

## How to Check <!-- role: check -->

- **Visual Sign:** Grid appears in the foreground or competes with points/lines.
- **The Test:** Ask viewers to adjust toward “as light as possible while usable” and compare typical picks to ~0.2 (the paper’s safe default) [@heerCrowdsourcingGraphicalPerception2010a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce gridline alpha toward 0.2.
- **Best Fix:** Adapt alpha based on plot density (since density showed a significant effect) and validate with a quick adjustment task as in [@heerCrowdsourcingGraphicalPerception2010a].
