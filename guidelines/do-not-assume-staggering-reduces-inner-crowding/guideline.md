---
id: do-not-assume-staggering-reduces-inner-crowding
title: Do Not Use Staggering to Solve Inner-Crowding Problems
bibliography: references.bib
description: "Staggering generally does not reduce distractors inside the targets\u2019\
  \ convex region, so it is not a reliable fix for inner crowding."
labels:
- chart:scatter
- task:track
- visual:position
- impact:accuracy
- data:multivariate
- audience:expert
- animation:pacing
- metric:inner-crowding
---

## The Rule <!-- role: advice -->

Do not rely on staggering to reduce inner crowding (distractors inside the convex hull of targets) during animated transitions.

## The Logic <!-- role: reason -->

Across large simulations, the paper finds staggering has little to no impact on inner crowding for dot-cloud transitions: regression lines for inner crowding are nearly identical with and without staggering, indicating minimal change [@chevalierNotsoStaggeringEffectStaggered2014].

- **The Principle:** Inner crowding is driven by spatial configuration (targets spread and intervening distractors), which timing offsets alone rarely change.
- **The Evidence:** Simulation analysis shows negligible average differences in inner crowding under both spatial and “smart” staggering orders, even when dwell increases [@chevalierNotsoStaggeringEffectStaggered2014].

## Where to Apply <!-- role: context -->

- **User Goal:** Keep track of a set of targets while distractors move through the region between them.
- **Data Type:** Transitions where targets form a hull that often contains distractors.
- **Audience:** Users sensitive to losing track of target positions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You have a highly structured transition where timing changes also change which points occupy the target hull over time.
- **Reason:** The paper’s conclusion is based on general/random dot-cloud transitions; special structured cases might differ but are not demonstrated [@chevalierNotsoStaggeringEffectStaggered2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to change something other than pacing to address the issue.
- **The Risk:** Adding staggering can add other costs (e.g., deformation or unpredictability) without fixing inner crowding [@chevalierNotsoStaggeringEffectStaggered2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** “Add staggering” whenever distractors appear between targets.
- **Why it fails:** Timing offsets rarely change whether distractors lie inside the targets’ convex region; the paper’s simulations show minimal effect [@chevalierNotsoStaggeringEffectStaggered2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Distractors still pass through the area enclosed by the targets during the transition.
- **The Test:** Sample frames and count distractors inside the targets’ convex hull with and without staggering; expect little change if you are in the paper’s regime [@chevalierNotsoStaggeringEffectStaggered2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Turn off staggering and focus on other parameters (since staggering won’t address inner crowding).
- **Best Fix:** Choose a different transition design goal than pacing alone—because the paper provides evidence that pacing changes are not an effective lever for inner crowding in general dot transitions [@chevalierNotsoStaggeringEffectStaggered2014].
