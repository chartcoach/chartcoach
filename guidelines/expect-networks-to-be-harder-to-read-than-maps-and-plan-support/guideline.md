---
id: expect-networks-to-be-harder-to-read-than-maps-and-plan-support
title: Treat Network Visualizations as High-Difficulty and Add Support
bibliography: references.bib
description: Assume networks are harder for general audiences to interpret than other
  common visualizations and design accordingly.
labels:
- chart:network
- chart:map
- task:correlate
- data:network
- impact:comprehension
- audience:novice
- source:borner-2019
---

## The Rule <!-- role: advice -->

Assume network visualizations are difficult for many users to read; use extra instructional support, interaction, or alternative representations when targeting general audiences.

## The Logic <!-- role: reason -->

The paper reports assessment results showing participants had particular difficulty reading network layouts, and it cites evidence that map-based visualizations can increase recall accuracy compared to networks.

- **The Principle:** Visualization-type difficulty differences (networks as harder)
- **The Evidence:** [@bornerDataVisualizationLiteracy2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding relationships (“with whom”) from relational data
- **Data Type:** Relational/network datasets
- **Audience:** Museum visitors, students, or general public without specialized training

## When to Break It <!-- role: exceptions -->

- **Scenario:** Expert audiences trained in network analysis
- **Reason:** The paper’s difficulty findings target general/novice populations; experts may not need the same scaffolding [@bornerDataVisualizationLiteracy2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Simplicity—added guidance, annotations, or alternative views take time and space
- **The Risk:** Oversimplification could hide important structure if you avoid networks entirely

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Publishing a dense force-directed network as the only view and expecting accurate reading
- **Why it fails:** It ignores documented literacy limitations specific to networks [@bornerDataVisualizationLiteracy2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Users misidentify relationships, miss clusters, or cannot explain what proximity/links mean.
- **The Test:** Run interpretation questions (e.g., identify key connections or groups); if errors cluster around the network view, you need added support [@bornerDataVisualizationLiteracy2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add interaction for details-on-demand and search/locate to reduce cognitive load.
- **Best Fix:** Provide scaffolding or complementary representations (e.g., map-based or other structured views) and explicitly teach how to interpret the network’s layout and encodings [@bornerDataVisualizationLiteracy2019].
