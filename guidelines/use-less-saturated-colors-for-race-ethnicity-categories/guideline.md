---
id: use-less-saturated-colors-for-race-ethnicity-categories
title: Use Less-Saturated Colors for Race and Ethnicity Palettes
bibliography: references.bib
description: Prefer toned-down, less-saturated hues for racial categories to reduce
  strong positive/negative color associations.
labels:
- chart:all
- task:categorize
- visual:color
- impact:neutrality
- data:categorical
- audience:general
- topic:race-ethnicity
- source:datawrapper
---

## The Rule <!-- role: advice -->

Choose toned-down (less saturated) colors for racial/ethnic categories, and avoid highly saturated “crayon” colors that carry strong value-laden associations.

## The Logic <!-- role: reason -->

Highly saturated colors can imply meaning (e.g., danger, correctness, importance, competence). For sensitive identity categories, you typically don’t want those adjectives attached to any group, so reducing saturation helps keep the encoding more neutral.

- **The Principle:** Reduce semantic overload in color encoding
- **The Evidence:** [@muth_race_ethnicity_colors_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare groups without moral or status framing implied by color
- **Data Type:** Nominal categories (race/ethnicity/world-region groupings)
- **Audience:** Broad/public audiences

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need maximum separability between many categories and muted colors become too hard to distinguish
- **Reason:** The post warns that less-saturated colors can be harder for colorblind people to distinguish and may fail contrast tests, which can outweigh the neutrality benefit [@muth_race_ethnicity_colors_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced category pop and potentially lower discriminability between similar hues.
- **The Risk:** Pastels/low-contrast fills may create accessibility issues, especially in small marks.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Making everything pastel without checking distinguishability or contrast
- **Why it fails:** Muted palettes can blur together and may not meet contrast needs, harming readability and accessibility [@muth_race_ethnicity_colors_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Categories look interchangeable at a glance, or thin shapes/labels become hard to read.
- **The Test:** View the chart small (thumbnail size) and see whether categories remain distinct; then check whether light fills reduce legibility of labels/marks [@muth_race_ethnicity_colors_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase separation by adjusting lightness/hue slightly while keeping saturation moderate.
- **Best Fix:** Keep fills relatively muted but add darker or more saturated outlines to preserve distinguishability and improve contrast performance [@muth_race_ethnicity_colors_2024].
