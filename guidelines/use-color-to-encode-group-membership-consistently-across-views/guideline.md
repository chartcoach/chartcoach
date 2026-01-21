---
id: use-color-to-encode-group-membership-consistently-across-views
title: Use Color to Encode Group Membership Consistently Across Related Views
bibliography: references.bib
description: Assign stable colors to major groups (e.g., disease groups, risk groups)
  and reuse them to support cross-view connection.
labels:
- chart:multiview
- task:identify
- visual:color
- impact:comprehension
- data:categorical
- audience:expert
- custom:health-groups
---

## The Rule <!-- role: advice -->

Assign colors to meaningful groups (e.g., disease groups, risk groups) and keep those color assignments consistent across all related sub-visualizations.

## The Logic <!-- role: reason -->

In the paper’s designs, group membership is repeatedly encoded with color (e.g., non-communicable vs communicable vs injury; metabolic vs behavioral vs environmental/occupational). Reusing the same group colors across sub-visualizations helps users identify entities and connect patterns between views without re-learning encodings. [@olaSimpleChartsDesign2016]

- **The Principle:** Stable categorical encoding supports cross-view mapping
- **The Evidence:** [@olaSimpleChartsDesign2016]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify clusters/causes/risks and relate them across multiple sub-visualizations
- **Data Type:** Categorical groupings with repeated appearance in multiple views (clusters nested in groups)
- **Audience:** Users doing multi-step exploration across facets

## When to Break It <!-- role: exceptions -->

- **Scenario:** A view’s primary purpose is to encode magnitude with color intensity (spectrum), and group colors would conflict with that channel.
- **Reason:** The paper separates Spectrum use (mortality intensity) from Group-by-color use (category membership). [@olaSimpleChartsDesign2016]

## The Price <!-- role: costs -->

- **The Sacrifice:** Limits palette flexibility; you must reserve colors for group meaning.
- **The Risk:** If too many groups are assigned distinct hues, discrimination may degrade. [@olaSimpleChartsDesign2016]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reassigning colors per chart “for aesthetics.”
- **Why it fails:** Users cannot transfer what they learned in one sub-visualization to another, undermining integrated sensemaking. [@olaSimpleChartsDesign2016]

## How to Check <!-- role: check -->

- **Visual Sign:** The same group appears in different colors across panels.
- **The Test:** Pick a group (e.g., communicable) and verify it has one stable color everywhere it appears. [@olaSimpleChartsDesign2016]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Define a single palette keyed to groups and apply it globally across the tool.
- **Best Fix:** Encode group membership redundantly through both color and structural grouping (e.g., spatial grouping + color), so group meaning survives even when some views use color for intensity. [@olaSimpleChartsDesign2016]
