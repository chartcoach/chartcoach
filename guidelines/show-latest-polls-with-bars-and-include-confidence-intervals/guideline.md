---
id: show-latest-polls-with-bars-and-include-confidence-intervals
title: Show the latest poll (or poll average) with bars and include confidence intervals
  to communicate uncertainty
bibliography: references.bib
description: "Pair a latest-value bar view with uncertainty bands so readers don\u2019\
  t mistake polls for final results."
labels:
- chart:bar
- task:compare
- visual:uncertainty
- impact:trust
- data:categorical
- audience:general
- domain:elections
- tool:datawrapper
---

## Use bars for the latest polling snapshot and add confidence intervals <!-- role: advice -->

Use a bar or column chart to compare parties in the latest poll (or an average of recent polls), and include confidence intervals so the snapshot communicates uncertainty instead of false precision.

## Why uncertainty displays prevent overconfident readings of polls <!-- role: reason -->

A latest-value bar chart invites precise comparisons, but polls are estimates with sampling uncertainty. Showing confidence intervals visually signals that small differences may not be meaningful and that the values are not election results.

**Mechanism:** Uncertainty ranges reduce the tendency to read small rank changes as definitive by making overlap visible and by reframing point estimates as intervals.

**Evidence:** The post recommends bar/column charts for the latest poll/average/forecast and explicitly highlights showing confidence intervals to communicate uncertainty and that polls are not final results [@muth_german_election_2021].

**Notes:** This guideline applies equally to single-poll snapshots and aggregated averages when you want a “where things stand now” graphic.

## When this applies to election snapshots <!-- role: context -->

- **User Goal:** Understand current party standings at a glance.
- **Task:** Compare categories (parties) at a single point in time.
- **Data:** Latest poll, daily average of multiple releases, or a summarized forecast.
- **Chart Setting:** Article lead graphic, sidebar, or “latest update” module.
- **Audience:** Readers prone to over-reading small differences.
- **Success Criterion:** Readers perceive the standings as estimates with uncertainty, not as final or exact numbers.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You are visualizing certified election results rather than polls. **Why:** The key uncertainty is different (and often not sampling-based), so confidence intervals can confuse rather than clarify [@muth_german_election_2021].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More visual complexity and potentially more legend/label work. **Risk:** If intervals are too subtle, readers may ignore them; if too prominent, they can overwhelm the bars. **Mitigation:** Keep intervals visually integrated and explain what level they represent in the subtitle or note [@muth_german_election_2021].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Presenting a tight ranking of parties as plain bars with exact labels and no uncertainty cue. **Why it fails:** Readers interpret tiny differences as decisive leads, even when uncertainty makes them effectively tied [@muth_german_election_2021].

## Quick tests <!-- role: check -->

**Failure Sign:** The headline takeaway hinges on a 1–2 point difference with no uncertainty context. **Quick Check:** If two parties are close, verify that your graphic visibly indicates uncertainty rather than only listing point values [@muth_german_election_2021]. **Stronger Test:** Ask someone to answer “Could these two parties be tied?” by looking only at the chart; they should be able to infer that from the intervals.

## What to do instead <!-- role: fix -->

- Add confidence intervals to the bars so overlap is visible and uncertainty is explicit [@muth_german_election_2021].
- If you cannot compute intervals, label the chart clearly as “poll” or “estimate” and avoid over-precise annotations that imply certainty [@muth_german_election_2021].
- Use an average of multiple recent polls when the latest single poll is an outlier and your goal is a stable snapshot [@muth_german_election_2021].
- Pair the snapshot with a small trend chart when you need both “now” and “movement” in the same story package [@muth_german_election_2021].
