---
id: show-polls-over-time-with-a-line-chart-and-explicit-smoothing-choice
title: Show poll dynamics over time with a line chart and make the smoothing level
  an explicit editorial choice
bibliography: references.bib
description: Use poll line charts for change over time, and deliberately choose (and
  communicate) how smooth or ragged the lines should be.
labels:
- chart:line
- task:trend
- visual:position
- impact:clarity
- data:temporal
- audience:general
- domain:elections
- tool:datawrapper
---

## Use a poll line chart and choose a deliberate smoothing approach <!-- role: advice -->

Use a line chart to show how party polling changes over time, and decide explicitly whether to show ragged raw movement or a smoother averaged trend.

## Why smoothing is an editorial, not purely technical, choice <!-- role: reason -->

Polls are noisy and can fluctuate from sampling error and house effects, so a line chart can either emphasize volatility (less smoothing) or underlying movement (more averaging). Making smoothing a deliberate choice prevents accidental over-interpretation of wiggles or, conversely, accidental hiding of real shifts.

**Mechanism:** Smoothing reduces short-term variation that can distract from longer-term direction, while unsmoothed or lightly smoothed lines preserve day-to-day changes that may be newsworthy; choosing intentionally aligns the visual signal with the story’s intent.

**Evidence:** The post contrasts “ragged” versus “smooth” poll lines and frames newsroom choices around moving averages/Loess and different smoothing levels, implying that the level of smoothing materially changes interpretation [@muth_german_election_2021].

**Notes:** This is about matching the visual behavior (smooth vs ragged) to what you want readers to notice.

## When this applies to poll reporting <!-- role: context -->

- **User Goal:** Understand momentum and direction in party support.
- **Task:** Detect trends, turning points, and relative positions over time.
- **Data:** Repeated polls over dates, potentially from multiple institutes, with uneven frequency.
- **Chart Setting:** Pre-election coverage and poll trackers embedded in articles.
- **Audience:** General readers who may confuse noise for trend.
- **Success Criterion:** Readers see the intended level of stability or volatility without mistaking artifacts for meaningful change.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your purpose is to show each individual poll release as discrete events rather than a continuous trend. **Why:** A continuous smoothed line can imply continuity and precision that the underlying releases don’t support [@muth_german_election_2021].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Heavier smoothing can hide short-lived surges or drops; lighter smoothing can look chaotic. **Risk:** Readers may treat line wiggles as “real movement” or treat overly smooth curves as “certainty.” **Mitigation:** Align smoothing to the story question (short-term volatility vs underlying drift) and explain what the line represents [@muth_german_election_2021].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Applying smoothing without considering how it changes the narrative of momentum. **Why it fails:** The visual can accidentally exaggerate volatility or falsely suggest stability, changing what readers believe happened [@muth_german_election_2021].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers argue about tiny day-to-day line bends rather than the overall direction. **Quick Check:** Compare a lightly smoothed and more smoothed version; if the “story” changes drastically, you need to be explicit about which behavior you intend to communicate [@muth_german_election_2021]. **Stronger Test:** Ask a colleague to summarize the trend in one sentence; if they describe noise rather than direction (or vice versa), adjust smoothing.

## What to do instead <!-- role: fix -->

- Plot individual polls as points (and optionally connect with a light guide) if your intent is to show releases rather than a continuous trend [@muth_german_election_2021].
- Use a rolling average or similar aggregation when your intent is to communicate underlying movement rather than day-to-day noise [@muth_german_election_2021].
- Add annotations for key campaign events when you need readers to connect trend changes to real-world moments [@muth_german_election_2021].
- Narrow the time window (for example, show only the election year) when long histories make the trend hard to read at article scale [@muth_german_election_2021].
