---
id: prefer-position-or-length-over-slope-for-relation-perception-with-or-without-deltas
title: Prefer Position or Length Over Slope for Relation Perception in Paired Comparisons
bibliography: references.bib
description: Across multiple relational tasks, slope-based encodings produced worse
  performance than position or length encodings for judging relations between paired
  values.
labels:
- chart:bar
- chart:dot
- chart:slope
- task:compare
- task:search
- task:aggregate
- visual:position
- visual:length
- visual:orientation
- impact:accuracy
- impact:efficiency
- data:paired
- audience:novice
- audience:expert
- custom:channel-selection
---

## Use position or length channels instead of slope for pairwise relation judgments <!-- role: advice -->

For tasks that require judging relations between paired values, encode values or deltas using position or length rather than slope when you need higher efficiency and accuracy.

## Why slope underperforms for these relational tasks <!-- role: reason -->

Even though orientation is a basic visual feature, perceiving relational direction and differences from slope marks can be difficult in certain structured arrangements, reducing both search efficiency and ensemble discrimination performance. Position and length encodings supported better performance in the tested tasks.

**Mechanism:** Position and length provide more directly comparable magnitude cues for both individual values and deltas, while slope/orientation can be harder to parse in these relational display layouts.

**Evidence:** In visual search, search rates were worse for slope encodings than for position and length encodings; in proportion discrimination, accuracy was lower for slope encodings than for position and length encodings. [@nothelferMeasuresBenefitDirect2020a]

**Notes:** The observed slope difficulty may depend on the specific arrangement used (items aligned in a row), so slope performance may not generalize to all layouts.

## When this applies <!-- role: context -->

- **User Goal:** Quickly and accurately judge relations (direction or magnitude) between paired values.
- **Task:** Find an anomalous relation; judge prevalence of relation directions; estimate average deltas.
- **Data:** Paired comparisons where users must compare across many pairs.
- **Chart Setting:** Displays that arrange pairs in a structured row/strip layout or other regular arrangement.
- **Audience:** Broad; especially users scanning quickly.
- **Success Criterion:** Better scalability with more pairs and higher accuracy under brief viewing.

## When to break this rule <!-- role: exceptions -->

**Break it when:** Your design constraints require a slope-like representation and the user’s task is not relation perception across many pairs. **Why:** The evidence here is specific to relation-perception tasks and tested layouts.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some stylistic compactness or narrative appeal that slope-like displays can provide.\
**Risk:** Overgeneralizing channel rankings to contexts not tested (different layouts or tasks).\
**Mitigation:** Validate with a small task-matched pilot when slope is attractive for layout reasons.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Choosing slope encodings for relation perception because orientation is assumed to be universally efficient. **Why it fails:** Performance was comparatively poor for slope encodings in both search and ensemble direction tasks under the tested layouts.\
**Mistake:** Mixing channel choices across related panels (slope in one, length in another) for the same relation task. **Why it fails:** Users cannot rely on consistent perceptual cues across panels.

## Quick tests <!-- role: check -->

**Failure Sign:** Users make frequent mistakes on direction-of-change judgments when relations are encoded via slope.\
**Quick Check:** Ask users to quickly identify whether most pairs increase or decrease in a slope-encoded view and note error rate.\
**Stronger Test:** Compare task performance for slope vs. length/position using the same data and time constraints.

## What to do instead <!-- role: fix -->

- Switch relation encoding to a delta bar or delta position mark centered on a baseline.
- Use length or position for the underlying values when deltas cannot be shown.
- Separate slope-based storytelling views from task-critical analytic views where relation judgments must be efficient.
- Reduce the number of pairwise comparisons shown if slope must be retained.
