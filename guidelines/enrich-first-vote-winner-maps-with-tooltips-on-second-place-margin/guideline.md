---
id: enrich-first-vote-winner-maps-with-tooltips-on-second-place-margin
title: Add Second-Place Margins to Winner Map Tooltips
bibliography: references.bib
description: On winner-take-all district maps, include tooltip details about the runner-up
  and winning margin to add competitive context.
labels:
- chart:map
- task:explain
- visual:interaction
- impact:context
- data:geospatial
- audience:general
- domain:elections
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

On choropleth maps of winner-take-all “first vote” districts, include tooltip information about the first- and second-place parties and the winning margin. [@muth_german_election_2021]

## The Logic <!-- role: reason -->

A winner map alone hides competitiveness; adding runner-up and margin in tooltips reveals whether a district was a landslide or a close race without cluttering the map surface.

- **The Principle:** Layer detail-on-demand to add context without visual overload
- **The Evidence:** [@muth_german_election_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand not just who won each district, but how close it was
- **Data Type:** District winners plus vote shares (or vote counts) for first and second place
- **Audience:** General readers exploring district outcomes interactively [@muth_german_election_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart will be used in static form (no hover/tooltips).\
  **Reason:** Tooltip-only insights would disappear; the margin would need to be encoded differently. [@muth_german_election_2021]
- **Scenario:** You don’t have reliable second-place data.\
  **Reason:** Tooltips would be incomplete or misleading. [@muth_german_election_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:** More data prep and tooltip design work
- **The Risk:** Users who don’t interact may miss the key insight unless prompted with instructions (“hover to see margin”). [@muth_german_election_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing only the winner category per district.\
  **Why it fails:** It implies uniform strength and hides close contests. [@muth_german_election_2021]
- **The Wrong Fix:** Trying to print margins as labels on every district.\
  **Why it fails:** The map becomes unreadable due to label clutter. [@muth_german_election_2021]

## How to Check <!-- role: check -->

- **Visual Sign:** The map communicates winners but gives no sense of “tight vs. safe” seats.
- **The Test:** Hover a few districts: if you can’t quickly learn winner, runner-up, and margin, the tooltip is not doing its job. [@muth_german_election_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add tooltip fields for winner share, second-place share, and margin (votes or percentage points). [@muth_german_election_2021]
- **Best Fix:** Use the map for winners and reserve competitiveness detail for tooltips, plus a short note in the annotation encouraging hover interaction. [@muth_german_election_2021]
