---
id: rank-recommended-encodings-by-expressiveness-and-perceptual-effectiveness
title: Rank Encodings by Expressiveness and Perceptual Effectiveness
bibliography: references.bib
description: Filter invalid encodings and rank valid ones using data-type-aware effectiveness
  heuristics.
labels:
- chart:any
- task:choose-encoding
- visual:position
- impact:clarity
- data:mixed
- audience:analyst
- system:recommendation
---

## The Rule <!-- role: advice -->

When recommending charts, first enforce expressiveness constraints, then rank the remaining encodings using data-type-aware perceptual effectiveness heuristics.

## The Logic <!-- role: reason -->

Voyager’s Compass prevents misleading or inappropriate charts via expressiveness criteria (valid channel/mark combinations) and then ranks encodings using effectiveness principles (e.g., channel rankings by data type and penalties for over-encoding) [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Validity-first, effectiveness-second recommendation
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly get readable, appropriate charts without manual design expertise
- **Data Type:** Mixed nominal/ordinal/quantitative/temporal fields
- **Audience:** Analysts using automated recommendations

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user is intentionally creating unconventional or highly customized designs.
- **Reason:** Strict rule-based constraints may block desired bespoke encodings.

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced design expressivity in the recommender output.
- **The Risk:** Heuristic rankings may not match a user’s specific analytical intent.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Ranking “interestingness” without first removing invalid/inexpressive visualizations.
- **Why it fails:** Users may be shown charts that are hard to interpret or misleading even if they score high on some statistical metric [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Recommendations include charts that don’t “make sense” for the mark type (e.g., line/area without both x and y).
- **The Test:** Validate each suggested spec against required/disallowed channels per mark type before ranking.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Implement required/permitted channel constraints per mark type and only rank those that pass.
- **Best Fix:** Combine constraints with a weighted effectiveness score that accounts for channel rankings by data type, cardinality penalties, and over-encoding penalties, as done in Compass [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
