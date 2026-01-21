---
id: space-gridlines-at-least-8-pixels-apart
title: Keep Gridlines at Least 8 Pixels Apart
bibliography: references.bib
description: Avoid overly dense gridlines; they can reduce accuracy by making tracing
  and labeling difficult.
labels:
- chart:line
- chart:bar
- task:compare
- visual:gridlines
- impact:accuracy
- data:quantitative
- audience:general
---

## The Rule <!-- role: advice -->

When adding gridlines, ensure adjacent gridlines are separated by at least 8 pixels.

## The Logic <!-- role: reason -->

In Heer & Bostock’s chart size/gridline study, dense gridlines on small charts increased error sharply; they conclude dense packing impedes accurate tracing to labels and recommend a minimum separation of 8 pixels [@heerCrowdsourcingGraphicalPerception2010a].

- **The Principle:** Visual clutter and tracing interference
- **The Evidence:** Increased error with tight gridline spacing; explicit “≥8 pixels” recommendation [@heerCrowdsourcingGraphicalPerception2010a]

## Where to Apply <!-- role: context -->

- **User Goal:** Estimate or compare values accurately using reference lines
- **Data Type:** Quantitative charts with a numeric axis (0–100 in the study)
- **Audience:** Web chart readers on typical displays

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not using gridlines for value reading (purely decorative/structural), or labels are not needed.
- **Reason:** The harm described is tied to tracing to labels for value judgments [@heerCrowdsourcingGraphicalPerception2010a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer reference cues if you increase spacing or remove gridlines.
- **The Risk:** Too few gridlines can reduce accuracy compared to moderate gridlines.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding many gridlines to “increase precision” on a small chart.
- **Why it fails:** Over-dense gridlines become a fence-like texture and interfere with reading [@heerCrowdsourcingGraphicalPerception2010a].

## How to Check <!-- role: check -->

- **Visual Sign:** Gridlines visually merge into a texture; users must hunt for the right line.
- **The Test:** Measure pixel distance between neighboring gridlines; if \<8px, you are in the risk zone identified by [@heerCrowdsourcingGraphicalPerception2010a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase gridline interval or reduce the number of gridlines.
- **Best Fix:** Choose gridline intervals that maintain ≥8px separation at the rendered chart height (and re-evaluate at responsive sizes) [@heerCrowdsourcingGraphicalPerception2010a].
