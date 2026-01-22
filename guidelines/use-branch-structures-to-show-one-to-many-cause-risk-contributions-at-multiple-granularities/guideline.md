---
id: use-branch-structures-to-show-one-to-many-cause-risk-contributions-at-multiple-granularities
title: Use branch structures to show one-to-many contributions (e.g., a risk contributing
  to multiple causes) across granularities
bibliography: references.bib
description: Represent one-to-many contribution relationships with a branching form
  that summarizes totals and exposes constituent targets.
labels:
- task:relate
- task:explore
- visual:connection
- impact:insight
- data:relational
- audience:expert
- complexity:advanced
- domain:health
---

## Represent one-to-many contributions with branching that exposes targets <!-- role: advice -->

When a single factor (such as a risk) contributes to multiple outcomes (such as causes of death), encode that relationship with a branching structure that summarizes the total contribution and shows separate branches for each target.

## Why branching matches contribution structure in health data <!-- role: reason -->

Contribution relationships are naturally one-to-many; a branch form makes that structure visible and supports exploring which targets dominate and how targets differ by group.

**Mechanism:** A single source visual element anchors attention, and branches externalize the set of targets, enabling users to scan targets and compare their relative contributions.

**Evidence:** Cause–risk exploration used branching to show how a risk factor contributes to multiple causes, with a summarized top portion and multiple smaller branches for cause-specific contributions, enabling users to examine relationships at global and regional levels [@olaSimpleChartsDesign2016].

**Notes:** Branching can be used at different granularities, such as cluster-to-cluster or factor-to-cause.

## When this applies in health data visualization <!-- role: context -->

- **User Goal:** Understand which outcomes are driven by a selected factor and how strong those relationships are.
- **Task:** Relationship exploration, driver identification, explanation building.
- **Data:** One-to-many mappings with quantitative weights (attribution, contribution, or flow-like measures).
- **Chart Setting:** Interactive views where users select a factor or cluster and inspect its targets.
- **Audience:** Analysts exploring causal/risk attribution structures.
- **Success Criterion:** Users can identify the major targets and see group differences without switching contexts.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Relationships are primarily many-to-many and the task is symmetric between both sides. **Why:** A strictly one-to-many branch emphasis can hide the reciprocal exploration needs [@olaSimpleChartsDesign2016].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Branch structures can become visually complex as the number of targets grows. **Risk:** Overlapping branches reduce traceability. **Mitigation:** Aggregate to clusters first and use filtering or interaction to focus on a subset of targets.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Representing contribution as a simple table without structural cues. **Why it fails:** Users must mentally infer one-to-many structure and scan more effortfully for dominant targets [@olaSimpleChartsDesign2016].

## Quick tests <!-- role: check -->

**Failure Sign:** Users cannot quickly answer “what does this risk mainly affect?” **Quick Check:** Select a factor and see whether the top targets are immediately visible as distinct branches. **Stronger Test:** Ask users to identify the top three targets for several factors and measure whether branch tracing remains reliable.

## What to do instead <!-- role: fix -->

- Aggregate relationships to cluster level first, then allow drill-down to individual targets.
- Filter or threshold targets so only salient branches appear by default.
- Use group encoding (e.g., color) on branches to show target categories.
- Provide interaction to expand/collapse branches for a selected source.
