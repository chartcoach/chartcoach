---
id: avoid-dark-yellow-green
title: Filter Out Dark Yellow-Green Colors
bibliography: references.bib
description: Remove dark yellow-green colors to improve the aesthetic reception of
  visualization palettes.
labels:
- visual:color
- impact:aesthetics
- impact:preference
- audience:general
- data:nominal
---

## The Rule <!-- role: advice -->
Explicitly exclude dark yellow and olive-green regions from your color palette selection.

## The Logic <!-- role: reason -->
Aesthetic preference is a critical component of visualization acceptance. Research indicates that specific regions of color space are universally disliked across cultures.
*   **The Principle:** Aesthetic Preference Filtering.
*   **The Evidence:** Gramazio et al. [@gramazio_colorgorical_2017], as collated by Zeng and Battle [@zeng_review_2023], identify the dark yellowish-green region (specifically CIE LCh L ∈ [35, 75] and H ∈ [85°, 114°]) as "strongly disliked." Removing this region increases general palette preference without significantly harming discriminability.

## Where to Apply <!-- role: context -->
*   **User Goal:** Creating visualizations that are aesthetically pleasing and likely to be adopted/preferred by users.
*   **Data Type:** Any categorical data.
*   **Audience:** General audiences where engagement and first impressions matter.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Naturalistic Domains.
*   **Reason:** If the data represents real-world objects requiring these colors (e.g., a map of vegetation types, forestry data, or military camouflage patterns).

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose a slice of the available color space, which may make it harder to find distinguishable colors for palettes with many categories (8+).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Attempting to "fix" a dark yellow by making it more saturated.
*   **Why it fails:** It often remains in the "disliked" hue range unless the lightness is significantly altered.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for colors resembling "olive," "mud," or "mustard."
*   **The Test:** Ask a user to rate the pleasantness of the colors. If they grimace at a specific brownish-green, remove it.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Shift the hue toward Orange or pure Green, or significantly increase the Lightness to turn it into a bright Yellow.
*   **Best Fix:** Define a prohibition zone in your color selection tool corresponding to hue angles between 85° and 114° in CIE LCh.
