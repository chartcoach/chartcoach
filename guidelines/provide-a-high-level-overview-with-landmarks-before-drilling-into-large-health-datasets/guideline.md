---
id: provide-a-high-level-overview-with-landmarks-before-drilling-into-large-health-datasets
title: Provide an overview with clear landmarks (age, location, time) before drill-down
  in large health datasets
bibliography: references.bib
description: Start sensemaking with a compact overview that establishes key categories
  and relationships, then enable deeper exploration.
labels:
- task:overview
- task:explore
- visual:layout
- impact:orientation
- data:multifaceted
- audience:novice
- complexity:intermediate
- domain:health
---

## Begin exploration with an overview that anchors users in the major facets <!-- role: advice -->

In big health data tools, provide a high-level overview that clearly identifies core landmarks (such as age groups, regions, and years) and exposes major cause–risk relationships before users drill into finer detail.

## Why an overview with landmarks supports sensemaking <!-- role: reason -->

Sensemaking benefits from stable orientation points that help users decide where to explore next; without landmarks, large multifaceted datasets can feel unbounded and exploration becomes inefficient.

**Mechanism:** Landmarks reduce search costs and provide a mental map of the dataset’s structure, enabling users to move from overview to focused investigation.

**Evidence:** An overview visualization summarized mortality across age groups, regions, and years while also showing cause–risk relationships and cluster structure, explicitly motivated by the need to provide landmarks given the sizable number of data items [@olaSimpleChartsDesign2016].

**Notes:** The overview is complementary to perspective-specific views (demography/chronology/geography).

## When this applies in health data visualization <!-- role: context -->

- **User Goal:** Decide where to focus analysis and maintain orientation across many facets.
- **Task:** Initial scanning, prioritization, and navigation into deeper questions.
- **Data:** Large, multifaceted datasets with multiple granularities.
- **Chart Setting:** Multi-view analytic applications where users can drill down.
- **Audience:** Mixed expertise, including new users who need an entry point.
- **Success Criterion:** Users can quickly pick a meaningful next step for exploration and understand what the major categories are.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Users already arrive with a single narrow query and known filters (e.g., a fixed region and cause). **Why:** An overview may add an unnecessary step for targeted lookups [@olaSimpleChartsDesign2016].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional design and screen space for a non-detail view. **Risk:** Overviews can oversimplify and hide important variation. **Mitigation:** Make the overview interactive so selections reveal deeper detail in linked views.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Dropping users directly into a detailed, dense view without category landmarks. **Why it fails:** Users lack orientation and may not know what to explore or how facets relate [@olaSimpleChartsDesign2016].

## Quick tests <!-- role: check -->

**Failure Sign:** First-time users ask what the main categories are or where to begin. **Quick Check:** A user should be able to name the main facets and make a selection within a short time. **Stronger Test:** Observe whether users can form a plausible exploration path (overview → selection → explanation) without instruction.

## What to do instead <!-- role: fix -->

- Add a compact legend-like landmark panel that lists the major facets and their categories.
- Include a summary of proportions (overall and by major groupings) to guide attention.
- Provide a high-level cause–risk relationship view that highlights prevalent relationships.
- Link overview selections to detailed views so users can immediately drill down from chosen landmarks.
