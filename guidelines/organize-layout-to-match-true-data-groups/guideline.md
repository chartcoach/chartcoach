---
id: organize-layout-to-match-true-data-groups
title: Arrange marks so proximity and color reflect true grouping in the data
bibliography: references.bib
description: Use perceptual grouping cues (proximity and shared appearance) to make
  real data groups effortless to see.
labels:
- chart:bar
- task:group
- visual:proximity
- impact:clarity
- data:categorical
- audience:novice
- complexity:core
---

## Make real groups look like groups <!-- role: advice -->

Lay out items so that members of the same group are adjacent and visually consistent (for example, using both proximity and shared color). Avoid scattering group members across the chart in ways that prevent perceptual grouping.

## Perceptual grouping guides attention automatically <!-- role: reason -->

Vision clusters items into groups using cues like proximity and shared color, enabling fast group-level comparisons. When the layout conflicts with the real group structure, viewers must do effortful search and integration instead of seeing the grouping directly.

**Mechanism:** Grouping cues reduce the attention needed to bind items into a category, enabling quicker within-group and between-group judgments.

**Evidence:** Visual grouping based on proximity and shared features can facilitate comprehension, and arranging grouped items contiguously strengthens the grouping compared to color alone [@zacksDesigningGraphsDecisionMakers2020].

**Notes:** Grouping can also hide outliers if they visually “fall out” of the group, so check for missed exceptions.

## Apply when group comparisons are important <!-- role: context -->

- **User Goal:** Compare categories within larger groups (e.g., regions, cohorts, product lines).
- **Task:** Summarize by group, compare group totals or typical values, spot within-group variation.
- **Data:** Hierarchical or grouped categorical data with multiple items per group.
- **Chart Setting:** Static charts where interaction is limited.
- **Audience:** Broad audiences who benefit from immediate structure.
- **Success Criterion:** Viewers can answer group-level questions quickly without scanning.

## When a different ordering serves a higher-priority task <!-- role: exceptions -->

**Break it when:** Another ordering (such as sorting by value) is the primary task and grouping would obscure ranking. **Why:** Enforcing contiguity for groups can interfere with the intended ordering-based message.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Group-contiguous layouts may reduce the ability to scan a single global ranking. **Risk:** Color-plus-proximity grouping can overemphasize groups and deemphasize cross-group comparisons. **Mitigation:** Ensure the ordering within and across groups matches the decision questions.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Encoding group membership by color but leaving group members interleaved across the axis. **Why it fails:** Color alone may not produce a strong enough perceptual group for fast group comparisons [@zacksDesigningGraphsDecisionMakers2020].
- **Mistake:** Creating groups visually that do not match the data’s true structure. **Why it fails:** Viewers attend to the wrong clusters and draw incorrect summaries [@zacksDesigningGraphsDecisionMakers2020].

## Quick tests <!-- role: check -->

**Failure Sign:** People answer item-level questions correctly but struggle with group-level summaries. **Quick Check:** Ask “which group is generally larger?”; if the reader must point back and forth across the entire chart, grouping is too weak. **Stronger Test:** Show two layouts (interleaved vs contiguous) and measure accuracy and time on group questions.

## What to do instead <!-- role: fix -->

- Reorder the axis so members of each group are contiguous.
- Use consistent color (and, if needed, spacing) to reinforce group boundaries.
- Add lightweight group headers or separators that align with the data grouping.
- If outliers matter, highlight them so they remain detectable despite grouping.
