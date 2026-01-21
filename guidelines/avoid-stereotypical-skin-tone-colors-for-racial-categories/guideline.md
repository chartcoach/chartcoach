---
id: avoid-stereotypical-skin-tone-colors-for-racial-categories
title: Avoid Stereotypical Skin-Tone Colors for Racial Categories
bibliography: references.bib
description: Do not map racial or ethnic categories to stereotypical skin-tone colors
  like black, white, yellow, or brown.
labels:
- chart:all
- task:categorize
- visual:color
- impact:respect
- data:categorical
- audience:general
- topic:race-ethnicity
- source:datawrapper
---

## The Rule <!-- role: advice -->

Do not assign racial or ethnic categories colors that resemble stereotypical skin tones (e.g., black for Black people, white for white people, yellow for Asian people). Prefer non-skin-tone hues.

## The Logic <!-- role: reason -->

Skin-tone-like mappings lean on stereotypes and can communicate insensitive, reductive associations rather than neutral categorization. This increases the chance your visualization reinforces bias instead of informing.

- **The Principle:** Avoid stereotype-priming in categorical color encodings
- **The Evidence:** [@muth_race_ethnicity_colors_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand differences between groups without implied hierarchy or stereotyping
- **Data Type:** Categorical group comparisons involving race, ethnicity, or world regions
- **Audience:** Broad/public audiences, including people represented by the categories

## When to Break It <!-- role: exceptions -->

- **Scenario:** A race category is intentionally de-emphasized as a neutral backdrop while other categories are highlighted for the story
- **Reason:** The post notes grayscale (including near-white) can be used as a background/least-important category in rare cases, but it should remain the exception [@muth_race_ethnicity_colors_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose “immediate” color-category associations some viewers may expect (even if those associations are problematic).
- **The Risk:** Without careful palette choice, categories may feel less intuitively distinct, requiring stronger labeling or legend design.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using “more subtle” skin tones (tan/peach/beige) to seem less offensive
- **Why it fails:** It still encodes people via skin color, keeping the stereotypical framing intact [@muth_race_ethnicity_colors_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Your palette contains black/white/yellow/brown/olive that appears to correspond directly to named racial groups.
- **The Test:** Read the legend aloud (“Black = black, White = white…”). If it sounds like skin-color coding, you’ve likely violated the rule [@muth_race_ethnicity_colors_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace skin-tone-like swatches with unrelated hues (e.g., switch to muted blues/greens/pinks/purples that don’t resemble skin).
- **Best Fix:** Rebuild the palette so all categories have equal visual dignity and no category-color pairing suggests skin tone; then re-check with colleagues or friends for unintended associations [@muth_race_ethnicity_colors_2024].
