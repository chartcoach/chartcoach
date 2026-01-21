---
id: minimize-working-memory-by-reducing-eye-travel
title: Reduce Eye Travel to Lower Working-Memory Load
bibliography: references.bib
description: "Keep related information close together so viewers don\u2019t have to\
  \ remember details while scanning."
labels:
- chart:any
- task:integrate
- visual:layout
- impact:speed
- data:any
- audience:novice
- complexity:basic
---

## The Rule <!-- role: advice -->

Lay out charts so viewers do not need to repeatedly look back and forth between distant elements (plot, legend, bullets, annotations) to answer core questions.

## The Logic <!-- role: reason -->

- **The Principle:** Visual processing relies on the world as an “outside memory”; when information is far apart, limited working memory makes integration slow and error-prone.
- **The Evidence:** The paper explains that distant lookups (like ceiling vs dashboard GPS) increase effort, and identifies legends and separated conclusions as sources of unnecessary memory demand [@zacksDesigningGraphsDecisionMakers2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Integrating categories, values, and conclusions quickly and accurately.
- **Data Type:** Any visualization with multiple supporting elements.
- **Audience:** Non-experts and time-pressured decision-makers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When co-locating would create overlap/occlusion that prevents reading the data.
- **Reason:** If proximity destroys legibility, it defeats comprehension [@zacksDesigningGraphsDecisionMakers2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Layout flexibility; may require more space or reformatting.
- **The Risk:** Crowding if too much is packed together.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more explanatory text far from the chart.
- **Why it fails:** It increases integration burden and slows comprehension [@zacksDesigningGraphsDecisionMakers2020].

## How to Check <!-- role: check -->

- **Visual Sign:** A simple question requires multiple glances between separate regions.
- **The Test:** Track your own gaze: if answering requires repeated “ping-pong” between areas, memory demands are too high.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move the legend/notes closer; reduce the number of referenced elements.
- **Best Fix:** Replace lookups with direct encodings (direct labels, embedded explanations) so the viewer rarely has to leave the data region [@zacksDesigningGraphsDecisionMakers2020].
