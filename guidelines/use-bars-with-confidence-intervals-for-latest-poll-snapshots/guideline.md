---
id: use-bars-with-confidence-intervals-for-latest-poll-snapshots
title: Add Confidence Intervals to Poll Snapshot Bar Charts
bibliography: references.bib
description: When showing latest poll levels as bars, include confidence intervals
  to communicate uncertainty.
labels:
- chart:bar
- task:compare
- visual:color
- impact:trust
- data:categorical
- audience:general
- domain:elections
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

When visualizing the latest poll (or an average/forecast) as bars or columns, show confidence intervals to communicate uncertainty and that polls aren’t final results. [@muth_german_election_2021]

## The Logic <!-- role: reason -->

Bars support fast comparison of current levels across parties, while confidence intervals visually encode the plausible range so readers don’t treat point estimates as precise outcomes.

- **The Principle:** Uncertainty communication
- **The Evidence:** [@muth_german_election_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare current party standings “right now”
- **Data Type:** One poll, an average of recent polls, or a forecast with uncertainty
- **Audience:** General public consuming pre-election coverage [@muth_german_election_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You do not have uncertainty information.\
  **Reason:** Adding arbitrary intervals would mislead. [@muth_german_election_2021]
- **Scenario:** The focus is purely descriptive of certified election results (not polls).\
  **Reason:** Final results don’t require poll-style uncertainty framing. [@muth_german_election_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:** Visual simplicity and space
- **The Risk:** Viewers may misread intervals if you don’t explain what they represent (e.g., “95% certain”). [@muth_german_election_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing only a single bar value as if it were exact.\
  **Why it fails:** It invites overconfidence and “horse-race” certainty. [@muth_german_election_2021]
- **The Wrong Fix:** Hiding uncertainty in text only.\
  **Why it fails:** Readers scan visuals; uncertainty should be visible where comparisons happen. [@muth_german_election_2021]

## How to Check <!-- role: check -->

- **Visual Sign:** Readers could easily interpret the bars as exact predictions.
- **The Test:** Ask: “Can a viewer see at a glance that party shares have a range, not a single true number?” If not, add intervals. [@muth_german_election_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add confidence bands/whiskers to each bar and describe the level (e.g., 95%) in subtitle/annotation. [@muth_german_election_2021]
- **Best Fix:** Pair bars + intervals with a short explanation of how multiple polls are combined (latest poll vs. average) so the snapshot is interpretable. [@muth_german_election_2021]
