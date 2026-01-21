---
id: show-poll-trends-with-a-line-chart-and-smoothing
title: Show Poll Trends Over Time With Smoothed Lines
bibliography: references.bib
description: Use a line chart with an explicit smoothing/averaging choice to communicate
  how poll shares change over time.
labels:
- chart:line
- task:track
- visual:position
- impact:clarity
- data:temporal
- audience:general
- domain:elections
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Visualize polling over time with a line chart, and explicitly choose and apply an averaging/smoothing method (e.g., moving average or Loess) to control how ragged or smooth the trend appears. [@muth_german_election_2021]

## The Logic <!-- role: reason -->

Explain trend direction and timing by encoding poll share as position over time, while smoothing reduces noise from frequent, uneven poll releases so viewers perceive the underlying movement rather than day-to-day jitter.

- **The Principle:** Signal vs. noise in time series
- **The Evidence:** [@muth_german_election_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** See how party support rises/falls and when shifts occur
- **Data Type:** Repeated poll measurements over time from multiple institutes
- **Audience:** General public reading election coverage [@muth_german_election_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only need to communicate “where things stand now” (latest poll or average), not the full time trend.\
  **Reason:** A line chart adds historical context that may be unnecessary for a snapshot task. [@muth_german_election_2021]
- **Scenario:** Your story is about the volatility/raggedness itself.\
  **Reason:** Heavy smoothing can hide the short-term variation you’re trying to highlight. [@muth_german_election_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:** Some immediacy and detail about individual poll releases
- **The Risk:** Smoothing choices can be interpreted as editorializing if not explained (e.g., overly smooth lines imply stability). [@muth_german_election_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Applying smoothing without stating the method/extent.\
  **Why it fails:** Readers can’t judge how much the line is “processed” vs. raw polling. [@muth_german_election_2021]
- **The Wrong Fix:** Using the same line treatment regardless of polling frequency.\
  **Why it fails:** Periods with sparse polls can look deceptively stable or overly jagged depending on settings. [@muth_german_election_2021]

## How to Check <!-- role: check -->

- **Visual Sign:** Lines look either distractingly spiky (too ragged) or unrealistically flat (too smooth).
- **The Test:** Compare your smoothed line to the underlying poll updates; if major changes appear “delayed” or “invented,” adjust smoothing/averaging. [@muth_german_election_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce or increase smoothing (or switch averaging window) until the line shows clear movement without constant jaggedness. [@muth_german_election_2021]
- **Best Fix:** Offer a clearly described approach (e.g., “10‑day rolling average”) and ensure it matches your editorial intent (trend vs. volatility). [@muth_german_election_2021]
