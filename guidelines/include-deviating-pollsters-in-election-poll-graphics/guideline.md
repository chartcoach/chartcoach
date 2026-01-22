---
id: include-deviating-pollsters-in-election-poll-graphics
title: Include deviating pollsters instead of relying on a single poll result
bibliography: references.bib
description: Show variation across pollsters so readers can see disagreement, potential
  bias, or outliers.
labels:
- chart:bar
- task:compare
- visual:position
- impact:trust
- data:categorical
- audience:general
- domain:elections
---

## Show multiple pollster results to reveal disagreement <!-- role: advice -->

Show results from more than one pollster in the same graphic when reporting an election polling snapshot. Make the differences between pollsters visible rather than collapsing them into a single source.

## Why pollster variation changes what a “poll result” means <!-- role: reason -->

Different polling organizations can produce meaningfully different results due to methods, house effects, or error, so a single poll can misrepresent the state of the race. When the audience sees the spread across pollsters, they can interpret any one number as one draw among several and better judge how settled or uncertain the picture is.

**Mechanism:** Presenting multiple sources exposes variance and reduces over-reliance on one potentially biased or erroneous estimate.

**Evidence:** Poll results can differ significantly across polling organizations, including cases where some pollsters are criticized as systematically leaning one way, so considering deviating polls gives a more reliable picture than a single source [@jockers_election_polls_2021].

**Notes:** This can be done even without building a full statistical aggregation model.

## When to include multiple pollsters in a poll graphic <!-- role: context -->

- **User Goal:** Understand the current standing while accounting for disagreement between sources.
- **Task:** Compare parties/candidates and gauge robustness across sources.
- **Data:** Multiple polls collected over a similar time window from different pollsters.
- **Chart Setting:** Election coverage where a single poll might be treated as “the” number.
- **Audience:** Readers who may not know that pollsters differ systematically.
- **Success Criterion:** The audience can see whether an apparent lead depends on a specific pollster.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Only one credible poll is available for the time window you need to report. **Why:** You cannot display cross-pollster variation that does not exist in your available data.

## Tradeoffs and risks of showing multiple pollsters <!-- role: costs -->

**Sacrifice:** The chart becomes denser and may take more space than a single set of bars. **Risk:** Readers may be overwhelmed or may not know how to summarize the spread. **Mitigation:** Keep labeling clear so viewers can distinguish pollsters and recognize any overall central tendency.

## Common mistakes when handling pollster disagreement <!-- role: mistakes -->

- **Mistake:** Highlighting one poll as definitive while ignoring other contemporary polls. **Why it fails:** It hides meaningful disagreement and can amplify one pollster’s quirks or errors.
- **Mistake:** Mixing polls from different time windows without signaling timing. **Why it fails:** It can make differences look like pollster disagreement when they are partly time effects.

## Quick tests for whether pollster disagreement is visible <!-- role: check -->

**Failure Sign:** The graphic implies there is one authoritative “result” despite multiple available sources. **Quick Check:** Can a reader identify at least two pollsters’ differing values for the same party/candidate? **Stronger Test:** Ask a reader to describe the “range” of values across pollsters; if they cannot, the design is not exposing disagreement.

## What to do instead when a single-poll display is misleading <!-- role: fix -->

- Add multiple pollster values for the same time window in a single view so differences are directly comparable.
- Include a simple summary such as an average alongside individual pollster results when you have several sources.
- Use a design that makes within-party/candidate variation across pollsters easy to spot (for example, separated or paired marks per pollster).
- If space is limited, narrow the set to the most relevant recent polls and state the inclusion rule.
