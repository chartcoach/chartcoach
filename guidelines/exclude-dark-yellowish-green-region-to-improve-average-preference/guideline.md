---
id: exclude-dark-yellowish-green-region-to-improve-average-preference
title: Exclude dark yellowish-green hues when optimizing for average palette preference
bibliography: references.bib
description: Avoid the dark yellowish-green region that is generally disliked to increase
  average preference in categorical palettes.
labels:
- chart:categorical
- task:choose
- visual:color
- impact:appeal
- data:categorical
- audience:novice
- complexity:intermediate
---

## Avoid dark yellowish-green hues to raise average preference <!-- role: advice -->

When designing categorical palettes for broad audiences, avoid sampling dark yellowish-green hues, because this region tends to reduce average preference and can be selected unintentionally under combined objectives.

## Why avoiding this region improves average outcomes <!-- role: reason -->

Some regions of color space are systematically disliked; filtering them prevents the optimization process from landing on unpleasant colors that arise as a side-effect of other objectives.

**Mechanism:** Preference-weighted selection can bias toward blues (via coolness) and discriminability can push toward opposite hues and lightness contrasts; this interaction can yield dark yellows that reduce preference, so filtering removes a common failure region.

**Evidence:** The palette-generation procedure explicitly excludes a dark yellowish-green region to improve typical preference outcomes, motivated by evidence that these colors are strongly disliked on average across cultures and by observed interactions between preference and discriminability objectives [@gramazioColorgoricalCreatingDiscriminable2017a]. The paper reports that this exclusion was important for producing aesthetically preferable discriminable palettes under the combined scoring approach [@gramazioColorgoricalCreatingDiscriminable2017a].

**Notes:** This is a population-average design choice and may not match individual preferences.

## When this applies <!-- role: context -->

- **User Goal:** Avoid audience dislike triggered by particular hues.
- **Task:** Generate or select a categorical palette with broad acceptability.
- **Data:** Categorical; colors are arbitrary identifiers (not semantically required).
- **Chart Setting:** Public-facing or stakeholder-reviewed visuals where dislike harms acceptance.
- **Audience:** Broad, culturally mixed audiences (average preference target).
- **Success Criterion:** Higher average preference without losing required discriminability.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your application requires those hues (e.g., constrained brand colors or semantic mapping). **Why:** Excluding the region may eliminate required colors.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Reduced available color space, which can make large palettes harder to construct. **Risk:** Over-filtering can exhaust viable colors earlier as palette size grows. **Mitigation:** Reduce palette size or relax other constraints if generation becomes difficult.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Allowing optimization to choose any hue while heavily weighting preference and discriminability simultaneously. **Why it fails:** The interaction can produce dark yellow selections that lower preference.
- **Mistake:** Treating personal preference as the target for a general-audience palette. **Why it fails:** The guideline targets average preference; individual variation can differ.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers react negatively to “muddy” yellow-green categories even if they are distinct. **Quick Check:** Scan the palette for dark yellow-green chips and remove or replace them. **Stronger Test:** Collect preference ratings for candidate palettes that differ only in whether this region is included.

## What to do instead <!-- role: fix -->

- Replace dark yellowish-green candidates with alternatives outside the region that preserve the weakest-pair discriminability.
- Increase reliance on lightness contrast among cooler hues rather than introducing dark yellows as complements.
- Constrain hue ranges explicitly so the generator never searches the disliked region.
- If constrained to that region, shift lightness and hue away from the darkest yellow-green area while validating discriminability in the target chart.
