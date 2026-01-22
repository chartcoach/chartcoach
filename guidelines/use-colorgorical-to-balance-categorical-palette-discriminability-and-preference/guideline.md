---
id: use-colorgorical-to-balance-categorical-palette-discriminability-and-preference
title: Use Colorgorical to balance categorical palette discriminability and preference
  for nominal color-hue encodings
bibliography: references.bib
description: Generate categorical (nominal) color-hue palettes by explicitly balancing
  discriminability and aesthetic preference rather than optimizing only one.
labels:
- chart:general
- task:aggregate
- visual:color
- impact:clarity
- data:categorical
- audience:general
- tool:colorgorical
---

## Balance discriminability and preference for categorical color-hue palettes <!-- role: advice -->

Use a categorical color-hue palette generation approach that explicitly trades off color discriminability and aesthetic preference when encoding nominal categories. Keep the balance configurable so you can prioritize discrimination performance or preference depending on the situation.

## Why a balanced categorical palette helps aggregation judgments <!-- role: reason -->

For nominal categories encoded by color hue, the limiting factor is often the least distinguishable pair of colors in the palette; balancing competing objectives helps avoid palettes that are either hard to tell apart or broadly disliked.

**Mechanism:** A palette that improves pairwise discriminability reduces confusions between categories, which supports aggregate judgments over many colored marks; a palette that improves pairwise preference can increase perceived pleasantness but may reduce discriminability if it drives colors closer together.

**Evidence:** Behavioral discrimination performance improves as palette discriminability increases and worsens as pairwise preference is upweighted, while preference ratings increase as pairwise preference increases, indicating a measurable tradeoff that can be tuned for categorical palettes [@gramazioColorgoricalCreatingDiscriminable2017]. This guidance is represented as collated graphical perception knowledge intended to be translated into actionable recommendation rules for visualization systems [@zengReviewCollationGraphical2023].

**Notes:** This guideline applies to categorical (nominal) color-hue use; it does not cover sequential or diverging colormaps for quantitative values.

## When to apply this to categorical encodings <!-- role: context -->

- **User Goal:** Judge overall composition of categories without frequent confusions or aversion to the colors.
- **Task:** Aggregate.
- **Data:** Nominal categories mapped to distinct colors; palette size may be more than a few categories.
- **Chart Setting:** Any chart where categories are distinguished primarily by color hue (e.g., maps, grouped marks, categorical overlays).
- **Audience:** General audiences with typical color vision (unless otherwise specified).
- **Success Criterion:** Fewer category confusions in aggregate judgments while maintaining acceptable user-rated preference.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot tolerate any reduction in discriminability for the sake of aesthetics. **Why:** Increasing pair-preference weighting can measurably worsen discrimination performance for categorical palettes.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may need to accept a compromise rather than maximizing a single objective (pure discriminability or pure preference).\
**Risk:** Over-prioritizing preference can increase category confusions in aggregate judgments; over-prioritizing discriminability can reduce user liking of the palette.\
**Mitigation:** Treat palette choice as an explicit tradeoff decision tied to the task’s success criterion (accuracy vs. preference).

## Common failure modes <!-- role: mistakes -->

**Mistake:** Choosing a categorical palette by “looks nice” alone when the task requires accurate aggregate judgments. **Why it fails:** Preference-oriented palettes can reduce discriminability and increase confusions between categories.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers miscount or misjudge which category dominates because two categories look too similar.\
**Quick Check:** Identify the two most similar colors in the palette and verify they remain distinguishable at the mark size used in the visualization.\
**Stronger Test:** Run a small timed discrimination or counting pilot using the real mark sizes and category frequencies.

## What to do instead <!-- role: fix -->

- Increase the relative importance of discriminability in the palette-generation settings when aggregate accuracy matters most.
- Decrease the relative importance of preference if you observe category confusions between similarly colored classes.
- Reduce the number of categories encoded by color hue if the palette becomes difficult to discriminate at the intended mark size.
- Use an alternative non-color encoding for some categories if the palette cannot remain discriminable at the required category count.
