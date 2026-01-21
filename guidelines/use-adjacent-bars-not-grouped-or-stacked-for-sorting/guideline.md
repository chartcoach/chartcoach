---
id: use-adjacent-bars-not-grouped-or-stacked-for-sorting
title: Place Bars Adjacent for Sorting Comparisons
bibliography: references.bib
description: For sorting tasks, show the compared values as adjacent bars rather than
  grouped or stacked placements that separate the comparisons.
labels:
- chart:bar
- task:sort
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- layout:adjacent
- source:graphical-perception
---

## The Rule <!-- role: advice -->

When a sorting judgment depends on comparing two category values, place the compared bars **adjacent** (side-by-side) so users can compare their positions directly.

## The Logic <!-- role: reason -->

In the reported sorting experiment, the “adjacent bars” arrangement ranks best among multiple position-based bar arrangements, outperforming alternatives where bars are separated into groups or embedded in stacked constructions [@clevelandGraphicalPerceptionTheory1984]. The review collates this as part of the evidence that position-based designs can differ in effectiveness depending on the specific construction [@zengReviewCollationGraphical2023].

- **The Principle:** Minimizing spatial separation and keeping comparisons in a single shared positional frame improves accuracy for sorting.
- **The Evidence:** Adjacent-bar design ranks above other tested bar arrangements for sorting accuracy [@clevelandGraphicalPerceptionTheory1984], as recorded in the collation dataset [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Sort or rank items by value (especially quick “which is larger” comparisons).
- **Data Type:** One quantitative measure across nominal categories.
- **Audience:** General audiences; dashboards and reports.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must emphasize grouping structure more than sorting accuracy (e.g., explicitly separated subgroups are the primary message).
- **Reason:** The highest-accuracy layout for sorting may not be the clearest for communicating hierarchical grouping; the cited evidence targets sorting performance [@clevelandGraphicalPerceptionTheory1984; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Adjacent placement can increase width and crowd labels when there are many categories.
- **The Risk:** Overcrowding can introduce new readability issues even if the perceptual comparison mechanism is strong.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Spreading related comparisons across separated groups (forcing eye travel) while still expecting fast, accurate sorting.
- **Why it fails:** The grouped placement ranks lower than adjacent bars for sorting accuracy in the reported results [@clevelandGraphicalPerceptionTheory1984; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The two values a user must compare are not next to each other; they require scanning across whitespace or subgroup breaks.
- **The Test:** Trace the shortest eye path between the two bars—if it crosses other groups/blocks, adjacency is violated.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reorder or reposition so the compared categories are adjacent within the same bar group.
- **Best Fix:** Use a layout where all items to be sorted share a single aligned axis and are ordered to support direct adjacent comparisons [@clevelandGraphicalPerceptionTheory1984; @zengReviewCollationGraphical2023].
