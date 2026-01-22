---
id: prefer-oriented-glyphs-over-oriented-textures-for-mean-orientation-summaries
title: Prefer oriented glyphs over oriented textures (when viewers must summarize
  average direction)
bibliography: references.bib
description: Average orientation is more accessible through object boundaries than
  internal textures, supporting glyph-based encodings for direction summaries.
labels:
- chart:map
- task:summarize
- visual:orientation
- impact:accuracy
- data:spatial
- audience:general
- complexity:intermediate
---

## Use oriented glyphs to support mean-direction judgments <!-- role: advice -->

Represent direction with oriented glyphs (discrete marks with clear boundaries) when viewers need to judge the average direction over a region. Avoid representing direction primarily with oriented textures if the goal is summary of direction.

## Why glyph boundaries support average-orientation extraction <!-- role: reason -->

Average orientation can be computed from ensembles, but the visual system can access average orientation more effectively from boundary contours than from surface texture patterns.

**Mechanism:** Boundary-based orientation signals are more readily pooled into an average than texture-based orientation signals, improving ensemble summaries of direction.

**Evidence:** Average orientation is more accessible through object boundaries than through internal textures, implying an advantage for oriented glyphs over oriented textures when summarizing direction (e.g., wind) [@szafirFourTypesEnsemble2016a].

**Notes:** This guideline concerns summary judgments (average direction), not fine-grained local direction tracing.

## When you should apply this guideline <!-- role: context -->

- **User Goal:** Understand the general direction of a field (e.g., wind direction) in a region or category.
- **Task:** Estimate average orientation/direction, possibly compare between regions.
- **Data:** Spatial fields where direction varies across many samples.
- **Chart Setting:** Maps or spatial grids that could encode direction as texture or as glyphs.
- **Audience:** Mixed audiences; quick situational interpretation.
- **Success Criterion:** Faster and more accurate average-direction judgments.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** The display must communicate continuous flow appearance rather than support average-direction estimation. **Why:** Textures may be chosen for continuous aesthetic/holistic flow depiction even if they are not optimal for mean estimation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Glyphs can increase clutter and overlap in dense regions. **Risk:** Too many glyphs can create crowding that reduces legibility. **Mitigation:** Reduce glyph density or aggregate spatially.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Encoding direction only as an oriented texture in a dense field when the key question is “what is the prevailing direction?” **Why it fails:** Average orientation from textures can be less accessible than from boundary-defined glyphs.

## Quick tests <!-- role: check -->

**Failure Sign:** Users struggle to state the prevailing direction for a region without zooming or inspecting small patches. **Quick Check:** Ask users to report the general direction in a region after a brief glance. **Stronger Test:** Compare accuracy and response time between texture-based and glyph-based prototypes for mean-direction questions.

## What to do instead when this fails <!-- role: fix -->

- Replace oriented textures with oriented glyphs for direction encoding.
- Decrease mark density by sampling or aggregating direction per region.
- Provide interaction to reveal local direction on demand while keeping a glyph-based summary visible.
