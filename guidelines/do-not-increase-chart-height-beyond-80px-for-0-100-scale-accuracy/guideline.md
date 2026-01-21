---
id: do-not-increase-chart-height-beyond-80px-for-0-100-scale-accuracy
title: Stop Increasing Chart Height Beyond ~80 Pixels When Accuracy Has Plateaued
bibliography: references.bib
description: "For 0\u2013100 value ranges, increasing chart height beyond ~80px yielded\
  \ little accuracy improvement in value comparisons."
labels:
- chart:line
- chart:bar
- task:compare
- visual:size
- impact:efficiency
- data:quantitative
- audience:general
---

## The Rule <!-- role: advice -->

For charts using a 0–100 scale, do not increase chart height beyond roughly 80 pixels if your goal is comparison accuracy.

## The Logic <!-- role: reason -->

Heer & Bostock found that 40px-tall charts produced significantly more error, but accuracy showed no significant improvement among taller conditions once height reached 80px and above (tested up to 320px) [@heerCrowdsourcingGraphicalPerception2010a]. They suggest the plateau occurs near where pixel and data resolutions match for the scale.

- **The Principle:** Diminishing returns from increased spatial resolution
- **The Evidence:** Significant error penalty at 40px; no significant differences among 80/160/320px heights [@heerCrowdsourcingGraphicalPerception2010a]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare or subtract values from marked points with minimal error
- **Data Type:** Quantitative values mapped to vertical position/length on a 0–100 range
- **Audience:** Web users viewing standard charts

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your y-range is much larger than 0–100 (or you need more pixel-per-unit resolution for other reasons).
- **Reason:** The plateau was observed specifically on a 0–100 scale; different scales may shift the saturation point [@heerCrowdsourcingGraphicalPerception2010a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Taller charts consume more layout space without improving accuracy.
- **The Risk:** If you keep charts too short (e.g., 40px), error rises significantly.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Making charts taller to “guarantee accuracy” without checking whether accuracy already plateaued.
- **Why it fails:** Past ~80px (for 0–100), extra height did not buy measurable accuracy in their study [@heerCrowdsourcingGraphicalPerception2010a].

## How to Check <!-- role: check -->

- **Visual Sign:** Large vertical whitespace with minimal added readability.
- **The Test:** If your chart spans 0–100, compute pixels-per-unit (height/100). At ~0.8 px/unit and above, expect diminishing accuracy returns per [@heerCrowdsourcingGraphicalPerception2010a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce height to ~80px and reallocate space (labels, annotations, or multiple small charts).
- **Best Fix:** Tune height based on scale and required precision; verify with a targeted comparison task test as in [@heerCrowdsourcingGraphicalPerception2010a].
