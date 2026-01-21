---
id: use-colorblind-aware-color-encodings
title: Design Color Encodings for Color-Vision Deficiency
bibliography: references.bib
description: Choose colormaps that remain discriminable under common forms of color
  blindness to prevent inaccessible and skewed interpretations.
labels:
- chart:heatmap
- task:interpret
- visual:color
- impact:accessibility
- data:ordered
- audience:general
- source:szafir-2018
---

## The Rule <!-- role: advice -->

Use colormaps that remain interpretable for people with color-vision deficiency; do not rely on rainbow hues for discrimination.

## The Logic <!-- role: reason -->

Color-vision deficiency can collapse distinctions between hues and shift perceived hues, further skewing the mapping between color and data and making parts of the visualization effectively unreadable, as explained in [@szafirGoodBadBiased2018].

- **The Principle:** Hue discrimination limits under color-vision deficiency
- **The Evidence:** [@szafirGoodBadBiased2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Reliably distinguish values or categories using color
- **Data Type:** Any visualization where color is the primary encoding (continuous or categorical)
- **Audience:** Public-facing or mixed audiences (includes viewers with color-vision deficiency)

## When to Break It <!-- role: exceptions -->

- **Scenario:** Color is purely decorative and no decisions depend on it
- **Reason:** If no information is encoded in color, accessibility constraints are less critical (though still preferable)

## The Price <!-- role: costs -->

- **The Sacrifice:** Some saturated hue combinations that look vivid to non-CVD viewers
- **The Risk:** Over-cautious palettes may reduce distinctiveness if too many categories are shown

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding labels while keeping problematic hues
- **Why it fails:** Viewers still cannot reliably discriminate the encoded differences at a glance, per [@szafirGoodBadBiased2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Multiple regions look identical or ambiguously similar when color is the only cue
- **The Test:** Verify that key distinctions do not depend on separating red/green-like hues (a known failure mode highlighted in [@szafirGoodBadBiased2018])

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch away from rainbow to a simpler sequential or diverging scale
- **Best Fix:** Choose a palette specifically intended to preserve value relationships and discriminability (the paper points to tools like ColorBrewer/Colorgorical as alternatives) and ensure the mapping matches the data type, per [@szafirGoodBadBiased2018]
