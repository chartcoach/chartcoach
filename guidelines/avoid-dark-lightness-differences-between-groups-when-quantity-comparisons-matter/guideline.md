---
id: avoid-dark-lightness-differences-between-groups-when-quantity-comparisons-matter
title: Avoid using darker luminance to encode a group (when viewers must compare group
  numerosity)
bibliography: references.bib
description: Darker groups can appear more numerous, biasing numerosity judgments
  in visual comparisons.
labels:
- chart:unit
- task:compare
- visual:color
- impact:trust
- data:categorical
- audience:general
- complexity:beginner
---

## Avoid luminance-driven bias in numerosity comparisons <!-- role: advice -->

Do not make one category systematically darker than another when viewers need to judge which group has more items. Keep luminance comparable across groups used for quantity comparisons.

## Why luminance biases perceived number <!-- role: reason -->

Perceived numerosity is not purely determined by the count of items; some visual features can systematically bias the apparent number of items in a set.

**Mechanism:** Luminance differences can change perceived numerosity, making some groups look more numerous even when the count is the same.

**Evidence:** Darker collections can be perceived as more numerous, implying that luminance differences can bias numerosity judgments in visual displays [@szafirFourTypesEnsemble2016a].

**Notes:** This concerns relative numerosity (which group has more), not exact counting.

## When you should apply this guideline <!-- role: context -->

- **User Goal:** Compare quantities between groups by sight.
- **Task:** Estimate or compare numerosity across categories.
- **Data:** Many individual marks representing discrete items (unit charts, dot plots, tagged text marks).
- **Chart Setting:** Static categorical comparisons; dense displays where counting is unlikely.
- **Audience:** General audiences; quick-glance decisions.
- **Success Criterion:** Quantity comparisons that are unbiased by visual styling.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** Numerosity comparisons are not a user task for the display. **Why:** The bias matters primarily when viewers use appearance to infer quantity.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose a convenient channel for emphasizing one group. **Risk:** Equalizing luminance may reduce salience for highlighting. **Mitigation:** Highlight with non-luminance cues that do not change apparent count for the compared groups.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a dark-vs-light scheme to distinguish categories in a chart where “which group is larger?” is central. **Why it fails:** Darker marks can bias viewers toward perceiving more items in that group.

## Quick tests <!-- role: check -->

**Failure Sign:** People consistently report that the darker group has more items when counts are equal or close. **Quick Check:** Run a “same count” sanity test by showing equal-sized groups with your styling and asking which looks larger. **Stronger Test:** A/B test a version with equalized luminance and compare numerosity judgment bias.

## What to do instead when this fails <!-- role: fix -->

- Use hues of similar luminance to distinguish groups used in numerosity comparisons.
- Reserve luminance variation for variables not tied to quantity judgments.
- Add explicit counts or an aggregate bar/label when accurate quantity comparison is required.
