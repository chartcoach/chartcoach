---
id: limit-shades-when-using-one-hue-for-categories
title: Limit the Number of Category Shades
bibliography: references.bib
description: If you encode categories using shades of one hue, keep the number of
  shades small and avoid implying false groupings.
labels:
- chart:general
- task:categorize
- visual:color
- impact:accessibility
- data:categorical
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

If you choose to encode categories with shades of a single hue, use only a small number of shades and avoid introducing additional hues unless they have meaning.

## The Logic <!-- role: reason -->

It’s difficult for readers to reliably distinguish many lightness steps, especially when there’s no order and no direct labels. Adding a second hue to “get more shades” can look like an additional grouping, causing viewers to infer categories that you didn’t intend [@muth_quantitative_vs_qualitative_2021].

- **The Principle:** Perceptual limits of lightness discrimination and accidental grouping
- **The Evidence:** [@muth_quantitative_vs_qualitative_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Distinguish a few categories without a “too colorful” look; improve grayscale robustness
- **Data Type:** A small set of nominal categories (best with direct labels)
- **Audience:** Broad audiences, including color-impaired readers, and stakeholders sensitive to “too colorful” designs

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need many categories and they are not directly labeled.
- **Reason:** The post’s rule of thumb implies many shades quickly become unreadable; a different encoding or chart type is more appropriate [@muth_quantitative_vs_qualitative_2021].
- **Scenario:** A second hue is genuinely meaningful (e.g., distinct parent group vs another group).
- **Reason:** Then hue change communicates structure rather than creating accidental structure [@muth_quantitative_vs_qualitative_2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer distinct categories can be shown clearly with color alone.
- **The Risk:** Readers may “rationalize” shade differences as rank/importance even if unintended, so “random” shading is risky [@muth_quantitative_vs_qualitative_2021].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using 4–6 shades of the same hue for unordered categories.
- **Why it fails:** Readers struggle to tell them apart and may give up, especially without ordering or labels [@muth_quantitative_vs_qualitative_2021].
- **The Wrong Fix:** Adding a second hue just to expand the palette.
- **Why it fails:** It can imply a new category split (e.g., “blue group vs non-blue group”) that wasn’t intended [@muth_quantitative_vs_qualitative_2021].

## How to Check <!-- role: check -->

- **Visual Sign:** The legend requires intense attention; categories look nearly identical; viewers mis-group segments by hue family.
- **The Test:** Convert to grayscale and/or print: if categories collapse into indistinguishable tones, you used too many shades [@muth_quantitative_vs_qualitative_2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of shaded categories (aggregate small ones into “Other”) or directly label categories to remove reliance on color.
- **Best Fix:** Switch to a chart/encoding that doesn’t depend on many color distinctions (or use distinct hues when categories must be distinguished) [@muth_quantitative_vs_qualitative_2021].
