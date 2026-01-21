---
id: report-poll-margins-of-error
title: Show Margins of Error in Election Poll Charts
bibliography: references.bib
description: Communicate polling uncertainty by visualizing the margin of error alongside
  reported poll shares.
labels:
- chart:bar
- task:compare
- visual:annotation
- impact:clarity
- data:uncertainty
- audience:general
- domain:elections
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Always display the margin of error when visualizing election poll results, using an explicit uncertainty depiction (e.g., ± bands/intervals around values).

## The Logic <!-- role: reason -->

Explaining polls as exact values implies false precision; showing uncertainty prevents readers from over-interpreting small differences that may be within sampling error, especially in tight races [@jockers_election_polls_2021].

- **The Principle:** Communicate uncertainty instead of point certainty
- **The Evidence:** [@jockers_election_polls_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Judge whether apparent leads or changes are meaningful vs. statistical noise
- **Data Type:** Sample-based election polling percentages extrapolated to an electorate
- **Audience:** General-news readers who may treat poll numbers like final results

## When to Break It <!-- role: exceptions -->

- **Scenario:** You do not have any margin-of-error or uncertainty information from the pollster or source.
- **Reason:** You can’t responsibly invent uncertainty values; instead, avoid precision cues and disclose that uncertainty is unavailable [@jockers_election_polls_2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra visual complexity and potentially more chart space.
- **The Risk:** Readers may find the chart harder to scan quickly if uncertainty marks dominate the display [@jockers_election_polls_2021].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reporting a single percentage as if it were a final result and omitting ± information.
- **Why it fails:** It encourages overconfident conclusions from differences that may be only 2–3 percentage points—i.e., within typical error margins [@jockers_election_polls_2021].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart shows only point values (e.g., bars or labels) with no intervals, bands, or stated ± range.
- **The Test:** Ask: “Could a reader tell what range the true value likely falls into?” If not, you’re not communicating uncertainty [@jockers_election_polls_2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a clear text note near the chart stating the margin of error (e.g., “±2–3 pp”) and what it applies to.
- **Best Fix:** Draw the uncertainty directly on the marks (e.g., interval/CI-style markers around each party’s share) so the range is visible at a glance [@jockers_election_polls_2021].
