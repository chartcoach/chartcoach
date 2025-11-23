---
id: tooltip-runner-up-margins
title: Include Runner-Up Margins in Tooltips
bibliography: references.bib
description: Add context to winner-take-all maps by listing the second-place candidate
  and the vote margin in the tooltip.
labels:
- chart:map
- task:drill-down
- visual:text
- impact:depth
- data:categorical
- audience:analyst
---

## The Rule <!-- role: advice -->
In "winner-take-all" visualization tooltips, include the name of the second-place candidate and the specific vote margin between them and the winner.

## The Logic <!-- role: reason -->
Winner-take-all maps (choropleths colored by the winning party) flatten the data into a binary outcome, hiding how close a race actually was. The text highlights that "one of the more interesting aspects to explore is the margin for the unlucky candidate who got second place" [@muth_german_election_2021]. Including this in the tooltip reveals the "closeness" of the race without cluttering the static visual.

*   **The Principle:** Detail on Demand
*   **The Evidence:** [@muth_german_election_2021]

## Where to Apply <!-- role: context -->
*   **User Goal:** exploring the "safety" of a district or identifying swing regions.
*   **Data Type:** Election results by district (First Vote / Direct Mandate).
*   **Audience:** Engaged users who interact with the map to learn deeper details.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Static, print-only visualizations.
*   **Reason:** Tooltips are an interactive feature; for print, this data would need to be encoded visually (e.g., opacity) or in a table.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Requires cleaner data preparation to calculate margins before visualizing.
*   **The Risk:** Tooltips can become large and block the view of the map if they contain too much text.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Only showing the winner's name and total votes.
*   **Why it fails:** It provides no context on the competitiveness of the district (e.g., a 10-vote win looks the same as a 10,000-vote win).

## How to Check <!-- role: check -->
*   **Visual Sign:** Hover over a "blue" district. Does it tell you that the "red" candidate was only 50 votes behind?
*   **The Test:** Find a district known to be a "swing" district. Does the tooltip confirm it was a close race?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add the absolute vote count for the top two candidates in the tooltip.
*   **Best Fix:** Calculate the difference and display a sentence like "Won by [Winner] with only [X] more votes than [Runner Up]" [@muth_german_election_2021].
