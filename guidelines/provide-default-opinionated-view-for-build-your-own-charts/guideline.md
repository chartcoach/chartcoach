---
id: provide-default-opinionated-view-for-build-your-own-charts
title: "Provide a Default, Opinionated View Before \u201CBuild Your Own\u201D"
bibliography: references.bib
description: When users can construct their own charts, provide a meaningful default
  view of the data as the starting point to reduce cognitive and functional labor.
labels:
- chart:interactive
- task:explore
- visual:multichannel
- impact:accessibility
- data:multivariate
- audience:novice
- principle:assistive
- source:community-practices
---

## The Rule <!-- role: advice -->

If your interface requires users to craft their own chart (e.g., choosing variables and encodings), provide a default, opinionated view of the data as the starting point.

## The Logic <!-- role: reason -->

A default view reduces the amount of planning, configuration, and interpretation work users must do before they can access any insight, lowering cognitive and functional labor in “build-your-own” analytic workflows, as captured in the Assistive principle of Chartability [@elavskyHowAccessibleMy2022].

- **The Principle:** Labor-reducing access (Assistive: Understandable + Perceivable)
- **The Evidence:** Chartability’s “No default ‘build-your-own’ provided” heuristic (synthesized from community practices) [@elavskyHowAccessibleMy2022]

## Where to Apply <!-- role: context -->

This advice is designed for analytic environments where chart construction is part of the workflow.

- **User Goal:** Get oriented and start analysis without first configuring a visualization
- **Data Type:** Multivariate datasets where users select variables/encodings to generate charts
- **Audience:** People with disabilities and other users who may face high cognitive load in exploratory “build-your-own” interfaces [@elavskyHowAccessibleMy2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The experience does not require users to build a chart (the visualization is already authored)
- **Reason:** The rule only applies when the interface expects users to assemble a chart themselves [@elavskyHowAccessibleMy2022]

## The Price <!-- role: costs -->

- **The Sacrifice:** You must pick (and maintain) an opinionated starting configuration rather than remaining fully neutral.
- **The Risk:** The default may not match every user’s immediate analytical intent, potentially biasing first impressions [@elavskyHowAccessibleMy2022]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing an empty canvas with only controls (variables, encodings, filters) and requiring the user to assemble the first view.
- **Why it fails:** It leaves users without an initial, accessible foothold, increasing cognitive burden in precisely the “build-your-own” situation this heuristic targets [@elavskyHowAccessibleMy2022]

## How to Check <!-- role: check -->

- **Visual Sign:** The interface opens to a blank/empty chart area and only becomes meaningful after the user makes multiple configuration choices.
- **The Test:** Start from a fresh session and attempt to learn something from the data without changing any settings; if you can’t, the default view is missing [@elavskyHowAccessibleMy2022]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Preload a single, sensible chart configuration (preselected variables and encodings) so the initial screen shows a meaningful view immediately [@elavskyHowAccessibleMy2022]
- **Best Fix:** Provide a well-chosen default view as the primary starting point while still allowing users to modify and “build their own” from that baseline [@elavskyHowAccessibleMy2022]
