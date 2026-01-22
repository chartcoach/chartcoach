---
id: use-shape-coercion-to-construct-simpsons-paradox-examples-while-holding-overall-correlation-fixed
title: "Use shape coercion to construct Simpson\u2019s paradox examples while holding\
  \ overall correlation fixed"
bibliography: references.bib
description: Create grouped patterns with opposing within-group trends while preserving
  the aggregate correlation by steering points toward sloped-line targets.
labels:
- chart:scatter
- task:teach
- visual:position
- impact:insight
- data:quantitative
- audience:novice
- custom:simpsons-paradox
- complexity:advanced
---

## Coerce points into grouped sloped lines while keeping the overall correlation unchanged <!-- role: advice -->

To generate a Simpson’s paradox demonstration, start from a dataset with a strong overall correlation and coerce points toward multiple within-group sloped-line patterns while enforcing the same aggregate correlation constraint.

## Why group structure can invert trends without changing the aggregate summary <!-- role: reason -->

The paradox arises because aggregate summaries can mask heterogeneous subgroup patterns; by introducing clustered groups with their own internal slopes, you can preserve the overall correlation while creating within-group correlations that differ in sign.

**Mechanism:** Constraining the overall correlation fixes one global relationship, but reshaping the dataset into separated groups changes conditional relationships inside each group.

**Evidence:** A dataset with a strong positive overall Pearson correlation was transformed into grouped negatively sloped line patterns such that the combined data retained the same positive correlation while each group had a negative correlation [@matejkaSameStatsDifferent2017].

**Notes:** This is a directed use of the same coercion framework, with the target defined as multiple sloped line segments.

## When you need an explicit example of aggregation masking subgroup trends <!-- role: context -->

- **User Goal:** Demonstrate that aggregate trends can differ from subgroup trends.
- **Task:** Create a dataset where within-group patterns oppose the combined pattern.
- **Data:** 2D quantitative points that can be partitioned into labeled groups.
- **Chart Setting:** Educational materials or testing of analysis workflows that must consider grouping.
- **Audience:** Viewers learning about statistical pitfalls and the value of visualization.
- **Success Criterion:** The overall correlation matches the seed’s correlation while each subgroup exhibits the intended opposing correlation.

## When not to use this construction approach <!-- role: exceptions -->

**Break it when:** Your audience cannot see or interact with subgroup labels. **Why:** Without visible grouping, the within-group trends required for the paradox will not be interpretable as intended [@matejkaSameStatsDifferent2017].

## Tradeoffs of building paradox examples via constrained optimization <!-- role: costs -->

**Sacrifice:** You may need many iterations and careful target design to make subgroup structure clear while maintaining the aggregate constraint. **Risk:** Overly rigid constraints can yield artifacts that look artificial rather than instructive. **Mitigation:** Treat the target pattern design (spacing, slopes, group separation) as part of the optimization specification [@matejkaSameStatsDifferent2017].

## Common mistakes in Simpson’s paradox demonstrations <!-- role: mistakes -->

**Mistake:** Showing only the aggregate regression or correlation without plotting groups. **Why it fails:** The paradox depends on subgroup structure that is invisible in a single undifferentiated view [@matejkaSameStatsDifferent2017].

## Quick tests for a valid paradox example <!-- role: check -->

**Failure Sign:** The aggregate and within-group correlations share the same sign or are too weak to perceive. **Quick Check:** Compute the overall Pearson correlation and each group’s correlation and verify they match the intended signs. **Stronger Test:** Plot groups with distinct encodings and confirm that the visual slopes align with the computed correlations [@matejkaSameStatsDifferent2017].

## What to do instead when the paradox is not clear <!-- role: fix -->

- Increase separation between groups in the target pattern so within-group structure is visually distinct.
- Strengthen within-group slopes in the target lines while maintaining the aggregate correlation constraint.
- Adjust group sizes or group placement in the target pattern to stabilize within-group trends.
- Restart from a seed dataset with a stronger aggregate correlation if the constraint leaves too little flexibility [@matejkaSameStatsDifferent2017].
