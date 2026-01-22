---
id: use-framework-based-pattern-blending-to-design-multifaceted-health-visualizations
title: Design multifaceted health visualizations by blending abstract organizational
  patterns (instead of selecting from chart catalogs)
bibliography: references.bib
description: Use an abstract pattern language to systematically map multiple facets
  of big health data into integrated visual structures.
labels:
- task:design
- task:sensemaking
- visual:structure
- impact:clarity
- data:multifaceted
- audience:expert
- complexity:advanced
- domain:health
---

## Use pattern blending as the starting design move <!-- role: advice -->

Design the visualization by selecting the organizational structures you need (patterns) and blending them into one representational form before choosing concrete chart types.

## Why pattern blending supports complex health sensemaking <!-- role: reason -->

An abstract set of organizational patterns makes design decisions about structure explicit and composable, which helps encode multiple facets and relationships in a single coherent space rather than scattering them across unrelated charts.

**Mechanism:** Choosing patterns first focuses design on how users must organize and relate data items during sensemaking, then instantiation turns those structures into visuals that support those tasks.

**Evidence:** Multifaceted big health data tasks require exploring several facets and unknown relationships simultaneously, and simple chart-like forms that encode only one or two facets are ineffective for such tasks [@olaSimpleChartsDesign2016]. A pattern-language approach provides reusable building blocks and a blending syntax that enabled creation of non-trivial, integrated health visualizations spanning demography, chronology, geography, and overview tasks [@olaSimpleChartsDesign2016].

**Notes:** The patterns are abstract and can be instantiated many ways, so the same blending can produce different visuals while keeping the structural intent stable.

## When this applies in health data visualization <!-- role: context -->

- **User Goal:** Develop and refine explanations (hypotheses) about disease burden, causes, risks, and how they vary across people, place, and time.
- **Task:** Exploratory sensemaking with inter-related subtasks (filter, rank, compare, relate, drill down).
- **Data:** High variety and many facets (e.g., causes, risks, age groups, countries/regions, time), often hierarchical and relational.
- **Chart Setting:** Interactive tools where users must see multiple facets at once to avoid memory-heavy switching.
- **Audience:** Public health professionals, analysts, or informed laypeople doing analytic exploration.
- **Success Criterion:** Users can perceive patterns and relationships quickly while maintaining orientation across facets.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The user task is a simple, single-facet judgment (e.g., compare one measure across categories). **Why:** A simple chart can be more efficient and easier to read than an elaborate blended structure [@olaSimpleChartsDesign2016].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More design and implementation effort up front because multiple facets must be mapped and integrated. **Risk:** Overly dense visuals can become hard to interpret if the pattern choices do not match user tasks. **Mitigation:** Keep task requirements foregrounded and use interaction to reveal latent detail progressively.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Picking a familiar chart type first and forcing multifaceted data into it. **Why it fails:** It tends to encode only a small subset of facets and blocks simultaneous exploration needed for big-data sensemaking [@olaSimpleChartsDesign2016].

## Quick tests <!-- role: check -->

**Failure Sign:** Users must constantly switch views or remember prior states to connect facets. **Quick Check:** List the facets and relationships the task needs; if your main view exposes only one or two at a time, the design is under-structured. **Stronger Test:** Walk through a real analysis question and verify users can answer it without relying on recall across separate displays.

## What to do instead <!-- role: fix -->

- Select the organizational patterns that match the needed structures (e.g., hierarchy, links, groups, ranks) before drawing any chart.
- Blend patterns to encode multiple facets in one integrated representation rather than splitting them into unrelated panels.
- Instantiate the same pattern differently across subviews when tasks differ, while keeping the structural intent consistent.
- Use interaction to control how much of the blended structure is visible at once when density is high.
