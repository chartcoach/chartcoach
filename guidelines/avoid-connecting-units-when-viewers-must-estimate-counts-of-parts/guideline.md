---
id: avoid-connecting-units-when-viewers-must-estimate-counts-of-parts
title: Avoid visually connecting units (when viewers must estimate how many parts
  are present)
bibliography: references.bib
description: Visual connections can cause underestimation of the number of original
  parts, harming numerosity judgments.
labels:
- chart:network
- task:estimate
- visual:connection
- impact:accuracy
- data:relational
- audience:general
- complexity:intermediate
---

## Avoid visual connections that reduce perceived part counts <!-- role: advice -->

Do not add connecting lines or visual joins between discrete units when users need to estimate how many units are present. Keep countable units visually separate for numerosity tasks.

## Why connections reduce perceived numerosity <!-- role: reason -->

When separate units are perceptually grouped into a connected whole, viewers can treat the connected structure as fewer segmented objects, biasing numerosity downward.

**Mechanism:** Visual connection promotes grouping that reduces the number of perceived segmented objects, which impairs number estimation based on those segments.

**Evidence:** Grouping objects using visual connection can cause viewers to underestimate the number of original parts, which is relevant for network-style displays of points connected by lines [@szafirFourTypesEnsemble2016a].

**Notes:** This applies even when each unit is still physically present, because the perceptual organization changes.

## When you should apply this guideline <!-- role: context -->

- **User Goal:** Understand “how many” items are in the display or in each category.
- **Task:** Estimate or compare numerosity from many marks.
- **Data:** Discrete items that could be connected (nodes/edges, linked marks, chained glyphs).
- **Chart Setting:** Node-link diagrams or any display that could introduce visual joins between parts.
- **Audience:** General audiences; quick-glance analysis.
- **Success Criterion:** Numerosity judgments that reflect actual counts.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** The primary task is to interpret connectivity rather than to estimate counts of parts. **Why:** Connections may be essential to show relationships, even if they distort perceived numerosity.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Removing connections can reduce readability of relational structure. **Risk:** Users may miss important edges or paths. **Mitigation:** Separate the “count” view from the “connection” view when both are needed.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Adding decorative or convenience connections (e.g., linking items) in a display where users must judge how many items exist. **Why it fails:** Connection-based grouping can make the set appear smaller than it is.

## Quick tests <!-- role: check -->

**Failure Sign:** Users systematically under-report counts compared to a disconnected version of the same display. **Quick Check:** Show connected vs disconnected variants and ask for rough counts; large drops indicate bias. **Stronger Test:** Measure error across participants for both variants and compare mean underestimation.

## What to do instead when this fails <!-- role: fix -->

- Remove or de-emphasize connections in the view used for numerosity judgments.
- Provide a separate relational view where connections are shown for topology tasks.
- Encode relationships with interaction (e.g., reveal connections on demand) rather than always-on joins.
