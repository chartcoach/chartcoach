---
id: encode-many-facets-in-one-space-for-big-health-sensemaking-not-one-or-two-facets-per-chart
title: Encode multiple facets and their relationships in a single integrated view
  for big health sensemaking tasks
bibliography: references.bib
description: Use non-trivial, integrated visual structures that show multiple facets
  simultaneously to support complex health analytics.
labels:
- task:explore
- task:relate
- visual:integration
- impact:insight
- data:multifaceted
- audience:expert
- complexity:advanced
- domain:health
---

## Build integrated views that expose several facets at once <!-- role: advice -->

For complex public health analytics, use an integrated visualization that simultaneously encodes multiple facets (attributes, hierarchies, ranks, and relationships) rather than separate charts that each show only one or two facets.

## Why integrated multifacet views enable complex analytic work <!-- role: reason -->

Big health tasks often require concurrent exploration of different entities and unknown/non-explicit relationships; integrated views reduce the need to search, switch contexts, and mentally compose separate representations.

**Mechanism:** Simultaneous visibility supports rapid perception of patterns and supports iterative hypothesis generation by keeping related facets and relationships co-present.

**Evidence:** Simple charts typically represent only one or two facets and are ineffective for complex sensemaking tasks that require exploring various facets and data elements simultaneously [@olaSimpleChartsDesign2016]. Sophisticated visualizations that encode many facets and support interaction are needed to handle big health data tasks such as outbreak prediction and at-risk population discovery [@olaSimpleChartsDesign2016].

**Notes:** Integration can be achieved by blending organizational patterns, not by cramming unrelated encodings together.

## When this applies in health data visualization <!-- role: context -->

- **User Goal:** Identify patterns, trends, correlations, and outliers across multiple health determinants and outcomes.
- **Task:** Multi-step sensemaking (filter → compare → relate → hypothesize).
- **Data:** Multivariate, hierarchical, relational (e.g., causes within clusters; risks within clusters; regions/country clusters; age groups; years).
- **Chart Setting:** Interactive analytics where users must explore and drill down.
- **Audience:** Public health professionals, researchers, and advanced general-public users.
- **Success Criterion:** Users can answer cross-facet questions without stitching together many separate views.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The decision depends on a single comparison or a single distribution. **Why:** Integrated multifacet structures add complexity that is unnecessary for simple perceptual tasks [@olaSimpleChartsDesign2016].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Integrated views can be visually dense and require careful interaction design. **Risk:** If too much is shown at once, users may struggle to find entry points. **Mitigation:** Provide landmarks and use interaction to reveal latent detail progressively.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Encoding many facets by adding more marks without a clear organizing structure. **Why it fails:** Density increases without improving users’ ability to relate facets, undermining sensemaking [@olaSimpleChartsDesign2016].

## Quick tests <!-- role: check -->

**Failure Sign:** The user cannot explain what each region of the visualization represents without external guidance. **Quick Check:** Ask whether the view makes at least three core facets simultaneously readable (e.g., entity, group, magnitude/ordering, relationship). **Stronger Test:** Give a realistic analytic question (e.g., “Which risks drive which causes in a region for an age group?”) and see if it can be answered within the same view.

## What to do instead <!-- role: fix -->

- Add explicit organizing structures (e.g., hierarchy, list-based ranking, grouped color, links) before increasing data density.
- Use interaction to highlight a selected entity and reveal its related facets rather than showing all relationships at full strength.
- Provide an overview + drill-down path within the same integrated structure.
- Reduce relationship clutter by filtering to high-salience relationships and enabling user-controlled thresholds.
