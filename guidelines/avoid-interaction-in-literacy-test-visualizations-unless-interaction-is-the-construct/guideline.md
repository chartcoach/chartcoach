---
id: avoid-interaction-in-literacy-test-visualizations-unless-interaction-is-the-construct
title: Avoid interaction in literacy test visualizations unless interaction is part
  of the construct
bibliography: references.bib
description: Use static charts for literacy measurement to prevent interaction discovery
  and manipulation from confounding reading/interpretation.
labels:
- chart:general
- task:interpret
- visual:interaction
- impact:validity
- data:general
- audience:novice
- method:assessment
---

## Avoid interaction in literacy test visualizations unless interaction is part of the construct <!-- role: advice -->

Use static visualizations without interaction techniques when the goal is to assess reading and interpretation of visually represented data, not tool use.

## Why interaction can add construct-irrelevant demands <!-- role: reason -->

If interaction is present, test performance can depend on whether users detect affordances and know how to use them, which shifts the measured construct toward interface discovery and manipulation. Removing interaction reduces this confound and keeps the assessment focused on interpreting the displayed encoding.

**Mechanism:** Eliminating interaction reduces additional task complexity and prevents performance variance caused by differences in interaction awareness.

**Evidence:** VLAT visualizations intentionally excluded interaction techniques to avoid additional complex tasks and to keep the focus on reading and interpreting visually represented data [@leeVLATDevelopmentVisualization2017].

**Notes:** Static aids such as gridlines can still be used to support value reading without changing the construct.

## When this applies <!-- role: context -->

- **User Goal:** Measure visualization literacy as read/interpret skill.
- **Task:** Standardized item answering under time constraints.
- **Data:** Any, provided the static encoding supports the intended tasks.
- **Chart Setting:** Web-based or paper-like administration without exploratory interaction.
- **Audience:** Non-experts with variable interaction literacy.
- **Success Criterion:** Score variance reflects decoding/interpretation, not affordance discovery.

## When to break it <!-- role: exceptions -->

**Break it when:** The target construct includes using interaction (e.g., brushing, sorting, axis reordering) as part of comprehension. **Why:** Removing interaction would under-measure the intended competency.

## Tradeoffs of removing interaction <!-- role: costs -->

**Sacrifice:** You cannot assess interactive sensemaking skills or adaptive exploration strategies. **Risk:** The test may underrepresent real-world analytic settings where interaction is standard. **Mitigation:** Add a separate interactive module if interaction competence is also important.

## Common mistakes when simplifying to static <!-- role: mistakes -->

**Mistake:** Removing interaction but leaving tasks that implicitly require interaction (e.g., “filter to a subgroup”). **Why it fails:** The task becomes impossible or forces guessing.

## Quick checks <!-- role: check -->

**Failure Sign:** Items require operations not possible on the displayed view. **Quick Check:** Attempt each item with no hover, filter, zoom, or selection actions available. **Stronger Test:** Run a pilot to confirm completion time and that users do not search for missing interactions.

## What to do if interaction is unavoidable <!-- role: fix -->

- Redefine the construct to include interaction competence and state it explicitly.
- Provide a short standardized interaction tutorial before the test module.
- Constrain interaction to one consistent technique across all items to reduce variability.
- Split scores into static-reading and interaction-usage subscores.
