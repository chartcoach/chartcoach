---
id: use-color-or-shading-to-distinguish-treemap-regions-by-attribute
title: Encode Secondary Attributes with Color in Treemaps
bibliography: references.bib
description: Use color (or grayscale shading) to differentiate treemap regions and
  to encode categorical or ordinal file attributes.
labels:
- chart:treemap
- task:categorize
- visual:color
- impact:clarity
- data:hierarchical
- audience:novice
- source:shneiderman-1992
---

## The Rule <!-- role: advice -->

Use distinct colors (or grayscale shading) within treemap rectangles to differentiate adjacent regions and to encode a meaningful attribute (e.g., type, owner, age, frequency of use).

## The Logic <!-- role: reason -->

With many small rectangles, color is needed for visual separation and can simultaneously carry additional information beyond size, enabling rapid scanning for patterns by attribute.

- **The Principle:** Redundant separation + attribute encoding via color
- **The Evidence:** Shneiderman states that “different colors (or gray shading) must be used within each region” and lists multiple attributes suitable for color coding [@shneidermanTreeVisualizationTreemaps1992].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify clusters (e.g., many graphics files) and interpret size in context of type/owner/age.
- **Data Type:** Weighted hierarchy with an additional attribute per leaf or node.
- **Audience:** Users exploring large directory trees or similar hierarchical inventories.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The attribute is not meaningful or would overwhelm the viewer with arbitrary hues.
- **Reason:** Shneiderman emphasizes that users’ needs vary and no single scheme fits all; misuse can reduce clarity [@shneidermanTreeVisualizationTreemaps1992].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires careful selection and management of a color mapping scheme.
- **The Risk:** Adjacent regions with the same color may blend together unless boundaries are added [@shneidermanTreeVisualizationTreemaps1992].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using the same color for many neighboring rectangles without borders.
- **Why it fails:** Regions become indistinguishable; Shneiderman notes a boundary line becomes necessary when adjacent areas share color [@shneidermanTreeVisualizationTreemaps1992].

## How to Check <!-- role: check -->

- **Visual Sign:** Users cannot tell where one rectangle ends and the next begins in same-colored areas.
- **The Test:** Look for merged-looking blocks of identical color that hide internal partitions.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add boundary lines where adjacent rectangles share the same color.
- **Best Fix:** Provide user controls to assign colors to attribute values and adjust parameters to match their task [@shneidermanTreeVisualizationTreemaps1992].
