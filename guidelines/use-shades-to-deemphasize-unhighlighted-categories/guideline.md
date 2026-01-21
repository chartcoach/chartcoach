---
id: use-shades-to-deemphasize-unhighlighted-categories
title: Use Shades to De-Emphasize the Background
bibliography: references.bib
description: Highlight the key category with a distinct hue and render the rest as
  shades of a single hue (often gray).
labels:
- chart:general
- task:highlight
- visual:color
- impact:focus
- data:categorical
- audience:novice
- complexity:basic
---

## The Rule <!-- role: advice -->

To highlight one category (or a small set), give it a distinct hue and color all non-highlighted categories as shades of a single hue (often gray).

## The Logic <!-- role: reason -->

This effectively collapses multiple categories into a higher-level group (“not highlighted”), where shades can differentiate without demanding attention. Because readers accept shades within a super-category, this approach draws focus to the highlighted element without confusing category meaning [@muth_quantitative_vs_qualitative_2021].

- **The Principle:** Visual hierarchy through grouping: highlight vs background
- **The Evidence:** [@muth_quantitative_vs_qualitative_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Spot the important category immediately
- **Data Type:** Categorical breakdowns where one item is the story
- **Audience:** Skimmers; presentations; dashboards

## When to Break It <!-- role: exceptions -->

- **Scenario:** Multiple categories are equally important for comparison.
- **Reason:** De-emphasizing “non-highlighted” categories undermines the viewer’s ability to compare them fairly [@muth_quantitative_vs_qualitative_2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** You reduce detail visibility among the non-highlighted categories.
- **The Risk:** If the highlight choice isn’t clearly motivated, audiences may infer editorial bias or hidden importance [@muth_quantitative_vs_qualitative_2021].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Highlighting too many categories with distinct hues.
- **Why it fails:** It destroys the focus and recreates the “confetti” problem [@muth_quantitative_vs_qualitative_2021].
- **The Wrong Fix:** Using multiple hues among the unhighlighted categories.
- **Why it fails:** Readers may interpret those hues as meaningful subgroups rather than “background” [@muth_quantitative_vs_qualitative_2021].

## How to Check <!-- role: check -->

- **Visual Sign:** The highlighted category doesn’t pop; the chart feels equally colorful everywhere.
- **The Test:** Squint: the highlighted element should remain the most salient; if not, background colors are too strong [@muth_quantitative_vs_qualitative_2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert all non-highlighted categories to one neutral hue with a few lightness steps.
- **Best Fix:** Reduce categories shown (aggregate “other”) or redesign to a chart where the highlighted comparison is naturally prominent [@muth_quantitative_vs_qualitative_2021].
