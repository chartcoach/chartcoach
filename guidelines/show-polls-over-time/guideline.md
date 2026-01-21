---
id: show-polls-over-time
title: Plot Poll Trends Over Time
bibliography: references.bib
description: Move beyond a single snapshot by charting poll results over time and
  annotating key events that explain shifts.
labels:
- chart:line
- task:trend
- visual:position
- impact:context
- data:temporal
- audience:general
- domain:elections
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Show election polls as a time series and annotate major political events so readers can see how support changes over time.

## The Logic <!-- role: reason -->

A single poll is only a snapshot; showing the trajectory helps readers interpret movement (rises, drops, recoveries) and connects changes to real-world campaign events, enabling explanation instead of isolated number reporting [@jockers_election_polls_2021].

- **The Principle:** Temporal context enables meaningful interpretation of change
- **The Evidence:** [@jockers_election_polls_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand dynamics (momentum, reversals, stability) during a campaign
- **Data Type:** Repeated polls over weeks/months (multiple observations across time)
- **Audience:** General public following an election during a campaign period

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only have one poll (or too few points) so a line implies continuity you can’t support.
- **Reason:** A trend chart suggests a time-based pattern; with insufficient observations it can overstate certainty about direction [@jockers_election_polls_2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** More design effort (data collection, cleaning, and annotation) and potentially more chart space.
- **The Risk:** With many parties/lines, the chart can become visually busy without careful labeling and annotation choices [@jockers_election_polls_2021].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Publishing isolated “latest poll” graphics repeatedly without showing prior context.
- **Why it fails:** Readers can’t tell whether the number represents a meaningful shift or normal variation over time [@jockers_election_polls_2021].

## How to Check <!-- role: check -->

- **Visual Sign:** The graphic contains only one date’s values and no indication of prior levels.
- **The Test:** Ask: “Can a reader tell whether support is rising, falling, or stable?” If they can’t, you’re missing the time dimension [@jockers_election_polls_2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add previous polls (even a short recent history) so the latest value is contextualized.
- **Best Fix:** Create a full time-series view (optionally with weekly averages) and add concise annotations tied to key campaign events that plausibly relate to visible shifts [@jockers_election_polls_2021].
