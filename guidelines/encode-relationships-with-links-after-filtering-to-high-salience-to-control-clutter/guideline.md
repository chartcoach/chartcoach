---
id: encode-relationships-with-links-after-filtering-to-high-salience-to-control-clutter
title: Encode relationships with links only after filtering to a high-salience subset
  (e.g., top quantile)
bibliography: references.bib
description: Reduce relationship clutter by showing only the most important links
  and letting interaction reveal more.
labels:
- task:relate
- task:explore
- visual:link
- impact:readability
- data:relational
- audience:expert
- complexity:advanced
- domain:health
---

## Show only the strongest relationships as links by default <!-- role: advice -->

When the number of relationships is large, draw links only for a filtered high-salience subset (such as relationships above a quantile threshold), and reveal additional relationships through interaction.

## Why link filtering preserves legibility while keeping relational structure <!-- role: reason -->

Link-based encodings scale poorly with dense graphs; filtering to the strongest relationships keeps the display interpretable while still conveying the main relational structure needed for hypothesis building.

**Mechanism:** Reducing edge count lowers occlusion and visual noise, allowing users to trace connections and perceive meaningful patterns.

**Evidence:** For relationships among causes, risks, and locations, only relationships above the third quantile were encoded to manage the large number of possible relationships while still supporting inference (e.g., linking sanitation risks to diarrheal disease in a selected region and age band) [@olaSimpleChartsDesign2016].

**Notes:** The threshold is a design parameter; the key is an explicit salience rule plus interactive access to the remainder.

## When this applies in health data visualization <!-- role: context -->

- **User Goal:** Identify major drivers and associations among health entities (causes, risks, locations, age groups).
- **Task:** Relationship finding and explanation building.
- **Data:** Many-to-many relationships where edge count is high relative to available space.
- **Chart Setting:** Node-link or branch/link structures in interactive exploratory tools.
- **Audience:** Analysts who need interpretable relational summaries.
- **Success Criterion:** Users can trace connections without overwhelming clutter.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task requires verifying absence of a relationship (not just finding strong ones). **Why:** Filtering can hide weak-but-relevant links and mislead users about non-existence [@olaSimpleChartsDesign2016].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Completeness; some true relationships are hidden initially. **Risk:** Users may over-trust the visible subset as “all relationships.” **Mitigation:** Make the filtering rule explicit and provide controls to adjust or expand it.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Displaying all links in a dense many-to-many relationship view. **Why it fails:** Link clutter prevents tracing and pattern detection, undermining the sensemaking goal [@olaSimpleChartsDesign2016].

## Quick tests <!-- role: check -->

**Failure Sign:** Links form an indistinguishable hairball and users cannot follow a connection end-to-end. **Quick Check:** If users cannot accurately count or trace links from a selected node, edge density is too high. **Stronger Test:** Ask users to identify the top related entities for a selected item and measure accuracy without zooming or repeated attempts.

## What to do instead <!-- role: fix -->

- Filter links to a defined salience subset (e.g., above a quantile or threshold).
- Add interaction to reveal hidden links for a selected node or upon demand.
- Aggregate relationships to higher-level clusters first, then allow drill-down to finer granularity.
- Provide a control to adjust the relationship threshold so users can broaden or narrow the view.
