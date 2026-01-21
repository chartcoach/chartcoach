---
id: preserve-semantic-consistency-in-encodings-across-scenes
title: Preserve Semantic Consistency in Encodings Across Scenes
bibliography: references.bib
description: Keep color and other encodings consistent in meaning across panels, tabs,
  and slides.
labels:
- visual:color
- task:compare
- impact:clarity
- custom:semantic-consistency
- audience:general
---

## The Rule <!-- role: advice -->

Use semantically consistent encodings (especially color) across all frames and panels so the same meaning always maps to the same visual treatment.

## The Logic <!-- role: reason -->

The paper highlights semantic consistency and “matching on content” as tactics that let viewers immediately recognize references across sections without re-decoding legends, improving transitions and comprehension.

- **The Principle:** Consistent mappings reduce re-interpretation and support cross-scene recognition.
- **The Evidence:** [@segelNarrativeVisualizationTelling2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Track entities or categories across panels/sections and understand connections quickly.
- **Data Type:** Multi-view/multi-step narratives comparing the same items over time or across facets.
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** A deliberate shift in meaning where a new mapping is essential (e.g., switching the variable encoded by color).
- **Reason:** Reusing the same encoding would mislead; instead, the change must be made explicit as a narrative event [@segelNarrativeVisualizationTelling2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less flexibility to choose “best” colors per individual chart.
- **The Risk:** Overloading a single encoding across many contexts can constrain design options [@segelNarrativeVisualizationTelling2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reassigning category colors between panels because each panel was designed independently.
- **Why it fails:** Viewers must repeatedly re-learn mappings, disrupting narrative flow [@segelNarrativeVisualizationTelling2010].

## How to Check <!-- role: check -->

- **Visual Sign:** The same category appears in different colors across the story.
- **The Test:** Spot-check a repeated entity across all scenes; its encoding should be identical unless a change is explicitly messaged [@segelNarrativeVisualizationTelling2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Create a shared palette/mapping table and apply it everywhere.
- **Best Fix:** Centralize encoding definitions and design all panels/steps from that shared schema [@segelNarrativeVisualizationTelling2010].
