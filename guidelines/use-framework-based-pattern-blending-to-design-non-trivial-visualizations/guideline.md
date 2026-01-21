---
id: use-framework-based-pattern-blending-to-design-non-trivial-visualizations
title: Use Pattern Blending to Systematically Build Non-Trivial Health Data Visualizations
bibliography: references.bib
description: Select abstract organizational patterns and blend them to create sophisticated
  visual structures for big health data.
labels:
- chart:custom
- task:design
- visual:structure
- impact:systematicity
- data:multifaceted
- audience:designer
- complexity:advanced
---

## The Rule <!-- role: advice -->

Start from abstract organizational patterns (e.g., Token, Coordinate, Link, Hierarchy) and blend them deliberately to map data to visual structure.

## The Logic <!-- role: reason -->

Designing big-data visualizations is labor-intensive and can become ad hoc. A pattern-language approach provides structure and vocabulary while still allowing creativity: designers choose organizational structures to convey, then instantiate them flexibly (the same blend can yield different visuals). [@olaSimpleChartsDesign2016]

- **The Principle:** Systematic mapping from data organization needs to visual structures
- **The Evidence:** [@olaSimpleChartsDesign2016]

## Where to Apply <!-- role: context -->

- **User Goal:** Support complex health-related tasks that require simultaneous exploration of facets and relationships
- **Data Type:** Multilevel public health data (causes, risks, geography, age, time)
- **Audience:** Visualization designers and tool builders

## When to Break It <!-- role: exceptions -->

- **Scenario:** You can meet the task with a straightforward, familiar representation (e.g., a single comparison) without loss of task support.
- **Reason:** Pattern blending is most valuable when the design is not obvious and the data/task complexity is high. [@olaSimpleChartsDesign2016]

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires upfront conceptual work to model tasks and data structures before drawing charts.
- **The Risk:** Blending too many patterns without clear task rationale can produce overly complex visuals. [@olaSimpleChartsDesign2016]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking a novel visualization form first and retrofitting data into it.
- **Why it fails:** The visual organization may not align with users’ tasks or the data’s structure, undermining sensemaking. [@olaSimpleChartsDesign2016]

## How to Check <!-- role: check -->

- **Visual Sign:** The visualization’s organization feels arbitrary (layout choices aren’t explainable in terms of the task/data).
- **The Test:** For each major visual structure, state which facet/relationship it encodes and which user task it supports; if you can’t, redesign using explicit patterns. [@olaSimpleChartsDesign2016]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Identify the key facets/relationships required for the primary tasks and explicitly map each to a pattern (e.g., use Link for relationships, Coordinate for rank).
- **Best Fix:** Redesign by selecting a small set of patterns, blending them intentionally (e.g., [Coordinate•List•Token•Link]) and then iterating on instantiation choices to balance density and comprehension. [@olaSimpleChartsDesign2016]
