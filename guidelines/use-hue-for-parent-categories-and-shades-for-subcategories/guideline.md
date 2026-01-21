---
id: use-hue-for-parent-categories-and-shades-for-subcategories
title: Use Hue for Categories and Shades for Subcategories
bibliography: references.bib
description: Use a hue to define each main category and shades of that hue to differentiate
  its subcategories.
labels:
- chart:general
- task:group
- visual:color
- impact:structure
- data:hierarchical
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When your data has categories and subcategories, assign each main category a distinct hue and use shades of that hue for its subcategories.

## The Logic <!-- role: reason -->

A hue shift signals a higher-level grouping (“different kind”), while shade variations within a hue help differentiate items that belong together. Readers infer that the shades’ job is to separate sub-items within a group, reducing the expectation that shades encode a magnitude or rank—especially when the chart is directly labeled and doesn’t need color as a category key [@muth_quantitative_vs_qualitative_2021].

- **The Principle:** Encode hierarchy via color: hue for groups, shades for within-group distinctions
- **The Evidence:** [@muth_quantitative_vs_qualitative_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Recognize grouping first, then distinguish items within groups
- **Data Type:** Hierarchical categories (category → subcategory), possibly unordered within each parent
- **Audience:** General audiences; especially when labels provide the primary identification

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need viewers to compare subcategories across parents (not within each parent).
- **Reason:** Separate shade ramps per parent can make cross-parent comparison harder because shades are relative to each hue family [@muth_quantitative_vs_qualitative_2021].
- **Scenario:** Colors are unnecessary because everything is directly labeled and separation lines suffice.
- **Reason:** The post notes some charts “don’t need colors at all” when direct labels remove the need for a color key [@muth_quantitative_vs_qualitative_2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** More palette planning; maintaining consistent shade steps across multiple hues can be tricky.
- **The Risk:** Viewers may still rationalize shades as meaning “more/less” if other cues suggest ordering [@muth_quantitative_vs_qualitative_2021].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using many unrelated hues for all subcategories.
- **Why it fails:** It increases visual noise and makes grouping harder to perceive [@muth_quantitative_vs_qualitative_2021].
- **The Wrong Fix:** Using shades but implying an order (e.g., darkest at top) when no order exists.
- **Why it fails:** It invites false interpretation of ranking within the group [@muth_quantitative_vs_qualitative_2021].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can’t immediately tell which items belong to which parent category.
- **The Test:** Ask someone to point to all items in one parent category without reading labels; if they can’t, the grouping cue isn’t strong enough [@muth_quantitative_vs_qualitative_2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce hues to the number of parent categories; move subcategory differentiation to shades within each hue.
- **Best Fix:** If subcategories are directly labeled, remove most color and use a minimal palette (or grayscale) plus clear separators [@muth_quantitative_vs_qualitative_2021].
