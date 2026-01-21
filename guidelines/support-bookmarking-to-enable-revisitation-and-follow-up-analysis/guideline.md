---
id: support-bookmarking-to-enable-revisitation-and-follow-up-analysis
title: Add Bookmarking for Revisit and Follow-Up
bibliography: references.bib
description: Let users save interesting recommended views for later review, sharing,
  or deeper analysis.
labels:
- chart:gallery
- task:curate
- visual:interaction
- impact:workflow
- data:any
- audience:analyst
- system:collaboration
---

## The Rule <!-- role: advice -->

Provide a one-click way to bookmark recommended charts and keep them in a dedicated bookmark gallery for later revisitation.

## The Logic <!-- role: reason -->

Voyager treats early exploration as a stage that produces candidate insights for later targeted investigation; bookmarking supports revisitation and sharing, and participants used it to collect findings during exploratory sessions [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Capturing intermediate findings during EDA
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Save promising patterns while continuing to explore broadly
- **Data Type:** Any exploratory workflow where users will return to specific views
- **Audience:** Analysts conducting iterative analysis

## When to Break It <!-- role: exceptions -->

- **Scenario:** Highly ephemeral, single-view interactions where users never browse multiple charts.
- **Reason:** Bookmarking adds overhead without providing revisitation value.

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional UI elements (buttons, a bookmark area) and state management.
- **The Risk:** Users may over-bookmark without organization, creating a cluttered collection.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Relying on users to remember “the good chart” or recreate it later.
- **Why it fails:** In breadth-oriented exploration, users encounter many views; without capture, valuable leads are lost [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users stop exploring to take external notes or screenshots of charts.
- **The Test:** Ask users to return to an earlier interesting view; if it’s hard, bookmarking is insufficient.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a bookmark button on each chart thumbnail and a bookmark gallery view.
- **Best Fix:** Store bookmarks as portable visualization specifications so users can revisit, share, or hand off to other tools for deeper analysis [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
