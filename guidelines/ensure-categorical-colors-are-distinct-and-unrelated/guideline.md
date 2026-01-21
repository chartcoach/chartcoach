---
id: ensure-categorical-colors-are-distinct-and-unrelated
title: Make Categorical Colors Maximally Distinct
bibliography: references.bib
description: Choose categorical colors that read as separate groups rather than shades
  of the same thing.
labels:
- chart:any
- task:categorize
- visual:color
- impact:clarity
- data:categorical
- audience:general
- complexity:basic
---

## The Rule <!-- role: advice -->

For categories, use clearly different hues that don’t look like lighter/darker versions of each other.

## The Logic <!-- role: reason -->

Categorical color should communicate separation, not magnitude; if colors appear related (like tints/shades), viewers may infer ordering or similarity that isn’t in the data [@muth_colorguide_2018].

- **The Principle:** Categorical separation vs. implied ordering
- **The Evidence:** [@muth_colorguide_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify and track categories (e.g., groups, parties, series).
- **Data Type:** Nominal categories with no inherent order.
- **Audience:** General audiences (including readers who don’t study legends carefully).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Categories are intentionally grouped into “families” (e.g., subcategories within a parent group).
- **Reason:** Related shades can help convey hierarchy—though the guide frames “distinctive colors” as the default for categories [@muth_colorguide_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Limited number of truly distinct hues before the palette becomes hard to manage.
- **The Risk:** Too many categories will still become confusing even with distinct hues [@muth_colorguide_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a single hue with multiple lightness steps for unrelated categories.
- **Why it fails:** It makes categories look ordered or similar, undermining categorical separation [@muth_colorguide_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** A viewer could describe multiple categories as “light blue / medium blue / dark blue.”
- **The Test:** Ask someone to name the colors; if they use the same base color name repeatedly, the hues are not distinctive enough [@muth_colorguide_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace same-hue shades with different hues (e.g., blue vs orange vs green).
- **Best Fix:** Start from a curated categorical palette collection, then adjust to keep each category visually independent [@muth_colorguide_2018].
