---
id: use-diverging-colormaps-for-pattern-matching-in-high-spatial-frequency-maps
title: Use a diverging colormap (cool-warm or spectral) for pattern matching in high-spatial-frequency
  maps
bibliography: references.bib
description: For matching longitudinal patterns in complex continuous quantitative
  maps, cool-warm and spectral rank highest among tested colormaps.
labels:
- chart:heatmap
- task:correlate
- visual:color
- impact:accuracy
- data:spatial
- audience:general
- domain:continuous-map
- condition:high-spatial-frequency
---

## Pattern matching in complex continuous maps with diverging palettes <!-- role: advice -->

Use a diverging colormap such as cool-warm or spectral when users must match a longitudinal pattern (profile) in a continuous quantitative map with high spatial frequency. Prefer these over greyscale and over the lower-ranked tested alternatives for this condition.

## Why diverging palettes help pattern matching at high spatial frequency <!-- role: reason -->

When patterns are fine-grained, viewers must integrate many local changes into an overall shape, and colormap design can either preserve or obscure these changes.

**Mechanism:** A diverging palette can increase discriminability of alternating rises and falls across a path, which supports recognizing and matching a profile pattern in visually complex fields.

**Evidence:** In the extracted pattern-perception condition (correlate-2), the ranking places cool-warm first and spectral second, with both significantly outperforming multiple other colormaps in the recorded significance pairs [@redaGraphicalPerceptionContinuous2018]. This task-conditioned ranking is represented as reusable structured knowledge for visualization recommendation and constraint/rule formulation [@zengReviewCollationGraphical2023].

**Notes:** This guideline is limited to the extracted pattern-matching condition and does not imply diverging palettes are best for value lookup.

## When to apply this rule <!-- role: context -->

- **User Goal:** Identify which candidate profile best matches the map’s elevation (or value) pattern along a specified path.
- **Task:** Correlate-style matching (pattern/profile matching against options).
- **Data:** Continuous spatial field with high spatial frequency (dense, fine features).
- **Chart Setting:** Continuous pseudocolor map plus an external set of candidate patterns.
- **Audience:** General audiences with normal color vision (as screened in the study setting).
- **Success Criterion:** Higher accuracy in selecting the correct matching pattern.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The user’s goal is to retrieve a specific numeric value at a location. **Why:** The retrieve-value ranking places rainbow above cool-warm and spectral in the extracted results.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** A diverging palette can be less aligned with value-lookup performance than the top retrieve-value option. **Risk:** Choosing a palette for pattern matching can make location-based value estimation less accurate. **Mitigation:** Separate “pattern task” and “value lookup task” modes with different palette defaults.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Keeping rainbow as the default palette even when the task is profile/pattern matching in complex maps. **Why it fails:** The extracted pattern-matching ranking favors cool-warm and spectral over rainbow in that condition.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers pick inconsistent profiles or confuse distractor patterns, especially on visually complex maps. **Quick Check:** Run a few pattern-matching questions and see whether accuracy drops sharply on the most complex maps. **Stronger Test:** Compare cool-warm and spectral against your current palette on identical pattern-matching prompts and track accuracy.

## What to do instead <!-- role: fix -->

- Use cool-warm if you want the top-ranked option for the extracted pattern-matching condition.
- Use spectral if you want a second top-ranked diverging option for the same condition.
- Offer both palettes and let the user switch when pattern matching is the active task.
