---
id: do-not-rely-on-crowded-dashboards-for-multifaceted-sensemaking-align-views-to-data-relationships
title: Do not rely on crowded dashboards for multifaceted sensemaking; align multi-view
  layout to data relationships
bibliography: references.bib
description: Avoid unstructured collections of charts that force mental integration;
  organize multiple views to mirror relationships in the data.
labels:
- chart:dashboard
- task:sensemaking
- visual:layout
- impact:cognitive-load
- data:multifaceted
- audience:expert
- complexity:advanced
- domain:health
---

## Organize multiple views by relationship, not by grid convenience <!-- role: advice -->

If you use multiple coordinated views, arrange them so their spatial organization reflects how the underlying facets relate, rather than placing them in a generic tabular dashboard layout.

## Why relationship-aligned layouts reduce mental integration burden <!-- role: reason -->

When views are merely juxtaposed, users must mentally integrate them; if the external organization does not represent relationships, internal cognitive work increases and sensemaking suffers.

**Mechanism:** Relationship-aligned spatial organization offloads integration work onto perception by making correspondences explicit, reducing the need for mental stitching across panels.

**Evidence:** Dashboards that crowd many simple charts can force users to mentally combine representations, and tabular organization that ignores data relationships can negatively affect internal mental processes during analysis [@olaSimpleChartsDesign2016]. Big data tasks require simultaneous exploration of facets and relationships, which simple separated charts often fail to support effectively [@olaSimpleChartsDesign2016].

**Notes:** This guideline does not prohibit multiple views; it targets unstructured “chart collages.”

## When this applies in health data visualization <!-- role: context -->

- **User Goal:** Relate multiple facets (e.g., age, location, risk, cause) while maintaining orientation.
- **Task:** Cross-facet comparison, relationship finding, hypothesis building.
- **Data:** Many facets with known structural correspondences (shared categories, hierarchies, or time).
- **Chart Setting:** Dashboards or multi-panel analytic applications.
- **Audience:** Users performing non-routine analytic work.
- **Success Criterion:** Users can connect facets without heavy mental effort.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The dashboard is for monitoring a small set of largely independent key performance indicators (KPIs). **Why:** Mental integration demands are low and a simple grid can maximize scan efficiency [@olaSimpleChartsDesign2016].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Relationship-aligned layouts may be less compact than a uniform grid. **Risk:** Over-structuring layout can reduce flexibility when users need arbitrary comparisons. **Mitigation:** Keep strong alignment for the primary relationships and allow interactive reconfiguration for secondary questions.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding more charts to the dashboard to cover more facets. **Why it fails:** More panels increase the need for mental integration and can crowd the space without improving relational understanding [@olaSimpleChartsDesign2016].

## Quick tests <!-- role: check -->

**Failure Sign:** Users frequently switch gaze between panels and verbally “translate” categories to connect them. **Quick Check:** If two views share a key dimension but are not visually aligned by it, the layout is relationship-blind. **Stronger Test:** Give a cross-facet question and observe whether users must manually reconcile labels across charts.

## What to do instead <!-- role: fix -->

- Align views using shared structures (e.g., shared ordering, shared coordinate frames, or shared grouping boundaries).
- Integrate multiple facets into one blended representation when cross-facet reasoning is central.
- Use structural patterns (e.g., track/stack/cell) to show separation and membership among subviews.
- Limit visible relationships to a meaningful subset and reveal more through interaction when relationship density is high.
