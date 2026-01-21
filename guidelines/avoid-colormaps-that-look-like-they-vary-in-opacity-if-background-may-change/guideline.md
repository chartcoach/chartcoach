---
id: avoid-colormaps-that-look-like-they-vary-in-opacity-if-background-may-change
title: Avoid Colormaps That Look Like They Vary in Opacity When Backgrounds May Change
bibliography: references.bib
description: To keep inferred value mappings stable across light and dark themes,
  use colormaps that do not appear to blend into the background.
labels:
- chart:heatmap
- chart:choropleth
- task:interpret
- visual:color
- impact:robustness
- data:quantitative
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

If the same visualization may appear on different background colors, use colormaps that will not appear to vary in opacity on any of those backgrounds.

## The Logic <!-- role: reason -->

Apparent opacity variation triggers an **opaque-is-more bias** that depends on the background (what looks more opaque flips between light and dark backgrounds). This can dampen or override the dark-is-more bias on dark backgrounds, making viewers’ inferred mappings unstable across themes [@schlossMappingColorMeaning2019a].

- **The Principle:** Background sensitivity emerges when the colormap is perceived as varying in opacity.
- **The Evidence:** Experiment 1 shows background effects grow as “opacity evidence” increases; Experiment 2 shows reversals consistent with opaque-is-more when scales are background interpolations [@schlossMappingColorMeaning2019a].

## Where to Apply <!-- role: context -->

- **User Goal:** Consistent interpretation of “high vs low” across contexts.
- **Data Type:** Sequential quantitative colormaps used in dashboards, papers, slides, or apps with light/dark mode.
- **Audience:** Broad audiences who may not carefully re-check legends each time.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally use a value-by-alpha/opacity-illusion design and you control the background (it will not change).
- **Reason:** Then leveraging opaque-is-more can be part of the design strategy rather than a failure mode [@schlossMappingColorMeaning2019a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose some “alpha-blended” aesthetics that can look compelling on a specific background.
- **The Risk:** Overcorrecting may lead you to choose highly curved multi-hue scales that are less familiar in your domain (the paper’s evidence here is specifically about mapping biases, not overall colormap quality) [@schlossMappingColorMeaning2019a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Testing the colormap only on the designer’s preferred background.
- **Why it fails:** The same scale can shift from dark-is-more dominated to opaque-is-more influenced depending on background, changing inferred mappings [@schlossMappingColorMeaning2019a].

## How to Check <!-- role: check -->

- **Visual Sign:** On one background the colors look like a solid ramp; on another they look like “transparent paint” thickening/thinning over the background.
- **The Test:** Preview the exact same color scale/legend on every intended background. If it looks like a linear blend into the background on any of them, treat it as opacity-varying and redesign [@schlossMappingColorMeaning2019a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Keep the background fixed (don’t reuse the same colormap across different themes).
- **Best Fix:** Replace the scale with one that does not visually resemble an interpolation between a single “reference color” and the background on any target background, then keep a consistent dark-more mapping [@schlossMappingColorMeaning2019a].
