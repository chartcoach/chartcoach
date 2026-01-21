---
id: use-navigation-order-to-match-priorities
title: Order Menus and View Options to Reflect Intended Priority
bibliography: references.bib
description: Avoid accidental framing from interaction conventions like list order
  and first-position effects.
labels:
- task:guide
- impact:framing
- custom:rhetoric:procedural
- audience:general-public
---

## The Rule <!-- role: advice -->

Order interactive choices (menus, “view more” lists) to match the priority you intend readers to perceive.

## The Logic <!-- role: reason -->

Spatial ordering and navigation conventions influence what users click first; listing one view first can implicitly privilege it and reinforce anchoring effects.

- **The Principle:** Procedural prioritization through ordering conventions
- **The Evidence:** [@hullmanVisualizationRhetoricFraming2011a]

## Where to Apply <!-- role: context -->

- **User Goal:** Explore multiple facets of a dataset
- **Data Type:** Dashboards or narrative interactives with multiple map/chart modes
- **Audience:** General readers following common web navigation habits

## When to Break It <!-- role: exceptions -->

- **Scenario:** Alphabetical ordering is required to support lookup tasks
- **Reason:** When findability is the primary goal, editorial priority ordering may hinder users.

## The Price <!-- role: costs -->

- **The Sacrifice:** Perceived neutrality (priority order looks editorial)
- **The Risk:** Users may accuse the design of bias if ordering implies agenda without disclosure.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Random or arbitrary ordering (“whatever came first”)
- **Why it fails:** There is no neutral order in practice; conventions will still privilege early items [@hullmanVisualizationRhetoricFraming2011a].

## How to Check <!-- role: check -->

- **Visual Sign:** One view receives disproportionate engagement simply because it is first
- **The Test:** Reorder the list and observe whether the likely exploration path changes; if so, order is a framing device.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add section headers (“Primary view,” “More maps”) to make prioritization explicit.
- **Best Fix:** Align ordering with a stated narrative structure (e.g., overview-first then details) and explain it briefly.
