---
id: show-margins-of-error-in-election-poll-charts
title: Show margins of error alongside election poll estimates
bibliography: references.bib
description: "Always visualize the uncertainty of poll estimates so readers don\u2019\
  t mistake them for precise results."
labels:
- chart:bar
- task:compare
- visual:position
- impact:trust
- data:uncertainty
- audience:general
- domain:elections
---

## Visualize poll uncertainty with an explicit margin of error <!-- role: advice -->

Show a margin of error for each reported poll value in the chart, not just in surrounding text. Use a clear uncertainty display (for example, an interval) that keeps the estimate and its plausible range visible together.

## Why uncertainty displays prevent false precision in poll reading <!-- role: reason -->

Poll numbers come from samples and statistical inference, so readers need a visible range to interpret them as estimates rather than exact outcomes. When uncertainty is encoded directly in the graphic, readers are more likely to judge whether differences are meaningful, especially in close races.

**Mechanism:** Displaying an uncertainty band or interval shifts interpretation from “exact rank/lead” to “overlapping plausible values,” reducing overconfident comparisons.

**Evidence:** Election polls are often treated like exact results even though typical samples imply an error of roughly plus or minus a few percentage points, which can materially change the interpretation of tight races [@jockers_election_polls_2021].

**Notes:** The key is to keep the uncertainty visually tied to the value it qualifies so it is not skipped.

## When election-poll uncertainty should be shown in the chart <!-- role: context -->

- **User Goal:** Understand who is leading and whether leads are meaningful.
- **Task:** Compare parties/candidates and assess closeness.
- **Data:** Sample-based poll percentages with stated sampling error or comparable uncertainty.
- **Chart Setting:** News, dashboards, or reports where poll values might be read as “results.”
- **Audience:** Broad public audiences with mixed statistical literacy.
- **Success Criterion:** Readers interpret estimates cautiously and avoid over-reading small differences.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You do not have any defensible uncertainty information for the poll values. **Why:** Displaying an invented or unspecified margin can mislead more than it helps.

## Tradeoffs and risks of adding margins of error <!-- role: costs -->

**Sacrifice:** You spend chart space and visual attention on uncertainty rather than only the central estimates. **Risk:** Poorly explained intervals can confuse readers who are unfamiliar with uncertainty displays. **Mitigation:** Ensure the uncertainty is labeled as a margin of error and is visually coupled to each estimate.

## Common mistakes when showing poll uncertainty <!-- role: mistakes -->

**Mistake:** Reporting a single poll percentage as a precise value with no uncertainty cue. **Why it fails:** It invites readers to treat small differences as meaningful when they may fall within sampling error.

## Quick tests for whether uncertainty is being communicated <!-- role: check -->

**Failure Sign:** Readers could quote a one- or two-point difference from the chart as a decisive lead. **Quick Check:** Can someone see (without reading surrounding text) that each estimate has a plausible range? **Stronger Test:** Ask a colleague to judge whether two close parties are “clearly different” using only the chart; if they answer confidently without mentioning uncertainty, the display is failing.

## What to do instead when uncertainty is missing or unclear <!-- role: fix -->

- Add a visible interval around each estimate that represents the stated margin of error.
- Label the interval directly in the chart (e.g., “margin of error: ±X percentage points”) so it is not missed.
- If the chart cannot accommodate intervals cleanly, switch to a design that can (for example, a layout that reserves space for uncertainty marks).
- If uncertainty cannot be obtained, avoid framing small differences as meaningful and present the values as approximate.
