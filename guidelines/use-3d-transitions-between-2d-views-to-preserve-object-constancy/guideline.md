---
id: use-3d-transitions-between-2d-views-to-preserve-object-constancy
title: Use 3D transitions between 2D views to preserve object constancy
bibliography: references.bib
description: Animate between related 2D representations through a 3D transition so
  viewers can visually track the same data objects across views.
labels:
- chart:hybrid
- task:track
- visual:motion
- impact:continuity
- data:multivariate
- audience:expert
- custom:animation
---

## Transition through 3D to keep data objects visually trackable <!-- role: advice -->

When switching between two related 2D charts of the same data, animate the change through a 3D transition so viewers can track objects across representations.

## Why object constancy reduces cognitive burden across chart changes <!-- role: reason -->

Motion allows preattentive tracking of items during transformation, reducing the need to re-read labels after each change; using a 3D intermediate state can also reduce some occlusion during the transition and communicate a spatial mental model relating dimensions.

**Mechanism:** Smooth motion preserves identity of marks across layouts, and a 3D intermediate view can expose the relationship between dimensions as “structure-from-motion.”

**Evidence:** Object constancy via animated transitions reduces cognitive burden by enabling visual tracking, and 3D transitions can provide object constancy between familiar 2D representations while offering a different way to handle occlusion in transitions [@brath3DInfoVisHere2014].

**Notes:** The primary value is continuity; the intermediate 3D view should remain interpretable.

## When to apply 3D transitions <!-- role: context -->

- **User Goal:** Understand how two views relate without re-parsing the entire display.
- **Task:** Move between summary and detailed views of the same measure(s).
- **Data:** Same entities shown under different arrangements (e.g., time series vs. categorical bars).
- **Chart Setting:** Interactive or animated medium where transitions can play.
- **Audience:** Viewers who may otherwise lose track of which item became which.
- **Success Criterion:** Users can follow items across the transition without rereading labels.

## When not to use it <!-- role: exceptions -->

**Break it when:** The presentation medium is static (print, screenshots) or animation cannot be relied upon. **Why:** The object-constancy benefit depends on motion being available to the viewer [@brath3DInfoVisHere2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Time and attention are spent on animation rather than the final state. **Risk:** The transition can introduce confusion if too many marks occlude each other mid-flight. **Mitigation:** Keep transitions short and ensure marks remain visually distinguishable during motion.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Abruptly switching between two layouts with no transition. **Why it fails:** Users must re-identify objects by rereading labels, increasing cognitive effort [@brath3DInfoVisHere2014].
- **Mistake:** Creating a transition where objects heavily overlap mid-animation. **Why it fails:** Occlusion interrupts tracking and breaks object constancy [@brath3DInfoVisHere2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Users ask “which one became that?” after the transition. **Quick Check:** Show the transition once and ask a user to track a specific item from start to end. **Stronger Test:** Compare task time and correctness with versus without the animated transition.

## What to do instead <!-- role: fix -->

- Use persistent highlighting of a selected item across views to maintain identity without animation.
- Use side-by-side coordinated views so the mapping between views is visible concurrently.
- Reduce the number of simultaneously animated marks by filtering to a subset of interest.
- Use a 2D transition strategy that staggers motion when 3D would produce heavy overlap.
