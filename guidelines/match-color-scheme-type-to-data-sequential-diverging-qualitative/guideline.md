---
id: match-color-scheme-type-to-data-sequential-diverging-qualitative
title: Match the Color Scheme Type to the Data
bibliography: references.bib
description: Choose sequential, diverging, or qualitative palettes based on whether
  values are ordered and whether extremes or categories matter.
labels:
- chart:choropleth
- task:encode
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- custom:color-scheme
---

## The Rule <!-- role: advice -->

Choose a sequential palette for ordered magnitude, a diverging palette for deviations around a meaningful center, and a qualitative palette for unordered categories; use colorblind-friendly colors.

## The Logic <!-- role: reason -->

Palette structure signals data structure: sequential implies ordered low→high; diverging highlights both extremes around a midpoint; qualitative separates categories without implying order. Muth describes these three scheme types and recommends choosing based on whether you want attention on high values, both extremes, or categories, and to use colorblind-friendly colors [@muth_choroplethmaps_2018].

- **The Principle:** Palette semantics must match data semantics
- **The Evidence:** [@muth_choroplethmaps_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly interpret what “more/less” or “different kind” means on the map
- **Data Type:** Region-level quantitative values (sequential/diverging) or categories (qualitative)
- **Audience:** Broad audiences including color-vision–deficient readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** None stated beyond matching scheme to intent
- **Reason:** The post frames scheme choice as dependent on message; breaking it risks misleading signals [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some “brand” colors or stylistic preferences may be incompatible with accessibility or scheme semantics.
- **The Risk:** A mismatched scheme makes readers infer order or neutrality where none exists [@muth_choroplethmaps_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a qualitative palette for ordered data (or a sequential palette for unordered categories)
- **Why it fails:** It miscommunicates whether the data is ordered and where attention should go [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The map suggests a “middle” or a “high end” that your data conceptually doesn’t have.
- **The Test:** Ask: “Is there an inherent order? Is there a meaningful midpoint?” If yes/no doesn’t match your palette type, change it [@muth_choroplethmaps_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to the appropriate palette family (sequential/diverging/qualitative) [@muth_choroplethmaps_2018].
- **Best Fix:** Use Datawrapper defaults or established palettes (e.g., as suggested in the post) to ensure appropriate behavior and accessibility [@muth_choroplethmaps_2018].
