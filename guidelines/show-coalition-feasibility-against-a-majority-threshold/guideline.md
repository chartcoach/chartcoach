---
id: show-coalition-feasibility-against-a-majority-threshold
title: Visualize Coalition Feasibility Against the 50% Majority Line
bibliography: references.bib
description: When explaining governing coalitions, show combined vote shares and mark
  the 50% threshold to separate possible from impossible coalitions.
labels:
- chart:bar
- task:group
- visual:position
- impact:clarity
- data:categorical
- audience:general
- domain:elections
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

When visualizing governing coalitions, show each coalition’s combined vote share and include a clear 50% majority threshold that separates possible from impossible coalitions. [@muth_german_election_2021]

## The Logic <!-- role: reason -->

Coalitions are a threshold problem: viewers need to see whether combined support crosses a fixed majority. A prominently marked reference line makes feasibility a direct visual judgment rather than mental arithmetic.

- **The Principle:** Threshold comparison with reference lines
- **The Evidence:** [@muth_german_election_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which party combinations can form a majority government
- **Data Type:** Party vote shares from latest poll/average, summed into coalition totals
- **Audience:** General public learning “who could govern with whom” [@muth_german_election_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your story is about coalition negotiations, not parliamentary arithmetic.\
  **Reason:** A 50% threshold chart can overemphasize math while ignoring political constraints. [@muth_german_election_2021]
- **Scenario:** You’re not working with vote shares that sum meaningfully (e.g., seat projections with special rules not represented).\
  **Reason:** The threshold may not match the metric you’re using. [@muth_german_election_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:** More explanation/annotation space (coalition names, totals, threshold)
- **The Risk:** Viewers may assume “mathematically possible” equals “politically likely” unless you label carefully. [@muth_german_election_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Listing coalitions without totals or a 50% marker.\
  **Why it fails:** Readers must calculate feasibility themselves and will make errors. [@muth_german_election_2021]
- **The Wrong Fix:** Showing only individual party shares and expecting readers to add them up.\
  **Why it fails:** Cognitive load is high and encourages cherry-picking. [@muth_german_election_2021]

## How to Check <!-- role: check -->

- **Visual Sign:** It’s not immediately obvious which coalitions clear a majority.
- **The Test:** Hide the numbers and ask: “Can I still tell at a glance which combinations pass 50%?” If not, strengthen the threshold cue. [@muth_german_election_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a bold 50% reference line and label each coalition with its total. [@muth_german_election_2021]
- **Best Fix:** Separate “possible” vs. “not possible” sections and ensure the chart is explicitly based on a stated poll basis (latest poll vs. average). [@muth_german_election_2021]
